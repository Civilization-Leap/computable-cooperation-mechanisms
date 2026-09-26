# REAL GC 01｜转换代价进入条件比较 V0.1

作者：子君赋｜出品：文明跃迁研究组  
日期：2026-09-25｜对象：PR #48 / `frontier_transition`  
起点：`616ceb7f6da57c94285d920293be4f86785d6d8a`

## 补正对象

前一版 `transition.py` 仅记录方向性成本，计算前沿时仍使用未调整的结果分量。本轮用原始 GitHub blob 核对后的源码复现了这一遗漏，再补上调用连接；不是重新设计研究目标或核心模型。

## 现在实际计算什么

`原始分量 → 单独声明的反馈 → 指定转换代价 → 同分量比较`

成本必须指定 `target_configuration` 和完整的 `(actor, dimension, horizon, unit)`。输入是该分量单位下的非负额外负担：`cost/risk` 加上负担，`benefit/feedback/option_value` 扣除负担。只改这一坐标，不以福利总分抵消别的坐标，也不作跨期折现或货币换算。

输入分量须不含另行声明的反馈及转换代价。重复目标坐标、标为 `already_included=True` 的成本、不存在的目标分量、单位或时间错配、负数、布尔值和非有限数字均被拒绝。程序无法识别未披露的经济重叠；不重复计入仍需证据与会计范围支持。

单独声明的反馈在此入口内先物化一次，再施加转换代价。原始输入不修改。计算后的分量不冒充新增观察事实；原值、来源状态、来源身份、运算和新值保留在 trace 中。

## 三组纯合成对照

甲主体在 A 的收益／成本为 6／5，在 B 为 7／2；乙主体和第三方相应分量完全相同。数字都是测试假设，不是国家数据。代码中的固定主体标识仅为现有 schema 槽位，两种配置使用相同策略元数据。

| B 的额外成本 | B 调整后的成本 | 声明范围内的前沿 | 解释 |
| --- | --- | --- | --- |
| 2 | 4 | A 被 B 支配，只留 B | 仅是给定合成分量的数学关系 |
| 4 | 6 | A、B 互不支配 | B 收益较高，但成本也较高；不跨分量抵消 |
| UNKNOWN | UNKNOWN | 不输出确定前沿 | 状态为 UNDECIDABLE，不把未知当作零 |

前两组的差异标为 `SENSITIVE`，仅指这两个合成取值，不代表现实合理区间已确定。通用比较函数保持 `robustness = NOT_ASSESSED`。

## 通道与未知不能被前沿列表掩盖

比较前后必须有同一候选集合、主体／分量／时间／单位范围、分析域和同一组具名通道定义。声明的通道证据为 UNKNOWN 时，不生成确定前沿或进入／离开结论；声明为关闭的配置单列排除，不因未被其他配置支配就留在可行前沿。成本高、转换缓慢均不会自动改写通道状态。

不存在通道声明不等于通道已经安全；这里始终只检查已声明范围。通道是否真实不可恢复、谁有权判断、证据是否充分，仍不是这段计算自行证明的事实。

## 复算

在包含本轮修改的仓库根目录运行：

```bash
python -m cases.real_gc_01.v0_2.transition_example
python -W error::ResourceWarning -m unittest discover -s tests -p 'test_real_gc_01_transition.py' -v
```

示例只向标准输出写 JSON，不覆盖输入。专项测试共 20 项，保留此前四项行为检验，并补充成本实算、未知传播、分量独立、目标绑定、输入保留、来源留痕、反馈接入与通道检查。全仓回归以对应提交的 GitHub Actions 记录为准。

## 范围不升级

这次补正只覆盖 `frontier_transition` 入口；没有重写 `model.py`、独立敏感性模块、GC-T01 现实证据或 REAL MA 01。它不意味着其它直接调用 `pareto_frontier` 的路径已获得相同检查。

`cost_coverage = DECLARED_ITEMS_ONLY`。未列出的现实成本不是经验证的零。无合理替代取值不能声称稳健；相关配置、单位、会计范围和假设仍需使用者审查。未改动此前的“已知—未知—条件性结论矩阵”版本快照。

```text
empirical_frontier = NOT_CALIBRATED
independent_validation = false
external_evidence_state_changed = false
policy_recommendation = false
```

本例的价值是让读者看见：是否计入转换代价，会改变给定分量的比较关系；它不把这种关系转换为现实政策选择。

续读：[现行证据矩阵](../gc_t01/KNOWN_UNKNOWN_CONDITIONAL_MATRIX_V0_1.md) · [取值来源与敏感性协议](../INPUT_PROVENANCE_AND_SENSITIVITY_V0_1.md) · [案例 PR #48](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/pull/48) · [文明跃迁网站](https://www.civitas.top/)
