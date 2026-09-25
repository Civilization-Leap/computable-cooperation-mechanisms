from mechanism_ref.comparison_export_cli import export_comparison


def test_export_projects_real_comparison_semantics():
    out = export_comparison({
        "plans": [
            {"plan_id": "A", "components": {"benefit": 10, "option": 0}},
            {"plan_id": "B", "components": {"benefit": 0, "option": 10}},
        ]
    })
    assert out["schema_version"] == "0.1"
    assert out["non_dominated"] == ["A", "B"]
    assert out["incomparable"] == [["A", "B"]]
    assert "winner" not in out
    assert "score" not in out


def test_export_reports_last_channel_removal():
    out = export_comparison({
        "plans": [
            {"plan_id": "A", "components": {"x": 2}},
            {"plan_id": "B", "components": {"x": 1}},
        ],
        "baseline_channels": [
            {"subject_id": "s1", "correction": True, "exit": False, "recovery": False}
        ],
        "candidate_channels": [
            {"subject_id": "s1", "correction": False, "exit": False, "recovery": False}
        ],
    })
    assert out["boundary_flags"] == ["s1:LAST_CHANNEL_REMOVED"]
