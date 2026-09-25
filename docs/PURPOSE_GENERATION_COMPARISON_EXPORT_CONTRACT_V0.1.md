# Purpose Generation comparison export — integration contract candidate

Issue: #50  
Base: `376304627b2c72341ceb03cbfb0b464a189fdd1d`  
Status: **CONTRACT CANDIDATE / NO LIVE COMPARISON CLAIM**

## Boundary

This integration may export comparison structure only. It must never emit `winner`, `recommended_goal`, `score`, `policy_recommendation`, or execution instructions.

## Discovery result

The current `mechanism-ref` CLI evaluates one baseline/candidate case against declared constraints, writes result/report files, and prints the overall declared-constraint status.

The current core truthfully provides:

- declared hard-constraint status;
- per-constraint SATISFIED / VIOLATED / UNKNOWN;
- baseline/candidate outcome deltas.

It does **not**, at the pinned base, implement a multi-plan non-dominated frontier, pairwise incomparability relation, assumption-reversal engine, or a general comparison-UNKNOWN dependency analysis.

Therefore those downstream fields MUST NOT be fabricated from the current single-candidate evaluator.

## Target downstream fields

- non_dominated
- dominated
- incomparable
- unknown_dependent
- assumption_reversals
- boundary_flags

## Fail-closed rule

Empty arrays must not be used to mean "feature not implemented". A live Purpose Generation comparison export is blocked until each required field either:

1. maps to an existing CCM semantic with tests; or
2. is introduced as an explicit new CCM comparison capability with its own version, tests and research boundary.

Manifestation UNKNOWN is not comparison UNKNOWN dependency.

## Next implementation gate

Build the comparison capability in CCM itself, not in the Purpose Generation adapter. The downstream adapter may only transport and validate it.
