# Try the declared rules in five minutes

Use Python 3.11–3.13. The evaluator and tests need only the Python standard library. Neither `pip install` nor `pip install -e .` is required when running from the source directory. The five-minute estimate assumes Python is installed and the source has been obtained.

## Obtain the fixed source

```bash
git clone --branch v0.1.0 --depth 1 https://github.com/Civilization-Leap/computable-cooperation-mechanisms.git
cd computable-cooperation-mechanisms
```

Git is only a download option. If you already have a source ZIP, extract it, open a terminal in the directory containing `mechanism_ref/`, `examples/`, and `tests/`, and skip `git clone`. All subsequent commands work offline. The `v0.1.0` tag resolves to `0960d01d73c73a6ad66644341e70a8cf8b10dd15`. If the interpreter is named `python3`, substitute it for `python` below.

## Run all four teaching variants

```bash
python -m mechanism_ref examples/shared_equipment_third_party_violation.json --out-dir outputs
python -m mechanism_ref examples/shared_equipment_unknown.json --out-dir outputs
python -m mechanism_ref examples/shared_equipment_ok.json --out-dir outputs
python -m mechanism_ref examples/shared_equipment_capacity_violation.json --out-dir outputs
```

Expected console results, in order:

```text
VIOLATED
UNKNOWN
SATISFIED
VIOLATED
```

Each command writes `<example-name>.result.json` and `<example-name>.report.md` under `outputs/`. Open either file in a text editor. The CLI exits successfully for all three valid evaluation statuses; a zero exit code does not mean the constraints were satisfied. Invalid inputs produce a CLI error.

## One change to inspect

Copy `examples/shared_equipment_ok.json`, then change only the constraint whose ID is `THIRD-PARTY`: lower `limit` from `1` to `0.25`. Leave C's candidate loss at `0.5` and leave A/B outcomes unchanged. These commands create and run the copy without altering the original:

```bash
python -c "import json,pathlib; p=pathlib.Path('examples'); c=json.loads((p/'shared_equipment_ok.json').read_text(encoding='utf-8')); next(r for r in c['constraints'] if r['id']=='THIRD-PARTY')['limit']=0.25; (p/'shared_equipment_lower_threshold.json').write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')"
python -m mechanism_ref examples/shared_equipment_lower_threshold.json --out-dir outputs
```

Expected: `VIOLATED`; the third-party check reports `0.5 <= 0.25 is false`. A and B still each save 3 CU. The original `ok` case continues to give `SATISFIED`. This illustrates sensitivity to a declared boundary, not a recommendation to change somebody's rights. The thresholds and outcomes are supplied by the author of the input, not discovered by the evaluator.

## Verify the fixed release

```bash
python -W error::ResourceWarning -m unittest discover -s tests -v
```

Expected: 12 passing tests. See the [comparison](SHARED_EQUIPMENT_COMPARISON.md) and [independent implementation task](INDEPENDENT_IMPLEMENTATION.md).

中文提示：四个结果依次为“违反、未知、满足、违反”。打开 `outputs` 下的报告，即可同时看见 A/B 的成本变化与 C 的损失边界。程序只检查输入中的声明，不判断这些数字是否真实，也不替任何主体决定是否合作。
