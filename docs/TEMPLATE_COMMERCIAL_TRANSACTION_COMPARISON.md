# Reusable Domain Template | Commercial Transaction / Acquisition Comparison

**Status:** experimental reusable template candidate

Use this template to compare multiple declared commercial arrangements against a common baseline without collapsing all consequences into one score and without treating a computed result as transaction advice or authorization.

## 1. Typical arrangements

- full acquisition
- minority investment
- long-term supply agreement
- joint venture or joint capacity
- licensing or access commitment
- strategic partnership
- status quo / no transaction

## 2. Required structure

1. State each actor's own purpose.
2. Define a common baseline.
3. Create separate candidate arrangements.
4. Keep actor, dimension, and unit separate.
5. Declare third-party impacts.
6. Declare hard boundaries and their source.
7. Preserve unknowns explicitly.
8. Record which parts the current evaluator cannot represent without distortion.

## 3. Typical actors

Acquirer or investor, target or supplier, employees, customers, competitors, regulators, and other affected ecosystem participants.

## 4. Candidate arrangements

At minimum, where relevant, compare full acquisition, continued independent commercial cooperation, minority investment or joint capacity, and status quo / no transaction.

## 5. Useful dimensions

Cost, transaction value, cash-flow exposure, supply continuity, access rights, control rights, switching cost, concentration or dependence, employee impact, customer impact, implementation risk, and reversibility or exit cost.

Do not merge unlike dimensions unless the domain supplies an explicit and justified conversion rule.

## 6. Hard boundaries

A hard boundary is a declared non-offsettable condition. Encoding it does not make it legitimate. Record who set it, its source, and whether its legitimacy is disputed.

## 7. What v0.1.1 can do

- compare declared baseline and candidate outcomes by actor + dimension + unit;
- check declared hard constraints independently of ordinary gains;
- preserve explicit UNKNOWN;
- compare separate candidate cases against a common baseline;
- produce deterministic reproducible reports.

## 8. What remains outside the current core

Do not silently encode valuation truth, future strategic behavior probability, market definition, bargaining-power dynamics, stakeholder consent, long-term commitment credibility, dynamic market structure, legal or regulatory conclusions, or real-world authorization.

Record those as evidence limits, representation gaps, or domain-extension needs.

## 9. Interpretation rule

A valid result means only: under these declared inputs and declared rules, these changes and constraint results follow.

It does not mean the data are true, the threshold is legitimate, the arrangement is fair, or the transaction should proceed.

## 10. Feedback classes

Use one or more when needed: A REPRESENTATION GAP; C MISSING ACTOR / IMPACT; D MISSING CONSTRAINT; E MISINTERPRETATION RISK; F DOMAIN EXTENSION; G CORE DEFECT.

## 11. Runnable teaching example

See `docs/BYOP_END_TO_END_ACQUISITION.md` and the three `examples/byop_acquisition_*.json` fixtures. All values are synthetic.
