# CCM-BYOP-01｜Capability Ledger

Status: V0.1 application boundary ledger

This ledger maps what a real user may want to do to what the current public tool can actually support. It is a guardrail against letting application language outrun implementation capability.

## Current public baseline

The public testing baseline is v0.1.1. It is a small deterministic reference implementation over declared actors, dimensions, units, baseline/candidate outcomes, hard constraints, and explicit unknowns.

| Real-use need | v0.1.1 status | How to use it now | Boundary / next-layer need |
|---|---|---|---|
| Declare affected actors | Supported | Declare actors referenced by results and constraints | Actor identity, authority, representation, and truthfulness are not verified |
| Compare baseline and candidate outcomes | Supported | Use matching actor + dimension + unit results | A result delta is not a welfare judgment |
| Compare several candidate arrangements | Partially supported | Model each candidate as a separate case against a common baseline, then compare reports | No built-in multi-candidate ranking |
| Represent cooperation and non-cooperation side by side | Partially supported | Treat cooperation and non-cooperation as explicit candidate arrangements, not moral labels | The tool does not decide which relation is preferable |
| Check hard constraints independently of ordinary gains | Supported | Declare hard constraints and inspect SATISFIED / VIOLATED / UNKNOWN | Who has standing to define a constraint or threshold is outside the evaluator |
| Preserve unknowns | Supported | Declare unknown values explicitly | The tool does not estimate or fill missing facts |
| Represent third-party burden | Minimally supported | Include the third party as an actor and declare relevant outcomes/constraints | Discovery of omitted affected parties is not automated |
| Represent privacy / non-public facts | Not directly supported | Use only facts safe to place in the case, or use externally verified abstractions | No confidential-computation or access-control layer |
| Represent power asymmetry | Not structurally complete | Encode observable consequences or hard protections where possible | Agenda-setting power, coercion, retaliation, and bargaining leverage need a domain extension |
| Model multi-stage negotiation | Not supported as a dynamic process | Compare snapshots or successive cases manually | No negotiation state machine or temporal strategy model |
| Accumulate trust from履约 / performance history | Not supported as a dynamic trust model | Record factual commitments/results outside the evaluator and compare snapshots | Do not convert trust into an unsupported personality/reputation score |
| Model irreversible consequences | Partially supported | Encode an irreversible boundary as a declared hard constraint when the condition is explicit | The evaluator does not discover irreversibility or validate the threshold |
| Validate whether input facts are true | Not supported | Require evidence/provenance outside the evaluator | Input truth remains a governance and evidence problem |
| Determine legitimacy, fairness, morality, or the correct social choice | Explicitly not supported | Keep these as human/institutional judgments informed by the report | Precise computation can enforce a rule; it cannot confer legitimacy on the rule |
| Authorize real-world action | Explicitly not supported | Use outputs as an input to deliberation, negotiation, trial design, or review | Real authority remains with the relevant actors and institutions |

## Rule for iteration

A real problem that cannot be represented correctly is not evidence that the problem should be forced into the current schema. It is a candidate input to the iteration process.

Classify the gap before changing code:

1. documentation gap;
2. case/template gap;
3. domain-extension need;
4. schema/core defect;
5. problem that should remain outside software.

The default is **not** to expand the core until a repeated, well-specified real-use need shows that the core contract itself is insufficient.
