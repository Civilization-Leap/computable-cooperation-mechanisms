# 竞争—合作可计算机制｜最小参考实现

**DEV-1 / v0.1.0.dev1。尚未构成正式开源发布。**

这是一个面向全球后续开发者的小型可运行起点：给定主体、资源、结果和明确约束，计算候选安排相对基线的分项变化，并报告已声明约束是满足、违反还是信息不足。

它**不**认证公平，不推断动机，不预测行为，不生成研究 H/T/L/RUN 状态，也不产生现实授权。

## 运行
```bash
python -m mechanism_ref examples/shared_equipment_ok.json --out-dir outputs
python -m unittest discover -s tests -v
```

## DEV-1 已实现的方法纪律
- 主体、维度、单位分列，不生成“公平总分”；
- 只对主体＋维度＋单位一致的基线/候选结果计算差值；
- 硬约束独立检查，普通收益不能抵销第三方硬约束；
- 明确 UNKNOWN 不补零；
- 输出包含输入复算哈希和解释边界。

## 三个原创教学变体
1. `shared_equipment_ok.json`：已声明约束满足；
2. `shared_equipment_third_party_violation.json`：A/B 普通成本下降，但 C 的保护门被违反；
3. `shared_equipment_unknown.json`：当前资源未知，因此相应硬检查保持 UNKNOWN。

## 边界
本实现不是正式 R1 B2B 盲测夹具，也不是 WP-01-A 的完整软件化。正式研究材料保持隔离。竞争、合作、联盟、阵营、共同体也不被编码为单向价值阶梯。

## 许可状态
许可证仍待正式发布前确认；DEV-1 不宣称已经完成公开开源发布。
