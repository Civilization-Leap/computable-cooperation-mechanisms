"""A boundary-sensitivity experiment, not a new empirical finding."""
import copy
from pathlib import Path
import unittest
from mechanism_ref.core import evaluate, load_case, report


class ThresholdTests(unittest.TestCase):
    def test_boundary_flip_preserves_all_declared_outcomes(self):
        original = load_case(Path(__file__).resolve().parents[1] / "examples/shared_equipment_ok.json")
        before = evaluate(original)
        for limit, expected in [(1, "SATISFIED"), (0.6, "SATISFIED"), (0.5, "SATISFIED"),
                                (0.49, "VIOLATED"), (0.25, "VIOLATED")]:
            with self.subTest(limit=limit):
                case = copy.deepcopy(original)
                next(c for c in case["constraints"] if c["id"] == "THIRD-PARTY")["limit"] = limit
                after = evaluate(case)
                self.assertEqual(after["overall_declared_constraint_status"], expected)
                self.assertEqual(after["outcome_deltas"], before["outcome_deltas"])
                self.assertEqual(after["checks"][0], before["checks"][0])
                self.assertEqual(case["baseline"], original["baseline"])
                self.assertEqual(case["candidate"], original["candidate"])
                if limit != 1:
                    self.assertNotEqual(after["input_sha256"], before["input_sha256"])
                if limit == 0.49:
                    changed = [i + 1 for i, (a, b) in enumerate(zip(report(before).splitlines(),
                               report(after).splitlines())) if a != b]
                    self.assertEqual(changed, [3, 5, 10])
