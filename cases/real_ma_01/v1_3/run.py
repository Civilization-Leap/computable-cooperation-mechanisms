#!/usr/bin/env python3
"""Reproduce REAL MA 01 V1.3 without overwriting source inputs."""

import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from cases.real_ma_01.v1_3.model import build_ccm_case, conditional_scenarios, summarize_result
from mechanism_ref.core import evaluate


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=here / "inputs" / "empirical_inputs.json")
    parser.add_argument("--output-dir", type=Path, default=here / "outputs")
    args = parser.parse_args()

    source = json.loads(args.input.read_text(encoding="utf-8"))
    ccm_input = build_ccm_case(source)
    result = evaluate(ccm_input)
    summary = summarize_result(result)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "ccm_input.json").write_text(json.dumps(ccm_input, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (args.output_dir / "ccm_result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (args.output_dir / "public_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    rows = conditional_scenarios()
    with (args.output_dir / "conditional_inventory_scenarios.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"REAL MA 01 V1.3 proposed-boundary status: {summary['proposed_boundary_status']}")
    print("Directional report items do not determine that status.")
    print(f"Wrote {len(rows)} conditional scenarios and derived JSON to {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
