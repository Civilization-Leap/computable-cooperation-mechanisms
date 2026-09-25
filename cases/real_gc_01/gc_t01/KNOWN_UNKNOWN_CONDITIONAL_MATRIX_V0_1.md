# GC-T01｜已知—未知—条件性结论矩阵 V0.1

Known, Unknown and Conditional Findings Matrix — REAL GC 01

作者：子君赋｜出品：文明跃迁研究组  
版本：V0.1｜核验日期：2026-09-25｜案例：REAL GC 01 / GC-T01  
核验起点：PR #48；head 58078fcd5e6688a40ed3b54778090ba2a9dc2c61；研究分支未合并。

**状态：来源核验后的研究摘要；NOT_CALIBRATED。**

研究目的仍是让双方及第三方看见利益、代价、反馈和保留选择的条件。本矩阵只回答：哪些研究内容已核实，哪些量仍未确定，哪些陈述依赖什么假设。它不替读者选择政策。

“已知”指本轮在具名原始来源中核实到的统计或研究内容，不把估计升级为观察事实；“未知”指本项目当前证据不足，不声称全世界无人知道；“条件性结论”只在所列模型、时期与假设范围内成立。

## 一、已核实内容及适用边界

| 编号／问题 | 在原始来源中核实到的内容 | 未知或不能外推之处 |
| --- | --- | --- |
| K01｜进口端承担 | USITC 回顾 2018–2021 年受 Section 232/301 影响的进口，估计关税近乎全部传导到美国进口商支付价格。[S1；E016] | 这是特定研究的估计，不是所有时期和商品的常数；进口商承担不能直接等同于消费者承担。 |
| K02｜直接行业变化 | USITC 对受 Section 301 影响行业估计：自华进口 −13%、美国生产价值 +0.4%、美国产品价格 +0.2%。[S1；E017] | 该报告未估计 Section 301 全部下游效应，不涵盖完整经济、长期或安全效果。三项不是可相加的福利分量。 |
| K03｜就业与反馈 | Flaaen/Pierce 在 2018–2019 年制造业研究中，区分进口保护、投入成本和反制，并报告暴露更高行业的相对就业下降。[S2；D17] | 这是行业相对效应；不能写成所有受保护企业或所有劳动者都受损，也不能直接移植为 2026 年就业预测。 |
| K04｜早期消费价格 | 美联储研究估计：2025 年 2–3 月对华关税截至 3 月已使核心商品 PCE 价格约增加 0.3%，核心 PCE 约增加 0.1%。[S3；E019] | 这是早期价格水平效应；不是全年通胀增幅，也不是一组独立、可叠加的两项损失。 |
| K05｜替代存在时间差 | 2024 年美联储研究在其样本与方法下，报告自华采购替代弹性经过约 3–4 年才明显增强。[S4；E023、D31] | 不能把这一时间当作每家企业的切换期限，更不能据此判定退出和重新进入具有相同成本。 |
| K06｜第三方不是空白 | 2026 年美联储研究将墨西哥对美出口增量分解为不同来源，估计约 53% 与其识别的贸易转移有关。[S5；E024–E025] | 分母是该研究的出口增量，不是墨西哥 GDP 或福利；所有权、工资、环境与净利益不能由份额直接推出。 |
| K07｜2025 研究估计 | BPEA 三月稿的基准进口端传导估计约为 90%；其短期模型按贸易条件假设报告不同结果，见下表。[S6；原 TOT-E01–E03] | 对象是 2025 年美国整体关税及模型内反制，不是单独中美措施；作者估计不等于 CCM 独立测量。 |

以上记录按原研究身份保留：研究估计为 `THIRD_PARTY_ESTIMATE`；来源身份另记 `OFFICIAL_SOURCE` 或 `THIRD_PARTY_SOURCE`。美联储工作论文／Notes 的作者分析不等于机构政策立场。旧账本 E/D/TOT 编号仅用于回溯，不证明其余行已全部复核。

