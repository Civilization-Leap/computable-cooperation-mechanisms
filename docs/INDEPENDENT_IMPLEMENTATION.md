# Independent Implementation Challenge

Task: [Issue #8](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/8). Reimplement the public `v0.1.0` behavior in a language you know. Keep the implementation in your own repository if that is simpler.

## Time and scope

Planning estimate for one developer familiar with the target language, JSON libraries, and basic tests:

| Work | Focused hours |
|---|---:|
| Read the four cases and current validation/evaluation behavior | 1–2 |
| Implement declared-input validation and evaluation | 4–8 |
| Compare the four outputs and document differences | 2–4 |
| Add a reproducible command and short usage note | 1–2 |
| Minimal semantic implementation total | **8–16** |

Budget **16–32 hours total** for a fuller attempt that also ports the malformed-input tests and documents parser, numeric, and serialization behavior. These are estimates, not measured contributor times. Learning a new language, building a UI, implementing an optimizer, package publication, or exact cross-language hash compatibility adds work and is outside the minimal target. Report actual time if you are comfortable doing so; that will improve the estimate.

The current package is 102 compact Python source lines. This is evidence of a small surface, not a measure of difficulty: validation and cross-language edge cases account for much of the work.

## Freeze the comparison target

- Release: `v0.1.0`.
- Commit: `0960d01d73c73a6ad66644341e70a8cf8b10dd15`.
- [Evaluator and validator](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/blob/v0.1.0/mechanism_ref/core.py).
- [Current tests](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/blob/v0.1.0/tests/test_core.py).
- [Inputs](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/tree/v0.1.0/examples).

The JSON schema file alone is not a full executable specification; read the validator and tests as well. Distinguish observed behavior from the intended modeling principles. If you find a bug or ambiguous input, report it rather than silently treating it as either a new requirement or a corrected upstream rule.

## What to compare

1. Parse JSON without silently accepting duplicate keys or non-finite values. State explicitly if your runtime/parser cannot reject an input the Python version rejects.
2. Validate declared units, actor/resource/outcome references, duplicate outcomes and constraint IDs, and supported fields according to the fixed source.
3. Compute `candidate - baseline` only where actor, dimension, and unit all match. Preserve unknown deltas as `null`; an absent matching outcome is not an invented zero.
4. Evaluate the current resource/outcome threshold checks against the **candidate**. `null` means `UNKNOWN`; invalid references are input errors. The current code does not independently evaluate baseline constraints.
5. For hard checks, overall precedence is `VIOLATED`, then `UNKNOWN`, then `SATISFIED`. A soft check does not change that hard-check aggregate. The current empty-hard-check aggregate is `SATISFIED`; this must not be interpreted as evidence that protections were supplied.
6. Repeat the evaluation and show deterministic semantic results and unchanged input.

Compare status, each check's ID/hard flag/status, and each outcome's actor/dimension/unit/baseline/candidate/delta. Keep check order and sorted outcome keys reproducible. Do not require identical whitespace, prose in `reason`, or the downstream software version string.

## Expected public cases

| Input suffix | Overall | `R-CAP` | `THIRD-PARTY` | A/B cost delta, each (CU) | C loss delta (TU) |
|---|---|---|---|---:|---:|
| `ok` | SATISFIED | SATISFIED | SATISFIED | -3 | +0.5 |
| `third_party_violation` | VIOLATED | SATISFIED | VIOLATED | -3 | +2 |
| `unknown` | UNKNOWN | UNKNOWN | SATISFIED | -3 | +0.5 |
| `capacity_violation` | VIOLATED | VIOLATED | SATISFIED | -4 | +0.5 |

All filenames have prefix `shared_equipment_` and suffix `.json`. Passing these four cases alone is **four-case agreement**, not complete input-language conformance.

## Hash compatibility is a separate result

The Python source hashes parsed input reserialized with `json.dumps(..., ensure_ascii=False, sort_keys=True, separators=(",",":"), allow_nan=False)`, then UTF-8 encoded and SHA-256 hashed. It does not hash the original file bytes, and it does not claim a language-neutral canonical-JSON standard. Numeric formatting, including integer/float distinctions, can differ between runtimes.

Report semantic agreement and hash agreement separately. If you cannot reproduce the Python serialization, document your own hash scheme under a distinct field or clearly mark hash compatibility unsupported. Do not silently describe a different digest as the upstream `input_sha256`.

## Return one small comparison

Link your repository in Issue #8 with language/runtime, exact upstream commit, one run command, the four-case comparison, malformed-input coverage, semantic differences, hash status, and optionally your actual time. Independent work does not need to merge upstream. A precise incompatibility or counterexample is useful even when the port remains incomplete.
