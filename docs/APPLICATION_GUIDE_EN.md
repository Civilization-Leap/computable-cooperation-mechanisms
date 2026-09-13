# How to Use Computable Competition–Cooperation Mechanisms on Real Problems

## Purpose: not merely to use a tool, but to help actors pursue their own goals more clearly

This project provides three things together:

1. **Theory** — why cooperation and non-cooperation, competition and coordination should be compared together in terms of benefits, harms, risks, and long-term consequences;
2. **Tooling** — a small reference implementation that makes declared actors, outcomes, constraints, third-party effects, unknowns, and failure conditions explicit enough to inspect and recompute;
3. **Method of use** — a way for different actors to bring their own goals, constraints, and candidate arrangements into a structured comparison without letting the tool choose their goals for them.

The real-world value is not that software produces a single “correct answer.” It is that conditions hidden inside positions, negotiations, organizational inertia, or conflict escalation can become visible earlier, so actors have a better chance to discover a better way to compete, cooperate, delay, limit, or exit.

---

## 1. Start from your own objective

Different actors do not need to enter the project with the same goal.

A firm may care about profit, cash flow, supply security, growth, control, and long-term competitiveness. Workers may care about income, safety, dignity, career development, and exit rights. Platforms may care about efficiency, growth, ecosystem stability, and compliance. Public institutions may care about public benefit, risk, stability, innovation, and resilience. Researchers may care about falsifiability, reproducibility, and extensibility. International actors may care about security, deterrence, miscalculation, escalation, and irreversible consequences.

**The actor owns the objective. The project does not assign it.**

The project instead helps ask:

- What am I actually trying to achieve?
- Which conditions are hard constraints?
- Which costs do I bear, and which are shifted to others?
- What do I gain and lose by cooperating?
- What do I gain and lose by not cooperating?
- What happens if competition escalates?
- What might be lost if competition is reduced?
- Is there a third arrangement?
- Which facts are known, inferred, or still unknown?
- Which consequences would be difficult or impossible to reverse?

---

## 2. Minimal workflow: begin with one real problem

### Step 1 — Define the problem before defining the answer

Write down:

- the situation;
- the direct actors;
- affected third parties;
- the current state;
- what you want to change.

Do not begin with “cooperation must be better” or “competition must continue.”

### Step 2 — Separate positions from underlying interests and constraints

Example:

- Position: “I cannot lower the price.”
- Possible underlying constraints: cash flow, minimum margin, capacity risk, financing terms.

If sensitive information cannot be disclosed, the method can use bounded disclosure, ranges, or third-party verification instead of demanding that every actor expose all private information.

### Step 3 — Define at least two candidate arrangements

At minimum compare:

- **A: cooperation / deeper cooperation / the current proposal**;
- **B: non-cooperation / status quo / independent action**.

Where useful, add:

- C: limited cooperation;
- D: delay;
- E: third-party guarantee, staged trial, exit clause, risk sharing, or another newly composed option.

### Step 4 — Make outcomes, constraints, and third-party effects explicit

For each candidate, record at least:

- what each actor gains;
- what each actor loses;
- what third parties bear;
- which hard constraints must hold;
- which outcomes remain unknown;
- which consequences are irreversible or very costly to restore.

### Step 5 — Use the reference tool for mechanical checks

The current v0.1.1 implementation can:

- compare declared baseline and candidate outcomes;
- compute deltas only for matching actor + dimension + unit;
- check declared hard constraints independently;
- preserve `UNKNOWN` instead of silently replacing it with zero;
- reject unsupported fields and inconsistent input;
- produce deterministic, reproducible output and hashes.

It **cannot**:

- decide whether an objective is legitimate;
- decide what a threshold should be;
- prove that input data are true;
- assign moral scores to actors;
- infer motives;
- predict behavior;
- replace negotiation, legal authority, or public decision-making.

### Step 6 — Return to human judgment and real negotiation

The output is not the end. It is input to the next round of reasoning.

Ask:

- Why is this threshold set here?
- Who participated in setting it?
- Who is absent but bears the consequences?
- Does the verdict flip when a parameter changes slightly?
- Which unknown matters most to verify next?
- Can the next step be small-scale, reversible, and easy to exit?

---

## 3. How different actors can use the method

### Business and commercial negotiation

**Possible goals:** cost reduction, supply stability, profit, acquisition, default-risk reduction, market growth.

**Method:**

- separate price, control, delivery time, cash flow, risk allocation, and exit rights into distinct dimensions;
- compare both cooperation and non-cooperation over short and long horizons;
- inspect whether gains shift costs to employees, suppliers, customers, or market competition;
- compose multiple deal structures instead of bargaining only over one scalar price;
- use limited or staged commitments to generate evidence before expanding cooperation.

