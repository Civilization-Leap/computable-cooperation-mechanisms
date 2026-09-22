# REAL MA 01 — Reproduction and Counterexample Challenge

Reproduce, challenge, or break the model; endorsement is not requested.

## Independent Challenge Sprint — Round 1

Choose the smallest useful contribution:

- **10–15 minutes — reproduce:** run the public default and report whether the documented result is reproduced.
- **20–40 minutes — challenge:** break one assumption, variable, boundary, unit, or authorization relationship.
- **45–90 minutes — bring a problem:** contribute one non-confidential real coordination problem or validation protocol.

A one-sentence contribution is enough to start:

> I think the model omits ______; this could cause ______; it could be checked with ______.

Use the [REAL MA 01 issue form](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/new?template=real_ma_01.yml) or add context to the [Round 1 coordination issue](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/45). If GitHub is a barrier, a maintainer may transcribe a contributor's emailed observation with permission and label its provenance.

Every contribution should receive a visible disposition: reproduced, accepted, partly accepted, not accepted with reasons, awaiting evidence, or representation gap. A contribution is not counted as independent validation merely because a maintainer or AI assistant reran it.

## Smallest useful checks

1. Run the untouched default and confirm five `UNKNOWN` boundary checks.
2. Enter a synthetic paid-faster trade-off: B1 costs more but takes less time, while all five proposed boundaries equal `1`. Confirm the boundary status remains `SATISFIED` and the two directional deltas remain visible.
3. Change exactly one proposed boundary to `0`. Confirm it becomes `VIOLATED` without erasing the other four checks.
4. Identify a real logistics outcome that cannot be represented without distortion. Report a `REPRESENTATION GAP` rather than forcing it into cost or time.

## If using real evidence

Do not submit confidential orders, contracts, personal data, or protected-record material. For each public value, provide its source, date, unit, corridor/order scope, whether it is a company claim or measured result, and any access restriction. The two report items require comparable A1 and B1 observations; a network-wide average is not silently interchangeable with a corridor result.

For each proposed boundary, also identify who proposed it, who is affected, who can legitimately accept a trade-off, and who verified the evidence. The software can enforce an entered line; it cannot grant authority to draw the line.

## What counts as a useful result

- a reproducible pass or failure;
- a counterexample showing that the two report items should be structured differently;
- evidence that one of the five boundaries is misdefined or lacks a legitimate verifier;
- a corridor where independent cooperation (A1) already delivers the claimed capability;
- a proposed additional dimension kept separate from the hard-boundary status;
- a representation gap or misuse risk.

Open a repository issue and link the exact commit, input hash, command, Python version, and output. Public discussion is not the same as a regulatory filing, endorsement, or independent validation.

## Evidence-state discipline

Outreach and participation states must not be collapsed:

`SENT → DELIVERED → REPLIED → TRIED → CHALLENGED → CHANGED → REUSED`

Only mark a state when direct evidence exists. All later states remain `UNKNOWN`; a sent invitation is not evidence of delivery, reading, endorsement, reproduction, adoption, or real-world effect.
