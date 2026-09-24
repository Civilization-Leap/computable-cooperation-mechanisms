# REAL GC 01 — Input provenance and sensitivity gate V0.1

This protocol applies before empirical calibration or any frontier-transition study.

## Two independent labels

Every material value must carry both:

1. **Evidence state** — what epistemic status the value has:
   `OBSERVED`, `OFFICIAL_CLAIM`, `THIRD_PARTY_ESTIMATE`,
   `CONDITIONAL_ASSUMPTION`, or `UNKNOWN`.
2. **Source provenance** — who supplied or constructed the value:
   `OFFICIAL_SOURCE`, `THIRD_PARTY_SOURCE`, or `PROJECT_ASSUMPTION`.

An official source does not automatically make a claim an observed outcome.

## Project-assumption sensitivity gate

If a `PROJECT_ASSUMPTION` can materially change:

- Pareto-frontier membership;
- a named channel-boundary state; or
- a frontier-membership transition,

the study must provide at least one reasoned alternative assumption before
reporting the affected frontier as robust.

Outputs:

- **ROBUST** — the relevant frontier/boundary structure survives the declared alternatives.
- **SENSITIVE** — at least one declared alternative changes that structure.
- **UNDECIDABLE** — evidence or alternative range is insufficient to establish either.

If the required alternative is absent, the affected result is
**UNDECIDABLE / SENSITIVITY_NOT_TESTED**. It must not be promoted to a robust
frontier result.

The alternative need not be the arithmetic negative of the project estimate.
It must be a plausible counter-assumption with an explicit reason.

## Interpretation boundary

Sensitivity analysis reports dependence on declared inputs. It does not choose
which input is politically correct and does not produce a policy recommendation.
