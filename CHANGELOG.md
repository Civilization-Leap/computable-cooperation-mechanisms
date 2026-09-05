# Changelog

## 0.1.0 — First open-source milestone release
- Freeze the first formal release line at `v0.1.0`.
- Publish the minimal deterministic reference implementation for declared actors, resources, outcomes, units, and constraints.
- Preserve explicit `UNKNOWN`, reject invalid references and undeclared units, and keep hard constraints independent from ordinary gains.
- Include four original synthetic teaching variants and 12 unit tests.
- Verify on Python 3.11, 3.12, and 3.13 with `ResourceWarning` treated as an error.
- Publish English and Chinese project overviews and release documentation.
- License repository code, documentation, original synthetic teaching examples, tests, and repository support files under Apache-2.0 unless a file states otherwise.
- Keep formal research manuscripts, controlled fixtures, restricted materials, and real-world authorization material outside this release.
- Reaffirm the interpretation boundary: software results are deterministic checks of declared inputs and constraints, not fairness certification, research validation, or real-world authorization.

## 0.1.0.dev3 — DEV-3 release candidate
- Adopt Apache-2.0 as the active repository license for code, documentation, original synthetic teaching examples, tests, and repository support files unless a file states otherwise.
- Add global project overview in English and Chinese covering purpose, objectives, method, application modes, scope, commercial independence, participation, and maintenance boundaries.
- Add a first-release readiness checklist.
- Promote English and Chinese README files to the DEV-3 release-candidate entry point.
- Record Apache-2.0 in package metadata.
- Use the package version as evaluator output version to reduce version drift.
- Keep formal research manuscripts, controlled fixtures, restricted materials, and other assets outside this repository out of license scope.

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
