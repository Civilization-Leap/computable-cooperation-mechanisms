# Run the BYOP Acquisition Teaching Cases

These three fixtures make the end-to-end acquisition example executable with the current evaluator. All values and thresholds are synthetic and invented for mechanism demonstration.

## Cases

- `examples/byop_acquisition_full.json`
- `examples/byop_acquisition_long_term_contract.json`
- `examples/byop_acquisition_minority_investment.json`

They share the same baseline and declared hard boundaries so that the reports can be compared without pretending to produce a universal ranking.

## Run

From the repository root:

```bash
python -m mechanism_ref examples/byop_acquisition_full.json --out-dir outputs/byop-full
python -m mechanism_ref examples/byop_acquisition_long_term_contract.json --out-dir outputs/byop-contract
python -m mechanism_ref examples/byop_acquisition_minority_investment.json --out-dir outputs/byop-minority
```

## Expected declared-constraint statuses

| Candidate | Expected status | Why |
|---|---|---|
| Full acquisition | `VIOLATED` | synthetic employee displacement is 120 PERSON against a declared limit of 50 |
| Long-term supply agreement | `SATISFIED` | both declared hard boundaries are within their synthetic limits |
| Minority investment + joint capacity | `UNKNOWN` | employee displacement is deliberately left unknown |

The expected statuses are verified by `tests/test_byop_acquisition.py`.

## What this demonstrates

The manufacturer may show ordinary gains in more than one candidate. That does not erase a declared hard violation, and an unresolved material value remains `UNKNOWN` rather than being filled with a favorable assumption.

The three reports still do **not** establish which arrangement should be chosen. They omit or simplify power asymmetry, antitrust, valuation, strategic deception, confidential facts, multi-period dynamics, and the legitimacy/provenance of the thresholds themselves.

Use the [end-to-end narrative](BYOP_END_TO_END_ACQUISITION.md) to interpret these fixtures and the [feedback protocol](BYOP_FEEDBACK_PROTOCOL.md) to turn the exposed gaps into extension proposals rather than silently expanding the core.
