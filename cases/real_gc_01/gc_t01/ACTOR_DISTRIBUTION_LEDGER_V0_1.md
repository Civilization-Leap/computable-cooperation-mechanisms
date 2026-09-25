# GC-T01 — Actor Distribution Ledger V0.1

**Case:** REAL GC 01  
**Module:** GC-T01  
**Scope:** historical U.S.–China tariff episode and identified spillover channels  
**As-of:** 2026-09-25  
**Status:** distribution mapping; not current-policy calibration.

## Purpose

This ledger prevents a national aggregate from hiding who receives gains, who
bears burdens, and which effects return to the initiating actor through
retaliation, downstream costs, or third-country restructuring.

A row is an evidence-backed channel, not a net-welfare score.

## Actor/channel map

| ID | Actor / affected class | Direction | Observed / estimated channel | Evidence basis | Evidence state | What remains unknown |
|---|---|---|---|---|---|---|
| D01 | U.S. importers | burden | Near-full tariff incidence on directly affected imports in USITC retrospective estimate | T01-E016 | THIRD_PARTY_ESTIMATE | firm heterogeneity, margins, contract incidence |
| D02 | U.S. buyers / consumers of affected goods | burden | Tariff pass-through raised affected import/consumer-goods prices; 2025 early Fed estimate also detected partial core-goods price effect | T01-E016/E019 | THIRD_PARTY_ESTIMATE | final 2025/26 pass-through, substitution, household distribution |
| D03 | U.S. producers in protected sectors | benefit | USITC estimated positive production-value response in affected Section 301 sectors | T01-E017 | THIRD_PARTY_ESTIMATE | sector dispersion, productivity, durability, upstream/downstream offsets |
| D04 | U.S. firms using tariffed inputs | burden / feedback | Import tariffs raise input costs; Fed evidence identifies supply-chain exposure as a contributor to export-growth slowdown | T01-E016/E026 | THIRD_PARTY_ESTIMATE | current magnitude by industry and firm |
| D05 | U.S. exporters targeted by retaliation | burden / feedback | Chinese retaliatory tariffs targeted U.S. exports; historical study finds targeted U.S. exports fell | T01-E020/E022 | OBSERVED + THIRD_PARTY_ESTIMATE | product-level incidence, firm survival, substitution |
| D06 | U.S. government | benefit (revenue channel) | Tariffs create customs revenue; NBER welfare accounting explicitly nets tariff revenue against private losses | T01-E021 | THIRD_PARTY_ESTIMATE | distribution/use of revenue; no assumption that revenue equals social benefit |
| D07 | Chinese exporters / producers serving U.S. market | burden / adjustment | Covered U.S. imports from China fell materially after tariffs | T01-E017/E018/E020 | THIRD_PARTY_ESTIMATE | exporter margins, firm exits, domestic reallocation |
| D08 | Chinese importers / buyers of targeted U.S. goods | burden / substitution | China imposed retaliatory tariffs on U.S. goods, changing relative import prices and sourcing incentives | T01-E022 | OBSERVED policy action; incidence UNKNOWN | Chinese-side pass-through and distribution require separate evidence |
| D09 | Mexican exporters / producers | benefit / diversion | Fed decomposition attributes a substantial share of later Mexican U.S.-export gains to trade diversion | T01-E024 | THIRD_PARTY_ESTIMATE | sector/firm distribution and persistence |
| D10 | Chinese-linked production / inputs in Mexico | mixed / restructuring | Fed estimates a broader China-via-Mexico production/input channel while finding direct transshipment small | T01-E025 | THIRD_PARTY_ESTIMATE | ownership, value-added origin, firm-level network |
| D11 | Other third-country suppliers | potential benefit / diversion | U.S. sourcing substitution away from China increased only with lag, implying alternative suppliers gained share over time | T01-E023 | THIRD_PARTY_ESTIMATE | country-specific gains/losses not yet ingested |
| D12 | Workers | mixed / unresolved | Producer expansion, export retaliation, downstream input costs, and geographic reallocation imply opposing labor channels | derived channel map only | UNKNOWN | wages, employment, geography, occupation, adjustment duration |
| D13 | Global/system interest | mixed / unresolved | Trade diversion and supply-chain reorganization change concentration and dependency rather than simply eliminating interdependence | T01-E023–E025 | THIRD_PARTY_ESTIMATE | resilience, concentration, duplicated capacity, systemic option value |

