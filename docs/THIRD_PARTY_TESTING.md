# Independent third-party testing

**Test address:** https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/14

We invite independent testers to reproduce, break, or reimplement this small
reference checker. You do **not** need to endorse the framework. A failed
reproduction, precise incompatibility, malformed input, or counterexample is
useful evidence.

Choose one track. Keep the frozen release and the development checkout
separate in your report.

## Track A — reproduce the frozen release

**Typical time:** 5–15 minutes after Python and Git are available.

Target:

- release: `v0.1.0`;
- commit: `0960d01d73c73a6ad66644341e70a8cf8b10dd15`;
- runtime: Python 3.11–3.13;
- dependencies after download: Python standard library only; no pip, network,
  account, API key, or model download.

```bash
git clone --branch v0.1.0 --depth 1 https://github.com/Civilization-Leap/computable-cooperation-mechanisms.git
cd computable-cooperation-mechanisms
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

Expected frozen test count: 12 passing tests. The valid cases all return process
exit 0 in `v0.1.0`; that exit code means the reports were produced, not that
every hard constraint was satisfied.

If Git is unavailable, download the
[v0.1.0 source archive](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/releases/tag/v0.1.0),
extract it, and run the same commands from the directory containing
`mechanism_ref/`, `examples/`, and `tests/`.

## Track B — challenge the development checkout

**Typical time:** 15–45 minutes.

This track tests current `main`, not the archived release. Record the exact
commit:

```bash
git clone https://github.com/Civilization-Leap/computable-cooperation-mechanisms.git
cd computable-cooperation-mechanisms
git rev-parse HEAD
python -W error::ResourceWarning -m unittest discover -s tests -v
python scripts/threshold_sweep.py
```

At the time this call was prepared, the candidate suite contained 18 tests:
the original 12, five CLI subprocess tests, and one threshold-sensitivity test.
If the count changes, report the commit and observed count rather than forcing
the old expectation.

The sweep holds A's, B's, and C's supplied outcomes fixed while changing only
the declared `THIRD-PARTY` limit. Expected statuses:

| Limit (TU) | A delta (CU) | B delta (CU) | C delta (TU) | Status |
|---|---:|---:|---:|---|
| 1 | -3.0 | -3.0 | +0.5 | SATISFIED |
| 0.6 | -3.0 | -3.0 | +0.5 | SATISFIED |
| 0.5 | -3.0 | -3.0 | +0.5 | SATISFIED |
| 0.49 | -3.0 | -3.0 | +0.5 | VIOLATED |
| 0.25 | -3.0 | -3.0 | +0.5 | VIOLATED |

This is elementary threshold behavior. Its purpose is to expose exactly where
the declared rule enters the verdict. It does not establish who may legitimately
set the line.

### Test the opt-in CI gates

These flags exist on current `main` and are absent from `v0.1.0`:

```bash
python -m mechanism_ref examples/shared_equipment_third_party_violation.json --out-dir outputs --fail-on-violation --fail-on-unknown
python -m mechanism_ref examples/shared_equipment_unknown.json --out-dir outputs --fail-on-violation --fail-on-unknown
python -m mechanism_ref examples/shared_equipment_ok.json --out-dir outputs --fail-on-violation --fail-on-unknown
```

Expected exit codes are 1, 3, and 0 respectively. Reports should be written
before the two semantic gate failures. Input or argument errors return 2.

### Test strict rejection

Add an unsupported top-level `id` field to a copy of
`examples/shared_equipment_ok.json` and run it. Expected behavior is an input
error containing:

```text
unsupported fields: ['id']
```

The supported case identifier is `case_id`. Record any input that is silently
accepted, silently coerced, or converted to `UNKNOWN` when it should be
rejected.

Useful challenges include duplicate JSON keys, non-finite numbers, undeclared
units, invalid references, duplicate outcomes, duplicate constraint IDs,
missing values, report-write failures, and platform-specific exit behavior.

## Track C — implement it independently

Reimplement the fixed `v0.1.0` semantics in a language you know. Do not port
line by line merely to match the Python structure. A separate repository is
welcome and no upstream merge is required.

Planning estimate:

- 8–16 focused hours for four-case semantic agreement;
- 16–32 hours including malformed-input coverage, documented differences, and
  a reproducible command.

See the full [independent implementation specification](INDEPENDENT_IMPLEMENTATION.md)
and [Issue #8](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/8).

## What to return

Reply in [Issue #14](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/14)
or link a separate public issue/repository. This compact template is enough:

```markdown
Tester / handle:
UTC date:
OS:
Language and runtime:
Track: A / B / C
Exact tag or commit:
Commands run:
Observed case statuses:
Observed test count:
Observed exit codes:
Semantic agreement: yes / partial / no
Hash agreement: yes / partial / no / not tested
Malformed-input coverage:
Unexpected behavior or counterexample:
Public evidence link:
Time spent (optional):
```

Report semantic agreement, hash agreement, and malformed-input coverage
separately. A four-case match is not complete input-language conformance.
Cross-language hash differences may reflect JSON serialization rather than
semantic disagreement.

## Evidence labels

Results will be described narrowly:

- **independent execution** — someone ran the supplied implementation;
- **independent reimplementation** — someone built a separate implementation;
- **counterexample or incompatibility** — a documented behavior, input, or
  representation gap;
- **external audit** — reserved for a separately scoped audit with stated
  methods and evidence.

Anonymous reports are welcome, but a public handle, exact environment, commit,
and raw evidence make the result easier to verify. Project-maintainer runs and
AI-assisted internal checks are not counted as independent third-party
validation.

## Interpretation boundary

A successful software test does not establish that:

- supplied facts are true;
- a threshold is legitimate;
- affected parties participated in setting it;
- the mechanism is fair, optimal, or safe;
- a real-world action is authorized.

The checker evaluates declared inputs under declared rules. Testing should
expose both what it does reliably and what it cannot establish.

## Maintainer-initiated invitations

The first three individualized invitations and their bounded test roles are
recorded in the [Wave 1 outreach log](THIRD_PARTY_TESTER_OUTREACH_WAVE1.md).
An invitation is not counted as external use or validation.

## 中文简要说明

可选择三条路径：复现冻结版、挑战当前开发版、或用另一种语言独立实现。
请记录运行环境、精确提交、命令、状态、退出码和异常；失败、差异和反例同样
有价值。测试成功不等于认可理论，也不构成公平认证、现实授权或外部审计。
结果可提交至 [Issue #14](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/14)。
