import unittest

from mechanism_ref.comparison import ComparisonInputError, Plan, compare_plans, dominates


class ComparisonTests(unittest.TestCase):
    def test_tradeoff_is_incomparable_not_aggregated(self):
        a = Plan("A", {"benefit": 10.0, "option_value": 0.0})
        b = Plan("B", {"benefit": 0.0, "option_value": 10.0})
        self.assertFalse(dominates(a, b))
        self.assertFalse(dominates(b, a))
        result = compare_plans((a, b))
        self.assertEqual(result["non_dominated"], ["A", "B"])
        self.assertEqual(result["incomparable"], [["A", "B"]])

    def test_componentwise_dominance(self):
        a = Plan("A", {"x": 2.0, "y": 3.0})
        b = Plan("B", {"x": 1.0, "y": 3.0})
        self.assertTrue(dominates(a, b))
        result = compare_plans((a, b))
        self.assertEqual(result["non_dominated"], ["A"])
        self.assertEqual(result["dominated"], ["B"])

    def test_equal_plans_do_not_dominate_each_other(self):
        a = Plan("A", {"x": 1.0})
        b = Plan("B", {"x": 1.0})
        self.assertFalse(dominates(a, b))
        self.assertFalse(dominates(b, a))

    def test_mismatched_components_fail_closed(self):
        with self.assertRaises(ComparisonInputError):
            dominates(Plan("A", {"x": 1.0}), Plan("B", {"y": 1.0}))

    def test_no_winner_or_score_output(self):
        result = compare_plans((Plan("A", {"x": 2.0}), Plan("B", {"x": 1.0})))
        self.assertNotIn("winner", result)
        self.assertNotIn("score", result)
        self.assertNotIn("recommended_goal", result)
        self.assertIn("capability_gaps", result)


if __name__ == "__main__":
    unittest.main()
