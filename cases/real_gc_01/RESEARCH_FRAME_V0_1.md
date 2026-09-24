# REAL GC 01 — U.S.–China Competition and Cooperation

## V0.1 Research Frame

**Status:** research-frame candidate; no policy conclusion  
**As-of date:** 2026-09-25  
**Project:** Computable Cooperation Mechanisms (CCM)  
**Author:** 子君赋  
**Produced by:** 文明跃迁研究组

## 1. Idealized research objective

REAL GC 01 asks:

> Under different domains, conditions, and time horizons, how should competition, cooperation, and mixed strategies be selected, combined, switched, and constrained so that the United States, China, and affected third parties can move toward jointly greater benefits and jointly lower risks?

“Jointly greater benefits” is **not** defined as a simple sum. A configuration that creates a large gain for one actor by imposing severe losses or irreversible risks on another actor is not automatically classified as a common optimum.

The project does **not** assume that cooperation is preferable to competition, that competition is preferable to cooperation, or that either country should surrender legitimate interests. The objective is a search criterion, not a predetermined conclusion.

## 2. Decision unit

The unit of analysis is not “the U.S.–China relationship” as one scalar.

A decision unit is:

```
(domain, action, counteraction, affected actors, time horizon, evidence state)
```

The first version will study three domain families separately:

1. trade and supply chains;
2. AI competition and safety cooperation;
3. military crisis and strategic stability.

Cross-domain aggregation is deferred until domain-specific assumptions and units are explicit.

## 3. Actors

Primary actors:

- `US`: United States;
- `CN`: China.

Third-party effects must not be collapsed into one residual number. V0.1 keeps at least four third-party classes:

- `TP_ALLIES_PARTNERS`: allies and partners materially affected by the choice;
- `TP_OTHER_STATES`: other states, especially those exposed to trade, technology, or security spillovers;
- `TP_FIRMS_WORKERS`: firms, workers, consumers, and supply-chain participants not adequately represented by national aggregates;
- `TP_GLOBAL_PUBLIC`: global public interests, including systemic stability and transboundary risks.

No actor class is presumed internally homogeneous. Distributional decomposition is required when aggregation would hide a material burden.

## 4. Strategy states

V0.1 compares four abstract strategy states. They are research conditions, not descriptions of either government and not normative labels.

| State | Working definition |
|---|---|
| `S0_HIGH_COMP_LOW_COOP` | high competition with low institutionalized cooperation |
| `S1_BOUNDED_COMP_MIN_COOP` | bounded competition plus minimum cooperation needed to manage shared risks/interdependence |
| `S2_HIGHER_COOP_RETAINED_COMP` | broader verifiable cooperation while preserving competition and exit options |
| `S3_ESCALATORY_RECURSION` | action–counteraction recursion in which each side’s move materially increases incentives for further counteraction |

A real policy can contain components from more than one state. The model must therefore permit domain-level mixtures rather than force a single label onto the entire bilateral relationship.

## 5. Outcome vector

For each actor or actor class `i`, record separately:

```
B_i(t) = direct and indirect benefits
C_i(t) = direct and indirect costs
R_i(t) = risk exposure
F_i(t) = feedback cost/benefit returning to i after responses by other actors
O_i(t) = option value: preserved future choices, switching ability, and exit capacity
```

A provisional actor-level accounting identity is:

```
U_i(t) = B_i(t) - C_i(t) - R_i(t) + F_i(t) + O_i(t)
```

This is an accounting scaffold, **not yet a commensurable welfare function**. Monetary, security, rights, mortality, autonomy, and irreversible-risk quantities must not be silently converted into one unit.

## 6. Causal feedback

Every scenario must expose, where relevant:

```
initial action
  -> response by the other primary actor
  -> third-party response
  -> structural change
  -> changed incentives / risk
  -> consequence returning to the initiating actor
```

This prevents a locally beneficial first move from being recorded as a complete benefit before its strategic feedback is considered.

## 7. Search rule

The model searches for **non-dominated configurations**, not a political winner.

Configuration A dominates B only if, under the declared evidence and uncertainty:

1. at least one materially affected actor is better off or less exposed to risk under A;
2. no materially affected actor is materially worse off under A;
3. no irreversible-risk boundary is crossed under A.

Where trade-offs remain, the result is a **Pareto set / decision frontier**, not a forced single optimum.

A stronger claim—“common maximum benefit and minimum risk”—may be made only if a configuration is demonstrably superior under the declared dimensions and robustness tests. Otherwise the output must preserve multiple non-dominated choices.

## 8. Minimum sufficient cooperation

V0.1 introduces a research object:

**Minimum Sufficient Cooperation (MSC):** the smallest verifiable cooperation set that prevents a specified competition process from crossing a declared shared-risk or irreversibility boundary while preserving as much legitimate competitive freedom as possible.

MSC is domain-specific. It must not be assumed identical for trade, AI, and military security.

Questions include:

- What competition can continue without destroying future cooperation or exit options?
- Which information, communication, verification, or emergency mechanisms are minimally necessary?
- When does reducing cooperation increase both sides’ risk?
- When can excessive cooperation create concentration, dependency, capture, or third-party harm?

