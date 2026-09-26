"""Synthetic assumption-sensitivity gate for REAL GC 01.

No values in this module are empirical U.S.-China estimates.
"""
from dataclasses import dataclass, replace
from typing import Dict, Tuple

from .model import Configuration, Measure, pareto_frontier


@dataclass(frozen=True)
class ProjectAssumption:
    id: str
    rationale: str
    baseline_value: float
    alternative_value: float
    target_configuration: str
    actor: str
    dimension: str
    horizon: str
    unit: str
    source_provenance: str = "PROJECT_ASSUMPTION"


def _replace_measure(c: Configuration, a: ProjectAssumption, value: float) -> Configuration:
    found = False
    measures = []
    for m in c.measures:
        if (m.actor, m.dimension, m.horizon, m.unit) == (a.actor, a.dimension, a.horizon, a.unit):
            measures.append(replace(m, value=value, evidence_state="CONDITIONAL_ASSUMPTION"))
            found = True
        else:
            measures.append(m)
    if not found:
        raise ValueError(f"assumption target not found: {a.id}")
    return replace(c, measures=tuple(measures))


def evaluate_assumption_sensitivity(
    configurations: Tuple[Configuration, ...],
    assumptions: Tuple[ProjectAssumption, ...],
) -> Dict[str, object]:
    """Compare baseline and reasoned alternatives.

    ROBUST: frontier unchanged across all declared alternatives.
    SENSITIVE: at least one alternative changes frontier membership.
    UNDECIDABLE: a project assumption lacks a usable alternative.
    """
    if not assumptions:
        return {
            "status": "ROBUST",
            "baseline_frontier": pareto_frontier(configurations)["frontier"],
            "alternative_frontiers": [],
            "reason": "no project assumptions declared",
        }
    for a in assumptions:
        if a.source_provenance != "PROJECT_ASSUMPTION":
            raise ValueError("sensitivity gate accepts PROJECT_ASSUMPTION only")
        if not a.rationale:
            raise ValueError("project assumption requires rationale")
        if a.alternative_value is None:
            return {
                "status": "UNDECIDABLE",
                "code": "SENSITIVITY_NOT_TESTED",
                "reason": f"missing alternative for {a.id}",
            }

    baseline = list(configurations)
    for a in assumptions:
        baseline = [
            _replace_measure(c, a, a.baseline_value) if c.id == a.target_configuration else c
            for c in baseline
        ]
    baseline_frontier = pareto_frontier(baseline)["frontier"]

    alternative_frontiers = []
    changed = False
    for a in assumptions:
        variant = list(baseline)
        variant = [
            _replace_measure(c, a, a.alternative_value) if c.id == a.target_configuration else c
            for c in variant
        ]
        frontier = pareto_frontier(variant)["frontier"]
        alternative_frontiers.append({"assumption_id": a.id, "frontier": frontier})
        if set(frontier) != set(baseline_frontier):
            changed = True

    return {
        "status": "SENSITIVE" if changed else "ROBUST",
        "baseline_frontier": baseline_frontier,
        "alternative_frontiers": alternative_frontiers,
        "interpretation_boundary": (
            "Reports dependence of the conditional frontier on declared project assumptions; "
            "does not select a politically correct value or recommend a policy."
        ),
    }
