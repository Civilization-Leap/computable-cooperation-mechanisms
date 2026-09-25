"""Classification fixture for a published third-party estimate range.

This does not reproduce the target study's structural model.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class PublishedEstimateRange:
    study_id: str
    lower: float
    upper: float
    unit: str
    evidence_state: str = "THIRD_PARTY_ESTIMATE"
    source_provenance: str = "THIRD_PARTY_SOURCE"


def classify_sign_sensitivity(r: PublishedEstimateRange):
    if r.lower > r.upper:
        raise ValueError("lower must not exceed upper")
    crosses_zero = r.lower < 0 < r.upper
    touches_zero = r.lower == 0 or r.upper == 0
    if crosses_zero or touches_zero:
        status = "SENSITIVE"
    elif r.lower > 0:
        status = "ROBUST_SIGN_POSITIVE_WITHIN_DECLARED_RANGE"
    else:
        status = "ROBUST_SIGN_NEGATIVE_WITHIN_DECLARED_RANGE"
    return {
        "status": status,
        "range": [r.lower, r.upper],
        "unit": r.unit,
        "evidence_state": r.evidence_state,
        "source_provenance": r.source_provenance,
        "structural_replication": False,
        "policy_recommendation": False,
        "interpretation_boundary": (
            "Classifies the sign behavior of a published estimate range only; "
            "does not validate the study model or recommend a policy."
        ),
    }


FAJGELBAUM_KHANDELWAL_2026_HEADLINE = PublishedEstimateRange(
    "NBER_W35064_2025_TARIFF_STUDY",
    -0.13,
    0.10,
    "percent_GDP",
)
