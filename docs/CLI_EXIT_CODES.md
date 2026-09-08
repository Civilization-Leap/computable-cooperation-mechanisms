# Optional CLI gates (unreleased)

The frozen v0.1.0 release returns 0 after successfully writing reports, including `VIOLATED` and `UNKNOWN`. The development CLI preserves that default and adds two opt-in flags. These flags are not present in the published v0.1.0 tag.

| Overall result | Default | --fail-on-violation | --fail-on-unknown | Both flags |
|---|---:|---:|---:|---:|
| SATISFIED | 0 | 0 | 0 | 0 |
| VIOLATED | 0 | 1 | 0 | 1 |
| UNKNOWN | 0 | 0 | 3 | 3 |
| Input / argument error handled by the CLI | 2 | 2 | 2 | 2 |

Use both flags if CI should continue only when the overall declared hard-constraint result is `SATISFIED`:

```bash
python -m mechanism_ref examples/shared_equipment_third_party_violation.json --out-dir outputs --fail-on-violation --fail-on-unknown
```

This example writes both reports, prints `VIOLATED`, and exits 1. A valid `UNKNOWN` case writes reports before exiting 3 with both flags. Invalid inputs are rejected before evaluation and report creation. An unsupported top-level `id` field produces `unsupported fields: ['id']`; the supported case identifier is `case_id`. This evidence concerns top-level field rejection and the tested validation rules; it is not a claim that every JSON Schema rule is enforced by a general schema engine.

The evaluator's overall result gives hard violations precedence over unknowns. These flags follow that existing aggregate; they do not reinterpret soft checks, add a new mechanism rule, or certify fairness. A report-write failure is also an execution failure: downstream code should read the printed status and generated evidence instead of inferring a semantic result from an exit code alone.

## 中文说明

默认退出码仍表示报告生成是否成功。新增 `--fail-on-violation` 在总体硬约束判定为违反时返回 1；新增 `--fail-on-unknown` 在总体判定为未知时返回 3。CI 若要求只有 `SATISFIED` 才继续，应同时使用两项。有效输入会先写完报告再返回门禁退出码，输入错误仍直接拒绝并返回 2。以上属于未发布的候选改动，不能写成 v0.1.0 已有功能。
