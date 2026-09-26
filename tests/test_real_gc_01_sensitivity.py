import unittest

from cases.real_gc_01.v0_2.model import Configuration, Measure
from cases.real_gc_01.v0_2.sensitivity import ProjectAssumption, evaluate_assumption_sensitivity


def config(cid, us_benefit, cn_benefit, third_risk):
    return Configuration(
        cid,
        "SYNTHETIC_SENSITIVITY",
        "S1_BOUNDED_COMP_MIN_COOP",
        (
            Measure("US", "benefit", "T1", us_benefit, "CONDITIONAL_ASSUMPTION", "index"),
            Measure("CN", "benefit", "T1", cn_benefit, "CONDITIONAL_ASSUMPTION", "index"),
            Measure("TP_GLOBAL_PUBLIC", "risk", "T1", third_risk, "CONDITIONAL_ASSUMPTION", "index"),
        ),
    )


class RealGC01SensitivityTests(unittest.TestCase):
    def test_opposite_reasoned_value_can_flip_frontier_and_is_sensitive(self):
        a = config("A", 6, 6, 3)
        b = config("B", 5, 5, 3)
        assumption = ProjectAssumption(
            "A-US-BENEFIT",
            "Synthetic counter-assumption tests whether the apparent frontier depends on the project value.",
            6,
            4,
            "A",
            "US",
            "benefit",
            "T1",
            "index",
        )
        result = evaluate_assumption_sensitivity((a, b), (assumption,))
        self.assertEqual("SENSITIVE", result["status"])
        self.assertEqual(["A"], result["baseline_frontier"])
        self.assertEqual({"A", "B"}, set(result["alternative_frontiers"][0]["frontier"]))

    def test_unchanged_frontier_is_robust(self):
        a = config("A", 8, 8, 2)
        b = config("B", 5, 5, 4)
        assumption = ProjectAssumption(
            "A-US-BENEFIT",
            "Alternative remains component-wise superior.",
            8,
            7,
            "A",
            "US",
            "benefit",
            "T1",
            "index",
        )
        result = evaluate_assumption_sensitivity((a, b), (assumption,))
        self.assertEqual("ROBUST", result["status"])
        self.assertEqual(["A"], result["baseline_frontier"])
        self.assertEqual(["A"], result["alternative_frontiers"][0]["frontier"])

    def test_missing_alternative_blocks_robust_frontier_claim(self):
        a = config("A", 6, 6, 3)
        b = config("B", 5, 5, 3)
        assumption = ProjectAssumption(
            "A-US-BENEFIT",
            "Deliberately incomplete project assumption.",
            6,
            None,
            "A",
            "US",
            "benefit",
            "T1",
            "index",
        )
        result = evaluate_assumption_sensitivity((a, b), (assumption,))
        self.assertEqual("UNDECIDABLE", result["status"])
        self.assertEqual("SENSITIVITY_NOT_TESTED", result["code"])

    def test_output_contains_no_winner_or_recommendation(self):
        a = config("A", 6, 6, 3)
        b = config("B", 5, 5, 3)
        assumption = ProjectAssumption(
            "A-US-BENEFIT", "Synthetic alternative.", 6, 4,
            "A", "US", "benefit", "T1", "index"
        )
        result = evaluate_assumption_sensitivity((a, b), (assumption,))
        self.assertNotIn("winner", result)
        self.assertNotIn("recommendation", result)


if __name__ == "__main__":
    unittest.main()
