# Both sides gain. Who else pays?

**Synthetic shared-equipment comparison; recomputed on 2026-09-08.**

## A result that can be checked

| Candidate | A cost (CU) | B cost (CU) | C reserved-slot loss (TU) | Equipment slots | Declared hard-check result |
|---|---:|---:|---:|---:|---|
| Constraints satisfied | 8 → 5 | 8 → 5 | 0 → 0.5 | 9 | SATISFIED |
| Third-party violation | 8 → 5 | 8 → 5 | 0 → 2 | 9 | VIOLATED |
| Resource unknown | 8 → 5 | 8 → 5 | 0 → 0.5 | unknown | UNKNOWN |
| Capacity violation | 8 → 4 | 8 → 4 | 0 → 0.5 | 11 | VIOLATED |

The declared limits are equipment slots `<= 10` and C's reserved-slot loss `<= 1 TU`. CU and TU are different declared units. Do not add the savings to the lost slots or describe the table as a common welfare scale.

The first two cases hold A/B costs, the equipment allocation, and both limits constant; the numerical change is C's candidate loss. The fourth case offers greater declared savings but exceeds equipment capacity. An explicitly unknown resource in the third case remains unknown.

These outcomes are supplied in the input. The code does not predict that sharing equipment causes these savings. It checks whether the supplied candidate satisfies supplied thresholds. The `SATISFIED` example still worsens C's declared loss by 0.5 TU; it is not a Pareto improvement or a fairness certificate. The identity of C, the limit of 1 TU, and the completeness and legitimacy of the protections all require justification outside this program. A protection omitted from the input will not be discovered by the evaluator.

## 中文短文｜约两百字

双方都获益，合作就值得接受吗？在一个共享设备的合成案例中，A、B的成本都从8降到5，节省完全相同；但第三方C的预留时段损失，一份方案是0.5，另一份是2。若事先声明损失不得超过1，前者满足约束，后者违反约束。再把设备占用设为未知，程序保留“未知”，不会把它当成零。这个可复算演示说明：双方收益相同，不代表第三方后果相同。程序检查的是给定声明；数据是否真实、边界为何成立，仍须由人核验。邀请你复跑，也指出它表达不了的关系。

## English shareable copy

Both parties save the same amount. Does that make both arrangements acceptable? In a synthetic shared-equipment pair, A and B each reduce their declared cost from 8 to 5 CU. C's reserved-slot loss is 0.5 TU in one candidate and 2 TU in the other. With a declared limit of 1 TU, the first satisfies the hard checks and the second violates them. An unknown equipment allocation in a third variant stays `UNKNOWN`.

This demonstrates a rule, not an empirical discovery: the parties' gains do not determine the result of a separately declared third-party constraint. The inputs, affected-party list, and thresholds still need human justification. Try the cases, or show a relationship this small representation cannot express.

[Run it in five minutes](FIVE_MINUTE_WALKTHROUGH.md) · [Challenge the representation](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/5)

## Reproduction record

Source checked: main `aa42932f659d4dccb44307237da64fc866664cde`; the evaluator, tests, and four inputs are unchanged from tag `v0.1.0` (`0960d01d73c73a6ad66644341e70a8cf8b10dd15`). All four examples were evaluated locally and the existing 12-test suite passed with `ResourceWarning` treated as an error.

| Input suffix | Evaluator input SHA-256 |
|---|---|
| `ok` | `a43ce35a760eac7ad27d7381a3008c553a3926fd7b86341276177b22615969cd` |
| `third_party_violation` | `5e99ad94c5afbb42821064b9a9d93fb0c9117fb5968e811b0a28f9caa158354c` |
| `unknown` | `c049ff5203b3b2b5b5e9bdc6afadd8579f45a76013ef4bf774b5e4dd108a0e92` |
| `capacity_violation` | `b54be6413d5a93ce553aadfe8f78f0cabaa668a5240478b1355c1655dbf0f1d4` |
