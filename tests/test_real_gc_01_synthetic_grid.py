import unittest

from cases.real_gc_01.v0_2.synthetic_grid import build_grid, run_grid


class RealGC01SyntheticGridTests(unittest.TestCase):
    def test_four_strategy_states_are_present(self):
        self.assertEqual(4, len(build_grid()))

    def test_escalatory_state_crosses_declared_synthetic_boundary(self):
        result = run_grid()
        s3 = next(x for x in result["configurations"] if x["id"] == "S3_ESCALATORY_RECURSION")
        self.assertEqual("VIOLATED", s3["boundary_status"]["GLOBAL-SYSTEMIC-RISK-T1"])

    def test_feedback_reverses_s3_initial_bilateral_benefit(self):
        result = run_grid()
        s3 = next(x for x in result["configurations"] if x["id"] == "S3_ESCALATORY_RECURSION")
        self.assertEqual(4.0, s3["post_feedback"]["US|benefit|T1|synthetic_index"])
        self.assertEqual(4.0, s3["post_feedback"]["CN|benefit|T1|synthetic_index"])

    def test_synthetic_grid_makes_no_empirical_or_policy_claim(self):
        result = run_grid()
        self.assertFalse(result["empirical_claim"])
        self.assertFalse(result["policy_recommendation"])
        self.assertEqual("CONDITIONAL_ASSUMPTION", result["evidence_class"])

    def test_frontier_is_reported_without_winner(self):
        result = run_grid()
        self.assertIn("frontier", result["pareto"])
        self.assertNotIn("winner", result["pareto"])


if __name__ == "__main__":
    unittest.main()
