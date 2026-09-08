"""Run the unchanged public tests/cases and one isolated threshold comparison.

Uses only the Python standard library; no installation or network access.
"""
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from mechanism_ref.core import evaluate, load_case  # noqa: E402


def main():
    out = ROOT / "outputs"
    out.mkdir(exist_ok=True)
    manifest_path = ROOT / "SOURCE_MANIFEST.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for name, expected in manifest["sha256"].items():
            actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
            if actual != expected:
                raise RuntimeError(f"Frozen source checksum mismatch: {name}")
        print(f"Frozen source checksums verified: {len(manifest['sha256'])} files", flush=True)

    print(f"Python {platform.python_version()}; standard library only", flush=True)
    tested = subprocess.run(
        [sys.executable, "-W", "error::ResourceWarning", "-m", "unittest",
         "discover", "-s", "tests", "-v"], cwd=ROOT, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False,
    )
    (out / "unit_tests.txt").write_text(tested.stdout, encoding="utf-8")
    print(tested.stdout, flush=True)
    if tested.returncode:
        return tested.returncode

    order = ["third_party_violation", "unknown", "ok", "capacity_violation"]
    rows = []
    for suffix in order:
        name = f"shared_equipment_{suffix}"
        subprocess.run(
            [sys.executable, "-m", "mechanism_ref", f"examples/{name}.json",
             "--out-dir", str(out)], cwd=ROOT, check=True,
        )
        r = json.loads((out / f"{name}.result.json").read_text(encoding="utf-8"))
        rows.append({"file": f"examples/{name}.json", "result": r})

    original = load_case(ROOT / "examples/shared_equipment_ok.json")
    changed = json.loads(json.dumps(original))
    next(c for c in changed["constraints"] if c["id"] == "THIRD-PARTY")["limit"] = 0.25
    changed_path = out / "shared_equipment_lower_threshold.json"
    changed_path.write_text(json.dumps(changed, ensure_ascii=False, indent=2), encoding="utf-8")
    subprocess.run(
        [sys.executable, "-m", "mechanism_ref", str(changed_path), "--out-dir", str(out)],
        cwd=ROOT, check=True,
    )
    before, after = evaluate(original), evaluate(changed)
    comparison = {
        "change": {"constraint_id": "THIRD-PARTY", "field": "limit", "before": 1, "after": 0.25},
        "before": before,
        "after": after,
        "outcome_deltas_unchanged": before["outcome_deltas"] == after["outcome_deltas"],
    }
    evidence = {"python": platform.python_version(), "original_cases": rows, "one_change": comparison}
    (out / "offline_reproduction.json").write_text(
        json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8",
    )
    print("One change: THIRD-PARTY limit 1 -> 0.25; C loss stays 0.5 TU.")
    print(f"{before['overall_declared_constraint_status']} -> {after['overall_declared_constraint_status']}; outcome deltas unchanged: {comparison['outcome_deltas_unchanged']}")
    print(f"Reports and evidence: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
