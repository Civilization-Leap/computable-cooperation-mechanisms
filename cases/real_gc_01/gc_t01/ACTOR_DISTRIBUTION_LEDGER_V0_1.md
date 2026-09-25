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
