import copy
import json
import unittest
from pathlib import Path

from cases.real_ma_01.v1_3.model import BOUNDARIES, build_ccm_case, conditional_scenarios, inventory_carrying_savings, summarize_result
from mechanism_ref.core import evaluate


INPUT = Path(__file__).parents[1] / "cases" / "real_ma_01" / "v1_3" / "inputs" / "empirical_inputs.json"


def default_input():
    return json.loads(INPUT.read_text(encoding="utf-8"))


class RealMA01V13Tests(unittest.TestCase):
    def test_default_preserves_five_unknown_boundaries(self):
        summary = summarize_result(evaluate(build_ccm_case(default_input())))
        self.assertEqual("UNKNOWN", summary["proposed_boundary_status"])
        self.assertEqual(5, len(summary["proposed_boundary_checks"]))
        self.assertEqual({"UNKNOWN"}, {x["status"] for x in summary["proposed_boundary_checks"]})

    def test_cost_and_time_are_reports_not_constraints(self):
        case = build_ccm_case(default_input())
        self.assertEqual(5, len(case["constraints"]))
        constrained = {x["dimension"] for x in case["constraints"]}
        self.assertNotIn("shipper_cost_usd_per_load", constrained)
        self.assertNotIn("transit_hours_per_load", constrained)

    def test_paid_faster_tradeoff_does_not_violate_boundaries(self):
        data = default_input()
        data["measurements"]["shipper_cost_usd_per_load"] = {"a1_independent_ai": 1000, "b1_merger_ai": 1200}
        data["measurements"]["transit_hours_per_load"] = {"a1_independent_ai": 40, "b1_merger_ai": 32}
        for _, _, dimension, _ in BOUNDARIES:
            data["boundary_evidence"][dimension] = 1
        summary = summarize_result(evaluate(build_ccm_case(data)))
        self.assertEqual("SATISFIED", summary["proposed_boundary_status"])
        self.assertEqual(200.0, summary["directional_reports"]["shipper_cost"]["delta"])
        self.assertEqual(-8.0, summary["directional_reports"]["transit_time"]["delta"])

    def test_each_boundary_can_independently_violate(self):
        for _, _, target, _ in BOUNDARIES:
            data = default_input()
            for _, _, dimension, _ in BOUNDARIES:
                data["boundary_evidence"][dimension] = 1
            data["boundary_evidence"][target] = 0
            summary = summarize_result(evaluate(build_ccm_case(data)))
            self.assertEqual("VIOLATED", summary["proposed_boundary_status"])
            violated = [x for x in summary["proposed_boundary_checks"] if x["status"] == "VIOLATED"]
            self.assertEqual(1, len(violated))

    def test_one_unknown_keeps_overall_unknown_without_violation(self):
        data = default_input()
        for _, _, dimension, _ in BOUNDARIES:
            data["boundary_evidence"][dimension] = 1
        data["boundary_evidence"][BOUNDARIES[0][2]] = None
        self.assertEqual("UNKNOWN", summarize_result(evaluate(build_ccm_case(data)))["proposed_boundary_status"])

    def test_invalid_boundary_evidence_is_rejected(self):
        data = default_input()
        data["boundary_evidence"][BOUNDARIES[0][2]] = 0.5
        with self.assertRaises(ValueError):
            build_ccm_case(data)

    def test_negative_or_nonfinite_measurement_is_rejected(self):
        for value in (-1, float("inf")):
            data = default_input()
            data["measurements"]["shipper_cost_usd_per_load"]["a1_independent_ai"] = value
            with self.assertRaises(ValueError):
                build_ccm_case(data)

    def test_conditional_grid_has_36_rows(self):
        self.assertEqual(36, len(conditional_scenarios()))
        self.assertEqual({"CONDITIONAL_RESEARCH_ASSUMPTION"}, {x["evidence_class"] for x in conditional_scenarios()})

    def test_published_inventory_arithmetic(self):
        self.assertAlmostEqual(57.0776255708, inventory_carrying_savings(100000, 0.20, 25), places=9)

    def test_build_does_not_mutate_source(self):
        data = default_input()
        before = copy.deepcopy(data)
        build_ccm_case(data)
        self.assertEqual(before, data)


if __name__ == "__main__":
    unittest.main()
