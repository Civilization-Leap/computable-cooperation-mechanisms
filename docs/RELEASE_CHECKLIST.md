# Release Readiness Checklist

This checklist governs the first formal tagged release of the minimal reference implementation. It is a software-release control document, not a research H/T/L/RUN gate and not a real-world authorization instrument.

## Repository identity

- [x] Public canonical repository: `Civilization-Leap/computable-cooperation-mechanisms`
- [x] Default branch: `main`
- [x] English and Chinese entry documentation present
- [x] Formal Apache-2.0 `LICENSE` present
- [x] License scope covers repository code, documentation, original synthetic examples, tests, and repository support files unless a file states otherwise
- [x] Controlled research materials remain excluded from the repository

## Functional baseline

- [x] Strict JSON parsing rejects duplicate keys and non-finite values
- [x] Invalid references and undeclared units are rejected
- [x] Explicit unknown values remain `UNKNOWN`
- [x] Hard constraints are evaluated independently of ordinary outcome gains
- [x] Deterministic recomputation is tested
- [x] Evaluation does not mutate input
- [x] New same-class teaching case can be added without scenario-specific core logic

## Verification

- [x] 12-unit-test suite
- [x] CI on Python 3.11
- [x] CI on Python 3.12
- [x] CI on Python 3.13
- [x] `ResourceWarning` treated as a CI error
- [x] Four original synthetic teaching variants executed in CI

## Public-scope controls

- [x] No fairness certification claim
- [x] No H/T/L/RUN research-state claim
- [x] No real-world authorization, arbitration, representation, or enforcement claim
- [x] No motive, loyalty, personality, ideology, or cooperation scoring
- [x] No controlled R1 B2B blind fixture included
- [x] Commercial downstream use described as independent responsibility
- [x] Maintenance boundary states no implied hosted-service or support commitment

## DEV-3 documentation package

- [x] Project purpose
- [x] Project objectives
- [x] Method
- [x] Application path
- [x] Current scope
- [x] Explicit non-scope
- [x] Global participation model
- [x] Commercial and independent downstream relationship
- [x] Maintenance boundary
- [x] License scope

## DEV-4 release freeze

- [x] Intended first release version frozen as `0.1.0`
- [x] `RELEASE_VERSION` declares `0.1.0`
- [x] `pyproject.toml` declares `0.1.0`
- [x] `mechanism_ref.__version__` declares `0.1.0`
- [x] English and Chinese README files identify the v0.1.0 release source
- [x] v0.1.0 release notes repeat the interpretation and research-material boundaries
- [x] Release automation is required to test the exact commit before creating the tag and GitHub Release

## Conditions for first tagged release

Before declaring a first formal release, verify on the exact release commit:

1. CI is green on all configured Python versions.
2. English and Chinese README status text matches the release version.
3. `RELEASE_VERSION`, `pyproject.toml`, and `mechanism_ref.__version__` match the intended tag.
4. `LICENSE`, `LICENSE_SCOPE.md`, and `CONTRIBUTING.md` contain no pending-license language.
5. No restricted research material, personal data, credentials, or secrets are present.
6. The release notes repeat the interpretation boundary: deterministic checks of declared inputs and constraints only; not fairness certification, research validation, or real-world authorization.
7. The release tag is created only after the above checks pass.

## Automated release rule

The first-release workflow is fail-closed. On the release-source commit it must:

- run the unit suite and all four teaching variants on Python 3.11, 3.12, and 3.13;
- mechanically confirm `RELEASE_VERSION`, package metadata, and runtime version all equal `0.1.0`;
- confirm the formal `LICENSE`, `LICENSE_SCOPE.md`, release notes, and contribution file are present;
- refuse release if a `LICENSE-PENDING.txt` file exists;
- only after successful verification create tag `v0.1.0` at the exact tested commit and create the GitHub Release using `docs/RELEASE_NOTES_v0.1.0.md`.

A public repository with an active license is open source, but a **formal project release** is recorded only when the version tag and GitHub Release record actually exist and have been verified.
