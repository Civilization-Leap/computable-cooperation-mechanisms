# CCM-BYOP-04｜AI 辅助试填报告

## 目的

检验现有 BYOP 结构是否能够承接公开真实问题，并区分：

- 当前工具可以表达什么；
- 只能作为领域模板表达什么；
- 哪些属于 representation gap；
- 哪些必须继续留在人类、制度、法律与现实授权层。

本轮不是独立第三方验证，也不计入外部采用证据。它是维护方的 AI 辅助内部试填。

## 试填对象

1. Microsoft / Activision Blizzard 并购与竞争影响；
2. Apple App Store / EU DMA 平台治理；
3. 自主武器国际规则。

均仅使用公开来源作为事实锚点，不推断未公开事实。

## 试填结果

### 1. Problem Card 是否可用

**结果：基本可用。**

三个案例都可以写出：

- 主体；
- 主体目的；
- 候选安排；
- 合作 / 不合作或不同制度安排的收益与损害；
- 第三方；
- 硬边界；
- UNKNOWN；
- 当前工具无法表达的部分。

这说明现有 Problem Card 已能作为现实问题的第一层“结构化显影”工具。

### 2. 当前 v0.1.1 是否足够直接运行

**结果：不应强行全部运行。**

原因不是 Problem Card 失败，而是三个现实问题都包含当前 core 没有表达的动态结构：

- 并购：控制权变化、长期承诺、动态竞争行为；
- 平台治理：规则改变后的生态反馈、市场力量与安全风险；
- 自主武器治理：升级链、扩散、责任链和不可逆路径。

若为了“让工具跑起来”而把这些部分删除，容易制造虚假的完整性。

因此“无法无失真进入 v0.1.1”被确认是一个有效输出，而不是失败。

### 3. 反馈分类是否足够

**结果：A–G 分类基本够用，但出现一个值得观察的重复现象。**

同一现实问题经常同时属于：

- A — REPRESENTATION GAP；
- C — MISSING ACTOR / IMPACT；
- D — MISSING CONSTRAINT；
- F — DOMAIN EXTENSION。

因此以后 triage 不应强制每个问题只选一个类别。可以指定一个 primary class，再保留 secondary classes。

### 4. “最小 adequate response”规则是否有效

**结果：有效。**

三个案例都没有立即证明 core/schema 必须改变。

更合理的下一层是：

- 并购 / 商业交易：先建立 reusable domain template；
- 平台治理：先建立 actor-role 与 rule-change template；
- 高后果 AI 治理：先建立 governance-only template，并明确禁止滑向操作性武器优化。

只有多个真实案例反复暴露同一个无法绕开的结构后，再讨论 core/schema。

## 本轮发现的 BYOP 入口改进点

1. 允许一个问题有 primary + secondary feedback classes；
2. 问题卡应更加明确地区分：事实、主体声明、分析假设、UNKNOWN；
3. 候选方案最好允许两种以上，而不是只写合作 / 不合作；
4. 对高后果领域应在 intake 阶段就声明禁止操作性危险优化；
5. 真实案例不必都转成 runnable fixture；只有在不损失关键结构时才进入 evaluator。

## 阶段结论

BYOP 入口已经具备承接真实问题的基本能力。

当前最重要的改进方向不是扩大 core，而是让更多真实问题进入，统计重复出现的结构缺口。

因此下一阶段应优先积累：

**real problem → structured intake → fit/gap judgment → reusable template candidate → only then consider core change**
