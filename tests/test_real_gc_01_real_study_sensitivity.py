import unittest

from cases.real_gc_01.gc_t01.real_study_sensitivity import (
    FAJGELBAUM_KHANDELWAL_2026_HEADLINE,
    PublishedEstimateRange,
    classify_sign_sensitivity,
)


class GCT01RealStudySensitivityTests(unittest.TestCase):
    def test_published_range_crosses_zero_and_is_sensitive(self):
        result = classify_sign_sensitivity(FAJGELBAUM_KHANDELWAL_2026_HEADLINE)
        self.assertEqual("SENSITIVE", result["status"])
        self.assertEqual([-0.13, 0.10], result["range"])

    def test_fixture_does_not_claim_structural_replication(self):
        result = classify_sign_sensitivity(FAJGELBAUM_KHANDELWAL_2026_HEADLINE)
        self.assertFalse(result["structural_replication"])
        self.assertFalse(result["policy_recommendation"])

    def test_source_and_evidence_identity_are_preserved(self):
        result = classify_sign_sensitivity(FAJGELBAUM_KHANDELWAL_2026_HEADLINE)
        self.assertEqual("THIRD_PARTY_ESTIMATE", result["evidence_state"])
        self.assertEqual("THIRD_PARTY_SOURCE", result["source_provenance"])

    def test_non_crossing_range_is_not_mislabeled_sensitive(self):
        r = PublishedEstimateRange("synthetic-positive", 0.02, 0.10, "percent_GDP")
        self.assertEqual(
            "ROBUST_SIGN_POSITIVE_WITHIN_DECLARED_RANGE",
            classify_sign_sensitivity(r)["status"],
        )

    def test_invalid_range_is_rejected(self):
        with self.assertRaises(ValueError):
            classify_sign_sensitivity(PublishedEstimateRange("bad", 0.10, -0.13, "percent_GDP"))


if __name__ == "__main__":
    unittest.main()
