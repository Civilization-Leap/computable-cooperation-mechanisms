# GC-T01 — Terms-of-Trade Evidence Node V0.1

**Case:** REAL GC 01  
**Module:** GC-T01  
**Question:** Did the 2025 U.S. tariff episode generate a sufficiently large U.S. terms-of-trade improvement to stabilize the sign of aggregate welfare estimates?  
**As-of:** 2026-09-25  
**Status:** evidence-node assessment; no policy recommendation.

## Why this node matters

The 2026 Fajgelbaum–Khandelwal study reports a welfare range crossing zero.
A central sign-switch mechanism is whether foreign exporters reduce pre-tariff
prices enough to improve U.S. terms of trade.

The relevant decomposition is not:

```
tariff rate -> welfare
```

but:

```
tariff
 -> foreign pre-tariff export-price response
 -> exchange-rate response
 -> U.S. importer landed-price response
 -> quantities / substitution
 -> tariff revenue and retaliation
 -> terms-of-trade contribution
 -> aggregate welfare
```

## Evidence records

| ID | Evidence | Period/scope | State | Provenance | Interpretation |
|---|---|---|---|---|---|
| TOT-E01 | Fajgelbaum–Khandelwal report about 90% tariff pass-through into prices paid by U.S. importers | 2025 tariff episode | THIRD_PARTY_ESTIMATE | THIRD_PARTY_SOURCE | High importer pass-through limits how much burden can simply be presumed shifted abroad |
| TOT-E02 | Same study reports aggregate welfare range about -0.13% to +0.10% GDP across scenarios | 2025 | THIRD_PARTY_ESTIMATE | THIRD_PARTY_SOURCE | Welfare sign is not invariant |
| TOT-E03 | Study identifies terms-of-trade response as a material determinant of whether aggregate effect is negative or positive | 2025 | THIRD_PARTY_ESTIMATE | THIRD_PARTY_SOURCE | Sign-switch node |
| TOT-E04 | Earlier 2018–19 micro evidence found tariffs were almost fully passed through to U.S. import prices, with little systematic fall in foreign pre-tariff prices during the studied period | 2018–19 | THIRD_PARTY_ESTIMATE | THIRD_PARTY_SOURCE | Historical comparator only; cannot be substituted for 2025 measurement |
| TOT-E05 | Federal Reserve real-time 2025 consumer-price work detected tariff effects in U.S. core goods by March 2025 | early 2025 | THIRD_PARTY_ESTIMATE | OFFICIAL_SOURCE | Confirms domestic price channel exists; does not by itself identify foreign export-price response |
| TOT-E06 | Exchange-rate movements can alter dollar import prices independently of exporter markups | mechanism | OBSERVED_MECHANISM | MIXED_SOURCES | Requires explicit FX adjustment before attributing a price change to foreign incidence |

## What would establish a terms-of-trade improvement

For a policy-relevant empirical claim, evidence must distinguish:

1. tariff-inclusive landed price paid by U.S. importer;
2. foreign pre-tariff export price;
3. exchange-rate movement;
4. product-quality/composition change;
5. freight/insurance changes;
6. supplier switching.

A fall in a dollar import-price index alone is insufficient if it is caused by
composition or exchange rates rather than foreign exporters accepting lower
pre-tariff prices.

## Current adjudication

The evidence supports:

- substantial incidence remained on U.S. importers;
- the welfare sign in the target study is scenario-sensitive;
- terms of trade are a material sign-switch node.

The evidence assembled here does **not** yet establish one sufficiently precise,
study-compatible realized 2025 terms-of-trade magnitude that would collapse the
published welfare range to one side of zero.

Therefore:

`TERMS_OF_TRADE_REALIZED_MAGNITUDE = UNKNOWN`

`WELFARE_SIGN = SENSITIVE`

`CURRENT_AGGREGATE_DIRECTION = UNDECIDABLE`

This does not mean “no effect.” It means the currently assembled evidence does
not justify converting the study's sign-sensitive range into one directional
aggregate conclusion.

## What is already more certain than the aggregate sign

The following can remain separately reported without waiting for a single net
welfare sign:

- tariff incidence on U.S. importers is substantial;
- domestic price effects occurred;
- tariff revenue occurred;
- sourcing/substitution responses occurred;
- distributional effects differ across firms, sectors, workers, and locations;
- retaliation and supply-chain feedback can return costs to the initiating side.

These component findings must not be erased by the aggregate-sign uncertainty.

## Evidence needed to resolve the node

Priority data:

- product-level foreign pre-tariff unit values / prices around 2025 tariff changes;
- matched tariff-inclusive U.S. landed prices;
- bilateral/product FX controls;
- supplier/product composition controls;
- study-consistent quantity elasticities;
- retaliation treatment;
- confidence intervals or plausible bounds for the resulting terms-of-trade contribution.

## CCM conclusion

**TOT_NODE = OPEN / MATERIAL / SIGN-DETERMINING**

Until this node is resolved with compatible evidence, GC-T01 must not promote
the 2025 study to a robust positive or negative aggregate result, and must not
map it to an S0–S3 policy ordering.
