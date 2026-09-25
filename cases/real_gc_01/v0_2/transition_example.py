"""One-command synthetic cost comparison, not a national-policy simulation."""
import json

from .model import Configuration, Measure
from .transition import TransitionCost, frontier_transition


def _configuration(cid, benefit, cost):
    # Fixed schema identifiers are placeholders; both configurations use the
    # same strategy metadata. No numerical claim about any country is made.
    return Configuration(cid, "SYNTHETIC_COST_ACCOUNTING", "S1_BOUNDED_COMP_MIN_COOP", (
        Measure("US", "benefit", "T1", benefit, "CONDITIONAL_ASSUMPTION", "toy_unit"),
        Measure("US", "cost", "T1", cost, "CONDITIONAL_ASSUMPTION", "toy_unit"),
        Measure("CN", "benefit", "T1", 5, "CONDITIONAL_ASSUMPTION", "toy_unit"),
        Measure("TP_GLOBAL_PUBLIC", "risk", "T1", 1, "CONDITIONAL_ASSUMPTION", "toy_unit"),
    ))


def run_example():
    configurations = (_configuration("A", 6, 5), _configuration("B", 7, 2))
    runs = []
    for value in (2, 4, None):
        cost = TransitionCost(
            "A", "B", "US", "cost", "T1", value, "toy_unit",
            "UNKNOWN" if value is None else "CONDITIONAL_ASSUMPTION",
            "Low/high/unknown illustrative burden; all other inputs held fixed.",
            target_configuration="B", source_provenance="PROJECT_ASSUMPTION",
            source_ref="synthetic example only",
        )
        result = frontier_transition(configurations, configurations, direction="A->B",
                                     transition_costs=(cost,))
        runs.append({"declared_burden": value, "result": result})
    return {
        "case": "REAL_GC_01_TRANSITION_COST_SYNTHETIC_EXAMPLE",
        "evidence_class": "CONDITIONAL_ASSUMPTION",
        "empirical_claim": False,
        "independent_validation": False,
        "external_evidence_state_changed": False,
        "policy_recommendation": False,
        "sampled_cost_sensitivity": "SENSITIVE" if runs[0]["result"]["after_frontier"]
        != runs[1]["result"]["after_frontier"] else "NO_CHANGE_IN_TWO_SAMPLES",
        "sensitivity_scope": "Two declared synthetic burdens only; not a plausible empirical range.",
        "runs": runs,
    }


if __name__ == "__main__":
    print(json.dumps(run_example(), ensure_ascii=False, indent=2, allow_nan=False))
