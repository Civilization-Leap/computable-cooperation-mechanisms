# v0.1.0 — First Open-Source Milestone Release

`v0.1.0` is the first formal open-source milestone release of **Computable Competition–Cooperation Mechanisms — Minimal Open Reference Implementation**.

## What this release provides

- strict JSON parsing and validation for declared actors, resources, outcomes, units, and constraints;
- baseline/candidate outcome deltas without collapsing dimensions into a universal score;
- independent hard-constraint checks so ordinary gains do not erase a violated protection boundary;
- explicit `UNKNOWN` preservation for valid-but-unknown inputs, while invalid references and undeclared units are rejected;
- deterministic recomputation with an input SHA-256 and input immutability tests;
- four original synthetic teaching variants, including satisfied, third-party violation, unknown-resource, and capacity-violation cases;
- 12 unit tests and CI on Python 3.11, 3.12, and 3.13 with `ResourceWarning` treated as an error;
- English and Chinese project overviews covering purpose, objectives, method, application modes, scope, global participation, commercial independence, and maintenance boundaries;
- Apache-2.0 licensing for repository code, documentation, original synthetic examples, tests, and repository support files unless a file states otherwise.

## Interpretation boundary

This software performs **deterministic checks of declared inputs and declared constraints only**. It does not certify fairness, validate a research hypothesis, infer motives, predict behavior, create H/T/L/RUN research states, or authorize, arbitrate, represent, enforce, or otherwise control real-world action.

A `SATISFIED`, `VIOLATED`, or `UNKNOWN` software result is a result inside the declared model. It is not a real-world permission, prohibition, fairness judgment, policy decision, legal conclusion, or research-stage upgrade.

## Research-material boundary

This release does not include the formal R1 B2B blind fixture, WP-01-A controlled materials, research answer keys, private/controlled datasets, personal data, credentials, or real-world authorization material. Those materials remain outside this repository and outside this release merely by virtue of the repository's Apache-2.0 license.

## Commercial and downstream use

Independent and commercial downstream use is permitted under Apache-2.0. Downstream products and services remain independently responsible for their claims, data, validation, security, deployment, support, legal obligations, and real-world consequences. Use of this code does not imply endorsement by the project or its contributors.

## Milestone meaning

This release is intentionally small. It establishes a runnable, inspectable, recomputable, and extensible open-source starting point. It is not a commitment by the initiator to build or operate a complete global platform. Further development may be undertaken independently by downstream teams and contributors.
