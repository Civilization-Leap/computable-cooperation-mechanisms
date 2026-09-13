# Computable Competition–Cooperation Mechanisms
## Minimal Open Reference Implementation

**Latest published release: v0.1.1. Apache-2.0.**

## Why this project exists

**What does cooperation gain and cost? What does non-cooperation gain and cost? Who benefits, who bears the burden, and who was never at the table?**

This project explores a more explicit and challengeable way to reason about competition and cooperation. It takes self-interest seriously without assuming that one actor's gain is the whole system's gain. It asks whether interests, constraints, third-party effects, exit conditions, unknowns, and irreversible consequences can become visible earlier—before positions harden or costs are silently shifted elsewhere.

Start with the idea, not the code: [Can We Learn to Compete and Cooperate Better?](docs/PUBLIC_IDEA_GUIDE_EN.md) · [我们能否学会更好地竞争与合作？](docs/PUBLIC_IDEA_GUIDE_ZH.md) · [short share copy](docs/PUBLIC_SHARE_COPY.md)

**Same outcomes. Different verdict.** A and B each save 3 CU; C loses 0.5 TU. Lower only C's declared loss ceiling from 0.5 to 0.49: `SATISFIED` becomes `VIOLATED`, with all outcome deltas unchanged. A computation can enforce a line precisely without establishing that the line is legitimate. [Run the threshold sweep and inspect both complete reports](docs/THRESHOLD_SENSITIVITY.md).

Human societies constantly compete, cooperate, form alliances, blocs, and communities. **How many of the mechanisms behind those relationships are explicit enough to inspect, recompute, falsify, and improve?**

This repository is a deliberately small, globally reusable starting point. Given declared actors, resources, outcomes, and constraints, it shows what changes under a candidate arrangement, which declared constraints are satisfied or violated, and what remains unknown.

It does **not** assume cooperation is always preferable, certify fairness, infer motives, predict behavior, create research H/T/L/RUN states, or authorize real-world action.

**Project purpose, objectives, method, application modes, scope, global participation, commercial independence, and maintenance boundaries:** [Project Overview](docs/PROJECT_OVERVIEW.md) · [中文项目总览](docs/PROJECT_OVERVIEW.zh-CN.md)

## Bring your own problem

**Do not stop at reading the theory or reproducing our examples. Bring a real competition/cooperation problem and use the current tool to discover what can be represented, what remains unknown, and where the model breaks.**

Shortest path:

**Understand → Bring a Problem → Model → Run → Interpret → Challenge → Extend**

