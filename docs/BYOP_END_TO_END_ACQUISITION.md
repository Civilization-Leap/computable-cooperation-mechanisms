# BYOP End-to-End Example｜Acquire the Supplier, or Keep It Independent?

Status: V0.1 synthetic teaching example. **Not empirical evidence, legal advice, valuation advice, or a recommendation to acquire a company.**

The purpose is to show how a real-world question travels through the BYOP loop and where v0.1.1 must stop.

## 1. Real question

A manufacturer depends on a key component supplier whose deliveries have become unstable. The manufacturer is considering acquisition.

Its declared purpose is:

> Improve supply continuity while controlling long-term cost and avoiding unacceptable concentration or third-party harm.

The question is not “Is cooperation good?” It is:

> Compared with continued independence, what do acquisition and less-integrated alternatives gain, cost, and place at risk?

## 2. Actors

For the synthetic example:

- **M** — manufacturer;
- **S** — supplier;
- **E** — affected employee group;
- **C** — downstream customer group.

A real case may require competitors, upstream suppliers, regulators, lenders, communities, or other actors. Omission must not be interpreted as absence of effect.

## 3. Candidate arrangements

### Baseline — remain independent under current purchasing pattern
Potential gain: preserves supplier independence and market optionality.  
Potential harm: supply instability and repeated negotiation continue.

### Candidate A — full acquisition
Potential gain: greater control over capacity and investment coordination.  
Potential harm: integration cost, reduced supplier independence, concentration risk, employee/customer burden.

### Candidate B — long-term supply agreement
Potential gain: continuity without full ownership transfer.  
Potential harm: contractual lock-in and incomplete control.

### Candidate C — minority investment + joint capacity program
Potential gain: shared investment and stronger coordination while preserving some independence.  
Potential harm: governance complexity and residual supply risk.

The current evaluator should **not** rank A/B/C into a universal winner. Each should be represented as a separate case against the same baseline.

## 4. Synthetic dimensions

Use only declared, comparable dimensions. For example:

| Actor | Dimension | Example unit | Meaning |
|---|---|---|---|
| M | annual procurement cost | CU/year | ordinary cost, not total welfare |
| M | supply interruption exposure | days/year | expected declared interruption exposure, if the case has a defensible declared value |
| S | financing burden | CU/year | declared financing burden |
| E | involuntary displacement | persons | affected employee count, if known and safe to represent |
| C | delivery delay | days | downstream delay exposure |

Do not combine these into one “fairness” number.

## 5. Example hard boundaries

A synthetic case might declare:

- customer delivery delay must not exceed a stated limit;
- employee displacement must not exceed a stated limit without a separate transition arrangement;
- capacity must remain above a declared continuity floor.

For every threshold ask:

1. who proposed it;
2. who is protected by it;
3. what evidence supports it;
4. who can challenge or revise it.

The evaluator can check `actual <= limit`. It cannot establish that the limit deserves authority.

## 6. What v0.1.1 can do

For each candidate, it can:

- compute matching baseline/candidate deltas;
- keep dimensions and units separate;
- check declared hard constraints;
- preserve UNKNOWN;
- show that ordinary gains do not erase a hard violation;
- produce deterministic output for the declared case.

## 7. What v0.1.1 cannot do cleanly

A realistic acquisition decision depends on factors beyond the current core, including:

- bargaining power and coercion;
- strategic misrepresentation;
- antitrust/competition-law analysis;
- valuation uncertainty and financing structure;
- multi-period integration dynamics;
- cultural/organizational effects;
- confidential information;
- whether employee/customer representatives had standing in setting thresholds;
- legitimacy of the final decision.

These are not to be silently approximated. They become BYOP feedback.

## 8. Example feedback produced by this use

This case would likely generate at least two useful reports:

**F — DOMAIN EXTENSION:** acquisition/strategic-partnership cases need a reusable domain template for control rights, time horizons, concentration, and exit/reversal conditions.

**A — REPRESENTATION GAP:** power asymmetry and multi-stage bargaining cannot currently be represented without flattening important causal structure.

That is a successful result. The example has exposed where a domain layer may be needed without proving that the minimal core should immediately expand.

## 9. Return to reality

After running candidate cases, the responsible actors should return to the real decision process and ask:

- Which result differences are supported by evidence?
- Which are only declarations?
- Which constraints failed?
- Which important facts remain UNKNOWN?
- Who was omitted?
- Which threshold lacks a defensible provenance or appeal path?
- Is there a new candidate arrangement worth negotiating?
- What evidence would change the decision?

The output is an input to deliberation. It is not the acquisition decision.

## 10. Iteration loop

`Real problem → Problem Card → Candidate cases → Run → Interpret → Expose gaps → Classify feedback → Template/domain/core decision → Re-test`

This is the intended growth mechanism for the open project.
