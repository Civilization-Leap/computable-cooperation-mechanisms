"""Subprocess checks of the opt-in exit-code contract and saved evidence."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
CASES = {"ok": "SATISFIED", "third_party_violation": "VIOLATED",
         "unknown": "UNKNOWN", "capacity_violation": "VIOLATED"}


class CliTests(unittest.TestCase):
    def check_cases(self, flags, expected_codes):
        for suffix, status in CASES.items():
            with self.subTest(suffix=suffix), tempfile.TemporaryDirectory() as tmp:
                stem = "shared_equipment_" + suffix
                proc = subprocess.run(
                    [sys.executable, "-W", "error::ResourceWarning", "-m", "mechanism_ref",
                     str(ROOT / "examples" / (stem + ".json")), "--out-dir", tmp, *flags],
                    cwd=ROOT, text=True, capture_output=True, check=False)
                self.assertEqual(proc.returncode, expected_codes[status], proc.stderr)
                self.assertEqual(proc.stdout.strip(), status)
                result = json.loads((Path(tmp) / (stem + ".result.json")).read_text())
                self.assertEqual(result["overall_declared_constraint_status"], status)
                self.assertIn(status, (Path(tmp) / (stem + ".report.md")).read_text())

    def test_default_preserves_report_only_exit_codes(self):
        self.check_cases([], dict(SATISFIED=0, VIOLATED=0, UNKNOWN=0))

    def test_violation_flag_preserves_unknown(self):
        self.check_cases(["--fail-on-violation"], dict(SATISFIED=0, VIOLATED=1, UNKNOWN=0))

    def test_unknown_flag_preserves_violation(self):
        self.check_cases(["--fail-on-unknown"], dict(SATISFIED=0, VIOLATED=0, UNKNOWN=3))

    def test_combined_gate_requires_satisfied(self):
        self.check_cases(["--fail-on-violation", "--fail-on-unknown"],
                         dict(SATISFIED=0, VIOLATED=1, UNKNOWN=3))

    def test_unsupported_top_level_id_is_rejected_without_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            case = json.loads((ROOT / "examples/shared_equipment_ok.json").read_text())
            case["id"] = "unrecognized"
            source = Path(tmp) / "bad.json"
            source.write_text(json.dumps(case))
            out = Path(tmp) / "reports"
            proc = subprocess.run(
                [sys.executable, "-m", "mechanism_ref", str(source), "--out-dir", str(out),
                 "--fail-on-violation", "--fail-on-unknown"],
                cwd=ROOT, text=True, capture_output=True, check=False)
            self.assertEqual(proc.returncode, 2)
            self.assertIn("unsupported fields: ['id']", proc.stderr)
            self.assertEqual(proc.stdout, "")
            self.assertFalse(out.exists())
