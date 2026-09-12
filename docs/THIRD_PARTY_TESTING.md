# Independent third-party testing

**Public test address:** https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/14

**Current fixed software release:** `v0.1.1`

Release page: https://github.com/Civilization-Leap/computable-cooperation-mechanisms/releases/tag/v0.1.1

Offline bundle: `computable-cooperation-mechanisms-v0.1.1-offline.tar.gz`

Expected bundle SHA-256:

```text
15f11f18b8438821bb1215439754aebc182023bb2a53a68efacbdf12b8947d12
```

We invite independent testers to **reproduce it, break it, reimplement it, or challenge the evidence and governance claims**. Endorsement is not requested. A failed reproduction, precise incompatibility, malformed input, counterexample, missing provenance field, or realistic misuse path is a useful result.

The project checks declared inputs under declared rules. It does not establish that the inputs are true, that a threshold is legitimate, that affected parties participated in setting it, that a mechanism is fair, or that a real-world action is authorized.

## Fastest route — 5 to 15 minutes

Requires Python 3.11–3.13. After downloading the source, the checker and test suite use only the Python standard library: no pip, account, API key, model download, or hosted service is required.

```bash
git clone --branch v0.1.1 --depth 1 https://github.com/Civilization-Leap/computable-cooperation-mechanisms.git
cd computable-cooperation-mechanisms
python scripts/reproduce_offline.py
```

Or run the four public cases and suite directly:

```bash
python -m mechanism_ref examples/shared_equipment_third_party_violation.json --out-dir outputs
python -m mechanism_ref examples/shared_equipment_unknown.json --out-dir outputs
python -m mechanism_ref examples/shared_equipment_ok.json --out-dir outputs
python -m mechanism_ref examples/shared_equipment_capacity_violation.json --out-dir outputs
python -W error::ResourceWarning -m unittest discover -s tests -v
```

Expected case statuses, in order:

```text
VIOLATED
UNKNOWN
SATISFIED
VIOLATED
```

Expected test count for `v0.1.1`: **18 passing tests**.

Repository CI verifies the exact release on Python 3.11, 3.12, and 3.13. That is automated CI evidence, not independent third-party execution. Please state the exact runtime you actually use.

## Track A — reproduce `v0.1.1`

**Typical time:** 5–15 minutes.

Report:

- OS and Python version;
- exact tag `v0.1.1` or exact commit;
- commands run;
- four observed statuses;
- observed test count;
- whether the offline bundle SHA-256 matches;
- any mismatch, warning, or unexpected behavior.

A successful run is evidence of independent execution only. It is not fairness certification, empirical validation, or policy approval.

## Track B — try to break `v0.1.1`

**Typical time:** 15–45 minutes.

### 1. Threshold sensitivity

Run:

```bash
python scripts/threshold_sweep.py
```

The supplied outcomes remain fixed while only the declared `THIRD-PARTY` limit changes.

| Limit (TU) | A delta (CU) | B delta (CU) | C delta (TU) | Status |
|---|---:|---:|---:|---|
| 1 | -3.0 | -3.0 | +0.5 | SATISFIED |
| 0.6 | -3.0 | -3.0 | +0.5 | SATISFIED |
| 0.5 | -3.0 | -3.0 | +0.5 | SATISFIED |
| 0.49 | -3.0 | -3.0 | +0.5 | VIOLATED |
| 0.25 | -3.0 | -3.0 | +0.5 | VIOLATED |

This is elementary threshold behavior. Its purpose is to expose exactly where the declared rule enters the verdict. **A precise computation can enforce a line; it does not establish who had authority to draw the line or whether the line is legitimate.**

### 2. CI exit gates

```bash
python -m mechanism_ref examples/shared_equipment_third_party_violation.json --out-dir outputs --fail-on-violation --fail-on-unknown
python -m mechanism_ref examples/shared_equipment_unknown.json --out-dir outputs --fail-on-violation --fail-on-unknown
python -m mechanism_ref examples/shared_equipment_ok.json --out-dir outputs --fail-on-violation --fail-on-unknown
```

Expected exit codes: **1, 3, 0**. Reports should be written before semantic gate failures. Input or argument errors return 2.

### 3. Strict rejection

