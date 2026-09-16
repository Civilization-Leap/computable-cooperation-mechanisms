# REAL MA 01 — Corridor Model V1.3

This runnable public case asks a narrow question: with comparable AI capability, what does a hypothetical merger arrangement (B1) add beyond independent open cooperation (A1), and where do its costs and safeguards fall?

It does **not** decide whether the Union Pacific–Norfolk Southern proposal should be approved. It does not certify the applicant's forecasts, infer motives, or turn research thresholds into law.

## What V1.3 changes

V1.3 implements the condition split stated in the public manuscript:

- **Directional report items:** shipper cost delta and transit-time delta. These show a trade-off and never determine the overall boundary status.
- **Five proposed boundaries:** verified labor transition plan, community safety review, non-discriminatory access, human override, and rollback drill. Only these five feed the declared hard-boundary status.

Therefore a voluntarily purchased faster service may have a positive cost delta and a negative time delta without being mislabeled `VIOLATED`. A boundary becomes `VIOLATED` only when evidence is explicitly entered as `0`; missing evidence stays `UNKNOWN`.

The earlier V1.2 companion package described in the manuscript remains a historical research artifact outside this repository. V1.3 is the first REAL MA 01 package committed here; it does not rewrite that history or claim that the old implementation already had this split.

## Run

From the repository root:

```bash
python cases/real_ma_01/v1_3/run.py
python -m unittest -v tests.test_real_ma_01_v13
```

The default input deliberately contains nulls. The expected proposed-boundary status is `UNKNOWN`. The run writes derived files under `outputs/`; it never rewrites `inputs/empirical_inputs.json`.

## What is calculated

- A1/B1 cost and time deltas, only when both values are supplied;
- five separately visible boundary checks;
- a 36-row hypothesis grid for inventory carrying cost, including the transparent example `100,000 × 20% × 25 / 8,760 ≈ 57.08 USD`.

The 36 rows are conditional arithmetic, not measured merger effects. The public default contains no real order data and all five boundary-evidence fields are unknown.

## Bring evidence or a counterexample

Copy `inputs/empirical_inputs.json`; do not edit generated output as if it were source data. Record the corridor/order scope, unit, date, source, access conditions, and who has authority to accept each boundary. Then run with:

```bash
python cases/real_ma_01/v1_3/run.py --input /path/to/traceable-copy.json --output-dir /tmp/real-ma-01
```

See [`docs/REAL_MA_01_REPRODUCTION_CHALLENGE.md`](../../../docs/REAL_MA_01_REPRODUCTION_CHALLENGE.md). Failed fits and evidence that A1/B1 cannot be compared as modeled are valid results.
