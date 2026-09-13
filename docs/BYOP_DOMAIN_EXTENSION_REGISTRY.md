# BYOP Domain Extension Registry

This registry is the intake layer for reusable domain-specific extensions built from real use.

## Principle

Do not expand the core merely because one domain has extra vocabulary. Prefer the smallest adequate layer:

`documentation → teaching/example → reusable template → domain extension → core/schema`

A domain extension should be proposed only when the same missing structure recurs across multiple problems in the same field and cannot be handled cleanly by documentation or a reusable template.

## Registration fields

For each proposal, record:

1. Domain and problem class
2. Repeated real-use need
3. Current representation gap
4. Why documentation or a teaching case is insufficient
5. Proposed additional fields, constraints, workflow, or adapter
6. What remains outside computation
7. Privacy / confidentiality requirements
8. Misinterpretation risks
9. Synthetic reproducible example
10. Tests or falsification conditions
11. Maintainer / downstream owner, if any
12. Status: proposed / experimental / reusable / independent fork / rejected

## Registered reusable template candidates

### 1. Commercial transaction / acquisition comparison

**Status:** experimental reusable template candidate

**Purpose:** compare several declared business arrangements against a common baseline without producing a universal winner.

**Current runnable candidates:** full acquisition; long-term supply agreement; minority investment + joint capacity.

**What v0.1.1 can show:** actor-specific deltas, declared hard-constraint results, and explicit UNKNOWN values.

**What it does not establish:** valuation truth, stakeholder consent, competition effects, bargaining power, legal validity, commitment credibility, transaction legitimacy, or whether any arrangement should be authorized.

See:

- [Reusable commercial transaction template](TEMPLATE_COMMERCIAL_TRANSACTION_COMPARISON.md)
- [BYOP end-to-end acquisition example](BYOP_END_TO_END_ACQUISITION.md)

### 2. Platform rule change / multi-actor burden

**Status:** experimental reusable template candidate

**Purpose:** compare alternative platform or ecosystem rules while keeping the rule setter, business users, end users, intermediaries, competitors, regulators, and other affected third parties explicit.

**What v0.1.1 can show:** static actor-specific outcome changes, hard-constraint results, UNKNOWN, and multi-candidate comparisons against one baseline.

**What it does not establish:** real security probabilities, dynamic ecosystem response, market-power evolution, legal interpretation, consent, legitimacy, or whether a rule should be adopted.

See [Reusable platform rule-change template](TEMPLATE_PLATFORM_RULE_CHANGE.md).

## High-consequence governance research track

The autonomous-weapons governance case from BYOP-04 remains a governance research input, not a runnable domain template. Dynamic escalation, diffusion, accountability, irreversibility, and rule legitimacy are not adequately represented by the current core. No operational weapons optimization or deployment logic belongs in the public reference implementation.

## Promotion rule

A template should not become a domain extension merely because it exists. Promotion requires repeated real-use evidence that the same missing structure recurs and cannot be handled by documentation, a teaching example, or the reusable template itself.

A domain extension should not become a core/schema change unless the missing structure is cross-domain, materially affects the declared semantics, and can be specified and falsified without silently importing domain-specific judgments.

## How to propose another domain

Open or comment in [BYOP Issue #25](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/25) and classify the proposal as `F — DOMAIN EXTENSION`.

Include the smallest synthetic example that preserves the missing mechanism. Do not post confidential contracts, personal data, private bargaining positions, or security-sensitive details.
