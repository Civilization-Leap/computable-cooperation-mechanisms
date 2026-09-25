# GC-T01 — 2025 Tariff Study Sensitivity Case V0.1

**Target:** Fajgelbaum & Khandelwal, NBER Working Paper 35064 (2026), study of the 2025 U.S. tariffs  
**Identity:** REAL_STUDY_SENSITIVITY_MAPPING  
**As-of:** 2026-09-25  
**Purpose:** identify which study assumptions/empirical uncertainties change the sign of the reported welfare result.

## Published headline evidence

The study reports, at headline level:

- roughly 90% tariff pass-through into prices paid by U.S. importers;
- tariff revenue around 1.2% of GDP;
- aggregate welfare effects ranging from about **-0.13% to +0.10% of GDP** across scenarios;
- the sign of the aggregate result depends importantly on whether the United
  States obtains a terms-of-trade improvement.

These are the study authors' estimates/model results. They are not CCM
measurements and are not automatically transferable to another tariff episode.

## Sensitivity structure

The headline range itself is evidence that a single-sign result is not robust
to the study's plausible scenario structure:

```
scenario / empirical assumption set A
    -> welfare effect < 0

scenario / empirical assumption set B
    -> welfare effect > 0
```

Therefore CCM records:

`headline_sign_status = SENSITIVE`

not:

`policy_effect = POSITIVE`

and not:

`policy_effect = NEGATIVE`

## Sign-switch driver

The key reported driver is the U.S. **terms-of-trade effect**: whether foreign
export prices fall sufficiently relative to U.S. prices so that part of the
tariff burden is shifted abroad.

The study's high import-price pass-through finding constrains this mechanism:
large pass-through to U.S. importers means a positive aggregate result cannot be
assumed merely from the tariff rate itself.

For CCM purposes the causal structure is:

```
tariff
 -> importer price incidence
 -> tariff revenue / domestic reallocation
 -> foreign-price / terms-of-trade response
 -> retaliation and general-equilibrium responses
 -> aggregate welfare range
```

The final sign is therefore downstream of empirical quantities that are not
known with certainty.

## CCM sensitivity disposition

| Question | Disposition |
|---|---|
| Does the study report one invariant welfare sign? | NO |
| Do plausible study scenarios cross zero? | YES |
| Can CCM label the headline result ROBUST positive or ROBUST negative? | NO |
| Appropriate CCM label | **SENSITIVE** |
| Does SENSITIVE mean the policy has no effects? | NO |
| Does this study establish S0/S1/S2/S3 ordering? | NO |

## Why this matters

This is the first reality-grounded example in REAL GC 01 where the correct
computational result is not a policy winner but a dependency statement:

> the sign of the modeled aggregate welfare effect changes with the empirical
> treatment of a material causal channel.

That is precisely the class of case the CCM sensitivity gate is intended to
preserve rather than collapse.

## Non-transfer rules

Do not:

- apply the -0.13%/+0.10% range to 2018;
- combine it arithmetically with the 2018 Fajgelbaum et al. welfare dollars;
- treat tariff revenue as a free social gain;
- infer household, worker, sector, China-side, or third-country distribution
  from the aggregate welfare range;
- infer that a positive aggregate scenario satisfies channel-based
  irreversibility constraints;
- convert the study into a recommendation for or against tariffs.

## Reproduction state

`published_range_recorded = true`

`sign_sensitivity_identified = true`

`full_structural_replication = false`

`independent_validation = false`

`policy_recommendation = false`

## Next testable task

Construct a minimal **study-faithful sensitivity fixture** with no invented
policy conclusion:

- endpoint A = -0.13% GDP;
- endpoint B = +0.10% GDP;
- provenance = THIRD_PARTY_SOURCE;
- evidence state = THIRD_PARTY_ESTIMATE;
- sensitivity result = SENSITIVE because the declared plausible range crosses
  zero.

The fixture must test classification only. It must not claim to reproduce the
paper's structural model.
