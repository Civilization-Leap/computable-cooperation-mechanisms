"""Sweep one declared limit using the standard library; retain exact inputs/reports."""
import argparse
import copy
import csv
import difflib
import json
from pathlib import Path
import platform
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from mechanism_ref.core import evaluate, load_case, report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=ROOT / "outputs/threshold_sweep")
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    original = load_case(ROOT / "examples/shared_equipment_ok.json")
    before = evaluate(original)
    rows = []
    for limit in (1, 0.6, 0.5, 0.49, 0.25):
        case = copy.deepcopy(original)
        next(c for c in case["constraints"] if c["id"] == "THIRD-PARTY")["limit"] = limit
        result = evaluate(case)
        assert result["outcome_deltas"] == before["outcome_deltas"]
        stem = "limit_" + str(limit).replace(".", "_")
        for suffix, obj in (("input.json", case), ("result.json", result)):
            (args.out_dir / (stem + "." + suffix)).write_text(
                json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        (args.out_dir / (stem + ".report.md")).write_text(report(result), encoding="utf-8")
        deltas = {(d["actor"], d["dimension"], d["unit"]): d["delta"]
                  for d in result["outcome_deltas"]}
        rows.append({"limit": limit, "status": result["overall_declared_constraint_status"],
                     "A_delta_CU": deltas[("A", "ordinary_cost", "CU")],
                     "B_delta_CU": deltas[("B", "ordinary_cost", "CU")],
                     "C_delta_TU": deltas[("C", "reserved_slot_loss", "TU")],
                     "input_sha256": result["input_sha256"]})
        print(f"limit={limit}: {result['overall_declared_constraint_status']}")
    with (args.out_dir / "sweep.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    left = (args.out_dir / "limit_0_5.report.md").read_text(encoding="utf-8").splitlines(keepends=True)
    right = (args.out_dir / "limit_0_49.report.md").read_text(encoding="utf-8").splitlines(keepends=True)
    diff = "".join(difflib.unified_diff(left, right, fromfile="limit_0_5.report.md", tofile="limit_0_49.report.md", n=0))
    (args.out_dir / "reports.diff").write_text(diff, encoding="utf-8")
    (args.out_dir / "provenance.json").write_text(json.dumps({
        "python": platform.python_version(), "evidence_type": "local synthetic recomputation",
        "source_case": "examples/shared_equipment_ok.json",
        "only_changed_input_field": "constraints[THIRD-PARTY].limit",
        "outcome_deltas_unchanged": True,
        "report_changed_line_numbers": [i + 1 for i, (a, b) in enumerate(zip(left, right)) if a != b],
        "note": "The original free-text description still says <= 1 TU; it is retained to change only one input field. Evaluation uses operator and limit. Threshold authorship/consent is not represented."
    }, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
