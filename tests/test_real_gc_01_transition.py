import unittest

from cases.real_gc_01.v0_2.model import Configuration, Measure
from cases.real_gc_01.v0_2.transition import TransitionCost, frontier_transition


def config(cid, state, us, cn, risk):
    return Configuration(
        cid, "SYNTHETIC_TRANSITION", state,
        (
            Measure("US", "benefit", "T1", us, "CONDITIONAL_ASSUMPTION", "index"),
            Measure("CN", "benefit", "T1", cn, "CONDITIONAL_ASSUMPTION", "index"),
            Measure("TP_GLOBAL_PUBLIC", "risk", "T1", risk, "CONDITIONAL_ASSUMPTION", "index"),
        ),
    )


class RealGC01TransitionTests(unittest.TestCase):
    def test_reports_frontier_membership_change_without_should(self):
        before = (
            config("S0", "S0_HIGH_COMP_LOW_COOP", 6, 6, 3),
            config("S1", "S1_BOUNDED_COMP_MIN_COOP", 5, 5, 3),
        )
        after = (
            config("S0", "S0_HIGH_COMP_LOW_COOP", 4, 4, 5),
            config("S1", "S1_BOUNDED_COMP_MIN_COOP", 5, 5, 3),
        )
        result = frontier_transition(before, after, direction="S0->S1")
        self.assertEqual(["S1"], result["entered_frontier"])
        self.assertEqual(["S0"], result["exited_frontier"])
        rendered = str(result).lower()
        self.assertNotIn("should_switch", rendered)
        self.assertNotIn("recommendation", result)

    def test_transition_cost_is_directional_not_symmetric(self):
        before = (config("S0", "S0_HIGH_COMP_LOW_COOP", 6, 6, 3),)
        after = (config("S0", "S0_HIGH_COMP_LOW_COOP", 6, 6, 3),)
        forward = TransitionCost(
            "S0", "S1", "TP_FIRMS_WORKERS", "cost", "T1", 2, "index",
            "CONDITIONAL_ASSUMPTION", "synthetic restructuring cost"
        )
        result = frontier_transition(before, after, direction="S0->S1", transition_costs=(forward,))
        self.assertEqual("S0", result["transition_costs"][0]["from_state"])
        self.assertEqual("S1", result["transition_costs"][0]["to_state"])
        with self.assertRaises(ValueError):
            frontier_transition(before, after, direction="S1->S0", transition_costs=(forward,))

    def test_reverse_direction_can_have_different_cost(self):
        c = config("S1", "S1_BOUNDED_COMP_MIN_COOP", 5, 5, 3)
        forward = TransitionCost(
            "S0", "S1", "TP_FIRMS_WORKERS", "cost", "T1", 2, "index",
            "CONDITIONAL_ASSUMPTION", "synthetic forward cost"
        )
        reverse = TransitionCost(
            "S1", "S0", "TP_FIRMS_WORKERS", "cost", "T1", 7, "index",
            "CONDITIONAL_ASSUMPTION", "synthetic reverse cost after relationship restructuring"
        )
        f = frontier_transition((c,), (c,), direction="S0->S1", transition_costs=(forward,))
        r = frontier_transition((c,), (c,), direction="S1->S0", transition_costs=(reverse,))
        self.assertNotEqual(f["transition_costs"][0]["value"], r["transition_costs"][0]["value"])

    def test_transition_output_has_no_winner(self):
        c = config("S1", "S1_BOUNDED_COMP_MIN_COOP", 5, 5, 3)
        result = frontier_transition((c,), (c,), direction="S0->S1")
        self.assertNotIn("winner", result)
        self.assertIn("does not state", result["interpretation_boundary"])


if __name__ == "__main__":
    unittest.main()