**Example: acquisition**

Do not compare only “buy / do not buy.” Compare long-term procurement, minority equity, joint investment, supply guarantees, second sourcing, staged acquisition, or cooperation with exit conditions. The tool can show declared changes and constraint results; it does not decide whether an acquisition is legitimate or desirable.

### Labor and organizations

**Possible goals:** income, safety, dignity, continuity, organizational efficiency, business survival.

Use the method to separate what lies behind “raise pay / do not raise pay” or “lay off / do not lay off,” compare short-term cost against turnover and skill loss, preserve non-compensable protections, and design arrangements that can be renegotiated or exited.

### Platforms and ecosystems

**Possible goals:** growth, efficiency, user experience, creator/merchant stability, safety.

Separate platform gains from participant burdens, compare rule change versus no change, identify hidden third-party risk, and preserve appeal, correction, and renegotiation paths.

### Public governance and social innovation

**Possible goals:** public service, efficiency, risk control, stability, innovation.

Make visible who benefits, who bears costs, and who is missing from the table; represent protections that cannot simply be offset by aggregate gains; compare policy alternatives explicitly; and keep disputes about facts, thresholds, rights, and consequences visible rather than hiding them inside a single score.

The tool can assist comparison. It cannot confer legitimacy on public policy.

### AI / AGI and high-consequence technology governance

**Possible goals:** capability benefits, safety, competitive advantage, public benefit, reduction of irreversible risk.

Compare deployment and non-deployment, openness and restriction, competitive escalation and coordination. Keep direct gains, systemic risk, third-party burdens, and irreversible consequences separate. Keep the question of **who has authority to set the threshold** explicit instead of hiding it inside computation.

**Example: disconnected autonomous weapons**

Actors may include militaries, states, adversaries, civilians, allies, technology suppliers, and future diffusion environments. Compare tactical benefits, reduced personnel exposure, the cost of non-use, adversary follow-on adoption, misidentification risk, broken responsibility chains, proliferation, and the effect on future conflict thresholds. The tool can help make variables, constraints, and unknowns explicit; it cannot determine the justice of war or authorize weapon use.

### International relations, alliances, and conflict prevention

**Possible goals:** security, deterrence, sovereignty, development space, crisis stability.

Make security fears and commitment structures visible, compare cooperation and non-cooperation symmetrically, explore arms-race and escalation chains through counterfactuals, identify steps that close future negotiation windows, and—where no compatible solution exists—at least make confrontation costs and irreversible outcomes visible earlier.

---

## 4. Bring Your Own Problem (BYOP)

Use this template:

1. **Situation** — what is happening?
2. **Actors** — who participates and who is affected?
3. **Actor objectives** — what does each actor want?
4. **Current positions** — what are they currently saying or demanding?
5. **Underlying constraints** — what interests, capacities, limits, and risks actually drive behavior?
6. **Candidate arrangements** — include at least cooperation and non-cooperation, plus third paths where relevant.
7. **Outcome dimensions** — money, time, safety, control, risk, opportunity, exit rights, third-party effects, etc.
8. **Hard constraints** — which outcomes are unacceptable and cannot be offset by other gains?
9. **Unknowns** — what is not known yet?
10. **Irreversibilities** — what would be difficult to restore once changed?
11. **Question for the tool** — e.g. Which candidate violates a declared boundary? Which unknown is decisive? Does a threshold change flip the verdict?

---

## 5. What “helping actors achieve their goals” means here

The project does not promise to maximize every actor’s payoff.

It aims to help actors:

- define their objectives more clearly;
- see the actual conditions required to pursue them;
- see what their preferred arrangement does to others;
- see the costs of non-cooperation, not only the benefits of cooperation;
- discover previously hidden third options;
- preserve more room for correction before high-consequence decisions;
- use verifiable performance to lower the cost of future cooperation;
- understand confrontation boundaries and costs more clearly when cooperation is impossible.

So the division of labor is:

**Theory explains why the problem should be viewed this way. The tool makes part of the structure runnable and recomputable. Real actors remain responsible for objectives, value judgments, negotiation, authorization, and action.**

---

## 6. Start here

- Idea guide: [`Can We Learn to Compete and Cooperate Better?`](PUBLIC_IDEA_GUIDE_EN.md)
- Five-minute run: repository [`README.md`](../README.md)
- Public testing: [`THIRD_PARTY_TESTING.md`](THIRD_PARTY_TESTING.md)
- Current public testing baseline: `v0.1.1`

> **A mechanism becomes useful not merely because it can compute, but because it helps real actors see choices, costs, and consequences earlier while preserving the ability to change course.**
