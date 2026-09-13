# BYOP Domain Extension Registry

This registry is the intake layer for reusable domain-specific extensions built from real use.

## Principle

Do not expand the core merely because one domain has extra vocabulary. Prefer the smallest adequate layer:

`documentation → teaching/template → domain extension → core/schema`

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

## First registered domain template

### Commercial transaction / acquisition comparison

**Status:** experimental teaching template

**Purpose:** compare several declared business arrangements against a common baseline without producing a universal winner.

**Current runnable candidates:**

- full acquisition;
- long-term supply agreement;
- minority investment + joint capacity.

**What v0.1.1 can show:** actor-specific deltas, declared hard-constraint results, and explicit UNKNOWN values.

**What it does not establish:** valuation truth, employee consent, antitrust effects, bargaining power, legal validity, fiduciary duties, transaction legitimacy, or whether any arrangement should be authorized.

See [BYOP end-to-end acquisition example](BYOP_END_TO_END_ACQUISITION.md).

## How to propose another domain

Open or comment in [BYOP Issue #25](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/25) and classify the proposal as `F — DOMAIN EXTENSION`.

Include the smallest synthetic example that preserves the missing mechanism. Do not post confidential contracts, personal data, private bargaining positions, or security-sensitive details.