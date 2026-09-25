# GC-T01 — Trade and Supply Chains Evidence Ledger V0.1

**Case:** REAL GC 01  
**Module:** GC-T01  
**As-of:** 2026-09-25  
**Status:** evidence intake only; not model calibration and not a policy conclusion.

## Rules

1. Record source provenance separately from evidence state.
2. An official statistic may be `OBSERVED`; an official statement about expected effects remains `OFFICIAL_CLAIM`.
3. Do not infer welfare, causality, strategy superiority, or a Pareto frontier from trade totals alone.
4. Current-year partial data must remain partial-period data.
5. Differences between official datasets must be preserved and explained before combining them.
6. No project estimate enters a robust frontier without the alternative-assumption sensitivity gate.

## Initial evidence records

| ID | Claim / measurement | Value | Period | Evidence state | Provenance | Source | Use boundary |
|---|---|---:|---|---|---|---|---|
| T01-E001 | U.S.–China goods + services trade | USD 494.6bn | 2025 | OBSERVED | OFFICIAL_SOURCE | USTR, PRC country page | Estimated total reported by USTR; not a welfare measure |
| T01-E002 | U.S. goods exports to China | USD 106.0bn | 2025 | OBSERVED | OFFICIAL_SOURCE | USTR | Rounded USTR figure |
| T01-E003 | U.S. goods imports from China | USD 308.7bn | 2025 | OBSERVED | OFFICIAL_SOURCE | USTR | Rounded USTR figure |
| T01-E004 | U.S. goods trade deficit with China | USD 202.7bn | 2025 | OBSERVED | OFFICIAL_SOURCE | USTR | Accounting balance; not itself a net-loss measure |
| T01-E005 | U.S. services exports to China | USD 57.2bn | 2025 | OBSERVED | OFFICIAL_SOURCE | USTR | Services flow, not distributional incidence |
| T01-E006 | U.S. services imports from China | USD 22.8bn | 2025 | OBSERVED | OFFICIAL_SOURCE | USTR | Services flow |
| T01-E007 | U.S. services trade surplus with China | USD 34.4bn | 2025 | OBSERVED | OFFICIAL_SOURCE | USTR | Accounting balance |
| T01-E008 | U.S. goods exports to China | USD 105.9778bn | 2025 | OBSERVED | OFFICIAL_SOURCE | U.S. Census Foreign Trade | Nominal, not seasonally adjusted |
| T01-E009 | U.S. goods imports from China | USD 308.6519bn | 2025 | OBSERVED | OFFICIAL_SOURCE | U.S. Census Foreign Trade | Nominal, not seasonally adjusted |
| T01-E010 | U.S. goods balance with China | -USD 202.6741bn | 2025 | OBSERVED | OFFICIAL_SOURCE | U.S. Census Foreign Trade | Nominal, not seasonally adjusted |
| T01-E011 | U.S. goods exports to China, Jan–Jul | USD 65.1725bn | 2026 Jan–Jul | OBSERVED | OFFICIAL_SOURCE | U.S. Census Foreign Trade | Partial year only |
| T01-E012 | U.S. goods imports from China, Jan–Jul | USD 156.3902bn | 2026 Jan–Jul | OBSERVED | OFFICIAL_SOURCE | U.S. Census Foreign Trade | Partial year only |
| T01-E013 | U.S. goods balance with China, Jan–Jul | -USD 91.2177bn | 2026 Jan–Jul | OBSERVED | OFFICIAL_SOURCE | U.S. Census Foreign Trade | Partial year only |
| T01-E014 | BEA annual release reports China goods deficit | USD 202.1bn | 2025 | OBSERVED | OFFICIAL_SOURCE | BEA annual trade release | Census-basis annual-release figure; preserve source-method difference from USTR/Census page |
| T01-E015 | BEA annual release reports exports/imports with China | exports USD 106.3bn; imports USD 308.4bn | 2025 | OBSERVED | OFFICIAL_SOURCE | BEA annual trade release | Rounded annual-release values; do not overwrite Census detail |

## Source-method reconciliation note

USTR reports rounded 2025 goods values of exports USD 106.0bn, imports USD 308.7bn, deficit USD 202.7bn. The Census country table reports USD 105.9778bn, USD 308.6519bn, and -USD 202.6741bn. BEA's annual release reports Census-basis values rounded to USD 106.3bn exports, USD 308.4bn imports, and USD 202.1bn deficit.

These differences are small relative to the totals but are **not silently harmonized**. Before any empirical calibration, the model must select a source/method appropriate to the variable and retain the citation and vintage.

## What these records do not establish

They do not establish:

- whether more competition or more cooperation is preferable;
- the causal effect of any tariff, export control, industrial policy, or negotiated arrangement;
- how gains and burdens are distributed within either country;
- effects on third countries, firms, workers, consumers, resilience, security, or option value;
- action–counteraction feedback;
- an MSC level;
- any irreversible channel closure;
- any frontier transition.

Those require separate evidence records.

## Next evidence gaps

Before GC-T01 can calibrate even one conditional comparison, collect independently sourced evidence for:

- tariff/restriction incidence and pass-through;
- supply-chain substitution/diversion and third-country effects;
- sector-level distribution across firms, workers, and consumers;
- resilience / concentration / switching-cost measures;
- action–counteraction timing;
- preserved or lost exit/substitution channels.

Until then, GC-T01 remains **EVIDENCE_INTAKE / NOT_CALIBRATED**.


## Second evidence intake — tariff incidence, pass-through, retaliation, and diversion

The following records concern the 2018–2021 tariff episode unless explicitly stated otherwise. Historical estimates are not treated as direct measurements of 2026 effects.

