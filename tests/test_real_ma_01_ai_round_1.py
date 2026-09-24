import json
import tempfile
import unittest
from pathlib import Path

from cases.real_ma_01.challenges.ai_round_1.run_challenges import run_round


ROOT = Path(__file__).parents[1]
ROUND = ROOT / "cases" / "real_ma_01" / "challenges" / "ai_round_1"
DEFAULT_INPUT = ROOT / "cases" / "real_ma_01" / "v1_3" / "inputs" / "empirical_inputs.json"


class RealMA01AIRound1Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        specs = json.loads((ROUND / "challenge_specs.json").read_text(encoding="utf-8"))
        default_input = json.loads(DEFAULT_INPUT.read_text(encoding="utf-8"))
        cls.output = run_round(specs, default_input)

    def test_six_perspectives_are_present(self):
        self.assertEqual(6, len(self.output["results"]))
        self.assertEqual(
            {"shipper", "connecting_carrier", "workforce", "community", "competition_and_regulation", "autonomous_logistics"},
            {x["perspective"] for x in self.output["results"]},
        )

    def test_all_declared_assertions_pass(self):
        self.assertTrue(self.output["all_assertions_pass"])
        self.assertTrue(all(x["assertions_pass"] for x in self.output["results"]))

    def test_evidence_boundary_is_explicit(self):
        self.assertEqual("AI_ASSISTED_STRESS_TEST", self.output["evidence_class"])
        self.assertFalse(self.output["independent_validation"])
        self.assertFalse(self.output["external_evidence_state_changed"])

    def test_expected_finding_distribution(self):
        self.assertEqual(
            {"REPRODUCED": 1, "CHALLENGED": 3, "INSUFFICIENT_EVIDENCE": 1, "REPRESENTATION_GAP": 1},
            self.output["finding_counts"],
        )

    def test_representation_gap_is_not_forced_into_number(self):
        gap = next(x for x in self.output["results"] if x["perspective"] == "competition_and_regulation")
        self.assertEqual("REPRESENTATION_GAP", gap["mode"])
        self.assertNotIn("observed", gap)
        self.assertIn("market concentration", gap["missing_dimensions"])

    def test_paid_faster_tradeoff_remains_visible(self):
        shipper = next(x for x in self.output["results"] if x["perspective"] == "shipper")
        self.assertEqual("SATISFIED", shipper["observed"]["boundary_status"])
        self.assertEqual(200.0, shipper["observed"]["cost_delta"])
        self.assertEqual(-8.0, shipper["observed"]["time_delta"])

    def test_runner_does_not_need_to_modify_default_input(self):
        before = DEFAULT_INPUT.read_bytes()
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "result.json"
            path.write_text(json.dumps(self.output), encoding="utf-8")
            self.assertTrue(path.exists())
        self.assertEqual(before, DEFAULT_INPUT.read_bytes())


if __name__ == "__main__":
    unittest.main()