- [Public BYOP entry](docs/BYOP_PUBLIC_ENTRY_EN.md)
- [BYOP Start Here](docs/BYOP_START_HERE.md)
- [中文应用指南](docs/APPLICATION_GUIDE_ZH.md) · [English Application Guide](docs/APPLICATION_GUIDE_EN.md)
- [Problem Card](docs/BYOP_PROBLEM_CARD.md)
- [Capability Ledger](docs/BYOP_CAPABILITY_LEDGER.md)
- [Input Mapping](docs/BYOP_INPUT_MAPPING.md)
- [Feedback Protocol](docs/BYOP_FEEDBACK_PROTOCOL.md)
- [Runnable acquisition example](docs/BYOP_END_TO_END_ACQUISITION.md)
- [Domain Extension Registry](docs/BYOP_DOMAIN_EXTENSION_REGISTRY.md)
- [Bring a real problem: Issue #25](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/25)

A failed fit is useful evidence. If the material mechanism cannot be represented without distortion, record a **REPRESENTATION GAP** rather than forcing a verdict. Repeated real-use gaps are the preferred source of new templates, domain extensions, and—only when necessary—core/schema changes.

## Try it in five minutes

Requires Git for this download route and Python 3.11–3.13 to run; the evaluator and tests use only the Python standard library. **No `pip install` or `pip install -e .` is needed when running from the extracted repository directory.** Start from the fixed v0.1.1 release:

```bash
git clone --branch v0.1.1 --depth 1 https://github.com/Civilization-Leap/computable-cooperation-mechanisms.git
cd computable-cooperation-mechanisms
python scripts/reproduce_offline.py
```

The reproduction path exercises the public teaching cases and current test suite. No account, API key, model download, or hosted service is needed after obtaining the source.

The historical [v0.1.0 Release](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/releases/tag/v0.1.0) remains frozen. The fixed [v0.1.1 Release](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/releases/tag/v0.1.1) is the current public testing baseline.

## Independent third-party testing

**Reproduce it, break it, or reimplement it. Endorsement is not requested.**
Choose a 5–15 minute release reproduction, a 15–45 minute break-it challenge, an independent implementation, or a 10–30 minute non-code review of evidence labels, rule provenance, and misuse risks. Use the [testing guide](docs/THIRD_PARTY_TESTING.md) and return results in [Issue #14](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/14). Failed reproductions, incompatibilities, and counterexamples are useful results.

## Both sides gain. Who else pays?

In the shared-equipment teaching pair, A and B each reduce their declared cost from 8 to 5 CU. Their savings are identical in both candidates. Yet C's reserved-slot loss changes from 0.5 to 2 TU, crossing the declared limit of 1 TU: `SATISFIED` becomes `VIOLATED`. The same gains can coexist with different constraint results.

These are **synthetic inputs and a reproducible illustration of the declared rule**, not measured benefits or a new empirical finding. [Inspect the comparison and its limits](docs/SHARED_EQUIPMENT_COMPARISON.md), or [challenge what the representation cannot express](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/5).

## Independent Implementation Challenge

**Reproduce the public semantics in another language. A separate repository is welcome.** Start with [Issue #8](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/8).

For a developer familiar with their chosen language and JSON tooling, budget **8–16 focused hours for a minimal four-case semantic implementation**, or **16–32 hours total** to include malformed-input checks, a documented comparison, and a reproducible command. These are planning estimates, not observed completion times; exact Python-compatible hashing may require more work.

The task covers parsing, validation, comparable deltas, independent hard checks, explicit unknowns, and deterministic output. [Scope, effort breakdown, expected results, and submission format](docs/INDEPENDENT_IMPLEMENTATION.md). Bring back a repository link and differences you found; no upstream merge or ongoing service commitment is required.

## Break it, extend it, or reimplement it

We are not asking people to endorse the framework. Useful contributions include:

- a synthetic coordination problem the current representation cannot express;
- a strong counterexample to a current modeling assumption;
- a new same-class scenario that requires no scenario-specific core logic;
- a better explicit representation of uncertainty;
- an independent implementation in another language;
- a domain-specific fork that remains independent of this repository.

Start with the open [contribution and research challenges](../../issues), especially issues labeled `good first issue` or `help wanted`. Independent forks and downstream implementations count as successful diffusion even if they never merge back upstream.

## Current method

- actor/dimension/unit results stay separate; no universal fairness score;
- baseline/candidate deltas are computed only for matching actor + dimension + unit;
- hard constraints are checked independently of ordinary gains;
- explicit unknowns are preserved rather than filled with zero;
- invalid references and undeclared units are rejected rather than converted to `UNKNOWN`;
- unsupported top-level fields are rejected explicitly: adding `id` yields `unsupported fields: ['id']`; the declared case identifier is `case_id`;
- evaluation is deterministic and does not mutate its input;
- output contains a reproducibility hash and an interpretation boundary.

## Teaching variants

1. `shared_equipment_ok.json` — declared constraints satisfied.
2. `shared_equipment_third_party_violation.json` — A and B reduce ordinary cost, but C's hard protection is violated; gains do not offset it.
3. `shared_equipment_unknown.json` — current resource value is explicitly unknown, so the hard check remains `UNKNOWN`.
4. `shared_equipment_capacity_violation.json` — a same-class extension case that violates resource capacity without scenario-specific core logic.

## Optional CI gate

Default exit 0 means reports were produced, including for violated or unknown constraints. In v0.1.1, `--fail-on-violation` returns 1 for an overall hard violation; `--fail-on-unknown` returns 3 for overall `UNKNOWN`. Use **both flags** if a CI gate must require SATISFIED. Reports are written before semantic failure exits; malformed inputs still fail with exit 2. [Exit-code table and command](docs/CLI_EXIT_CODES.md). These flags are absent from the historical v0.1.0 tag.

## Verification

The frozen v0.1.0 suite contains 12 tests. v0.1.1 contains 18: those original 12, five subprocess CLI tests, and one threshold-sensitivity test. CI runs the current suite with `ResourceWarning` treated as an error on Python 3.11, 3.12, and 3.13, executes all four teaching variants, and exercises the offline reproduction path. The formal release workflow repeats exact-commit verification before creating the version tag and GitHub Release.

A user independently reported successful reproduction on **Python 3.12.3** of the frozen v0.1.0 materials, including 13 source/metadata hashes, the original 12 tests with ResourceWarning as an error, and all four cases without pip. This is a user-reported run and is not silently promoted into independent verification of v0.1.1. [Evidence and exact scope](docs/THRESHOLD_SENSITIVITY.md#reproduction-provenance).

## Scope boundary

This is a teaching/reference implementation, not the formal R1 B2B blind fixture and not a complete software implementation of WP-01-A or the wider research program. Formal and controlled research materials remain separate. Competition, cooperation, alliance, bloc, and community are not encoded as a one-way value ladder.

The software checks **declared inputs and declared constraints**. It does not prove that inputs are true, that a mechanism is fair or legitimate, or that a real-world deployment is safe or authorized.

## Extend

Add another JSON case with the same contract. New constraint types require explicit code, tests, and documentation rather than silent interpretation. Independent teams may fork and extend the project under Apache-2.0 without depending on a centrally operated service.

See [CONTRIBUTING.md](CONTRIBUTING.md), [Global Outreach Kit](docs/OUTREACH_KIT.md), the [release-readiness checklist](docs/RELEASE_CHECKLIST.md), and the [v0.1.1 release notes](docs/RELEASE_NOTES_v0.1.1.md).

## Cite archived releases

The frozen **v0.1.0 archive** has version DOI [10.5281/zenodo.22656544](https://doi.org/10.5281/zenodo.22656544). The [all-versions DOI](https://doi.org/10.5281/zenodo.22656543) identifies the release family. Those identifiers are not a v0.1.1 version DOI. A v0.1.1-specific archive identifier, if created, must be recorded separately after archive verification.

All 34 archived files match the v0.1.0 tag byte-for-byte. Zenodo records the canonical version `0.1.0` and author `Zijunfu`. [Archive verification and metadata correction history](docs/ZENODO_ARCHIVE.md).

GitHub citation metadata in [`CITATION.cff`](CITATION.cff) continues to point to the verified v0.1.0 archive until a newer archived version is independently bound.

## License and commercial use

The repository is licensed under the **Apache License, Version 2.0**. Unless a file states otherwise, the license uniformly covers repository code, documentation, original synthetic teaching examples, tests, and implementation-support files authored for this repository. See [`LICENSE`](LICENSE) and [`LICENSE_SCOPE.md`](LICENSE_SCOPE.md).

Commercial and independent downstream use is permitted under Apache-2.0. A downstream product or service remains independently responsible for its claims, data, validation, security, deployment, support, legal obligations, and real-world consequences.

Using this project does not imply project endorsement, fairness certification, research validation, or real-world authorization. Research manuscripts, controlled research fixtures, restricted materials, and other assets not included in this repository are not licensed merely because this repository is Apache-2.0 licensed.

## Maintenance model

This repository is an open research starting point, not a promise of continuous hosted service, unlimited maintainer support, a fixed roadmap, or long-term compatibility. Downstream providers may make their own service commitments independently.