## 9. Irreversible / catastrophic-risk boundary

Expected-value maximization is insufficient where plausible outcomes include catastrophic or practically irreversible harm.

V0.1 therefore separates:

- ordinary reversible trade-offs;
- high-impact but recoverable losses;
- structural lock-in / option destruction;
- catastrophic or irreversible outcomes.

A scenario crossing a declared irreversible-risk boundary is not automatically offset by unrelated aggregate benefits.

Thresholds are **not yet populated**. They require domain-specific evidence and justification.

## 10. Evidence states

Every material input must carry one of:

- `OBSERVED`
- `OFFICIAL_CLAIM`
- `THIRD_PARTY_ESTIMATE`
- `CONDITIONAL_ASSUMPTION`
- `UNKNOWN`

Rules:

- `UNKNOWN` is not zero.
- An official claim is not automatically an observed effect.
- A conditional scenario is not a forecast.
- AI-assisted analysis is not independent validation.
- Missing evidence must not be filled to make a preferred strategy win.

## 11. Time horizons

At minimum:

- `T0`: immediate / <= 1 year;
- `T1`: medium term / 1–5 years;
- `T2`: long term / > 5 years.

A strategy that improves `T0` while degrading `T1/T2` must expose that trade-off rather than netting it away.

## 12. First three study modules

### GC-T01 — Trade and supply chains

Initial questions:

- Which gains arise from competition, diversification, negotiated trade, or technical cooperation?
- Which gains are genuinely strategy-specific rather than attributable to technology or ordinary market adaptation?
- What are the response effects of tariffs, restrictions, diversification, substitution, and reciprocal measures?
- Who bears costs inside each country and among third parties?
- Which choices preserve switching and future bargaining options?

Public baseline: USTR currently reports estimated 2025 U.S.–China goods-and-services trade of USD 494.6 billion. In June 2026 USTR also described a government-to-government Board of Trade mechanism intended to manage bilateral trade while seeking potentially mutually beneficial trade in selected non-sensitive goods and retaining national-security measures. These are contextual observations, not evidence that a particular cooperation level is optimal.

### GC-AI01 — AI competition and safety cooperation

Initial questions:

- Which forms of AI competition improve capability, productivity, safety, or diffusion?
- Which competitive dynamics create incentives to reduce safety margins or increase strategic opacity?
- Which safety information can be shared without requiring either side to surrender legitimate security or commercial interests?
- What is the MSC set for high-consequence AI incidents?
- How do controls or cooperation affect third countries’ access, dependency, and risk?

No quantitative baseline is asserted in V0.1.

### GC-S01 — Military crisis and strategic stability

Initial questions:

- Which competitive actions increase deterrence for one actor but increase perceived vulnerability for the other?
- When does an action–counteraction sequence reduce both actors’ security?
- Which communication, verification, deconfliction, or emergency-stop mechanisms constitute MSC?
- Which outcomes are too catastrophic or irreversible to be traded against ordinary economic gains?

No probability of war, victory, or political forecast is assigned in V0.1.

## 13. Current factual context

This research frame is being opened during a period in which competition and cooperation coexist in observable policy.

On 24 September 2026, the White House hosted Chinese President Xi Jinping for a state visit. Chinese official statements around the visit describe an objective of cooperation, bounded competition, controlled differences, and peace. U.S. trade policy in 2026 likewise contains both restrictive/national-security instruments and a newly described bilateral trade-management mechanism for selected non-sensitive trade.

These facts motivate the research question. They do not validate the CCM objective function or establish the effects of any policy.

## 14. V0.1 non-claims

V0.1 does **not** claim:

- that one country is responsible for the current state of bilateral relations;
- that cooperation is generally superior to competition;
- that competition is generally superior to cooperation;
- that a numerical “correct” U.S.–China policy has been calculated;
- that national welfare can be reduced to GDP or trade volume;
- that third-party interests are homogeneous;
- that official statements establish realized outcomes;
- that AI-generated scenarios constitute empirical evidence;
- that the three initial modules exhaust the relationship.

## 15. Falsification and challenge requirements

A useful challenge may show that:

- an actor or burden is missing;
- a variable is not measurable;
- an assumed causal link fails;
- feedback is double-counted;
- two dimensions cannot legitimately be aggregated;
- a proposed MSC mechanism increases another risk;
- a non-dominated result changes under plausible assumptions;
- an allegedly reversible choice destroys a real exit option;
- a third path dominates the competition/cooperation choices currently represented.

Strong conclusions remain open to counterexample and revision.

## 16. Next executable milestone

**REAL_GC_01_V0.2_MIN_MODEL**

Build the smallest executable model that:

1. accepts actor-specific outcome vectors without forcing commensurability;
2. represents `S0–S3` and mixed domain strategies;
3. carries evidence state and time horizon on every material input;
4. propagates at least one declared action–response–feedback chain;
5. identifies dominated and non-dominated configurations;
6. separately flags irreversible-risk boundary crossings;
7. leaves missing quantities `UNKNOWN`;
8. produces no “winner” when evidence is insufficient.

The first conditional grid should use synthetic assumptions only. Empirical calibration follows after the model’s representation boundaries are explicit.
