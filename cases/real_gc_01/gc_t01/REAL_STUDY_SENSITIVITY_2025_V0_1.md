# GC-T01 — 2025 Tariff Study Sensitivity Case V0.1

**Target:** Fajgelbaum & Khandelwal, *Tariffs in 2025: Short-Run Impacts on the US Economy*  
**Verified source:** March 26–27, 2026 BPEA conference draft [S1 below]  
**Original registry reference:** NBER Working Paper 35064; not independently refetched in this check  
**Identity:** REAL_STUDY_SENSITIVITY_MAPPING  
**As-of:** 2026-09-25  
**Purpose:** distinguish the study's reported empirical estimates from its assumption-dependent model results.

**Source-verification amendment:** the NBER page/PDF returned 403 during this check. The readable BPEA draft is fixed explicitly; this note does not assume byte identity with the later NBER version. The earlier unqualified “tariff revenue around 1.2% of GDP” and foreign-export-price-only explanation are corrected below.

## Verified study content

The BPEA draft reports:

- baseline importer-price pass-through of about 90%;
- short-run model welfare changes of **-0.13% / +0.10% GDP** without/with terms-of-trade adjustments, with labor fixed across sectors (Table 6);
- a separate labor-mobility alternative of **-0.50% / +0.28% GDP** (Table A.8);
- tariff-revenue counterfactual components of **1.08% / 1.15% GDP** in Table 6, not actual calendar-year tariff receipts.

The last three bullets are author-model results, not CCM measurements. The two labor settings stay separate. The paired endpoints are scenario outputs, **not a confidence interval**, a probability distribution or a guarantee that realized welfare lies between them. The policy universe is the overall 2025 U.S. tariff episode modeled in the paper, not only bilateral U.S.–China measures.

## Sensitivity structure

Within each specified model setting, alternative treatment of terms-of-trade adjustment produces reported changes on different sides of zero:

```
fixed labor + terms-of-trade setting A -> -0.13% GDP
fixed labor + terms-of-trade setting B -> +0.10% GDP
```

Therefore the existing classification label is scoped as:

`headline_sign_status = SENSITIVE`

`scope = VERIFIED_BPEA_FIXED_LABOR_SCENARIOS`

This is a statement about the reported model outputs. It is not a verdict on a political choice or a new empirical frontier.

## Assumptions behind the difference

The study distinguishes foreign import-supply price responses from U.S. producer/export price and income adjustments. High importer pass-through alone does not identify the entire terms-of-trade contribution. In particular, the discussion of export-side effects and overall price/income adjustment matters to the difference between the two settings [S1, sections 5.2.2–5.3, printed pp. 26–31].

A useful inventory is:

```
tariff changes
 -> importer prices and quantities
 -> foreign supply and U.S. producer/export price responses
 -> income, revenue and modeled retaliation
 -> assumption-dependent model outcomes
```

This is not an additive formula. **Table 6 expressly says its four components are non-additive.** Sharing a paper, table and unit is not enough to justify adding reported components.

## CCM sensitivity disposition

| Question | Disposition |
|---|---|
| Does the fixed-labor comparison retain one sign across its two settings? | No; the author-reported outputs are on different sides of zero |
| Are these endpoints statistical confidence bounds? | No; they are model-scenario outputs |
| Does the full paper contain only this labor setting? | No; Table A.8 reports a separate labor-mobility exercise |
| What does the current CCM fixture check? | The signs of supplied endpoints only |
| Has CCM rerun the structural model or identified the realized terms-of-trade response? | No |
| Does this identify a bilateral or joint-interest S0–S3 result? | No |

## Why this matters

A source-faithful dependency statement retains both the measured/estimated inputs and the assumptions needed to obtain each model result. It does not select a convenient endpoint or make a policy recommendation.

## Non-transfer rules

Do not:

- transfer the 2025 model results to 2018;
- combine Table 6 and Table A.8 into a statistical confidence interval;
- present model tariff-revenue components as actual annual receipts;
- add Table 6 components, which are explicitly non-additive;
- mix vintages or splice these values into the 2018 welfare-dollar accounting;
- infer household, worker, China-side or third-country distribution from a U.S. aggregate;
- infer channel availability or irreversibility from a positive or negative aggregate number;
- convert source results into a policy ranking or recommendation.

## Reproduction state

`published_range_recorded = true`

`sign_sensitivity_identified = true`

`verified_vintage = BPEA_2026_MARCH_CONFERENCE_DRAFT`

`nber_current_vintage_reverified = false`

`full_structural_replication = false`

`independent_validation = false`

`policy_recommendation = false`

The existing `real_study_sensitivity.py` fixture retains the two fixed-labor endpoints (-0.13 / +0.10 percent GDP). This amendment verifies their limited source scope; it neither changes the code nor promotes endpoint classification to structural replication or a validated multi-party frontier.

## Primary source and companion matrix

[S1] Fajgelbaum and Khandelwal, BPEA conference draft, March 26–27, 2026: abstract, sections 5.2.2–5.3, Table 6 (printed p. 32), Table A.8 (printed p. 64).  
https://www.brookings.edu/wp-content/uploads/2026/03/1_Fajgelbaum-Khandelwal_unembargoed.pdf

[Known, Unknown and Conditional Findings Matrix V0.1](KNOWN_UNKNOWN_CONDITIONAL_MATRIX_V0_1.md) gives the Chinese-language synthesis and correction record. The prior contents remain traceable in Git history.
