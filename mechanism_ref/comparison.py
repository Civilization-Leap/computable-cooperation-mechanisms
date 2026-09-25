"""Multi-plan componentwise comparison for Purpose Generation integration.

This module does not select a winner. It preserves componentwise incomparability.
V0.1 intentionally excludes UNKNOWN dependency and assumption-reversal analysis;
those remain explicit gaps rather than empty-success claims.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


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