## 二、作者模型的条件表：不是政策评分

| 编号 | 原研究设定 | 作者报告的模型福利变化 | 定位 |
| --- | --- | --- | --- |
| C01 | 劳动不跨部门流动；不计贸易条件调整 | −0.13% GDP | 表 6 |
| C02 | 劳动不跨部门流动；计入贸易条件调整 | +0.10% GDP | 表 6 |
| C03 | 允许劳动跨部门流动；不计贸易条件调整 | −0.50% GDP | 表 A.8 |
| C04 | 允许劳动跨部门流动；计入贸易条件调整 | +0.28% GDP | 表 A.8 |

来源：[S6]。这是作者反事实模型的情景结果，不是置信区间、实现值或胜负概率。前两行不能代表论文全部假设范围；劳动流动两行单独保留，不与短期两行拼成一个“综合区间”。CCM 的既有区间分类器只检查输入端点，未复现原模型，也未验证其数据与参数。

**有条件可报告：**在这份具名版本中，改变贸易条件／劳动调整设定，作者报告的结果发生变化。**不可据此报告：**当某现实变量过线，中美就“应该”转入某种关系状态。

## 三、关键未知及需要补足的证据

| 编号／对象 | 当前未确定事项 | 补证要求与边界 |
| --- | --- | --- |
| U01｜实际贸易条件 | 本项目尚不能以同口径证据识别足以区分作者两类设定的整体价格响应。 | 分别核对进口端、美国生产者／出口端价格，以及汇率、构成、运输与基准反事实；不把汇率影响一概排除在经济效应之外。[S6 §§5.2.2–5.3] |
| U02｜中国内部承担 | 尚无本项目已对齐的中国家庭、劳动者、进口商、出口商完整分量表。 | 需要可定位原件、样本、时期、识别方法；不能用美国估计对称填入中国。既有 D27 未给出具体研究，暂不作已核实证据。 |
| U03｜第三方净变化 | 已知存在贸易重组研究，但本项目缺少相同口径的工资、增加值、环境、依赖与退出能力联合数据。 | 具体国家、行业和群体分列；出口增长只占其中一个分量。[S5；D33] |
| U04｜通道能否恢复 | CH-MARKET、CH-INPUT、CH-REENTRY、CH-EMERGENCY 对具名主体的可用性与恢复条件仍未充分确立。 | 先确定主体、能力、通道、时间窗口及恢复条件；昂贵或缓慢不自动等于永久关闭。 |
| U05｜完整共同利益 | GC-T01 尚未形成覆盖中美内部群体、第三方及系统风险的兼容现实数据。 | 不能从单国汇总或一个关税研究生成现实 S0–S3 排序，也没有计算出共同最大利益／最小风险的唯一配置。 |

## 四、本轮定向更正

### 贸易条件不是单一路径

先前把关键问题主要写成“外国出口商是否降价”，解释过窄。原稿同时区分进口端与美国生产者／出口端调整。[S6，正文页 26–31]

### 同一论文也未必能相加

表 6 注明四个分项并非加法分解。来自同文、同表、同单位，仍不自动满足可加性；必须看估计对象和计算定义。[S6，正文页 32]

### “约 1.2% GDP”不能写成年度实收事实

此前表述缺少口径。表 6 的关税收入反事实分量为 1.08%／1.15% GDP，不是 2025 年财政实际征收额；本矩阵不保留未限定的 1.2% 说法。[S6，表 6]

### 本轮固定到可核验版本

NBER 网页与 PDF 在本次访问中返回 403。本轮依据可读取的 BPEA 三月会议稿，不宣称已重新验证 NBER 四月稿或确认两版逐字一致。

## 五、计算状态与对外使用

本轮没有改变核心模型、合成输入、S0–S3 定义或通道判据，也没有运行新的现实前沿计算。

