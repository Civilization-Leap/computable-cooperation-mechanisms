"""Negative checks for the public-entry smoke gate, not new model assertions."""
import unittest
from pathlib import Path

from scripts.check_real_gc_01_entry import check_documents, check_example, check_test_output, guide_commands

ROOT = Path(__file__).resolve().parents[1]


class RealGC01EntryTests(unittest.TestCase):
    def test_current_document_bindings(self):
        check_documents(ROOT)

    def test_zero_tests_cannot_be_reported_as_pass(self):
        with self.assertRaises(ValueError):
            check_test_output("Ran 0 tests in 0.000s\n\nOK\n")
        check_test_output("Ran 20 tests in 0.005s\n\nOK\n")

    def test_single_quoted_pattern_or_duplicate_command_block_is_rejected(self):
        text = (ROOT / "cases/real_gc_01/README.md").read_text(encoding="utf-8")
        broken = text.replace('"test_real_gc_01_transition.py"', "'test_real_gc_01_transition.py'")
        with self.assertRaises(ValueError):
            guide_commands(broken)
        with self.assertRaises(ValueError):
            guide_commands(text + text)

    def test_empty_example_is_not_success(self):
        with self.assertRaises(ValueError):
            check_example("{}")


if __name__ == "__main__":
    unittest.main()
