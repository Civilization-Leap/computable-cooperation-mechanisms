"""REAL GC 01 V0.2 minimal research model.

This module compares declared conditional configurations. It does not score,
rank, recommend, or predict U.S.–China policy.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Dict, Iterable, List, Optional, Tuple

EVIDENCE_STATES = {
    "OBSERVED",
    "OFFICIAL_CLAIM",
    "THIRD_PARTY_ESTIMATE",
    "CONDITIONAL_ASSUMPTION",
    "UNKNOWN",
}
HORIZONS = {"T0", "T1", "T2"}
STRATEGY_STATES = {
    "S0_HIGH_COMP_LOW_COOP",
    "S1_BOUNDED_COMP_MIN_COOP",
    "S2_HIGHER_COOP_RETAINED_COMP",
    "S3_ESCALATORY_RECURSION",
}
ACTORS = {
    "US",
    "CN",
    "TP_ALLIES_PARTNERS",
    "TP_OTHER_STATES",
    "TP_FIRMS_WORKERS",
    "TP_GLOBAL_PUBLIC",
}
DIMENSIONS = {"benefit", "cost", "risk", "feedback", "option_value"}
HIGHER_IS_BETTER = {"benefit", "feedback", "option_value"}
LOWER_IS_BETTER = {"cost", "risk"}


@dataclass(frozen=True)
class Measure:
    actor: str
    dimension: str
    horizon: str
    value: Optional[float]
    evidence_state: str
    unit: str


@dataclass(frozen=True)
class IrreversibleBoundary:
    id: str
    actor: str
    dimension: str
    horizon: str
    operator: str
    limit: float
    unit: str


@dataclass(frozen=True)
class FeedbackStep:
    order: int
    actor: str
    effect_actor: str
    dimension: str
    horizon: str
    delta: Optional[float]
    evidence_state: str
    unit: str
    description: str


@dataclass(frozen=True)
class Configuration:
    id: str
    domain: str
    strategy_state: str
    measures: Tuple[Measure, ...]
    boundaries: Tuple[IrreversibleBoundary, ...] = ()
    feedback_chain: Tuple[FeedbackStep, ...] = ()


def _finite_or_none(value: Optional[float], path: str) -> None:
    if value is None:
        return
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not isfinite(value):
        raise ValueError(f"{path}: expected finite number or None")


def validate_configuration(c: Configuration) -> None:
    if c.strategy_state not in STRATEGY_STATES:
        raise ValueError("unknown strategy_state")
    seen = set()
    for m in c.measures:
        if m.actor not in ACTORS:
            raise ValueError(f"unknown actor: {m.actor}")
        if m.dimension not in DIMENSIONS:
            raise ValueError(f"unknown dimension: {m.dimension}")
        if m.horizon not in HORIZONS:
            raise ValueError(f"unknown horizon: {m.horizon}")
        if m.evidence_state not in EVIDENCE_STATES:
            raise ValueError(f"unknown evidence_state: {m.evidence_state}")
        if m.evidence_state == "UNKNOWN" and m.value is not None:
            raise ValueError("UNKNOWN evidence must keep value None")
        if m.evidence_state != "UNKNOWN" and m.value is None:
            raise ValueError("known evidence state requires a value")
        _finite_or_none(m.value, "measure.value")
        key = (m.actor, m.dimension, m.horizon, m.unit)
        if key in seen:
            raise ValueError(f"duplicate measure: {key}")
        seen.add(key)
    for b in c.boundaries:
        if b.actor not in ACTORS or b.dimension not in DIMENSIONS or b.horizon not in HORIZONS:
            raise ValueError(f"invalid boundary: {b.id}")
        if b.operator not in {"<=", ">="}:
            raise ValueError(f"invalid boundary operator: {b.operator}")
        _finite_or_none(b.limit, "boundary.limit")
    orders = [x.order for x in c.feedback_chain]
    if orders != sorted(orders) or len(orders) != len(set(orders)):
        raise ValueError("feedback steps must have unique ascending order")
    for step in c.feedback_chain:
        if step.actor not in ACTORS or step.effect_actor not in ACTORS:
            raise ValueError("invalid feedback actor")
        if step.dimension not in DIMENSIONS or step.horizon not in HORIZONS:
            raise ValueError("invalid feedback dimension/horizon")
        if step.evidence_state not in EVIDENCE_STATES:
            raise ValueError("invalid feedback evidence_state")
        if step.evidence_state == "UNKNOWN" and step.delta is not None:
            raise ValueError("UNKNOWN feedback must keep delta None")
        if step.evidence_state != "UNKNOWN" and step.delta is None:
            raise ValueError("known feedback requires delta")
        _finite_or_none(step.delta, "feedback.delta")


def boundary_status(c: Configuration) -> Dict[str, str]:
    validate_configuration(c)
    idx = {(m.actor, m.dimension, m.horizon, m.unit): m.value for m in c.measures}
    out: Dict[str, str] = {}
    for b in c.boundaries:
        value = idx.get((b.actor, b.dimension, b.horizon, b.unit))
        if value is None:
            out[b.id] = "UNKNOWN"
        else:
            ok = value <= b.limit if b.operator == "<=" else value >= b.limit
            out[b.id] = "SATISFIED" if ok else "VIOLATED"
    return out


def apply_feedback(c: Configuration) -> Dict[Tuple[str, str, str, str], Optional[float]]:
    """Apply only explicitly declared feedback deltas.

    UNKNOWN propagates rather than becoming zero.
    """
    validate_configuration(c)
    values = {(m.actor, m.dimension, m.horizon, m.unit): m.value for m in c.measures}
    for step in c.feedback_chain:
        key = (step.effect_actor, step.dimension, step.horizon, step.unit)
        if key not in values:
            raise ValueError(f"feedback target has no declared measure: {key}")
        if values[key] is None or step.delta is None:
            values[key] = None
        else:
            values[key] = float(values[key]) + float(step.delta)
    return values


def _comparable_index(c: Configuration):
    validate_configuration(c)
    return {(m.actor, m.dimension, m.horizon, m.unit): m.value for m in c.measures}


def dominates(a: Configuration, b: Configuration) -> Optional[bool]:
    """Return True/False when dominance is decidable, else None.

    A configuration cannot dominate another if it violates a declared
    irreversible boundary. UNKNOWN values prevent a forced dominance result.
    """
    if any(v == "VIOLATED" for v in boundary_status(a).values()):
        return False
    ai, bi = _comparable_index(a), _comparable_index(b)
    if set(ai) != set(bi):
        return None
    weakly_better = True
    strictly_better = False
    for key in ai:
        av, bv = ai[key], bi[key]
        if av is None or bv is None:
            return None
        dimension = key[1]
        if dimension in HIGHER_IS_BETTER:
            if av < bv:
                weakly_better = False
            if av > bv:
                strictly_better = True
        else:
            if av > bv:
                weakly_better = False
            if av < bv:
                strictly_better = True
    return weakly_better and strictly_better


def pareto_frontier(configurations: Iterable[Configuration]) -> Dict[str, object]:
    configs = list(configurations)
    for c in configs:
        validate_configuration(c)
    dominated_by: Dict[str, List[str]] = {c.id: [] for c in configs}
    undecidable_pairs = []
    for target in configs:
        for challenger in configs:
            if target.id == challenger.id:
                continue
            d = dominates(challenger, target)
            if d is True:
                dominated_by[target.id].append(challenger.id)
            elif d is None and challenger.id < target.id:
                undecidable_pairs.append([challenger.id, target.id])
    frontier = [c.id for c in configs if not dominated_by[c.id]]
    return {
        "frontier": frontier,
        "dominated_by": dominated_by,
        "undecidable_pairs": undecidable_pairs,
        "interpretation_boundary": (
            "Conditional non-dominance over declared dimensions only; "
            "not a policy ranking, recommendation, forecast, or empirical validation."
        ),
    }