## Non-netting rule

The ledger deliberately does not compute:

```
U.S. producer gain
- U.S. consumer/importer loss
+ tariff revenue
- exporter retaliation loss
= national answer
```

Those terms differ in actor, distribution, time, evidence design, and sometimes
unit. A later model may compare compatible measures, but it may not erase a
materially worse component merely because another component is larger.

## Feedback map

Historical evidence now supports the existence—not a unified magnitude—of these
feedback paths:

```
US tariff
  -> US importer/input cost
  -> downstream US price/cost effects

US tariff
  -> lower China-origin imports
  -> Chinese exporter adjustment
  -> sourcing shifts to third countries
  -> changed US dependency structure

US tariff
  -> Chinese retaliation
  -> burden on targeted US exporters
  -> consequence returns to initiating side
```

The last chain is a direct REAL GC 01 example of `F_i(t)`: an initiating
action can generate a response whose consequences return to the initiator.

## Distributional unknowns that block calibration

GC-T01 must not yet assign a national net-benefit vector because the following
are unresolved or not made commensurable:

- household income distribution of price effects;
- producer gains versus downstream producer losses by sector;
- exporter losses attributable specifically to retaliation;
- employment/wage adjustment by geography and occupation;
- Chinese-side tariff incidence and producer/consumer distribution;
- third-country worker/consumer effects;
- long-run resilience and concentration effects;
- transition and rebuilding costs;
- option-value changes and channel closure/recovery.

## Current status

**DISTRIBUTION_CHANNELS_MAPPED / MATERIAL_INCIDENCE_UNRESOLVED / NOT_CALIBRATED**

The next admissible step is to ingest distribution evidence for firms, workers,
consumers, and retaliation-exposed sectors, preserving conflicting estimates
rather than forcing a national aggregate.


## Third intake — distribution magnitudes and heterogeneity

These records refine who was affected in the historical 2018–2019 episode. They
remain historical estimates, not direct measurements of 2026 policy effects.

