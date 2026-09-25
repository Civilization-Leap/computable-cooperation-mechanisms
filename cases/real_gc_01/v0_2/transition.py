"""Declared-cost frontier comparison; no policy choice or empirical calibration.

Input measures exclude the separately declared feedback and transition burdens.
Feedback is materialized once. A burden changes exactly one existing component.
No cross-actor, cross-dimension, cross-horizon, or currency aggregation occurs.
"""
from dataclasses import asdict, dataclass, replace
from math import isfinite
from typing import Dict, Optional, Tuple

from .model import (
    EVIDENCE_STATES, HIGHER_IS_BETTER, Configuration,
    apply_feedback, boundary_status, pareto_frontier, validate_configuration,
)

PROVENANCE = {"OFFICIAL_SOURCE", "THIRD_PARTY_SOURCE", "PROJECT_ASSUMPTION"}


@dataclass(frozen=True)
class TransitionCost:
    """Nonnegative incremental burden in the target component's own unit.

    Higher-is-better components are reduced; cost/risk components are increased.
    target_configuration is required when applying a cost (no implicit broadcast).
    already_included=True is rejected to prevent declared double accounting.
    """
    from_state: str
    to_state: str
    actor: str
    dimension: str
    horizon: str
    value: Optional[float]
    unit: str
    evidence_state: str
    rationale: str
    target_configuration: str = ""
    source_provenance: str = "PROJECT_ASSUMPTION"
    source_ref: str = ""
    already_included: bool = False


def _key(m):
    return (m.actor, m.dimension, m.horizon, m.unit)


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _validate_scope(before, after):
    """Membership changes require the same declared comparison universe."""
    if not before or not after:
        raise ValueError("before and after must be nonempty")
    for group in (before, after):
        ids = [c.id for c in group]
        if not all(_text(x) for x in ids) or len(ids) != len(set(ids)):
            raise ValueError("configuration ids must be nonempty and unique")
    if {c.id for c in before} != {c.id for c in after}:
        raise ValueError("before/after configuration ids must match")
    domains, scopes, boundary_definitions = set(), [], []
    for c in before + after:
        validate_configuration(c)
        if not _text(c.domain) or not c.measures:
            raise ValueError("nonempty domain and measures required")
        if any(not _text(m.unit) for m in c.measures):
            raise ValueError("measure unit must be nonempty")
        domains.add(c.domain)
        scopes.append({_key(m) for m in c.measures})
        ids = [b.id for b in c.boundaries]
        if not all(_text(x) for x in ids) or len(ids) != len(set(ids)):
            raise ValueError("boundary ids must be nonempty and unique")
        boundary_definitions.append({
            (b.id, b.affected_actor, b.protected_channel,
             b.closure_condition, b.rationale) for b in c.boundaries
        })
    if len(domains) != 1 or any(s != scopes[0] for s in scopes):
        raise ValueError("domain and actor/dimension/horizon/unit scope must match")
    if any(b != boundary_definitions[0] for b in boundary_definitions):
        raise ValueError("compare the same named channel definitions, not different boundaries")


def _materialize_feedback(configurations):
    materialized, trace = [], []
    for c in configurations:
        values = apply_feedback(c)
        targeted = {(s.effect_actor, s.dimension, s.horizon, s.unit)
                    for s in c.feedback_chain}
        measures = tuple(
            replace(m, value=values[_key(m)],
                    evidence_state="UNKNOWN" if values[_key(m)] is None
                    else "CONDITIONAL_ASSUMPTION")
            if _key(m) in targeted else m for m in c.measures
        )
        updated = replace(c, measures=measures, feedback_chain=())
        validate_configuration(updated)  # Reject non-finite derived quantities.
        materialized.append(updated)
        if c.feedback_chain:
            trace.append({"configuration": c.id,
                          "steps": [asdict(s) for s in c.feedback_chain]})
    return tuple(materialized), trace


