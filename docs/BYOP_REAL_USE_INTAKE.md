# BYOP Real-Use Intake and Triage

This document turns public BYOP submissions into a low-maintenance, repeatable open-source iteration process.

## Goal

The project should not grow because maintainers imagine features. It should grow when repeated real-use attempts expose explicit, testable limits.

The intake loop is:

**Real problem → structured intake → smallest synthetic case → run or stop → classify the gap → choose the smallest response layer → re-test**

## Intake channels

1. Use the GitHub **Bring Your Own Problem** issue form for a new public case.
2. Use Issue #25 for general BYOP discussion and cross-case synthesis.
3. Use Issue #14 for reproduction or implementation evidence that is primarily about software behavior rather than a domain problem.

## Minimum usable submission

A submission is useful when it states:

- the actor's purpose;
- participating and affected actors;
- candidate arrangements, including non-cooperation / status quo where relevant;
- gains, losses, risks, and hard boundaries;
- unknowns and evidence limits;
- what the current tool can and cannot represent;
- the smallest synthetic or anonymized example that preserves the mechanism.

A submission does **not** need to prove the theory correct. A clean representation failure is useful evidence.

## Triage classes

- **A — REPRESENTATION GAP**: material mechanism cannot be represented without distortion.
- **B — COUNTEREXAMPLE**: documented assumption or invariant fails.
- **C — MISSING ACTOR / IMPACT**: an affected party has no adequate place.
- **D — MISSING CONSTRAINT**: a non-offsettable condition cannot be represented.
- **E — MISINTERPRETATION RISK**: output invites a stronger claim than it supports.
- **F — DOMAIN EXTENSION**: core may be sufficient, but the field needs a reusable template or adapter.
- **G — CORE DEFECT**: declared semantics are implemented incorrectly or inconsistently.

## Response-layer rule

Always prefer the smallest adequate response:

**documentation → teaching/example → reusable template → domain extension → core/schema**

Core changes require evidence that the missing structure is not merely domain vocabulary and that the same need recurs across distinct cases.

## Evidence status

Use the following status vocabulary when summarizing a case:

- **SUBMITTED** — intake exists but has not been reproduced or reviewed.
- **TRIAGED** — classified and routed to a response layer.
- **REPRODUCED** — the stated behavior was independently or maintainer-reproduced from supplied material.
- **COUNTEREXAMPLE CONFIRMED** — a documented assumption or invariant is shown false within stated scope.
- **TEMPLATE CANDIDATE** — repeated need appears domain-specific and reusable.
- **CORE CANDIDATE** — repeated need appears general enough to justify core/schema consideration.
- **RESOLVED** — documentation/template/code response landed and was re-tested.

Do not turn SUBMITTED or TRIAGED into claims of validation, adoption, or empirical proof.

## Privacy and safety boundary

Public submissions must not include confidential contracts, personal data, private bargaining positions, proprietary datasets, credentials, classified material, or security-sensitive operational details. Reduce a real problem to a synthetic case whenever possible.

## Decision questions for maintainers and contributors

Before changing anything, ask:

1. Is this a problem in the current code, or a limitation of the model contract?
2. Can the issue be resolved by clearer documentation?
3. Does a reusable example or template solve it without touching the core?
4. Has the same gap appeared in more than one case?
5. Would a new field silently smuggle a normative assumption into the computation?
6. What still remains outside computation after the change?
7. What test would falsify the proposed fix?

## Success criterion

The loop succeeds when a real-use attempt produces one of two honest outcomes:

- the current tool represents the declared mechanism clearly enough to inspect and challenge; or
- the attempt exposes a precise boundary that can be classified, reproduced, and used to guide the next smallest change.

The project does not need to force every problem into software.
