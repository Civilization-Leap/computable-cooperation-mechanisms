# GC-T01 — Evidence Compatibility Audit V0.1

**Case:** REAL GC 01  
**Module:** GC-T01  
**As-of:** 2026-09-25  
**Purpose:** determine which ingested evidence can enter one conditional calculation without false arithmetic.

## Compatibility dimensions

Two records are numerically composable only when their intended calculation has
compatible:

1. period / policy episode;
2. population (country, sector, product, firm, household, county);
3. unit and price basis;
4. causal estimand;
5. baseline/counterfactual;
6. treatment universe;
7. treatment of retaliation;
8. treatment of tariff revenue;
9. treatment of third-country diversion;
10. equilibrium scope (accounting / partial equilibrium / general equilibrium).

“Same topic” is not sufficient.

## Audit matrix

| Evidence | Period | Population / scope | Unit / estimand | Retaliation | Third-country | Equilibrium scope | Current compatibility disposition |
|---|---|---|---|---|---|---|---|
| E001–E015 | 2025 / 2026 partial | bilateral aggregate trade | USD trade flows/balances | n/a | implicit in realized flows | accounting | **CONTEXT_ONLY** — descriptive scale, not welfare |
| E016 | 2018–21 | directly affected imports | tariff pass-through / importer incidence | mixed policy episode | not primary | econometric/partial | **GROUP A** |
| E017–E018 | 2018–21 | Section 301 affected sectors/products | import response, prices, production | report scope includes policy environment but estimands differ | not primary | sector/partial | **GROUP A with restrictions** |
| E019 | 2018–19; early 2025 | consumer goods / PCE | price pass-through | episode-specific | no | econometric | **SEPARATE** — two periods; early-2025 result not mergeable with 2018 welfare estimates |
| E020–E021 | 2018 | targeted trade + U.S. economy | import/export response; structural welfare | explicitly models retaliation | model incorporates trade reallocation | general equilibrium | **GROUP B** — internally coherent study, do not splice components with Group A |
| E022 | 2018–19 | tariff schedules | policy coverage / chronology | yes | no | observed policy | **TIMELINE ANCHOR** |
| E023 | 2017–23 | U.S. sourcing across countries | substitution elasticity/share | background episode | yes | empirical trade reallocation | **GROUP C** |
| E024–E025 | pre/post 2018–19 through 2021–24 | Mexico–U.S.–China supply links | decomposition of Mexican export gains | contextual | central | empirical decomposition | **GROUP C with source caveats** |
| E026 | 2018–19 | U.S. exporters exposed through inputs | export-growth effect | policy environment | no | firm/product empirical | **GROUP D** |
| D14 | 2018–19 | border + retail micro prices | pass-through | contextual | no | micro empirical | **GROUP A comparator**, not additive |
| D15 | 2018 | U.S. consumers/firms/economy | structural loss / real income | included | included/modelled | general equilibrium | **GROUP B** |
| D16 | 2018–19 | retaliation-exposed U.S. counties | consumption/employment growth | central | no | local causal | **GROUP E** |
| D17 | 2018–19 | U.S. manufacturing industries | relative employment / prices | explicit channel | no | industry empirical | **GROUP D** |
| D18–D19 | 2018–19 | U.S. firms/products using imported inputs | duty exposure / export growth | contextual | no | firm/product empirical | **GROUP D** |
| D20 | 2018–19 | U.S. agriculture products | retaliation coverage | central | no | observed policy exposure | **GROUP E anchor** |
| D21 | 2018–19 | U.S. local labor markets | employment effects | central | no | geographic causal | **GROUP E** |
| D22 | 2018–19 | U.S. firms linked to China | event returns + later firm outcomes | trade-war announcements | no | firm/event | **SEPARATE / corroborative** |
| D23 | trade-war period | Chinese listed firms | policy uncertainty | U.S. + Chinese tariffs | no | firm empirical | **GROUP F** |
| D24 | general / prior evidence | U.S. household income groups | distribution mechanism | not episode-matched | no | distribution synthesis | **CONTEXT / GAP POINTER** |
| D25–D27 | 2018–19 episode | Chinese exporters/firms | prices, quantities, uncertainty/reallocation | mixed | no | firm/product empirical | **GROUP F with source-specific units** |
| D28–D31 | multi-year post-2018 | third-country sourcing / Mexico | substitution, diversion, restructuring | contextual | central | trade-network empirical | **GROUP C** |
| D32–D33 | derived/gap | system / third-country actors | structural channel | n/a | central | derived / unknown | **NOT NUMERICALLY CALIBRATABLE** |

## Compatible evidence groups

### GROUP A — U.S. border incidence / direct Section 301 response

Can support a conditional historical statement about:

- importer incidence;
- directly affected import response;
- affected-sector price/production response.

Cannot by itself produce national welfare because retaliation, downstream firms,
local labor markets, tariff revenue, and third-country diversion are incomplete.

### GROUP B — internally coherent 2018 structural welfare model

E020/E021/D15 belong to one modeling framework and can be reproduced as a
**study-specific conditional result**.

Do not replace its internal components with preferred estimates from USITC,
Fed, or another paper without re-estimating the model.

### GROUP C — sourcing substitution / third-country diversion

Can support conditional analysis of:

- substitution lag;
- Mexico/other supplier diversion;
- direct transshipment versus broader production-link channels.

Cannot be added to GROUP B welfare dollars without a common counterfactual and
value-added accounting.

### GROUP D — U.S. downstream / exporter feedback

Can support existence and heterogeneous magnitude of the feedback path:

```
import tariff -> input cost -> downstream/export effect
```

Firm/product estimates are not directly additive to county employment effects.

### GROUP E — retaliation and local labor-market incidence

Can support:

```
foreign retaliation -> geographically concentrated U.S. employment/consumption effects
```

Local percentage-point effects cannot be added to national welfare dollars.

### GROUP F — Chinese firm/exporter adjustment

Can support China-side heterogeneity and adjustment channels. Current evidence
does not yet provide a compatible Chinese household/labor/general-welfare block.

## First admissible reality-grounded calculation

The audit identifies only one low-risk first calculation:

> **Reproduce a single study's internally coherent historical comparison, while
> keeping its own assumptions, units, counterfactual, and uncertainty intact.**

GROUP B is the clearest candidate because its tariff, retaliation, revenue, and
welfare accounting were estimated inside one framework.

However, even a successful reproduction must be labeled:

`HISTORICAL_STUDY_REPRODUCTION`

and must **not** be mapped directly to S0/S1/S2/S3 or to a 2026 policy choice.

## Prohibited arithmetic examples

Until a new harmonized model is built, do not calculate:

- USITC production gain + NBER welfare loss;
- Fed Mexico diversion share + NBER U.S. welfare dollars;
- county employment percentage points + national tariff revenue;
- Chinese firm uncertainty + U.S. consumer price effects;
- 2025/26 trade totals + 2018 causal elasticities as though periods were identical.

## Audit conclusion

**COMPATIBILITY_AUDIT = PASS**

The evidence base contains multiple useful causal channels but no single
cross-study dataset that presently supports a comprehensive empirical
competition/cooperation frontier.

**FIRST_ADMISSIBLE_EMPIRICAL_STEP:** reproduce one internally coherent historical
study result (GROUP B) and compare the reproduction with the published result,
without policy extrapolation.

**CURRENT FRONTIER STATUS:** NOT CALIBRATED.
