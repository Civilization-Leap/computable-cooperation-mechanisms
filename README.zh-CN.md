# 竞争—合作可计算机制｜最小参考实现

**DEV-2 / v0.1.0.dev2。仓库已公开，但尚未完成正式开源许可证授权。**

这是一个面向全球后续开发者的小型可运行起点：给定主体、资源、结果和明确约束，计算候选安排相对基线的分项变化，并报告已声明约束是满足、违反还是信息不足。

它**不**认证公平，不推断动机，不预测行为，不生成研究 H/T/L/RUN 状态，也不产生现实授权。

## 运行
```bash
python -m mechanism_ref examples/shared_equipment_ok.json --out-dir outputs
python -m unittest discover -s tests -v
```

## 当前已实现的方法纪律
- 主体、维度、单位分列，不生成“公平总分”；
- 只对主体＋维度＋单位一致的基线/候选结果计算差值；
- 硬约束独立检查，普通收益不能抵销第三方硬约束；
- 明确 UNKNOWN 不补零；
- 非法引用、未声明单位等输入错误直接拒绝，不伪装成 UNKNOWN；
- 计算具确定性，并验证不会修改原始输入；
- 输出包含输入复算哈希和解释边界。

## 四个原创教学变体
1. `shared_equipment_ok.json`：已声明约束满足；
2. `shared_equipment_third_party_violation.json`：A/B 普通成本下降，但 C 的保护门被违反；
3. `shared_equipment_unknown.json`：当前资源被明确标记为未知，因此相应硬检查保持 UNKNOWN；
4. `shared_equipment_capacity_violation.json`：同类场景扩展，仅通过更换输入触发资源容量违反，不在内核中写场景特判。

## 验证
DEV-2 单元测试共 12 项。Pull Request CI 在 Python 3.11、3.12、3.13 上运行测试，并把 `ResourceWarning` 当作错误，同时实际运行四个教学变体。

## 边界
本实现不是正式 R1 B2B 盲测夹具，也不是 WP-01-A 的完整软件化。正式研究材料保持隔离。竞争、合作、联盟、阵营、共同体也不被编码为单向价值阶梯。

## 扩展
可以按同一 JSON 合同新增同类场景。新增约束语义必须显式修改代码、测试和文档，不允许静默解释。

## 许可状态
仓库已公开，但正式许可证仍待确认。Apache-2.0 目前仍只是候选。仓库公开可见不等于已经完成正式开源许可授权。
