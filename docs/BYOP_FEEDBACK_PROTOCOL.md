# BYOP Feedback Protocol｜USE → TEST → FEEDBACK → EXTEND

The purpose of feedback is not to collect generic opinions. It is to turn real-use friction into a traceable decision about documentation, templates, domain extensions, or the core.

## Feedback classes

### A — REPRESENTATION GAP
A material part of the real problem cannot be represented without distortion.

Return:
- the missing concept;
- why it changes the comparison;
- the smallest synthetic example that exposes the gap.

### B — COUNTEREXAMPLE
A case shows that a documented assumption, invariant, or interpretation does not hold.

Return:
- exact version/commit;
- minimal input;
- expected reasoning;
- observed output;
- why this is a counterexample rather than a preference disagreement.

### C — MISSING ACTOR / IMPACT
A party that materially bears consequences has no adequate place in the representation.

Return:
- affected party class;
- consequence;
- why omission changes the result or interpretation.

### D — MISSING CONSTRAINT
A non-offsettable condition cannot be represented with the current hard-constraint mechanism.

Return:
- condition;
- unit/logic if known;
- who is affected;
- provenance/authority question.

### E — MISINTERPRETATION RISK
The output or documentation invites a stronger claim than the tool supports.

Examples:
- “computed” being read as “objective”;
- SATISFIED being read as “legitimate”;
- a declared threshold being read as an authorized threshold;
- an omitted actor being read as unaffected.

### F — DOMAIN EXTENSION
The core may be sufficient, but a field needs its own template, vocabulary, evidence conventions, or workflow.

Default response: build an independent domain layer before changing the core.

### G — CORE DEFECT
The existing declared contract is implemented incorrectly or inconsistently.

Return a minimal reproducible case whenever possible.

## Triage rule

For each report, choose the smallest adequate response:

1. **Documentation fix** — semantics were already supported but unclear.
2. **Teaching/template extension** — core semantics are enough; users need a reusable pattern.
3. **Domain extension** — the field needs additional structure without changing the minimal core.
4. **Core/schema change** — repeated, well-specified cases show the public contract itself is insufficient.
5. **Out of software scope** — legitimacy, authorization, evidence truth, confidential judgment, or another issue should remain outside the evaluator.

## Evidence discipline

A report is stronger when it includes:

- version/tag/commit;
- environment;
- exact input or synthetic reduction;
- exact command;
- observed output;
- expected interpretation;
- evidence or reasoning supporting the claim.

A domain expert's judgment can be valuable without being a software test. A software reproduction can be valuable without establishing domain legitimacy. Keep those evidence types separate.

## Privacy and safety

Do not post private contracts, personal data, security-sensitive operational details, confidential negotiation positions, or proprietary datasets in public issues. Reduce the problem to the smallest synthetic case that preserves the mechanism under challenge.

## Iteration principle

> The tool should not grow mainly because maintainers imagine more features. It should grow when real problems expose a repeated, explicit, testable boundary.

A failure to represent a real problem cleanly is not wasted use. It is one of the primary outputs this protocol is designed to capture.