目前 `transition.py` 记录方向性成本，但在比较前沿时并未把这些成本施加到结果分量；因此不能声称已完成“包含转换成本的现实比较”。原有算术恒等式检查与端点符号分类也不是独立结构复现。这些是能力范围说明，不是重启开发任务。

```text
empirical_frontier = NOT_CALIBRATED
structural_replication = false
independent_validation = false
external_evidence_state_changed = false
policy_recommendation = false
```

局部分量可以分别报告；未确定的总效应不抹去已核实分量，已核实分量也不自动组成完整共同利益结论。共同利益与风险目标保留，但不压缩为国家总分或政策优劣排序。

外部读者可只回应一项：“哪条记录的来源、时期、主体、因果解释或恢复条件有误？可用什么公开证据检查？”无需接受 CCM 的理论立场。

## 六、原始来源与续读

**[S1] USITC（2023-03-15）**  
Economic Impact of Section 232 and 301 Tariffs on U.S. Industries，调查 332-591／报告 5405；官方发布正文及研究范围说明。  
<https://www.usitc.gov/press_room/news_release/2023/er0315_63679.htm>

**[S2] Flaaen & Pierce（2019；页面更新 2020-05-26）**  
Disentangling the Effects of the 2018–2019 Tariffs on a Globally Connected U.S. Manufacturing Sector，FEDS 2019-086，摘要。  
<https://www.federalreserve.gov/econres/feds/disentangling-the-effects-of-the-2018-2019-tariffs-on-a-globally-connected-us-manufacturing-sector.htm>

**[S3] Federal Reserve FEDS Notes（2025-05-09）**  
Detecting Tariff Effects on Consumer Prices in Real Time，导言、Data 与 Theoretical Effect；观察仅到 2025 年 3 月。  
<https://www.federalreserve.gov/econres/notes/feds-notes/detecting-tariff-effects-on-consumer-prices-in-real-time-20250509.html>

**[S4] Haberkorn 等（2024-04-12）**  
Global trade patterns in the wake of the 2018–2019 U.S.–China tariff hikes，导言及来源替代分析。  
<https://www.federalreserve.gov/econres/notes/feds-notes/global-trade-patterns-in-the-wake-of-the-2018-2019-u-s-china-tariff-hikes-20240412.html>

**[S5] Aristizabal-Ramirez 等（2026-06-05）**  
Mexico in U.S. Supply Chains: Lessons from 2018–19 Tariffs，第 2 节及其识别限制；前期 2014–17 年、后期 2021–24 年。  
<https://www.federalreserve.gov/econres/notes/feds-notes/mexico-in-u-s-supply-chains-lessons-from-2018-19-tariffs-20260605.html>

**[S6] Fajgelbaum & Khandelwal（2026 年 3 月会议稿）**  
Tariffs in 2025: Short-Run Impacts on the U.S. Economy，BPEA Conference Draft；正文页 3、26–32、64，尤其第 5.2.2 节、表 6 与表 A.8。本轮已对表格页面图像核对。  
<https://www.brookings.edu/wp-content/uploads/2026/03/1_Fajgelbaum-Khandelwal_unembargoed.pdf>

来源定位说明：正文页码依 PDF 印刷页号；S6 的 PDF 第一页为外封面。来源核验日期不等于研究数据年份。

同一案例续读：[主体分配账本](ACTOR_DISTRIBUTION_LEDGER_V0_1.md)、[兼容性审计](EVIDENCE_COMPATIBILITY_AUDIT_V0_1.md)、[现实研究敏感性说明](REAL_STUDY_SENSITIVITY_2025_V0_1.md)、[贸易条件节点](TERMS_OF_TRADE_EVIDENCE_NODE_V0_1.md)。

[CCM 仓库](https://github.com/Civilization-Leap/computable-cooperation-mechanisms) · [本案 PR #48](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/pull/48) · [文明跃迁网站](https://www.civitas.top/)
