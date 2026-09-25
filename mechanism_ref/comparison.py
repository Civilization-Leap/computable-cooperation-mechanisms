"""Multi-plan componentwise comparison for Purpose Generation integration.

This module does not select a winner. It preserves componentwise incomparability.
V0.1 intentionally excludes UNKNOWN dependency and assumption-reversal analysis;
those remain explicit gaps rather than empty-success claims.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence


class ComparisonInputError(ValueError):
    pass


@dataclass(frozen=True)
class Plan:
    plan_id: str
    components: Mapping[str, float]


def dominates(left: Plan, right: Plan) -> bool:
    """Strict Cartesian-product dominance.

    left dominates right iff every named component is >= and at least one is >.
    Component sets must match exactly. No weighting, summing or thresholding.
    """
    if set(left.components) != set(right.components):
        raise ComparisonInputError("plan component sets must match exactly")
    if not left.components:
        raise ComparisonInputError("plans require at least one component")
    all_not_worse = all(left.components[k] >= right.components[k] for k in left.components)
    any_better = any(left.components[k] > right.components[k] for k in left.components)
    return all_not_worse and any_better


def compare_plans(plans: tuple[Plan, ...]) -> dict[str, object]:
    if len(plans) < 2:
        raise ComparisonInputError("comparison requires at least two plans")
    ids = [p.plan_id for p in plans]
    if len(ids) != len(set(ids)):
        raise ComparisonInputError("plan ids must be unique")

    dominated_by: dict[str, list[str]] = {p.plan_id: [] for p in plans}
    incomparable: set[tuple[str, str]] = set()

    for i, left in enumerate(plans):
        for right in plans[i + 1 :]:
            if dominates(left, right):
                dominated_by[right.plan_id].append(left.plan_id)
            elif dominates(right, left):
                dominated_by[left.plan_id].append(right.plan_id)
            else:
                incomparable.add(tuple(sorted((left.plan_id, right.plan_id))))

    dominated = sorted(pid for pid, by in dominated_by.items() if by)
    non_dominated = sorted(pid for pid, by in dominated_by.items() if not by)
    return {
        "non_dominated": non_dominated,
        "dominated": dominated,
        "incomparable": [list(pair) for pair in sorted(incomparable)],
        "dominated_by": {pid: sorted(by) for pid, by in sorted(dominated_by.items()) if by},
        "capability_gaps": [
            "unknown_dependent",
            "assumption_reversals",
            "channel_criterion_boundary_flags",
        ],
    }


@dataclass(frozen=True)
class UnknownRange:
    """A bounded unknown component for sensitivity analysis."""

    component: str
    low: float
    high: float

    def __post_init__(self) -> None:
        if self.low > self.high:
            raise ComparisonInputError("unknown range low must be <= high")


def _with_value(plan: Plan, component: str, value: float) -> Plan:
    if component not in plan.components:
        raise ComparisonInputError(f"unknown component {component!r} is not present in plan")
    updated = dict(plan.components)
    updated[component] = value
    return Plan(plan.plan_id, updated)


def unknown_dependency(
    plans: tuple[Plan, ...],
    *,
    plan_id: str,
    unknown: UnknownRange,
) -> dict[str, object] | None:
    """Report dependency only when endpoint values change the comparison structure.

    This is deliberately narrower than "an unknown exists". It asks whether the
    non-dominated/dominated/incomparable structure changes across the declared
    range endpoints. No probability or preferred endpoint is introduced.
    """
    matches = [p for p in plans if p.plan_id == plan_id]
    if len(matches) != 1:
        raise ComparisonInputError("unknown dependency requires exactly one matching plan")
    target = matches[0]

    low_plans = tuple(
        _with_value(p, unknown.component, unknown.low) if p.plan_id == plan_id else p
        for p in plans
    )
    high_plans = tuple(
        _with_value(p, unknown.component, unknown.high) if p.plan_id == plan_id else p
        for p in plans
    )
    low_result = compare_plans(low_plans)
    high_result = compare_plans(high_plans)

    keys = ("non_dominated", "dominated", "incomparable")
    changed = any(low_result[k] != high_result[k] for k in keys)
    if not changed:
        return None
    return {
        "unknown_id": f"{plan_id}:{unknown.component}",
        "effect": "comparison_structure_changes_across_range",
        "low": {k: low_result[k] for k in keys},
        "high": {k: high_result[k] for k in keys},
    }


@dataclass(frozen=True)
class AssumptionVariant:
    """One named alternative value for a project-estimated component."""

    variant_id: str
    plan_id: str
    component: str
    value: float


def assumption_reversal(
    plans: tuple[Plan, ...],
    variants: Sequence[AssumptionVariant],
) -> dict[str, object] | None:
    """Detect whether alternative project-estimate values reverse comparison structure.

    The baseline is the supplied plan set. Each variant changes exactly one
    named component for one plan. A reversal is reported only when at least one
    of non-dominated/dominated/incomparable differs from baseline. No variant is
    preferred and no policy conclusion is produced.
    """
    baseline = compare_plans(plans)
    keys = ("non_dominated", "dominated", "incomparable")
    changed_variants: list[dict[str, object]] = []

    ids = {p.plan_id for p in plans}
    for variant in variants:
        if variant.plan_id not in ids:
            raise ComparisonInputError("assumption variant references unknown plan")
        changed_plans = tuple(
            _with_value(p, variant.component, variant.value)
            if p.plan_id == variant.plan_id
            else p
            for p in plans
        )
        result = compare_plans(changed_plans)
        if any(result[k] != baseline[k] for k in keys):
            changed_variants.append(
                {
                    "variant_id": variant.variant_id,
                    "plan_id": variant.plan_id,
                    "component": variant.component,
                    "value": variant.value,
                    "comparison": {k: result[k] for k in keys},
                }
            )

    if not changed_variants:
        return None
    return {
        "effect": "comparison_structure_reverses_under_assumption_variant",
        "baseline": {k: baseline[k] for k in keys},
        "changed_variants": changed_variants,
    }


@dataclass(frozen=True)
class ChannelState:
    """Availability of one correction/exit/recovery channel for one subject."""

    subject_id: str
    correction: bool
    exit: bool
    recovery: bool


def channel_boundary_flags(
    baseline: Sequence[ChannelState],
    candidate: Sequence[ChannelState],
) -> list[str]:
    """Flag structural loss of the last available channel for a named subject.

    This is a channel criterion, not a numerical risk threshold. A flag occurs
    when a subject had at least one correction/exit/recovery channel in baseline
    and the candidate removes all three. Subjects must be explicitly present in
    both states; missing representation fails closed.
    """
    def index(states: Sequence[ChannelState]) -> dict[str, ChannelState]:
        result: dict[str, ChannelState] = {}
        for state in states:
            if state.subject_id in result:
                raise ComparisonInputError("duplicate channel subject")
            result[state.subject_id] = state
        return result

    before = index(baseline)
    after = index(candidate)
    if set(before) != set(after):
        raise ComparisonInputError(
            "baseline/candidate channel subject sets must match exactly"
        )

    flags: list[str] = []
    for subject_id in sorted(before):
        b = before[subject_id]
        a = after[subject_id]
        had_channel = b.correction or b.exit or b.recovery
        has_channel = a.correction or a.exit or a.recovery
        if had_channel and not has_channel:
            flags.append(f"{subject_id}:LAST_CHANNEL_REMOVED")
    return flags
