# GC-T01 — Terms-of-Trade Evidence Node V0.1

**Case:** REAL GC 01  
**Module:** GC-T01  
**Question:** Which import-side and U.S. export/producer-price responses distinguish the target study's alternative terms-of-trade settings?  
**As-of:** 2026-09-25  
**Status:** evidence-node assessment; no policy recommendation.

**Source-verification amendment:** this note now uses the readable March 26–27, 2026 BPEA conference draft of Fajgelbaum and Khandelwal, *Tariffs in 2025: Short-Run Impacts on the US Economy* [S1 below]. The NBER page/PDF returned 403 in this check. Identity with the later NBER vintage is not assumed. Earlier wording that reduced the terms-of-trade mechanism to foreign exporters cutting prices was too narrow.

## Why this node matters

In the verified draft, the short-run model with labor fixed across sectors reports different welfare changes under alternative terms-of-trade assumptions (Table 6). The mechanism includes both foreign import-supply prices and U.S. producer/export prices and income adjustments. It is not fully identified by importer pass-through alone [S1, sections 5.2.2–5.3, printed pp. 26–32].

The relevant decomposition is not:

```
tariff rate -> welfare
```

The channels to distinguish are:

```
tariff changes
 -> importer-price incidence and quantity/substitution responses
 -> foreign pre-tariff supply prices
 -> U.S. producer/export prices and factor-income adjustment
 -> tariff revenue and modeled retaliation
 -> model-dependent terms-of-trade and welfare effects
```

This is a channel inventory, not an additive formula or a claim that the project has estimated the entire chain.

## Evidence records

| ID | Evidence | Period/scope | Evidence state | Source provenance | Interpretation |
|---|---|---|---|---|---|
| TOT-E01 | Baseline importer-price pass-through is estimated at about 90% | 2025 overall U.S. tariff episode in the verified draft | THIRD_PARTY_ESTIMATE | THIRD_PARTY_SOURCE | Does not by itself identify the export-side price or complete terms-of-trade response [S1] |
| TOT-E02 | Table 6 reports -0.13% and +0.10% GDP under alternative terms-of-trade settings | Short run; labor fixed across sectors | THIRD_PARTY_ESTIMATE | THIRD_PARTY_SOURCE | Model scenarios, not a confidence interval or realized outcome [S1, Table 6] |
| TOT-E03 | Import-side and U.S. producer/export-side adjustments enter the terms-of-trade comparison; export-side aggregate effects are difficult to identify | Same study and vintage | THIRD_PARTY_ESTIMATE | THIRD_PARTY_SOURCE | A material assumption-dependent node, not only a foreign-exporter-discount question [S1, sections 5.2.2–5.3] |
| TOT-E04 | USITC reports near-full importer-price pass-through for directly affected imports | 2018–2021 | THIRD_PARTY_ESTIMATE | OFFICIAL_SOURCE | Historical comparator, not a substitute for 2025 measurement [S2] |
| TOT-E05 | Federal Reserve authors estimate early price effects from February–March 2025 China tariffs through March | Early 2025 only | THIRD_PARTY_ESTIMATE | OFFICIAL_SOURCE | Domestic price channel; not independent identification of foreign export prices [S3] |
| TOT-E06 | Separating exchange rates, product composition, quality, freight and supplier changes is necessary for attribution | Project measurement checklist | CONDITIONAL_ASSUMPTION | PROJECT_ASSUMPTION | No numerical effect is assigned; this checklist alone supplies neither a measured terms-of-trade change nor a frontier |

TOT-E04 is now anchored to a directly readable primary source; its revised source and period are explicit. TOT-E06 replaces the earlier nonstandard labels `OBSERVED_MECHANISM / MIXED_SOURCES` with a clearly declared project measurement requirement, not an empirical estimate.

## What would identify the relevant price response

Evidence would need to distinguish:

1. tariff-inclusive prices paid by U.S. importers;
2. foreign pre-tariff supply prices;
3. U.S. producer/export prices and associated income responses;
4. exchange-rate movements;
5. product quality/composition and supplier changes;
6. freight and insurance;
7. the study's counterfactual, quantity responses and time horizon.

A dollar import-price index alone does not identify who absorbed a tariff or the full terms-of-trade contribution. Exchange-rate changes may themselves alter real relative prices; they must be distinguished for causal attribution, not automatically removed from the economic effect. Import and export sides must use compatible units and price definitions [S1, sections 5.2.2–5.3].

## Current assessment

The sources support reporting their own importer-incidence estimates and their model dependence separately. The project has not assembled a compatible estimate of the full realized price response that selects between the study's alternative settings.

Accordingly, within the scope of evidence assembled here:

`TERMS_OF_TRADE_REALIZED_MAGNITUDE = UNKNOWN`

`WELFARE_SIGN = SENSITIVE_WITHIN_VERIFIED_STUDY_SETTINGS`

`CURRENT_AGGREGATE_DIRECTION = UNDECIDABLE`

UNKNOWN describes this project's evidentiary position; it does not assert that the quantity is unknowable or that all researchers lack evidence. The study's labor-mobility alternative is separately reported in Table A.8 (-0.50% / +0.28% GDP), rather than merged with Table 6 into a statistical interval.

## What can be reported separately

Specific studies' estimates of importer incidence, domestic prices, sectoral output, sourcing and distribution can be attributed with their own periods and populations. Aggregate uncertainty does not erase those estimates, and the estimates do not by themselves establish a complete national or joint-interest result.

The numerical components in Table 6 are expressly **non-additive**, even though they are in one table and use the same units. In that table the tariff-revenue components are model-counterfactual quantities (1.08% / 1.15% GDP), not measured calendar-year receipts. Neither those components nor estimates from other studies may be summed without the paper's accounting definitions [S1, Table 6 note].

## Evidence needed to resolve the node

Priority material is a matched, study-consistent account of import and export/producer prices, exchange rates, composition, quantities, retaliation and uncertainty. More aggregate trade totals alone will not identify it.

## CCM conclusion

**TOT_NODE = OPEN / MATERIAL / ASSUMPTION_DEPENDENT**

No empirical S0–S3 ordering follows. No model code, synthetic input or policy recommendation is changed by this source-verification amendment. The existing endpoint classifier is not a structural replication.

## Primary sources and companion matrix

[S1] Fajgelbaum and Khandelwal, BPEA conference draft, March 26–27, 2026, sections 5.2.2–5.3; Tables 6 and A.8.  
https://www.brookings.edu/wp-content/uploads/2026/03/1_Fajgelbaum-Khandelwal_unembargoed.pdf

[S2] USITC, March 15, 2023, *Economic Impact of Section 232 and 301 Tariffs on U.S. Industries*, findings and scope.  
https://www.usitc.gov/press_room/news_release/2023/er0315_63679.htm

[S3] Federal Reserve FEDS Notes authors, May 9, 2025, *Detecting Tariff Effects on Consumer Prices in Real Time*.  
https://www.federalreserve.gov/econres/notes/feds-notes/detecting-tariff-effects-on-consumer-prices-in-real-time-20250509.html

See [Known, Unknown and Conditional Findings Matrix V0.1](KNOWN_UNKNOWN_CONDITIONAL_MATRIX_V0_1.md) for the Chinese-language synthesis and remaining evidence gaps.
