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
- requested runtime: Python 3.11–3.13;
- dependencies after download: Python standard library only; no pip, network,
  account, API key, or model download.

The release contains a CI matrix for Python 3.11, 3.12, and 3.13. The latest
development PR also completed all three matrix jobs successfully. That is CI
evidence, not independent third-party execution. The reported external
reproduction so far used Python 3.12.3; please state the exact runtime you
actually test.

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

### Fixed development checkpoint

Use commit `198723d0b0c8e2ea13f3d0d01b0d3078c81db3b4` when you need a
fixed, falsifiable comparison rather than floating `main`:

```bash
git checkout 198723d0b0c8e2ea13f3d0d01b0d3078c81db3b4
```

At that checkpoint, the suite must report 18 passing tests: the original 12,
five CLI subprocess tests, and one threshold-sensitivity test. The four public
case statuses must remain `VIOLATED`, `UNKNOWN`, `SATISFIED`, and
`VIOLATED`; the threshold sweep and exit-code expectations below are also
fixed. A different result is a failed reproduction or a version-specific
incompatibility.

For a later `main` commit, report the actual test count and compare it with
that commit's CI and documentation. A count below 18 is a review trigger, not
automatically a defect: tests may have been consolidated, removed, or replaced.
The fixed checkpoint remains the stable anchor.

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

## Track D — review the evidence and governance claims without code

**Typical time:** 10–30 minutes. No programming or local execution is required.

This track is for auditors, accountability researchers, civic technologists,
domain practitioners, and affected-party advocates. Read this guide, the
[threshold-sensitivity note](THRESHOLD_SENSITIVITY.md), and the generated report
comparison. Return one concrete weakness in any of these areas:

1. whether the evidence labels distinguish execution, reimplementation,
   counterexample, methodological review, and audit without overstating them;
2. what a reader could wrongly infer from `SATISFIED`, `VIOLATED`, or
   `UNKNOWN`;
3. which provenance fields are missing for a declared threshold—who proposed
   it, under what authority or evidence, whose interests it protects, who was
   affected or absent, and how it can be contested, amended, or retired;
4. one realistic misuse path in which precise computation gives an unjustified
   appearance of legitimacy.

A useful response can be a paragraph, annotated screenshot, issue comment, or
proposed field list. State which document and section you reviewed. This is a
**document-only methodological review**, not software validation or an external
audit. If you also run code, report that execution separately under Track A or
B.

## What to return

Reply in [Issue #14](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/14)
or link a separate public issue/repository. This compact template is enough:

```markdown
Tester / handle:
UTC date:
OS:
Language and runtime:
Track: A / B / C / D
Exact tag or commit (A–C):
Commands run (A–C):
Observed case statuses (A–C):
Observed test count (A–C):
Observed exit codes (A–C):
Semantic agreement: yes / partial / no / not tested
Hash agreement: yes / partial / no / not tested
Malformed-input coverage:
Document and sections reviewed (D):
Evidence label or boundary challenged (D):
Concrete misuse path or missing provenance field (D):
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
- **document-only methodological review** — a non-code review of evidence
  labels, interpretation boundaries, rule provenance, or likely misuse; it is
  not software validation;
- **external audit** — reserved for a separately scoped audit with stated
  methods, independence criteria, and evidence. Track D alone does not qualify.

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

可选择四条路径：复现冻结版、挑战固定开发版、用另一种语言独立实现，或不
运行代码而审阅证据标签、解释边界、阈值来源与可能误用。代码轨道须记录运行
环境、精确提交、命令、状态与退出码；文档轨道须指出具体章节、缺失字段或误用
路径。失败、差异和反例同样有价值。测试成功不等于认可理论；文档审阅也不冒充
软件验证或外部审计。结果可提交至
[Issue #14](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/14)。
