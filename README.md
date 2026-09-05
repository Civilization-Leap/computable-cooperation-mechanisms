# Computable Competition–Cooperation Mechanisms — Minimal Reference Implementation

**DEV-2 / v0.1.0.dev2. Public repository. Licensed under Apache-2.0.**

A small, globally reusable starting point for expressing and recomputing multi-actor mechanism conditions. Given declared actors, resources, outcomes and constraints, it shows what changes under a candidate arrangement, which declared constraints are satisfied or violated, and what remains unknown.

It does **not** certify fairness, infer motives, predict behavior, create research H/T/L/RUN states, or authorize real-world action.

## Run
```bash
python -m mechanism_ref examples/shared_equipment_ok.json --out-dir outputs
python -m unittest discover -s tests -v
```

## Current method
- actor/dimension/unit results stay separate; no universal fairness score;
- baseline/candidate deltas are computed only for matching actor + dimension + unit;
- hard constraints are checked independently of ordinary gains;
- explicit unknowns are preserved rather than filled with zero;
- invalid references and undeclared units are rejected rather than converted to UNKNOWN;
- evaluation is deterministic and does not mutate its input;
- output contains a reproducibility hash and an interpretation boundary.

## Teaching variants
1. `shared_equipment_ok.json` — declared constraints satisfied.
2. `shared_equipment_third_party_violation.json` — A and B reduce ordinary cost, but C's hard protection is violated; gains do not offset it.
3. `shared_equipment_unknown.json` — current resource value is explicitly unknown, so the hard check remains UNKNOWN.
4. `shared_equipment_capacity_violation.json` — a same-class extension case that violates resource capacity without any scenario-specific core logic.

## Verification
The DEV-2 unit suite contains 12 tests. Pull request CI runs them with `ResourceWarning` treated as an error on Python 3.11, 3.12, and 3.13, and also executes all four teaching variants.

## Scope
This is a teaching/reference implementation, not the formal R1 B2B blind fixture and not WP-01-A. The formal research materials remain separate. Competition, cooperation, alliance, bloc and community are not encoded as a one-way value ladder.

## Extension
Add another JSON case with the same contract. New constraint types require explicit code and tests rather than silent interpretation.

## License
The repository is licensed under the **Apache License, Version 2.0**. Unless a file states otherwise, the license uniformly covers repository code, documentation, original synthetic teaching examples, tests, and implementation-support files authored for this repository. See [`LICENSE`](LICENSE) and [`LICENSE_SCOPE.md`](LICENSE_SCOPE.md).

Commercial and independent downstream use is permitted under Apache-2.0. A downstream product or service remains independently responsible for its claims, deployment, validation, support, and legal obligations. Using this project does not imply project endorsement, fairness certification, research validation, or real-world authorization.

Research manuscripts, controlled research fixtures, restricted materials, and other assets not included in this repository are not licensed merely because this repository is Apache-2.0 licensed.
