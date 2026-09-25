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
