# GC-T01 — Historical Study Reproduction V0.1

**Target study:** Fajgelbaum, Goldberg, Kennedy & Khandelwal, *The Return to Protectionism*  
**Identity:** HISTORICAL_STUDY_REPRODUCTION  
**As-of:** 2026-09-25  
**Scope:** published headline-accounting reproduction only; not full structural-model replication.

## Version control finding

The public record contains materially different headline numbers across versions:

| Version | Import-purchaser loss | Aggregate real-income/welfare loss | Import response | Export response |
|---|---:|---:|---:|---:|
| March 2019 NBER revision | USD 68.8bn | USD 7.8bn | -31.5% | -11.0% |
| October 2019 / published-version summary | USD 51bn | USD 7.2bn | large decline; NBER page summarizes final revision | study framework revised |

These versions must not be mixed. The CCM evidence ledger previously contained
both number sets from different public versions. This reproduction therefore
records them as separate vintages rather than treating one as an error.

## Reproduction A — March 2019 headline accounting

Public March-2019 abstract reports:

- annual consumer/producer loss from higher import costs: USD 68.8bn;
- aggregate welfare loss after tariff revenue and domestic-producer gains: USD 7.8bn.

Therefore the combined offset embedded in that published headline accounting is:

```
68.8 - 7.8 = 61.0 (USD bn)
```

This exactly matches the NBER Digest description of approximately USD 61bn in
offsetting domestic-producer income/tariff-revenue effects for that early
version.

**Reproduction status:** REPRODUCED_HEADLINE_IDENTITY

This does not independently reproduce the paper's elasticities, input-output
system, regional allocation, or general-equilibrium solution.

## Reproduction B — October 2019 / published-version headline accounting

The revised NBER page reports:

- loss to U.S. consumers/firms buying imports: USD 51bn (0.27% GDP);
- aggregate real-income loss after tariff revenue and domestic-producer gains:
  USD 7.2bn (0.04% GDP).

The implied combined offset is:

```
51.0 - 7.2 = 43.8 (USD bn)
```

**Reproduction status:** REPRODUCED_HEADLINE_IDENTITY

Again, USD 43.8bn is an implied residual from the revised headline figures; it
must not be labeled as a directly observed producer gain or tariff-revenue
measurement.

## Why this is not a full independent replication

A full replication would require the exact study vintage's:

- tariff-line data and timing;
- import/export microdata construction;
- estimated demand/export elasticities;
- input-output linkages;
- regional exposure construction;
- model code and calibration;
- counterfactual solution.

The public headline arithmetic alone cannot recreate those objects.

Accordingly:

`independent_structural_replication = false`

`headline_accounting_reproduced = true`

`external_evidence_state_changed = false`

## CCM implication

The exercise demonstrates a central compatibility rule:

> a result can be internally coherent inside one study while still being
> unsuitable for arithmetic combination with estimates from another study or
> another vintage of the same study.

It also exposes a versioning hazard: using USD 68.8bn from the March version
together with USD 7.2bn from the October/published version would manufacture a
USD 61.6bn residual that belongs to neither reported accounting.

## Current admissible conclusion

The historical study's headline accounting can be arithmetically reproduced at
the version level. The underlying causal/general-equilibrium model has **not**
been independently reproduced here.

No result in this file establishes a 2026 U.S.–China policy frontier, an S0–S3
ordering, or a recommendation.