Add an unsupported top-level `id` field to a copy of `examples/shared_equipment_ok.json`.

Expected input error:

```text
unsupported fields: ['id']
```

The supported identifier is `case_id`.

Useful challenges include duplicate JSON keys, non-finite numbers, undeclared units, invalid references, duplicate outcomes, duplicate constraint IDs, missing values, report-write failures, and platform-specific exit behavior.

## Track C — implement it independently

Reimplement the public semantics in another language. Do not port line by line merely to match Python structure. A separate repository is welcome; no upstream merge is required.

Planning estimate:

- 8–16 focused hours for four-case semantic agreement;
- 16–32 hours including malformed-input coverage, documented differences, and a reproducible command.

See [INDEPENDENT_IMPLEMENTATION.md](INDEPENDENT_IMPLEMENTATION.md) and [Issue #8](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/8).

Report semantic agreement, hash agreement, and malformed-input coverage separately. Cross-language hash differences may reflect JSON serialization rather than semantic disagreement.

## Track D — review the claims without running code

**Typical time:** 10–30 minutes. No programming is required.

This track is for auditors, accountability researchers, civic technologists, domain practitioners, affected-party advocates, and anyone who can identify a concrete governance or interpretation failure.

Read this guide and [THRESHOLD_SENSITIVITY.md](THRESHOLD_SENSITIVITY.md), then return at least one concrete weakness in any of these areas:

1. a misleading inference a reader could draw from `SATISFIED`, `VIOLATED`, or `UNKNOWN`;
2. missing provenance for a threshold: who proposed it, under what authority or evidence, whose interests it protects, who was affected or absent, and how it can be contested, amended, or retired;
3. a realistic misuse path in which precise computation gives an unjustified appearance of legitimacy;
4. a weakness in the evidence labels used to distinguish execution, reimplementation, counterexample, methodological review, and audit.

A Track D response is a **document-only methodological review**, not software validation or an external audit. When a review is cited, its scope, reasoning, evidence, document version, and any voluntarily disclosed relevant methodological background should remain attached. A name, title, or institution does not establish correctness or independence.

Anonymous and affected-party feedback are welcome. Credentials are not an admission gate. Private replies are not permission to publish attribution or quotations.

## What to return

Reply in [Issue #14](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/14) or link a separate public issue/repository.

```markdown
Tester / handle:
UTC date:
Track: A / B / C / D
OS / runtime (A–C):
Exact tag or commit (A–C):
Commands run (A–C):
Observed statuses (A–C):
Observed test count (A–C):
Observed exit codes (A–C):
Bundle SHA-256 agreement: yes / no / not tested
Semantic agreement: yes / partial / no / not tested
Hash agreement: yes / partial / no / not tested
Malformed-input coverage:
Document/section reviewed (D):
Concrete boundary, provenance, or misuse concern (D):
Reasoning/evidence and what could change the assessment (D):
Unexpected behavior or counterexample:
Public evidence link:
Time spent (optional):
```

## Evidence labels

Results are described narrowly:

- **independent execution** — someone ran the supplied implementation;
- **independent reimplementation** — someone built a separate implementation;
- **counterexample or incompatibility** — a documented behavior, input, or representation gap;
- **document-only methodological review** — a bounded non-code review of evidence labels, interpretation boundaries, rule provenance, or likely misuse;
- **external audit** — reserved for a separately scoped audit with stated methods, independence criteria, and evidence.

Maintainer runs and AI-assisted internal checks are not counted as independent third-party validation.

## Historical release

`v0.1.0` remains available as the first frozen milestone and has Zenodo version DOI `10.5281/zenodo.22656544`. New public testing should normally target `v0.1.1`; use `v0.1.0` only when reproducing the historical release specifically.

## 中文简要说明

当前公开测试基线为 **v0.1.1**。最快路径约 5–15 分钟：下载固定版本后运行 `python scripts/reproduce_offline.py`。也可选择进一步击破输入与退出门禁、用另一种语言独立实现，或不运行代码而审阅证据标签、阈值来源、受影响方参与及现实误用风险。

项目不要求测试者认同理论。失败、差异、反例和无法表达的问题都属于有效结果。软件测试成功不等于公平、正当、实证有效或现实授权。

结果提交入口：
https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/14