| ID | Actor/class | Finding | Evidence state | Provenance | Source | Boundary |
|---|---|---|---|---|---|---|
| D14 | U.S. importers and consumers | Tariffs were almost fully passed through to total prices paid by importers; retail-price pass-through was more mixed, consistent with some retailer-margin absorption | THIRD_PARTY_ESTIMATE | THIRD_PARTY_SOURCE | Cavallo et al., NBER WP 26396 | Separates border incidence from store-level incidence |
| D15 | U.S. consumers and importing firms | Fajgelbaum et al. estimate USD 51bn loss to U.S. consumers/firms buying imports and USD 7.2bn aggregate real-income loss after tariff revenue and domestic-producer gains | THIRD_PARTY_ESTIMATE | THIRD_PARTY_SOURCE | NBER WP 25638 | Structural/general-equilibrium estimate, not observed cash loss |
| D16 | U.S. counties highly exposed to Chinese retaliation | Upper-quartile exposed counties experienced about a 3.8 percentage-point decline in consumption growth; high-exposure counties also had about a 1 pp relative decline in overall employment and ~1.5 pp in goods-producing employment | THIRD_PARTY_ESTIMATE | THIRD_PARTY_SOURCE | Waugh, NBER WP 26353 / NBER Digest | Local difference-in-differences estimate; concentrated exposure, not national average |
| D17 | U.S. manufacturing industries | Greater tariff exposure was associated with relative employment reductions because import-protection gains were offset by larger input-cost and retaliatory-tariff effects; producer prices rose with input costs | THIRD_PARTY_ESTIMATE | OFFICIAL_SOURCE | Federal Reserve FEDS 2019-086 | Industry-relative estimate; does not imply every protected industry lost employment |
| D18 | U.S. firms exposed through imported inputs | Firms later exposed to tariffs represented 84% of U.S. exports and 65% of manufacturing employment in linked data; average affected firm implied new-duty cost about USD 900 per worker | THIRD_PARTY_ESTIMATE | THIRD_PARTY_SOURCE | Handley, Kamal & Monarch, NBER WP 26611 | Firm-linked historical exposure; not a worker wage loss measure |
| D19 | U.S. exporters using tariffed inputs | Most-exposed products had lower export growth; 2019Q3 estimated effect equivalent to about a 2% ad-valorem export tariff for a typical product, up to 4% for above-average exposure | THIRD_PARTY_ESTIMATE | THIRD_PARTY_SOURCE | NBER WP 26611 | Supply-chain feedback estimate |
| D20 | U.S. agriculture | Retaliatory tariffs covered U.S. agricultural/food products valued at USD 30.4bn in 2017, with tariff increases ranging from 2% to 140% | OBSERVED policy coverage | OFFICIAL_SOURCE | USDA ERS ERR-304 | Exposure base, not itself realized export loss |
| D21 | U.S. local labor markets / agriculture | Detailed geographic study finds import tariffs did not measurably raise or lower employment in newly protected sectors to date, while retaliatory tariffs had clear negative employment effects, primarily in agriculture; compensation only partly mitigated harms | THIRD_PARTY_ESTIMATE | THIRD_PARTY_SOURCE | Autor et al., NBER WP 32082 | Historical causal estimate; compensation and political effects are separate dimensions |
| D22 | U.S. firms linked to China | Firms importing from, exporting to, or selling in China had worse stock returns around tariff announcements; those differences forecast later declines in profits, sales, employment, and investment | THIRD_PARTY_ESTIMATE | THIRD_PARTY_SOURCE | Amiti et al., NBER WP 28758, rev. 2026 | Financial-event/firm heterogeneity evidence; welfare estimate remains model-dependent |
| D23 | Chinese listed firms | U.S. tariff exposure and Chinese retaliatory-tariff exposure increased measured trade-policy uncertainty, with stronger effects for smaller and less capital-intensive firms | THIRD_PARTY_ESTIMATE | THIRD_PARTY_SOURCE | Benguria et al., NBER WP 27920 | Firm uncertainty effect; not a complete Chinese welfare measure |
| D24 | U.S. consumers by income | Prior Fed synthesis notes evidence that existing import-tariff burdens tend to fall more heavily on lower-income households and that trade-related price changes can have group-specific real-income effects | THIRD_PARTY_ESTIMATE | OFFICIAL_SOURCE | Federal Reserve IFDP Note 2018-04-03 | General distribution mechanism; not specific magnitude for 2018 China tariffs |

## Distributional implications for CCM representation

The evidence rejects three simplifying representations:

1. **One U.S. payoff.** Importers, protected producers, downstream manufacturers,
   exporters, agricultural regions, consumers, and government revenue can move
   in different directions.
2. **One time effect.** Border incidence can appear quickly while supply-chain
   substitution, employment, investment, and geographic adjustment evolve over
   longer horizons.
3. **Protection = employment gain.** Historical manufacturing evidence identifies
   simultaneous protection, input-cost, and retaliation channels; the net
   employment association can differ from the direct protected-sector channel.

The model therefore must preserve at least:

```
actor/class × dimension × horizon × provenance × evidence_state
```

before asking whether one configuration dominates another.

## Conflicting / complementary evidence rule

D14–D24 are not treated as a vote count. Different papers identify different
populations and mechanisms. In particular:

- complete border pass-through can coexist with mixed retail pass-through;
- protected-sector output gains can coexist with manufacturing employment losses
  in industries exposed to input costs and retaliation;
- national aggregate estimates can coexist with much larger local effects in
  retaliation-exposed counties;
- tariff revenue can coexist with private incidence and does not cancel it by
  definition.

A later calibration must preserve these distinctions rather than choose the
estimate most favorable to a preferred strategy.

## Status after third intake

**DISTRIBUTION_EVIDENCE_INGESTED / HETEROGENEITY_CONFIRMED / CHINA_AND_THIRD_PARTY_DISTRIBUTION_STILL_THIN / NOT_CALIBRATED**

The next evidence priority is the Chinese-side and third-country distribution:
firm adjustment, employment/consumer incidence, sourcing relocation, and which
exit/substitution channels remained open or became costly to restore.
