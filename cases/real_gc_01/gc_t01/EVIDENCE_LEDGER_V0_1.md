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