def _apply_costs(configurations, costs, direction):
    by_id = {c.id: c for c in configurations}
    seen, trace = set(), []
    for cost in costs:
        if f"{cost.from_state}->{cost.to_state}" != direction:
            raise ValueError("transition cost direction does not match analysis direction")
        if not _text(cost.target_configuration) or cost.target_configuration not in by_id:
            raise ValueError("cost requires an explicit existing target_configuration")
        if not _text(cost.rationale):
            raise ValueError("transition cost requires rationale")
        if cost.source_provenance not in PROVENANCE:
            raise ValueError("invalid source_provenance")
        if cost.source_provenance != "PROJECT_ASSUMPTION" and not _text(cost.source_ref):
            raise ValueError("non-project costs require a source_ref")
        if cost.already_included is not False:
            raise ValueError("cost is already included or its accounting basis is unclear")
        if cost.evidence_state not in EVIDENCE_STATES:
            raise ValueError("invalid cost evidence_state")
        if cost.value is None:
            if cost.evidence_state != "UNKNOWN":
                raise ValueError("missing cost must be explicitly UNKNOWN")
        elif (cost.evidence_state == "UNKNOWN" or isinstance(cost.value, bool)
              or not isinstance(cost.value, (int, float))
              or not isfinite(cost.value) or cost.value < 0):
            raise ValueError("known cost must be a finite nonnegative burden")
        c = by_id[cost.target_configuration]
        key = _key(cost)
        if key not in {_key(m) for m in c.measures}:
            raise ValueError("cost target component/unit missing; do not invent a zero baseline")
        identity = (c.id, key)
        if identity in seen:
            raise ValueError("duplicate cost target; declare one non-overlapping burden per component")
        seen.add(identity)
        old = next(m for m in c.measures if _key(m) == key)
        sign = -1 if cost.dimension in HIGHER_IS_BETTER else 1
        value = None if old.value is None or cost.value is None else old.value + sign * cost.value
        updated = replace(old, value=value, evidence_state=(
            "UNKNOWN" if value is None else "CONDITIONAL_ASSUMPTION"))
        replacement = replace(c, measures=tuple(updated if _key(m) == key else m for m in c.measures))
        validate_configuration(replacement)
        by_id[c.id] = replacement
        trace.append({"cost": asdict(cost), "before_component": asdict(old),
                      "operation": "subtract_burden" if sign == -1 else "add_burden",
                      "after_component": asdict(updated)})
    return tuple(by_id[c.id] for c in configurations), trace


def _snapshot(configurations):
    """Do not turn unresolved comparisons or closed channels into a frontier."""
    eligible, excluded, unresolved, channels = [], [], [], {}
    for c in configurations:
        checks = boundary_status(c)
        channels[c.id] = checks
        if "VIOLATED" in checks.values():
            excluded.append(c.id)
            continue
        if "UNKNOWN" in checks.values():
            unresolved.append({"configuration": c.id, "reason": "CHANNEL_EVIDENCE_UNKNOWN"})
        unknown = [_key(m) for m in c.measures if m.value is None]
        if unknown:
            unresolved.append({"configuration": c.id, "reason": "COMPONENT_UNKNOWN",
                               "components": unknown})
        eligible.append(c)
    return {
        "status": "UNDECIDABLE" if unresolved else "COMPLETE_CONDITIONAL",
        "frontier": None if unresolved else sorted(pareto_frontier(eligible)["frontier"]),
        "excluded_by_declared_channels": sorted(excluded),
        "unresolved": unresolved,
        "channel_checks": channels,
    }


def frontier_transition(
    before: Tuple[Configuration, ...],
    after: Tuple[Configuration, ...],
    *,
    direction: str,
    transition_costs: Tuple[TransitionCost, ...] = (),
) -> Dict[str, object]:
    """Compare post-feedback snapshots, applying explicit burdens to after only.

    A -> B never implies B -> A. No undeclared cost is assumed to be zero.
    Known derived values are tagged conditional; raw evidence is kept in traces.
    This routine does not establish coverage or robustness of the input set.
    """
    parts = direction.split("->") if isinstance(direction, str) else []
    if len(parts) != 2 or not all(_text(p) and p == p.strip() for p in parts) or parts[0] == parts[1]:
        raise ValueError("direction requires exactly two distinct nonempty labels")
    before, after, transition_costs = tuple(before), tuple(after), tuple(transition_costs)
    _validate_scope(before, after)
    before_values, before_feedback = _materialize_feedback(before)
    after_values, after_feedback = _materialize_feedback(after)
    adjusted, cost_trace = _apply_costs(after_values, transition_costs, direction)
    pre = _snapshot(before_values)
    unadjusted = _snapshot(after_values)
    post = _snapshot(adjusted)
    complete = pre["frontier"] is not None and post["frontier"] is not None
    return {
        "direction": direction,
        "comparison_status": "COMPLETE_CONDITIONAL" if complete else "UNDECIDABLE",
        "before_frontier": pre["frontier"],
        "after_frontier": post["frontier"],
        "entered_frontier": sorted(set(post["frontier"]) - set(pre["frontier"])) if complete else None,
        "exited_frontier": sorted(set(pre["frontier"]) - set(post["frontier"])) if complete else None,
        "after_before_transition_costs": unadjusted,
        "after_with_transition_costs": post,
        "before_comparison": pre,
        "transition_costs": [asdict(c) for c in transition_costs],
        "transition_costs_applied": bool(transition_costs),
        "cost_trace": cost_trace,
        "feedback_trace": {"before": before_feedback, "after": after_feedback},
        "adjusted_after_measures": [
            {"configuration": c.id, "measures": [asdict(m) for m in c.measures]}
            for c in adjusted
        ],
        "cost_coverage": "DECLARED_ITEMS_ONLY",
        "robustness": "NOT_ASSESSED",
        "interpretation_boundary": (
            "Conditional comparison of declared components and channel evidence only. "
            "It does not state that any government or actor should switch. "
            "No policy ranking, empirical validation, total-cost coverage, or global "
            "robustness is established. Reverse costs require separate inputs. "
            "Missing undeclared costs are not certified as zero; declared UNKNOWN "
            "components block a determinate frontier."
        ),
    }
