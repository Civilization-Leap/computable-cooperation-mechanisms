"""Synthetic S0-S3 conditional grid for REAL GC 01.

Numbers are dimensionless research assumptions. They are not measurements,
forecasts, policy scores, or descriptions of either country.
"""
import json

from .model import Configuration, FeedbackStep, IrreversibleBoundary, Measure, apply_feedback, boundary_status, pareto_frontier

ACTORS = ("US", "CN", "TP_GLOBAL_PUBLIC")
STATE_VALUES = {
    # benefit, risk, option value for US / CN / global third-party interest
    "S0_HIGH_COMP_LOW_COOP": {
        "US": (7, 7, 5), "CN": (7, 7, 5), "TP_GLOBAL_PUBLIC": (3, 8, 4),
    },
    "S1_BOUNDED_COMP_MIN_COOP": {
        "US": (8, 4, 7), "CN": (8, 4, 7), "TP_GLOBAL_PUBLIC": (6, 4, 7),
    },
    "S2_HIGHER_COOP_RETAINED_COMP": {
        "US": (9, 3, 6), "CN": (9, 3, 6), "TP_GLOBAL_PUBLIC": (8, 3, 6),
    },
    "S3_ESCALATORY_RECURSION": {
        "US": (10, 10, 2), "CN": (10, 10, 2), "TP_GLOBAL_PUBLIC": (2, 12, 1),
    },
}


def _measures(values):
    out = []
    for actor, (benefit, risk, option_value) in values.items():
        out.extend([
            Measure(actor, "benefit", "T1", benefit, "CONDITIONAL_ASSUMPTION", "synthetic_index"),
            Measure(actor, "risk", "T1", risk, "CONDITIONAL_ASSUMPTION", "synthetic_index"),
            Measure(actor, "option_value", "T1", option_value, "CONDITIONAL_ASSUMPTION", "synthetic_index"),
        ])
    return tuple(out)


def build_grid():
    boundary = IrreversibleBoundary(
        "GLOBAL-RECOVERY-CHANNEL",
        "TP_GLOBAL_PUBLIC",
        "recovery",
        "loss of a credible correction/recovery channel after systemic escalation",
        "CONDITIONAL_ASSUMPTION",
        True,
        "synthetic mechanism test; not a claim about real U.S.-China conditions",
    )
    configs = []
    for state, values in STATE_VALUES.items():
        feedback = ()
        if state == "S3_ESCALATORY_RECURSION":
            feedback = (
                FeedbackStep(1, "CN", "US", "benefit", "T1", -6, "CONDITIONAL_ASSUMPTION", "synthetic_index", "synthetic counteraction feedback"),
                FeedbackStep(2, "US", "CN", "benefit", "T1", -6, "CONDITIONAL_ASSUMPTION", "synthetic_index", "synthetic reciprocal feedback"),
            )
        state_boundary = boundary
        if state == "S3_ESCALATORY_RECURSION":
            state_boundary = IrreversibleBoundary(
                boundary.id, boundary.affected_actor, boundary.protected_channel,
                boundary.closure_condition, boundary.evidence_state, False, boundary.rationale
            )
        configs.append(Configuration(state, "SYNTHETIC_CROSS_DOMAIN", state, _measures(values), (state_boundary,), feedback))
    return configs


def run_grid():
    configs = build_grid()
    return {
        "study_id": "REAL_GC_01_V0_2_SYNTHETIC_GRID_01",
        "evidence_class": "CONDITIONAL_ASSUMPTION",
        "empirical_claim": False,
        "policy_recommendation": False,
        "configurations": [
            {
                "id": c.id,
                "boundary_status": boundary_status(c),
                "post_feedback": {
                    "|".join(k): v for k, v in sorted(apply_feedback(c).items())
                },
            }
            for c in configs
        ],
        "pareto": pareto_frontier(configs),
        "interpretation_boundary": (
            "Synthetic mechanism test only. Values are deliberately constructed "
            "to test representation and decision logic; they are not empirical "
            "estimates of U.S., China, or third-party outcomes."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run_grid(), ensure_ascii=False, indent=2, sort_keys=True))
