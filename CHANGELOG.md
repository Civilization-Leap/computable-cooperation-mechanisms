# Changelog

## DEV-3 licensing decision — Apache-2.0 adopted
- Formally adopt the Apache License, Version 2.0 for this repository.
- Apply one unified license scope to repository code, documentation, original synthetic teaching examples, tests, and implementation-support files unless a file explicitly states otherwise.
- Permit commercial and independent downstream development subject to Apache-2.0.
- Clarify that downstream use does not imply project endorsement, fairness certification, research validation, or real-world authorization.
- Keep research manuscripts, controlled fixtures, restricted materials, and assets outside this repository outside the repository license grant.
- Remove the obsolete pending-license marker and add `LICENSE_SCOPE.md`.

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
