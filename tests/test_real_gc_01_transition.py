import copy
import math
import unittest
from dataclasses import replace

from cases.real_gc_01.v0_2.model import Configuration, FeedbackStep, IrreversibleBoundary, Measure
from cases.real_gc_01.v0_2.transition import TransitionCost, frontier_transition


STATE = "S1_BOUNDED_COMP_MIN_COOP"
EVIDENCE = "CONDITIONAL_ASSUMPTION"


def config(cid, state, us, cn, risk, cost=2):
    return Configuration(cid, "SYNTHETIC_TRANSITION", state, (
        Measure("US", "benefit", "T1", us, EVIDENCE, "index"),
        Measure("US", "cost", "T1", cost, EVIDENCE, "index"),
        Measure("CN", "benefit", "T1", cn, EVIDENCE, "index"),
        Measure("TP_GLOBAL_PUBLIC", "risk", "T1", risk, EVIDENCE, "index"),
        Measure("TP_FIRMS_WORKERS", "cost", "T1", 0, EVIDENCE, "index"),
    ))


def pair():
    # Pure arithmetic fixture; no state-specific empirical or policy assumptions.
    return (config("A", STATE, 6, 5, 1, 5), config("B", STATE, 7, 5, 1, 2))


def burden(value=4, **kwargs):
    cost = TransitionCost("A", "B", "US", "cost", "T1", value, "index",
                          "UNKNOWN" if value is None else EVIDENCE,
                          "synthetic incremental burden", target_configuration="B")
    return replace(cost, **kwargs)


def measure(result, cid="B", dimension="cost", actor="US", horizon="T1"):
    row = next(x for x in result["adjusted_after_measures"] if x["configuration"] == cid)
    return next(m for m in row["measures"] if (m["actor"], m["dimension"], m["horizon"])
                == (actor, dimension, horizon))


def channel(configurations, b_open):
    boundary = IrreversibleBoundary("RECOVERY", "TP_GLOBAL_PUBLIC", "recovery",
                                    "synthetic channel unavailable", EVIDENCE, True,
                                    "named synthetic criterion, not inferred from cost")
    return tuple(replace(c, boundaries=(replace(boundary,
                 channel_open=b_open if c.id == "B" else True,
                 evidence_state="UNKNOWN" if c.id == "B" and b_open is None else EVIDENCE),))
                 for c in configurations)


