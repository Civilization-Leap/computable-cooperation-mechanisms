# Computable Competition–Cooperation Mechanisms — Minimal Reference Implementation

**DEV-1 / v0.1.0.dev1. Not yet an open-source release.**

A small, globally reusable starting point for expressing and recomputing multi-actor mechanism conditions. Given declared actors, resources, outcomes and constraints, it shows what changes under a candidate arrangement, which declared constraints are satisfied or violated, and what remains unknown.

It does **not** certify fairness, infer motives, predict behavior, create research H/T/L/RUN states, or authorize real-world action.

## Run
```bash
python -m mechanism_ref examples/shared_equipment_ok.json --out-dir outputs
python -m unittest discover -s tests -v
```

## DEV-1 method
- actor/dimension/unit results stay separate; no universal fairness score;
- baseline/candidate deltas are computed only for matching actor + dimension + unit;
- hard constraints are checked independently of ordinary gains;
- explicit unknowns are preserved rather than filled with zero;
- output contains a reproducibility hash and an interpretation boundary.

## Teaching variants
1. `shared_equipment_ok.json` — declared constraints satisfied.
2. `shared_equipment_third_party_violation.json` — A and B reduce ordinary cost, but C's hard protection is violated; gains do not offset it.
3. `shared_equipment_unknown.json` — current resource value is unknown, so the hard check remains UNKNOWN.

## Scope
This is a teaching/reference implementation, not the formal R1 B2B blind fixture and not WP-01-A. The formal research materials remain separate. Competition, cooperation, alliance, bloc and community are not encoded as a one-way value ladder.

## Extension
Add another JSON case with the same contract. New constraint types require explicit code and tests rather than silent interpretation.

## License status
License candidate is still pending release approval. No public-release claim is made by DEV-1.
