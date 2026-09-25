import unittest

from mechanism_ref.comparison import AssumptionVariant, ComparisonInputError, Plan, UnknownRange, assumption_reversal, compare_plans, dominates, unknown_dependency


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

    def test_unknown_reported_only_when_comparison_changes(self):
        plans = (
            Plan("A", {"benefit": 5.0, "option": 5.0}),
            Plan("B", {"benefit": 4.0, "option": 6.0}),
        )
        dep = unknown_dependency(
            plans,
            plan_id="A",
            unknown=UnknownRange("option", 4.0, 7.0),
        )
        self.assertIsNotNone(dep)
        self.assertEqual(dep["effect"], "comparison_structure_changes_across_range")

    def test_unknown_not_reported_when_structure_is_stable(self):
        plans = (
            Plan("A", {"benefit": 10.0, "option": 10.0}),
            Plan("B", {"benefit": 1.0, "option": 1.0}),
        )
        dep = unknown_dependency(
            plans,
            plan_id="A",
            unknown=UnknownRange("option", 8.0, 12.0),
        )
        self.assertIsNone(dep)

    def test_unknown_range_does_not_choose_endpoint(self):
        dep = unknown_dependency(
            (
                Plan("A", {"x": 1.0, "y": 1.0}),
                Plan("B", {"x": 2.0, "y": 0.0}),
            ),
            plan_id="A",
            unknown=UnknownRange("y", -1.0, 3.0),
        )
        self.assertNotIn("preferred", dep)
        self.assertNotIn("winner", dep)

    def test_assumption_reversal_reported_when_structure_changes(self):
        plans = (
            Plan("A", {"benefit": 5.0, "option": 5.0}),
            Plan("B", {"benefit": 4.0, "option": 6.0}),
        )
        result = assumption_reversal(
            plans,
            (AssumptionVariant("opposite-estimate", "A", "option", 7.0),),
        )
        self.assertIsNotNone(result)
        self.assertEqual(
            result["effect"],
            "comparison_structure_reverses_under_assumption_variant",
        )

    def test_stable_assumption_variant_not_reported_as_reversal(self):
        plans = (
            Plan("A", {"benefit": 10.0, "option": 10.0}),
            Plan("B", {"benefit": 1.0, "option": 1.0}),
        )
        result = assumption_reversal(
            plans,
            (AssumptionVariant("opposite-estimate", "A", "option", 8.0),),
        )
        self.assertIsNone(result)

    def test_assumption_reversal_has_no_preferred_variant(self):
        result = assumption_reversal(
            (
                Plan("A", {"x": 1.0, "y": 1.0}),
                Plan("B", {"x": 2.0, "y": 0.0}),
            ),
            (AssumptionVariant("v1", "A", "y", 3.0),),
        )
        # If the variant does not change comparison structure, None is the
        # correct result and itself proves no preferred/winner field exists.
        if result is not None:
            self.assertNotIn("preferred", result)
            self.assertNotIn("winner", result)
            self.assertNotIn("recommendation", result)

if __name__ == "__main__":
    unittest.main()