class RealGC01TransitionTests(unittest.TestCase):
    # Original four behavioral checks retained, with formerly unbound costs fixed.
    def test_reports_frontier_membership_change_without_should(self):
        before = (config("S0", "S0_HIGH_COMP_LOW_COOP", 6, 6, 3),
                  config("S1", STATE, 5, 5, 3))
        after = (config("S0", "S0_HIGH_COMP_LOW_COOP", 4, 4, 5),
                 config("S1", STATE, 5, 5, 3))
        result = frontier_transition(before, after, direction="S0->S1")
        self.assertEqual(["S1"], result["entered_frontier"])
        self.assertEqual(["S0"], result["exited_frontier"])
        self.assertNotIn("should_switch", str(result).lower())
        self.assertNotIn("recommendation", result)

    def test_transition_cost_is_directional_not_symmetric(self):
        cases = (config("S0", "S0_HIGH_COMP_LOW_COOP", 6, 6, 3),
                 config("S1", STATE, 6, 6, 3))
        forward = TransitionCost("S0", "S1", "TP_FIRMS_WORKERS", "cost", "T1", 2,
                                 "index", EVIDENCE, "synthetic restructuring cost",
                                 target_configuration="S1")
        result = frontier_transition(cases, cases, direction="S0->S1", transition_costs=(forward,))
        self.assertEqual(2, measure(result, "S1", actor="TP_FIRMS_WORKERS")["value"])
        with self.assertRaises(ValueError):
            frontier_transition(cases, cases, direction="S1->S0", transition_costs=(forward,))

    def test_reverse_direction_can_have_different_cost(self):
        cases = (config("S0", "S0_HIGH_COMP_LOW_COOP", 6, 6, 3),
                 config("S1", STATE, 6, 6, 3))
        forward = TransitionCost("S0", "S1", "TP_FIRMS_WORKERS", "cost", "T1", 2,
                                 "index", EVIDENCE, "forward fixture", target_configuration="S1")
        reverse = replace(forward, from_state="S1", to_state="S0", value=7,
                          target_configuration="S0", rationale="reverse fixture")
        f = frontier_transition(cases, cases, direction="S0->S1", transition_costs=(forward,))
        r = frontier_transition(cases, cases, direction="S1->S0", transition_costs=(reverse,))
        self.assertEqual(2, measure(f, "S1", actor="TP_FIRMS_WORKERS")["value"])
        self.assertEqual(7, measure(r, "S0", actor="TP_FIRMS_WORKERS")["value"])

    def test_transition_output_has_no_winner(self):
        result = frontier_transition(pair(), pair(), direction="A->B")
        self.assertNotIn("winner", result)
        self.assertIn("does not state", result["interpretation_boundary"])
        self.assertEqual("NOT_ASSESSED", result["robustness"])

    def test_cost_is_applied_and_changes_conditional_membership(self):
        result = frontier_transition(pair(), pair(), direction="A->B", transition_costs=(burden(),))
        self.assertEqual(["B"], result["after_before_transition_costs"]["frontier"])
        self.assertEqual(["A", "B"], result["after_frontier"])
        self.assertEqual(6, measure(result)["value"])
        self.assertEqual(7, measure(result, dimension="benefit")["value"])
        self.assertEqual(5, measure(result, "A")["value"])
        self.assertTrue(result["transition_costs_applied"])

    def test_known_alternative_costs_and_unknown_are_distinct(self):
        def run(value):
            return frontier_transition(pair(), pair(), direction="A->B",
                                       transition_costs=(burden(value),))
        self.assertEqual(["B"], run(2)["after_frontier"])
        self.assertEqual(["A", "B"], run(4)["after_frontier"])
        unknown = run(None)
        self.assertEqual("UNDECIDABLE", unknown["comparison_status"])
        for key in ("after_frontier", "entered_frontier", "exited_frontier"):
            self.assertIsNone(unknown[key])
        self.assertIsNone(measure(unknown)["value"])
        self.assertEqual("UNKNOWN", measure(unknown)["evidence_state"])

    def test_unknown_baseline_is_not_filled_with_zero(self):
        a, b = pair()
        b = replace(b, measures=tuple(replace(m, value=None, evidence_state="UNKNOWN")
                                      if m.actor == "US" and m.dimension == "cost" else m
                                      for m in b.measures))
        result = frontier_transition((a, b), (a, b), direction="A->B", transition_costs=(burden(2),))
        self.assertIsNone(measure(result)["value"])
        self.assertIsNone(result["after_frontier"])

    def test_target_actor_horizon_and_unit_are_not_guessed(self):
        for change in ({"target_configuration": ""}, {"target_configuration": "missing"},
                       {"actor": "TP_OTHER_STATES"}, {"unit": "USD"}, {"horizon": "T2"}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                frontier_transition(pair(), pair(), direction="A->B",
                                    transition_costs=(burden(**change),))

    def test_invalid_costs_and_evidence_are_rejected(self):
        for value in (-1, math.nan, math.inf, True, "4"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                frontier_transition(pair(), pair(), direction="A->B", transition_costs=(burden(value),))
        for cost in (burden(2, evidence_state="UNKNOWN"), burden(None, evidence_state=EVIDENCE),
                     burden(2, evidence_state="MISSING"), burden(2, rationale=" ")):
            with self.subTest(cost=cost), self.assertRaises(ValueError):
                frontier_transition(pair(), pair(), direction="A->B", transition_costs=(cost,))

    def test_duplicate_or_preincluded_cost_is_rejected(self):
        for costs in ((burden(), burden()), (burden(already_included=True),)):
            with self.subTest(costs=costs), self.assertRaises(ValueError):
                frontier_transition(pair(), pair(), direction="A->B", transition_costs=costs)

    def test_higher_is_better_burden_does_not_net_across_components(self):
        result = frontier_transition(pair(), pair(), direction="A->B",
                                    transition_costs=(burden(2, dimension="benefit"),))
        self.assertEqual(5, measure(result, dimension="benefit")["value"])
        self.assertEqual(2, measure(result)["value"])
        self.assertEqual(["A", "B"], result["after_frontier"])

    def test_channel_unknown_blocks_and_closed_is_excluded(self):
        for open_state in (None, False):
            cases = channel(pair(), open_state)
            result = frontier_transition(cases, cases, direction="A->B", transition_costs=(burden(),))
            if open_state is None:
                self.assertIsNone(result["after_frontier"])
            else:
                self.assertEqual(["B"], result["after_with_transition_costs"]["excluded_by_declared_channels"])
                self.assertEqual(["A"], result["after_frontier"])

    def test_high_cost_does_not_infer_channel_closure(self):
        cases = channel(pair(), True)
        result = frontier_transition(cases, cases, direction="A->B", transition_costs=(burden(1000),))
        self.assertEqual("SATISFIED", result["after_with_transition_costs"]["channel_checks"]["B"]["RECOVERY"])
        self.assertEqual(["A", "B"], result["after_frontier"])

    def test_declared_feedback_enters_comparison_once(self):
        a, b = pair()
        b = replace(b, feedback_chain=(FeedbackStep(1, "CN", "US", "benefit", "T1", -2,
                     EVIDENCE, "index", "independent synthetic feedback, not the transition cost"),))
        result = frontier_transition((a, b), (a, b), direction="A->B", transition_costs=(burden(),))
        self.assertEqual(5, measure(result, dimension="benefit")["value"])
        self.assertEqual(6, measure(result)["value"])
        self.assertEqual(["A"], result["after_frontier"])
        self.assertEqual(1, len(result["feedback_trace"]["after"]))

    def test_unknown_feedback_cannot_yield_a_determinate_frontier(self):
        a, b = pair()
        b = replace(b, feedback_chain=(FeedbackStep(1, "CN", "US", "benefit", "T1", None,
                     "UNKNOWN", "index", "unknown synthetic response"),))
        result = frontier_transition((a, b), (a, b), direction="A->B", transition_costs=(burden(),))
        self.assertIsNone(result["after_frontier"])

    def test_original_inputs_are_not_mutated(self):
        cases, costs = pair(), (burden(),)
        original = copy.deepcopy((cases, costs))
        one = frontier_transition(cases, cases, direction="A->B", transition_costs=costs)
        two = frontier_transition(cases, cases, direction="A->B", transition_costs=costs)
        self.assertEqual(original, (cases, costs))
        self.assertEqual(one, two)

    def test_comparison_scope_and_boundary_definitions_must_match(self):
        a, b = pair()
        variants = ((a,), (a, a), (a, replace(b, domain="other")),
                    (a, replace(b, measures=b.measures[:-1])),
                    (a, channel((b,), True)[0]))
        for after in variants:
            with self.subTest(after=after), self.assertRaises(ValueError):
                frontier_transition((a, b), after, direction="A->B", transition_costs=(burden(),))

    def test_raw_provenance_preserved_without_upgrading_derived_values(self):
        with self.assertRaises(ValueError):
            frontier_transition(pair(), pair(), direction="A->B",
                                transition_costs=(burden(2, source_provenance="OFFICIAL_SOURCE"),))
        cost = burden(2, source_provenance="THIRD_PARTY_SOURCE", source_ref="synthetic-ref",
                      evidence_state="THIRD_PARTY_ESTIMATE")
        result = frontier_transition(pair(), pair(), direction="A->B", transition_costs=(cost,))
        self.assertEqual("THIRD_PARTY_ESTIMATE", result["cost_trace"][0]["cost"]["evidence_state"])
        self.assertEqual(EVIDENCE, measure(result)["evidence_state"])

    def test_nonfinite_derived_value_is_rejected(self):
        a, b = pair()
        b = replace(b, measures=tuple(replace(m, value=1e308) if m.actor == "US" and
                                      m.dimension == "cost" else m for m in b.measures))
        with self.assertRaises(ValueError):
            frontier_transition((a, b), (a, b), direction="A->B", transition_costs=(burden(1e308),))

    def test_direction_requires_one_unambiguous_pair(self):
        for direction in ("", "A", "A->", "->B", "A->B->C", "A->A", " A->B"):
            with self.subTest(direction=direction), self.assertRaises(ValueError):
                frontier_transition(pair(), pair(), direction=direction)


if __name__ == "__main__":
    unittest.main()
