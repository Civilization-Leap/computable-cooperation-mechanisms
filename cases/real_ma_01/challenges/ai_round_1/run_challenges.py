#!/usr/bin/env python3
"""Run REAL MA 01 AI-assisted stress tests against V1.3.

The output is a maintainer-observed AI challenge record. It is not independent
validation, a transaction opinion, or evidence of real-world effects.
"""

import argparse
import copy
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from cases.real_ma_01.v1_3.model import build_ccm_case, summarize_result
from mechanism_ref.core import evaluate


HERE = Path(__file__).resolve().parent
DEFAULT_INPUT = ROOT / "cases" / "real_ma_01" / "v1_3" / "inputs" / "empirical_inputs.json"


def _load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def _run_executable(spec, default_input):
    data = copy.deepcopy(default_input)
    data["case_id"] = spec["id"]
    data["measurements"] = copy.deepcopy(spec["measurements"])
    data["boundary_evidence"] = copy.deepcopy(spec["boundary_evidence"])
    summary = summarize_result(evaluate(build_ccm_case(data)))
    expected = spec["expected"]
    assertions = {
        "boundary_status": summary["proposed_boundary_status"] == expected["boundary_status"],
    }
    if "cost_delta" in expected:
        assertions["cost_delta"] = summary["directional_reports"]["shipper_cost"]["delta"] == expected["cost_delta"]
    if "time_delta" in expected:
        assertions["time_delta"] = summary["directional_reports"]["transit_time"]["delta"] == expected["time_delta"]
    if "violated_constraint" in expected:
        violated = [x["constraint_id"] for x in summary["proposed_boundary_checks"] if x["status"] == "VIOLATED"]
        assertions["violated_constraint"] = violated == [expected["violated_constraint"]]
    if "unknown_constraint" in expected:
        unknown = [x["constraint_id"] for x in summary["proposed_boundary_checks"] if x["status"] == "UNKNOWN"]
        assertions["unknown_constraint"] = unknown == [expected["unknown_constraint"]]
    return {
        "id": spec["id"],
        "perspective": spec["perspective"],
        "mode": spec["mode"],
        "finding_class": spec["finding_class"],
        "question": spec["question"],
        "assertions": assertions,
        "assertions_pass": all(assertions.values()),
        "observed": {
            "boundary_status": summary["proposed_boundary_status"],
            "cost_delta": summary["directional_reports"]["shipper_cost"]["delta"],
            "time_delta": summary["directional_reports"]["transit_time"]["delta"],
            "checks": summary["proposed_boundary_checks"],
            "input_sha256": summary["input_sha256"],
        },
        "representation_gap": spec.get("representation_gap"),
        "external_task": spec["external_task"],
    }


def run_round(specs, default_input):
    results = []
    for spec in specs["challenges"]:
        if spec["mode"] == "EXECUTABLE":
            results.append(_run_executable(spec, default_input))
        elif spec["mode"] == "REPRESENTATION_GAP":
            results.append({
                "id": spec["id"],
                "perspective": spec["perspective"],
                "mode": spec["mode"],
                "finding_class": spec["finding_class"],
                "question": spec["question"],
                "assertions": {"gap_declared_without_forced_numeric_value": True},
                "assertions_pass": True,
                "covered_dimensions": spec["covered_dimensions"],
                "missing_dimensions": spec["missing_dimensions"],
                "external_task": spec["external_task"],
            })
        else:
            raise ValueError(f"unsupported challenge mode: {spec['mode']}")
    counts = {}
    for result in results:
        counts[result["finding_class"]] = counts.get(result["finding_class"], 0) + 1
    return {
        "round_id": specs["round_id"],
        "model_version": specs["model_version"],
        "as_of_date": specs["as_of_date"],
        "evidence_class": specs["evidence_class"],
        "independent_validation": False,
        "external_evidence_state_changed": False,
        "interpretation_boundary": "AI-assisted and maintainer-observed stress test only. It does not establish delivery, independent reproduction, endorsement, adoption, authority, or real-world effect.",
        "all_assertions_pass": all(x["assertions_pass"] for x in results),
        "finding_counts": counts,
        "results": results,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--specs", type=Path, default=HERE / "challenge_specs.json")
    parser.add_argument("--default-input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=HERE / "ai_round_1_results.json")
    args = parser.parse_args()
    output = run_round(_load(args.specs), _load(args.default_input))
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{output['round_id']}: {'PASS' if output['all_assertions_pass'] else 'FAIL'}")
    print(f"Finding counts: {json.dumps(output['finding_counts'], sort_keys=True)}")
    print("Evidence class: AI_ASSISTED_STRESS_TEST; independent validation: false")
    return 0 if output["all_assertions_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
