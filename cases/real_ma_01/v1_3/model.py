"""REAL MA 01 V1.3: directional reports plus five proposed boundaries.

This module organizes declared evidence. It does not estimate the merger's
real-world effect, endorse a transaction, or establish legitimate thresholds.
"""

import copy
import math


REPORT_DIMENSIONS = (
    "shipper_cost_usd_per_load",
    "transit_hours_per_load",
)

BOUNDARIES = (
    ("LABOR-TRANSITION", "workforce", "labor_transition_plan_verified", "Labor transition plan verified"),
    ("COMMUNITY-SAFETY", "community", "community_safety_review_verified", "Community safety review verified"),
    ("NONDISCRIMINATORY-ACCESS", "connecting_carrier", "nondiscriminatory_access_verified", "Non-discriminatory access verified"),
    ("HUMAN-OVERRIDE", "operations", "human_override_verified", "Human override verified"),
    ("ROLLBACK-DRILL", "operations", "rollback_drill_verified", "Rollback drill verified"),
)


def _finite_nonnegative(value, path):
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
        raise ValueError(f"{path} must be null or a finite non-negative number")
    return float(value)


def _evidence(value, path):
    if value not in (None, 0, 1) or isinstance(value, bool):
        raise ValueError(f"{path} must be null, 0, or 1")
    return value


def build_ccm_case(empirical_input):
    """Translate the editable evidence file into the public CCM case schema."""
    data = copy.deepcopy(empirical_input)
    measurements = data.get("measurements", {})
    boundary_evidence = data.get("boundary_evidence", {})
    for key in REPORT_DIMENSIONS:
        item = measurements.get(key, {})
        if set(item) != {"a1_independent_ai", "b1_merger_ai"}:
            raise ValueError(f"measurements.{key} must contain a1_independent_ai and b1_merger_ai")
        item["a1_independent_ai"] = _finite_nonnegative(item["a1_independent_ai"], f"measurements.{key}.a1_independent_ai")
        item["b1_merger_ai"] = _finite_nonnegative(item["b1_merger_ai"], f"measurements.{key}.b1_merger_ai")
    for _, _, dimension, _ in BOUNDARIES:
        boundary_evidence[dimension] = _evidence(boundary_evidence.get(dimension), f"boundary_evidence.{dimension}")

    actors = [
        {"id": "shipper", "role": "freight customer"},
        {"id": "workforce", "role": "employees and drivers"},
        {"id": "community", "role": "affected communities"},
        {"id": "connecting_carrier", "role": "connecting and short-line carriers"},
        {"id": "operations", "role": "network operations and accountable human operators"},
    ]
    baseline = [
        {"actor": "shipper", "dimension": REPORT_DIMENSIONS[0], "unit": "USD_PER_LOAD", "value": measurements[REPORT_DIMENSIONS[0]]["a1_independent_ai"]},
        {"actor": "shipper", "dimension": REPORT_DIMENSIONS[1], "unit": "HOUR_PER_LOAD", "value": measurements[REPORT_DIMENSIONS[1]]["a1_independent_ai"]},
    ]
    candidate = [
        {"actor": "shipper", "dimension": REPORT_DIMENSIONS[0], "unit": "USD_PER_LOAD", "value": measurements[REPORT_DIMENSIONS[0]]["b1_merger_ai"]},
        {"actor": "shipper", "dimension": REPORT_DIMENSIONS[1], "unit": "HOUR_PER_LOAD", "value": measurements[REPORT_DIMENSIONS[1]]["b1_merger_ai"]},
    ]
    for _, actor, dimension, _ in BOUNDARIES:
        baseline.append({"actor": actor, "dimension": dimension, "unit": "BINARY_EVIDENCE", "value": None})
        candidate.append({"actor": actor, "dimension": dimension, "unit": "BINARY_EVIDENCE", "value": boundary_evidence[dimension]})

    constraints = [
        {"id": bid, "kind": "outcome", "description": description, "actor": actor, "dimension": dimension, "unit": "BINARY_EVIDENCE", "operator": ">=", "limit": 1, "hard": True}
        for bid, actor, dimension, description in BOUNDARIES
    ]
    return {
        "schema_version": "coop.case.v0.1",
        "case_id": data.get("case_id", "REAL_MA_01_CORRIDOR_V1_3"),
        "title": "REAL MA 01: A1 independent AI cooperation versus B1 merger with comparable AI",
        "units": {"cost": "USD_PER_LOAD", "time": "HOUR_PER_LOAD", "evidence": "BINARY_EVIDENCE"},
        "actors": actors,
        "baseline": {"allocations": {}, "outcomes": baseline},
        "candidate": {"allocations": {}, "outcomes": candidate},
        "constraints": constraints,
        "notes": "Directional cost/time results are report items, not hard constraints. Five proposed boundaries alone determine the declared-constraint status. Null means UNKNOWN. This is not a transaction opinion or effect certification.",
    }


def summarize_result(result):
    """Separate directional results from proposed-boundary checks."""
    deltas = {d["dimension"]: d for d in result["outcome_deltas"] if d["dimension"] in REPORT_DIMENSIONS}
    return {
        "case_id": result["case_id"],
        "comparison": "B1_MINUS_A1",
        "directional_reports": {
            "shipper_cost": deltas[REPORT_DIMENSIONS[0]],
            "transit_time": deltas[REPORT_DIMENSIONS[1]],
        },
        "proposed_boundary_status": result["overall_declared_constraint_status"],
        "proposed_boundary_checks": result["checks"],
        "input_sha256": result["input_sha256"],
        "interpretation_boundary": result["interpretation_boundary"],
    }


def inventory_carrying_savings(cargo_value_usd, annual_holding_rate, hours_saved):
    value = _finite_nonnegative(cargo_value_usd, "cargo_value_usd")
    rate = _finite_nonnegative(annual_holding_rate, "annual_holding_rate")
    hours = _finite_nonnegative(hours_saved, "hours_saved")
    return value * rate * hours / 8760.0


def conditional_scenarios():
    """Return 36 hypothesis-only combinations; none are empirical merger effects."""
    rows = []
    for cargo_value in (50_000, 100_000, 200_000):
        for holding_rate in (0.10, 0.20, 0.30):
            for hours_saved in (12, 24, 25, 48):
                rows.append({
                    "cargo_value_usd": cargo_value,
                    "annual_holding_rate": holding_rate,
                    "hours_saved": hours_saved,
                    "inventory_carrying_savings_usd": inventory_carrying_savings(cargo_value, holding_rate, hours_saved),
                    "evidence_class": "CONDITIONAL_RESEARCH_ASSUMPTION",
                })
    return rows
