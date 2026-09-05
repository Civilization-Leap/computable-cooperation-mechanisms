# Changelog

## 0.1.0.dev2 — DEV-2
- Close test and CLI file handles; run ResourceWarning as an error in CI.
- Reject undeclared units, missing resource references, duplicate outcomes, and unsupported future-capability fields.
- Require baseline/candidate resource key alignment.
- Preserve explicit UNKNOWN while distinguishing it from invalid references.
- Verify evaluation does not mutate its input.
- Add a fourth same-class capacity-violation teaching case with no core special casing.
- Add GitHub Actions CI for Python 3.11–3.13.
- Expand the unit suite from 6 to 12 tests.

## 0.1.0.dev1 — DEV-1
- Minimal strict JSON loader and input validation.
- Baseline/candidate comparable outcome deltas.
- Resource and outcome hard-constraint checks.
- Explicit UNKNOWN preservation.
- Three original synthetic teaching variants.
- JSON + Markdown output and six unit tests.
