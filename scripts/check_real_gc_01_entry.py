"""Read-only guide binding checks and opt-in fresh-clone R1 execution.

The marked README blocks are the command source; an allowlist prevents arbitrary
Markdown commands from being executed. This is not corpus_lint or a model test.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
GUIDE = Path("cases/real_gc_01/README.md")
ENGLISH = Path("cases/real_gc_01/gc_t01/KNOWN_UNKNOWN_CONDITIONAL_MATRIX_EN_V0_1.md")
MATRIX = "cases/real_gc_01/gc_t01/KNOWN_UNKNOWN_CONDITIONAL_MATRIX_V0_1.md"
PIN = "c822d1729bf4d4ed5a4c6c0f518c255c36cbf0ca"
BLOBS = {
    "cases/__init__.py": "8133c643b5d7d01466d588f42d2c38129e3ccd10",
    "cases/real_gc_01/v0_2/model.py": "01f091ab2de1d7183f9bd6a2c40a73e676c82a9b",
    "cases/real_gc_01/v0_2/transition.py": "bbf04ea24a0efaa0512b4a3f04fb8eff04654d02",
    "cases/real_gc_01/v0_2/transition_example.py": "a9cf1f2935abe2f354553c6d1c7ebc7cf7e2f8d3",
    "tests/test_real_gc_01_transition.py": "de50e54b155c038fdd51a07a8561bccd60941ccd",
    MATRIX: "8a936368264c1eb0cda8f3712ad6ae4739b4fb06",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def block(text, name):
    pattern = rf"<!-- {name}_BEGIN -->\s*```text\n(.*?)\n```\s*<!-- {name}_END -->"
    matches = re.findall(pattern, text, re.S)
    require(len(matches) == 1, f"exactly one {name} block required")
    return matches[0].splitlines()


def guide_commands(text):
    require(text.startswith("# REAL GC 01｜外部复算与反例入口 V0.2"), "guide version mismatch")
    require(text.count(f"<!-- R1_CODE_COMMIT: {PIN} -->") == 1, "code pin mismatch")
    require(text.count("<!-- R1_EXPECTED_TESTS: 20 -->") == 1, "test count binding missing")
    checkout = block(text, "R1_CHECKOUT")
    expected = [
        "git clone https://github.com/Civilization-Leap/computable-cooperation-mechanisms.git real-gc-01-round1",
        "cd real-gc-01-round1",
        "git fetch origin pull/48/head",
        f"git checkout --detach {PIN}",
        "git rev-parse HEAD",
    ]
    require(checkout == expected, "checkout commands differ from the declared fixed target")
    commands = block(text, "R1_PYTHON")
    require(commands == [
        "python --version",
        "python -m cases.real_gc_01.v0_2.transition_example",
        'python -W error::ResourceWarning -m unittest discover -s tests -p "test_real_gc_01_transition.py" -v',
    ], "Python commands changed or shell-unsafe pattern quoting")
    return checkout, commands


def check_documents(root):
    guide = (root / GUIDE).read_text(encoding="utf-8")
    commands = guide_commands(guide)
    english = (root / ENGLISH).read_text(encoding="utf-8")
    ids = re.findall(r"^\| ([KCU]\d{2})(?: /| \|)", english, re.M)
    require(ids == [f"K{i:02}" for i in range(1, 8)] + [f"C{i:02}" for i in range(1, 5)]
            + [f"U{i:02}" for i in range(1, 6)], "English excerpt must preserve all 16 row IDs once")
    require(BLOBS[MATRIX] in english and f"/blob/{PIN}/{MATRIX}" in english, "translation source not pinned")
    for n in range(1, 7):
        require(f"[S{n}]: https://" in english, f"missing primary source S{n}")
    require(ENGLISH.name in guide and "## R0" in guide, "English / no-run entry missing")
    require("Private reply" in guide[:2000] and "without consent" in guide[:2000], "private route not upfront")
    require("pre-repair" in guide and "默认 main 不含" in guide, "version snapshot caveat missing")
    require(f"/archive/{PIN}.zip" in guide, "ZIP is not pinned")
    print("DOCUMENT_BINDINGS_PASS: guide V0.2 / code V0.2 at", PIN, "/ matrix V0.1 / EN V0.1", flush=True)
    return commands


def check_test_output(text):
    require(re.search(r"^Ran 20 tests in .+$", text, re.M) is not None, "expected 20 tests; zero/missing tests is failure")
    require(re.search(r"^OK\s*$", text, re.M) is not None, "targeted unittest result not OK")


def check_example(text):
    data = json.loads(text)
    for name in ("empirical_claim", "independent_validation", "external_evidence_state_changed", "policy_recommendation"):
        require(data.get(name) is False, f"origin boundary changed: {name}")
    require(data.get("sampled_cost_sensitivity") == "SENSITIVE", "missing sampled sensitivity")
    runs = data.get("runs", [])
    require(len(runs) == 3, "expected three runs")
    for run, burden, cost, frontier in zip(runs, (2, 4, None), (4, 6, None), (["B"], ["A", "B"], None)):
        require(run["declared_burden"] == burden, "burden changed")
        result = run["result"]
        require(result["after_frontier"] == frontier, "frontier differs from untouched fixture")
        require(result["comparison_status"] == ("UNDECIDABLE" if burden is None else "COMPLETE_CONDITIONAL"), "status mismatch")
        b = next(row for row in result["adjusted_after_measures"] if row["configuration"] == "B")
        value = next(m["value"] for m in b["measures"] if m["actor"] == "US" and m["dimension"] == "cost")
        require(value == cost, "cost not applied as documented")
    print("R1_JSON_PASS: 2 -> 4/[B]; 4 -> 6/[A,B]; UNKNOWN -> UNDECIDABLE", flush=True)


def shell_command(command, cwd):
    print(f"\n$ {command}", flush=True)
    shell = [os.environ.get("COMSPEC", "cmd.exe"), "/d", "/s", "/c"] if os.name == "nt" else ["bash", "-eo", "pipefail", "-c"]
    result = subprocess.run(shell + [command], cwd=cwd, capture_output=True,
                            text=True, encoding="utf-8", errors="replace", timeout=120)
    print(result.stdout, end="", flush=True)
    print(result.stderr, end="", flush=True)
    require(result.returncode == 0, f"command failed ({result.returncode}): {command}")
    return result


def run_r1(checkout, commands):
    # Fresh repository, not the PR test merge. No model files or imports patched.
    with tempfile.TemporaryDirectory(prefix="gc01-r1-", ignore_cleanup_errors=True) as temp:
        cwd = Path(temp)
        for command in checkout:
            if command == "cd real-gc-01-round1":
                print("\n$ " + command, flush=True)
                cwd = cwd / "real-gc-01-round1"
                require(cwd.is_dir(), "clone directory absent")
            else:
                result = shell_command(command, cwd)
                if command == "git rev-parse HEAD":
                    require(result.stdout.strip() == PIN, "wrong checked-out commit")
        for path, expected in BLOBS.items():
            actual = subprocess.check_output(["git", "rev-parse", f"HEAD:{path}"], cwd=cwd, text=True).strip()
            require(actual == expected, f"pinned blob mismatch: {path}")
        print("PINNED_BLOBS_PASS; shell=" + ("cmd" if os.name == "nt" else "bash"), flush=True)
        for i, command in enumerate(commands):
            result = shell_command(command, cwd)
            if i == 0:
                require(re.search(r"Python 3\.(11|12|13)\.", result.stdout + result.stderr), "unsupported Python")
            elif i == 1:
                check_example(result.stdout)
            else:
                check_test_output(result.stdout + result.stderr)
        print("R1_FRESH_CLONE_AND_README_COMMANDS_PASS", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check-only", action="store_true")
    mode.add_argument("--run", action="store_true")
    args = parser.parse_args()
    commands = check_documents(ROOT)
    if args.run:
        run_r1(*commands)


if __name__ == "__main__":
    main()
