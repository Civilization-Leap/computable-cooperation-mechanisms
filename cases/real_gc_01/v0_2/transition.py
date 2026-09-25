"""Directional frontier-transition analysis for REAL GC 01.

Reports changes in non-dominated-set membership under declared conditions.
It does not say that an actor should switch strategy.
"""
from dataclasses import dataclass
from typing import Dict, Tuple

from .model import Configuration, pareto_frontier


@dataclass(frozen=True)
class TransitionCost:
    from_state: str
    to_state: str
    actor: str
    dimension: str
    horizon: str
    value: float
    unit: str
    evidence_state: str
    rationale: str


def frontier_transition(
    before: Tuple[Configuration, ...],
    after: Tuple[Configuration, ...],
    *,
    direction: str,
    transition_costs: Tuple[TransitionCost, ...] = (),
) -> Dict[str, object]:
    """Describe frontier membership changes in one declared direction.

    Transition costs are directional records. A -> B never implies B -> A.
    This function intentionally does not aggregate transition costs into welfare.
    """
    if "->" not in direction:
        raise ValueError("direction must be explicit, e.g. S0->S1")
    for c in transition_costs:
        if f"{c.from_state}->{c.to_state}" != direction:
            raise ValueError("transition cost direction does not match analysis direction")
        if not c.rationale:
            raise ValueError("transition cost requires rationale")

    before_frontier = set(pareto_frontier(before)["frontier"])
    after_frontier = set(pareto_frontier(after)["frontier"])
    entered = sorted(after_frontier - before_frontier)
    exited = sorted(before_frontier - after_frontier)

    return {
        "direction": direction,
        "before_frontier": sorted(before_frontier),
        "after_frontier": sorted(after_frontier),
        "entered_frontier": entered,
        "exited_frontier": exited,
        "transition_costs": [
            {
                "from_state": x.from_state,
                "to_state": x.to_state,
                "actor": x.actor,
                "dimension": x.dimension,
                "horizon": x.horizon,
                "value": x.value,
                "unit": x.unit,
                "evidence_state": x.evidence_state,
                "rationale": x.rationale,
            }
            for x in transition_costs
        ],
        "interpretation_boundary": (
            "Describes a conditional change in Pareto-frontier membership only. "
            "It does not state that any government or actor should switch, "
            "and reverse-direction costs must be analyzed separately."
        ),
    }
