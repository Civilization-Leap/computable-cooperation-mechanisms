# BYOP Input Mapping｜From a Real Problem to v0.1.1

This document is the bridge between the problem card and the current reference implementation.

## 1. Keep three layers separate

### Reality layer
What actors actually want, fear, know, hide, control, and experience.

### Declared model layer
Only the actors, dimensions, units, baseline/candidate outcomes, hard constraints, and unknowns explicitly represented in a case.

### Decision layer
Negotiation, authorization, trial, rejection, or further evidence gathering after reading the report.

The evaluator operates only on the declared model layer. It does not prove the reality layer and does not control the decision layer.

## 2. Mapping table

| Problem-card item | Current model representation | Notes |
|---|---|---|
| Actor | declared actor identifier | Include affected third parties when they are represented |
| Purpose / interest | usually **not** a direct evaluator field | Translate only measurable/declared consequences needed for comparison; keep the narrative purpose in documentation |
| Baseline | baseline result values | Use the same actor + dimension + unit when a delta is intended |
| Candidate arrangement | candidate result values | For several candidates, create separate cases against a common baseline |
| Benefit / harm | result dimension + value + unit | Do not collapse unlike dimensions into a universal score |
| Hard boundary | hard constraint | Ordinary gains do not cancel a violated hard constraint |
| Unknown fact | explicit unknown | Preserve UNKNOWN; do not infer zero |
| Third-party impact | third-party actor result and/or hard constraint | The tool does not discover omitted third parties |
| Evidence/provenance | external documentation for now | v0.1.1 does not validate evidence |
| Authority to set threshold | external governance record for now | Not inferred from the existence of a constraint |
| Appeal / revision path | external process for now | Not implemented as a core evaluator state |

## 3. Multiple candidates

The current tool does not rank multiple arrangements. Use a common baseline and one case per candidate:

- `case_status_quo.json`
- `case_acquisition.json`
- `case_long_term_contract.json`
- `case_minority_investment.json`

Run each independently. Then compare:

1. matching deltas;
2. which hard constraints are SATISFIED / VIOLATED / UNKNOWN;
3. which actors/dimensions differ;
4. which important questions remain outside the representation.

Do **not** add unlike dimensions together merely to obtain a winner.

## 4. Cooperation and non-cooperation

“Cooperate” and “do not cooperate” are not evaluator verdicts. They are candidate arrangements.

A useful comparison asks both directions:

- What does cooperation gain and cost?
- What does non-cooperation gain and cost?
- What does competition preserve or improve?
- What does reduced competition risk losing?
- Who is affected but absent from the arrangement?

## 5. When to stop modeling

Stop and report a representation gap when the result would depend materially on something the current model cannot express without distortion—for example coercive power, strategic deception, a dynamic escalation path, confidential information that cannot safely be abstracted, or an irreversible condition whose threshold has no defensible declared basis.

A clean “cannot yet represent this” is a successful output of the BYOP process.

## 6. Run and interpret

For the fixed public baseline:

```bash
git clone --branch v0.1.1 --depth 1 https://github.com/Civilization-Leap/computable-cooperation-mechanisms.git
cd computable-cooperation-mechanisms
python scripts/reproduce_offline.py
```

After reproducing the baseline, copy an existing same-class example and change only declared fields supported by the schema. Invalid or unsupported fields should be rejected rather than silently interpreted.

Interpret a report as:

> Under these declared inputs and declared rules, these deltas and constraint results follow.

Do not interpret it as:

> This arrangement is fair, legitimate, safe, morally correct, or authorized.