| ID | Finding | Period / scope | Evidence state | Provenance | Source | Model-use boundary |
|---|---|---|---|---|---|---|
| T01-E016 | U.S. importers bore nearly the full cost of section 232/301 tariffs; import prices rose about 1% for each 1% tariff increase | 2018–2021, directly affected products | THIRD_PARTY_ESTIMATE | OFFICIAL_SOURCE | USITC, Inv. 332-591 | Retrospective econometric estimate; not proof of identical pass-through in 2026 |
| T01-E017 | Section 301 tariffs reduced imports from China across affected sectors by about 13%, raised U.S. production value about 0.4%, and U.S. product prices about 0.2% | 2018–2021 | THIRD_PARTY_ESTIMATE | OFFICIAL_SOURCE | USITC | Sector-average estimate; distribution and general-equilibrium effects remain separate |
| T01-E018 | For covered imports from China, a 1% tariff increase was associated with roughly a 2% decrease in import value and quantity | 2018–2021 | THIRD_PARTY_ESTIMATE | OFFICIAL_SOURCE | USITC full report | Econometric response, not a universal elasticity |
| T01-E019 | U.S. tariffs in 2018–19 passed through fully and quickly to consumer-goods prices in the Fed study; 2025 China tariffs had partially passed through by March, with estimated +0.3% core-goods PCE and +0.1% core PCE | 2018–19 and Feb–Mar 2025 | THIRD_PARTY_ESTIMATE | OFFICIAL_SOURCE | Federal Reserve FEDS Note, 2025-05-09 | 2025 result is early-period evidence, not a final annual effect |
| T01-E020 | Targeted imports fell 31.5% within products and targeted U.S. exports fell 11.0%; study estimated complete pass-through to import prices | 2018 trade-war study | THIRD_PARTY_ESTIMATE | THIRD_PARTY_SOURCE | Fajgelbaum et al., NBER WP 25638 | Working-paper model estimates; do not merge mechanically with USITC sector estimates |
| T01-E021 | Same study estimated annual U.S. consumer/producer losses from higher import costs of USD 68.8bn and aggregate welfare loss of USD 7.8bn after tariff revenue and producer gains | 2018 episode | THIRD_PARTY_ESTIMATE | THIRD_PARTY_SOURCE | Fajgelbaum et al., NBER WP 25638 | Model-dependent welfare estimate; not an observed cash loss and not a current-policy estimate |
| T01-E022 | China retaliated against July/August 2018 Section 301 tranches with 25% tariffs on USD 34bn then USD 16bn of U.S. imports; September tranche covered USD 60bn at 5–10%, later raised to 5–15% | 2018–2019 policy sequence | OBSERVED | OFFICIAL_SOURCE | Federal Reserve FEDS Note timeline | Action–counteraction chronology; does not by itself identify net welfare effect |
| T01-E023 | China's U.S. import share fell from about 22% in 2017 to about 14% by Dec. 2023; substitution elasticity away from China rose meaningfully only after 3–4 years | 2017–2023 | THIRD_PARTY_ESTIMATE | OFFICIAL_SOURCE | Federal Reserve FEDS Note, 2024-04-12 | Long adjustment lag matters for T0/T1 separation |
| T01-E024 | Fed analysis attributes 53% of Mexico's export gains to the U.S. in its decomposition to trade diversion following 2018–19 China tariffs | comparison of 2014–17 with 2021–24 | THIRD_PARTY_ESTIMATE | OFFICIAL_SOURCE | Federal Reserve FEDS Note, 2026-06-05 | Identification has stated caveats; not all diversion is Chinese production |
| T01-E025 | Same analysis estimates direct China-to-Mexico-to-U.S. transshipment at less than 1 percentage point of Mexico's export gains and China's broader Mexico “backdoor” channel at about 14% of total Mexican export gains to the U.S. | 2021–24 vs pre-tariff baseline | THIRD_PARTY_ESTIMATE | OFFICIAL_SOURCE | Federal Reserve FEDS Note, 2026-06-05 | Informative bounds; authors explicitly note ownership/data limitations |
| T01-E026 | Supply-chain exposure to U.S. import tariffs contributed materially to the 2018–19 slowdown in U.S. export growth | 2018–2019 | THIRD_PARTY_ESTIMATE | OFFICIAL_SOURCE | Federal Reserve FEDS Note, 2020-10-16 | Establishes a feedback channel; magnitude requires underlying study before calibration |

### Causal-chain representation now supported by evidence

The ledger can now support a **historical** action–response chain without claiming that the same magnitudes apply today:

```
U.S. tariff action
  -> higher U.S. import prices / importer incidence
  -> reduced covered imports from China
  -> Chinese retaliatory tariffs on U.S. exports
  -> substitution and third-country trade diversion
  -> delayed supply-chain adjustment
  -> downstream / export-side feedback to U.S. actors
```

Every arrow above has at least one cited empirical or policy source, but the chain is not yet a calibrated unified causal model. Estimates come from different designs, scopes, years, and units.

### Evidence conflict / non-combinability rule

T01-E016 through E026 must **not** be added together as if they were components of one welfare equation. USITC sector estimates, Federal Reserve event/econometric studies, and NBER general-equilibrium estimates answer different questions. Any later calibration must identify:

- common period;
- common tariff universe;
- affected product/sector population;
- price level used;
- whether an estimate is partial-equilibrium or general-equilibrium;
- whether retaliation is included;
- whether third-country diversion is included.

Until those dimensions match, the evidence is complementary but not arithmetically composable.

### GC-T01 status after second intake

**EVIDENCE_INTAKE / CAUSAL_CHANNELS_IDENTIFIED / NOT_CALIBRATED**

The evidence is now sufficient to represent several historical causal channels. It is still insufficient to calculate a current U.S.–China competition/cooperation frontier.
