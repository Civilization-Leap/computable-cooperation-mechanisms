# v0.1.1 — Reproducibility and External-Testing Milestone

`v0.1.1` packages the development work completed after the frozen `v0.1.0` milestone into a fixed, reproducible release. It does not change the core evaluator semantics or the original four teaching fixtures.

## What is new

- opt-in CLI gates: `--fail-on-violation` returns exit 1 for an overall declared hard-constraint violation, and `--fail-on-unknown` returns exit 3 for overall `UNKNOWN`; default report-only behavior remains exit 0 for valid inputs;
- reports are written before semantic gate exits; malformed or unsupported inputs remain errors and return exit 2;
- 18 tests: the original 12 plus five CLI subprocess tests and one threshold-sensitivity test;
- a standard-library threshold sweep showing that the verdict can change while outcome deltas remain unchanged when only a declared protection threshold moves;
- `scripts/reproduce_offline.py`, which runs the current tests, all four teaching cases, and one isolated threshold change without pip, network access, API keys, model downloads, or hosted services after the source is obtained;
- bounded third-party testing tracks that distinguish frozen-release reproduction, a fixed development challenge, independent reimplementation, and non-code methodological review;
- explicit evidence-label boundaries: automated CI, maintainer/local checks, user-reported reproduction, independent execution, independent reimplementation, methodological review, and external audit are not interchangeable evidence claims.

## Exact interpretation boundary

This software performs **deterministic checks of declared inputs and declared constraints only**. It does not establish who had authority to set a threshold, whether a declared threshold is legitimate, whether the inputs are true, whether a mechanism is fair, or whether a real-world action is permitted.

A `SATISFIED`, `VIOLATED`, or `UNKNOWN` result is a result inside the declared model. It is not a fairness certification, policy decision, legal conclusion, research-stage upgrade, or real-world authorization.

## Reproduce after download

From the extracted `v0.1.1` source directory:

```bash
python scripts/reproduce_offline.py
```

Or run the suite directly:

```bash
python -W error::ResourceWarning -m unittest discover -s tests -v
python -m mechanism_ref examples/shared_equipment_third_party_violation.json --out-dir outputs
python -m mechanism_ref examples/shared_equipment_unknown.json --out-dir outputs
python -m mechanism_ref examples/shared_equipment_ok.json --out-dir outputs
python -m mechanism_ref examples/shared_equipment_capacity_violation.json --out-dir outputs
```

The release workflow verifies the exact release commit on Python 3.11, 3.12, and 3.13, runs the teaching examples and offline reproduction, then creates an exact-commit tag. It also attaches a `git archive` offline source bundle and a SHA-256 checksum file to the GitHub Release.

## Evidence provenance at release preparation

Repository CI is automated evidence, not independent third-party execution. A user previously reported successful reproduction of the frozen v0.1.0 materials on Python 3.12.3; that report remains evidence about the scope actually run and is not silently promoted into independent verification of v0.1.1. New independent evidence should identify the exact tag or commit tested.

## Historical and archive boundary

`v0.1.0` remains a frozen historical release with version DOI `10.5281/zenodo.22656544` and concept DOI `10.5281/zenodo.22656543`. Those identifiers must not be presented as the version DOI for `v0.1.1`. A v0.1.1-specific archive identifier, if created, must be recorded separately after archive verification.

Formal research manuscripts, controlled blind fixtures, restricted materials, personal data, credentials, and real-world authorization materials are not part of this software release.

## License and downstream use

Repository code, documentation, original synthetic examples, tests, and repository support files remain under Apache-2.0 unless a file states otherwise. Independent and commercial downstream use is permitted under that license; downstream users remain responsible for their own claims, data, validation, security, deployment, legal obligations, and real-world consequences.
