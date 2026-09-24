import unittest

from cases.real_gc_01.v0_2.model import (
    Configuration,
    FeedbackStep,
    IrreversibleBoundary,
    Measure,
    apply_feedback,
    boundary_status,
    dominates,
    pareto_frontier,
)


def measures(us_benefit=5, cn_benefit=5, third_risk=3, *, unknown=False):
    return (
        Measure("US", "benefit", "T1", us_benefit, "CONDITIONAL_ASSUMPTION", "index"),
        Measure("CN", "benefit", "T1", cn_benefit, "CONDITIONAL_ASSUMPTION", "index"),
        Measure(
            "TP_GLOBAL_PUBLIC",
            "risk",
            "T1",
            None if unknown else third_risk,
            "UNKNOWN" if unknown else "CONDITIONAL_ASSUMPTION",
            "index",
        ),
    )


class RealGC01V02Tests(unittest.TestCase):
    def test_better_for_one_without_worse_for_others_can_dominate(self):
        a = Configuration("A", "synthetic", "S1_BOUNDED_COMP_MIN_COOP", measures(6, 5, 3))
        b = Configuration("B", "synthetic", "S0_HIGH_COMP_LOW_COOP", measures(5, 5, 3))
        self.assertTrue(dominates(a, b))
        self.assertFalse(dominates(b, a))

    def test_simple_sum_cannot_hide_third_party_harm(self):
        a = Configuration("A", "synthetic", "S2_HIGHER_COOP_RETAINED_COMP", measures(100, 100, 50))
        b = Configuration("B", "synthetic", "S1_BOUNDED_COMP_MIN_COOP", measures(10, 10, 1))
        self.assertFalse(dominates(a, b))
        self.assertFalse(dominates(b, a))
        self.assertEqual({"A", "B"}, set(pareto_frontier([a, b])["frontier"]))

    def test_unknown_prevents_forced_dominance(self):
        a = Configuration("A", "synthetic", "S1_BOUNDED_COMP_MIN_COOP", measures(6, 6, 1))
        b = Configuration("B", "synthetic", "S0_HIGH_COMP_LOW_COOP", measures(5, 5, 0, unknown=True))
        self.assertIsNone(dominates(a, b))
        self.assertTrue(pareto_frontier([a, b])["undecidable_pairs"])

    def test_irreversible_boundary_violation_blocks_dominance(self):
        boundary = IrreversibleBoundary(
            "SYS-RISK", "TP_GLOBAL_PUBLIC", "risk", "T1", "<=", 10, "index"
        )
        a = Configuration(
            "A", "synthetic", "S2_HIGHER_COOP_RETAINED_COMP",
            measures(100, 100, 50), (boundary,)
        )
        b = Configuration(
            "B", "synthetic", "S1_BOUNDED_COMP_MIN_COOP",
            measures(1, 1, 1), (boundary,)
        )
        self.assertEqual("VIOLATED", boundary_status(a)["SYS-RISK"])
        self.assertFalse(dominates(a, b))

    def test_feedback_returns_consequences_to_initiator(self):
        c = Configuration(
            "A",
            "synthetic",
            "S3_ESCALATORY_RECURSION",
            measures(10, 5, 3),
            feedback_chain=(
                FeedbackStep(
                    1, "CN", "US", "benefit", "T1", -12,
                    "CONDITIONAL_ASSUMPTION", "index",
                    "counteraction returns a cost to the initiating actor",
                ),
            ),
        )
        result = apply_feedback(c)
        self.assertEqual(-2.0, result[("US", "benefit", "T1", "index")])

    def test_unknown_feedback_propagates(self):
        c = Configuration(
            "A",
            "synthetic",
            "S3_ESCALATORY_RECURSION",
            measures(),
            feedback_chain=(
                FeedbackStep(
                    1, "CN", "US", "benefit", "T1", None,
                    "UNKNOWN", "index", "response magnitude unknown",
                ),
            ),
        )
        result = apply_feedback(c)
        self.assertIsNone(result[("US", "benefit", "T1", "index")])

    def test_no_policy_winner_field_is_produced(self):
        a = Configuration("A", "synthetic", "S1_BOUNDED_COMP_MIN_COOP", measures(6, 5, 3))
        b = Configuration("B", "synthetic", "S0_HIGH_COMP_LOW_COOP", measures(5, 5, 3))
        result = pareto_frontier([a, b])
        self.assertNotIn("winner", result)
        self.assertNotIn("recommendation", result)
        self.assertIn("not a policy ranking", result["interpretation_boundary"])


if __name__ == "__main__":
    unittest.main()
