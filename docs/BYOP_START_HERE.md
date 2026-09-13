# Bring Your Own Problem｜Start Here

**Understand → Bring a Problem → Model → Run → Interpret → Challenge → Extend**

This is the shortest path from the project's theory to a real-use attempt and from a failed use attempt back into open-source iteration.

## 1. Understand

Read the public idea guide first:

- [我们能否学会更好地竞争与合作？](PUBLIC_IDEA_GUIDE_ZH.md)
- [Can We Learn to Compete and Cooperate Better?](PUBLIC_IDEA_GUIDE_EN.md)

The project does not assume that cooperation is always good or competition always bad. It asks what cooperation and non-cooperation each gain, cost, preserve, damage, or make irreversible—and who bears consequences without being at the table.

## 2. Check current capability

Read the [Capability Ledger](BYOP_CAPABILITY_LEDGER.md). Do not force a real problem into the current schema when a material mechanism is unsupported.

## 3. Bring a problem

Fill the [Problem Card](BYOP_PROBLEM_CARD.md). Start with your own purpose, affected actors, candidate arrangements, third-party impacts, hard boundaries, evidence/unknowns, and what would change your view.

## 4. Map it to the current tool

Use the [Input Mapping](BYOP_INPUT_MAPPING.md) to separate:

- reality;
- the declared computable model;
- the later human/institutional decision.

For several arrangements, use separate candidate cases against a common baseline. Do not create a universal score merely to obtain a winner.

## 5. Run

Reproduce the fixed v0.1.1 baseline first:

```bash
git clone --branch v0.1.1 --depth 1 https://github.com/Civilization-Leap/computable-cooperation-mechanisms.git
cd computable-cooperation-mechanisms
python scripts/reproduce_offline.py
```

Then build the smallest synthetic/anonymized case that represents your problem without disclosing confidential information.

## 6. Interpret

A valid report means:

> Under these declared inputs and declared rules, these deltas and constraint results follow.

It does **not** mean:

> The inputs are true, the threshold is legitimate, the arrangement is fair, or the action is authorized.

## 7. Challenge

If the problem cannot be represented cleanly, stop. That is useful evidence.

Classify the result using the [Feedback Protocol](BYOP_FEEDBACK_PROTOCOL.md): representation gap, counterexample, missing actor/impact, missing constraint, misinterpretation risk, domain extension, or core defect.

## 8. Extend only at the right layer

Prefer the smallest adequate response:

`documentation → teaching/template → domain extension → core/schema`

Some problems should remain outside software.

## 9. See one complete example

Read [Acquire the Supplier, or Keep It Independent?](BYOP_END_TO_END_ACQUISITION.md). It deliberately shows both what v0.1.1 can express and where a realistic acquisition problem exceeds the current core.

## 10. Return the result

Public feedback should use synthetic/anonymized material only. Never post confidential contracts, personal data, security-sensitive details, or private bargaining positions.

The intended loop is:

**Real problem → Problem Card → Candidate cases → Run → Interpret → Expose gaps → Classify feedback → Template/domain/core decision → Re-test**

The tool should grow because real problems expose repeated, explicit, testable boundaries—not because maintainers continuously invent features.
