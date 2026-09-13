# Why CCM Is Not “Just Use an AI”

> **AI and agents help us see, reason, compute, and act. CCM asks who gains, who bears the burden, what cannot be traded away, what remains unknown, and when the system must stop and reconsider.**

A capable model can already simulate multiple perspectives, list benefits and harms, identify third-party risks, and produce sophisticated recommendations. That does not make CCM redundant.

The distinction is between **capability** and **mechanism**.

If an AI notices a third party only because the prompt reminded it to, admits uncertainty only when it feels appropriate, or silently turns a hard boundary into a trade-off, the result still depends on the model, prompt, and context of that run.

CCM tries to externalize those requirements into a repeatable, inspectable structure.

## Different jobs

| | General AI | Advanced agent | CCM |
|---|---|---|---|
| Main question | What is the answer? | How do I accomplish the goal? | If the goal is pursued, who gains, who bears costs, what remains unknown, and what must not be crossed? |
| Goal source | Prompt / learned preferences | Task objective / workflow | Actor purposes are explicit, but CCM does not choose them for the actors |
| Multi-actor effects | Can be simulated | Can coordinate or compete | Actor separation is first-class |
| Third parties | Easy to omit | Often outside the task objective | Burdens on people outside the negotiating table must be exposed |
| Unknowns | Often estimated or filled in | Pressure to keep planning | `UNKNOWN` may remain `UNKNOWN` |
| Hard constraints | Policy / guardrails | Permissions | Kept separate from ordinary gains; not offset by a larger benefit elsewhere |
| Legitimacy | Usually outside the core task | Completion is central | Computation, factual truth, legitimacy, and authorization remain distinct |
| New evidence | Answer again | Re-plan | States can be upgraded, downgraded, frozen, or withdrawn |
| Diffusion | Usually not governed | Deployment is success | CCM also asks whether a solution should propagate and whether it can be misused |

## A good prompt can imitate the output, not the mechanism

A prompt can ask an AI to “analyze every side, include third parties, and state uncertainties.” That can be useful.

CCM adds structural requirements:

- actors remain separate rather than disappearing into a total score;
- third-party burdens cannot vanish because the third party lacks a seat at the table;
- explicit unknowns are preserved rather than filled with zero or a convenient assumption;
- hard constraints are not compensated away by unrelated gains;
- a precise calculation does not become a claim of fairness, legitimacy, or authority;
- maintainer observations, external-AI reviews, independent executions, and domain use carry different evidence labels;
- conclusions can be formally downgraded when new evidence appears;
- propagation is gated: an efficient solution may still be an efficient way to externalize harm;
- misuse is checked separately, because exposing a vulnerable party’s limits can itself enable more precise pressure.

If none of that structure exists and a model is simply asked to “think more broadly,” that is a better AI analysis. It is not yet CCM.

## The 0.50 / 0.49 example

In the public threshold-sensitivity example:

- A and B each reduce declared cost from 8 to 5;
- third party C’s loss remains 0.5;
- with a declared protection ceiling of 1, 0.6, or 0.5, the constraint is `SATISFIED`;
- lowering only that ceiling to 0.49 changes the result to `VIOLATED`.

Nothing about the actors’ outcomes changed. Only the line changed.

A calculator can determine whether `0.5 <= 0.49`.

The governance question is different: **Why is the line 0.49? Who had authority to draw it? Did C have any voice in the rule that decides C’s status?**

[Run the threshold sweep and inspect the full reports](THRESHOLD_SENSITIVITY.md).

## Why this matters more as agents become stronger

An agent can be extremely competent at pursuing a narrow objective. If the objective is “maximize my benefit,” it may also become extremely competent at externalizing costs that the task did not represent.

The intended relationship is therefore not `CCM vs. agents`:

```text
Human / organization
        ↓
Purpose
        ↓
CCM framing
actors / interests / burdens / hard constraints / unknowns
        ↓
AI / agent planning and execution
        ↓
CCM re-check
evidence / third parties / direction / irreversible effects
        ↓
execute / pause / downgrade / reject / renegotiate
```

**AI provides cognitive capability. Agents provide action capability. CCM provides competition–cooperation governance.**

## What CCM does not replace

CCM does not replace general reasoning, search, coding, vision, mathematical optimization, tool use, domain expertise, legal authority, or human responsibility.

Its focus is the layer most easily compressed by a task objective: **multi-actor relations, third-party burdens, hard boundaries, unknowns, irreversibility, legitimacy, and evidence governance.**

## Continue

- [Why this project exists](PUBLIC_IDEA_GUIDE_EN.md)
- [Bring your own problem](BYOP_START_HERE.md)
- [Application guide](APPLICATION_GUIDE_EN.md)
- [Run it in five minutes](../README.md#try-it-in-five-minutes)
- [Third-party testing](THIRD_PARTY_TESTING.md)
- [Civilization Leap — the wider context](https://www.civitas.top/)

CCM is not an attempt to make intelligence stronger.

**It is an attempt to keep stronger intelligence, stronger organizations, and stronger action capable of seeing other actors, uncertainty, boundaries, and the possibility of choosing again.**
