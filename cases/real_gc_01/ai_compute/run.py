"""Run the frozen synthetic suite and retain decision-before-action records."""

import gzip
import hashlib
import json
from collections import defaultdict
from pathlib import Path

from .model import POLICIES, run_suite


def main():
    folder = Path(__file__).parent
    protocol_bytes = (folder / "protocol.json").read_bytes()
    protocol = json.loads(protocol_bytes)
    runs = run_suite()
    grouped = defaultdict(list)
    for result in runs:
        grouped[tuple(result["policies"])].append(result)
    summary = []
    for policies, group in sorted(grouped.items()):
        summary.append({
            "policies": list(policies), "instances": len(group),
            "observed_channel_closure_instances": sum(any(r["final_state"]["closed"].values()) for r in group),
            "completed_without_observed_channel_closure_instances": sum(not any(r["final_state"]["closed"].values()) and not r["stopped_without_admissible_purpose"] for r in group),
            "no_admissible_purpose_instances": sum(r["stopped_without_admissible_purpose"] for r in group),
            "forecast_mismatch_instances": sum(any(e["after_action"] and e["after_action"]["forecast_mismatch"] for e in r["events"]) for r in group),
        })
    result = {"protocol": protocol,
              "protocol_sha256": hashlib.sha256(protocol_bytes).hexdigest(),
              "model_sha256": hashlib.sha256((folder / "model.py").read_bytes()).hexdigest(),
              "runs": runs, "summary": summary}
    output = folder / "results.json.gz"
    output.write_bytes(gzip.compress((json.dumps(result, ensure_ascii=False, separators=(",", ":")) + "\n").encode(), mtime=0))
    print(json.dumps({"runs": len(runs), "summary": summary}, indent=2))


if __name__ == "__main__":
    main()
