# REAL GC 01｜外部复算与反例入口 V0.2

**先看清：谁获益，谁承担代价，结论依赖哪些假设。**

作者：子君赋｜出品：文明跃迁研究组  
2026-09-25｜CCM 中美竞争与合作研究｜Round 1

本入口 V0.2 取代 V0.1 的参与说明；不改变固定代码 V0.2 或中文证据矩阵 V0.1。

本轮不要求你接受某种中美政策立场，也不要求先读完整理论。只邀请你检查一件具体的事：当转换代价、证据或受影响主体改变时，模型是否如实呈现影响，还是遗漏了一个足以改变判断的条件？一个运行失败、一处来源错误、一个反例，都可以成为有用贡献。

**私下回复邀请发送者，或[公开反馈：Issue #49](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/49)，任选一种。** 私下回复同样计入参与记录并按同一证据标准核对；没有许可，不公开其内容、身份或署名，也不要求机构背书。公开参与不是有效贡献的前提。没有收到邀请时，可私信维护者：<axdwzx@gmail.com>。请勿发送敏感材料；普通邮件不保证保密或绝对安全。

**Private reply to the invitation sender / maintainer, or [public Issue #49](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/49): either is valid.** Private replies count as participation and undergo the same evidence review; content, identity or attribution will not be made public without consent. No institutional endorsement is sought. Contact: <axdwzx@gmail.com>. Do not send sensitive material; ordinary email is not a secure channel.

**[English evidence excerpt: K01–K07, C01–C04, U01–U05](gc_t01/KNOWN_UNKNOWN_CONDITIONAL_MATRIX_EN_V0_1.md)** · [中文证据矩阵](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/blob/c822d1729bf4d4ed5a4c6c0f518c255c36cbf0ca/cases/real_gc_01/gc_t01/KNOWN_UNKNOWN_CONDITIONAL_MATRIX_V0_1.md)。本轮不使用铁路案例 Issue #45 或其表单。

## 1. 先选一个入口

| 你想检查什么 | 从哪里开始 | 最小产出 |
| --- | --- | --- |
| 不运行代码，也能检查记账吗？ | R0：只读样例源码和下方英中记账说明 | 一句遗漏、重复计入或所需证据 |
| 数字改变，比较是否真的改变？ | 下方固定版本的转换代价样例 | 原样运行结果，或一条失败日志 |
| 模型有没有漏掉代价或重复计入？ | 样例与转换代价说明 | 一个源码位置或最小改动；注明是否运行 |
| 研究证据是否支持文中的说法？ | 已知—未知—条件性结论矩阵 | 一个 K/C/U 行号、来源页码及差异 |

首轮材料固定到代码提交 `c822d1729bf4d4ed5a4c6c0f518c255c36cbf0ca`，不是滚动的“最新版”。入口 V0.2、代码 V0.2、中文证据矩阵 V0.1、英文摘译 V0.1 是不同对象，不互相代表。英文摘译不新增研究结论。

- [证据矩阵：已知、未知与条件性结论](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/blob/c822d1729bf4d4ed5a4c6c0f518c255c36cbf0ca/cases/real_gc_01/gc_t01/KNOWN_UNKNOWN_CONDITIONAL_MATRIX_V0_1.md)
- [转换代价说明：计算范围与限制](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/blob/c822d1729bf4d4ed5a4c6c0f518c255c36cbf0ca/cases/real_gc_01/v0_2/TRANSITION_COST_ACCOUNTING_V0_1.md)
- [样例源码](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/blob/c822d1729bf4d4ed5a4c6c0f518c255c36cbf0ca/cases/real_gc_01/v0_2/transition_example.py) · [20 项专项测试](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/blob/c822d1729bf4d4ed5a4c6c0f518c255c36cbf0ca/tests/test_real_gc_01_transition.py)
- [开发 PR #48](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/pull/48) · [代码基线 CI Run #156](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/actions/runs/36100233649)

**版本提示：**本入口创建时 PR #48 尚未合并，默认 main 不含本样例。证据矩阵第五节是修复前的能力快照；本轮转换代价实际行为以独立的转换代价说明和固定代码为准，不把旧快照当作当前程序状态。

## R0｜只读检查：零安装、零执行

只读上方固定样例源码；需要追查时再读转换代价说明。你不必 clone、安装 Python 或执行陌生仓库。一个问题即可：“这项记账遗漏了什么，或把什么算了两次？”

**只读记账摘要：**A 的收益／成本为 6／5，B 为 7／2；其它分量相同。额外代价只加入 B 的成本：2 → 4，4 → 6，未知 → 未知。不以更高收益抵消更高成本。反馈与转换代价必须代表不同后果；程序不能自行识别隐藏的经济重复计入。全部数字都是合成假设。

**R0 — Read only, no installation or execution.** Read the pinned example source above. Accounting in plain English: A has benefit/cost 6/5; B has 7/2; other components are equal. An extra burden changes only B's cost: 2 → 4, 4 → 6, unknown → unknown. Higher benefit does not offset higher cost. Feedback and transition burdens must represent distinct consequences; hidden economic double counting is not automatically detectable. All numbers are synthetic. Reply: **“This accounting omits ___ / counts ___ twice; check it with ___.”** A reasoned static objection is valid without a run. Planning effort: about five minutes, not measured.

## 2. R1｜原样复算

需要 Python 3.11–3.13。样例仅用标准库，无需安装第三方 Python 包。在新目录操作，不覆盖已有工作区：

<!-- R1_CODE_COMMIT: c822d1729bf4d4ed5a4c6c0f518c255c36cbf0ca -->
<!-- R1_EXPECTED_TESTS: 20 -->
<!-- R1_CHECKOUT_BEGIN -->
```text
git clone https://github.com/Civilization-Leap/computable-cooperation-mechanisms.git real-gc-01-round1
cd real-gc-01-round1
git fetch origin pull/48/head
git checkout --detach c822d1729bf4d4ed5a4c6c0f518c255c36cbf0ca
git rev-parse HEAD
```
<!-- R1_CHECKOUT_END -->

确认当前目录同时包含 `cases` 与 `tests` 后运行以下三条。以下区块也是 CI 的命令来源，双引号兼容 Bash、PowerShell 与 Windows cmd：

<!-- R1_PYTHON_BEGIN -->
```text
python --version
python -m cases.real_gc_01.v0_2.transition_example
python -W error::ResourceWarning -m unittest discover -s tests -p "test_real_gc_01_transition.py" -v
```
<!-- R1_PYTHON_END -->

本机使用 `python3` 或 `py -3.12` 时，一致替换命令中的 `python`。示例向标准输出写 JSON，不改输入。首次先保留未经改动的结果；运行失败也请报告，不要为匹配下表而改动输出。

不使用 Git：[下载固定提交源码 ZIP](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/archive/c822d1729bf4d4ed5a4c6c0f518c255c36cbf0ca.zip)，解压后在同时包含 `cases` 和 `tests` 的根目录运行最后三条 Python 命令。ZIP 不包含 Git 历史，不运行 `git rev-parse HEAD`；在反馈中注明下载地址和提交号。GitHub 的[源码归档说明](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives)解释了固定提交与压缩包字节稳定性的区别；本入口未给 ZIP 编造校验值。

**预期观察，不是要求你支持的答案：**

| 声明的 B 额外代价 | B 调整后的成本 | 固定合成输入下的观察 |
| --- | --- | --- |
| 2 | 4 | `after_frontier = [B]` |
| 4 | 6 | `after_frontier = [A, B]` |
| null（UNKNOWN） | null | `comparison_status = UNDECIDABLE`，确定前沿为 null |

A/B 是数学配置，不代表国家、政策或 S0–S3 的优劣。代码中的 US/CN/第三方只是现有数据槽位，两个配置使用相同策略元数据。测试集必须实际运行 20 项；`Ran 0 tests` 不是复算通过。测试通过只说明这些断言通过。

## 3. R2｜构造一个反例（可只读）

不允许运行代码也可以参与：给出源码位置、最小输入构想、预期错误与理由，并注明“只读分析，未运行”；不伪造实际输出。选择执行时，在单独副本中只改一个条件，并保留原样结果。可以测试单位或时间错配、未知成本、同一主体收益提高但选择能力下降，或同一个经济后果被同时写进反馈和转换代价。执行者提交输入或最小差异、实际输出和为何有问题；只读者提供推理与位置，不需要运行记录。

程序能拒绝已经披露的重复目标，**不能自行发现所有隐藏的经济重复计入**；直接调用低层 `pareto_frontier` 也不自动获得 `frontier_transition` 的全部检查。指出这些边界内的具体反例有价值，不必包装成全新发现。

## 4. R3｜核对一条证据或一个遗漏主体

选择[英文十六行摘译](gc_t01/KNOWN_UNKNOWN_CONDITIONAL_MATRIX_EN_V0_1.md)或中文矩阵的一条 K/C/U 记录，无需执行代码，给出原件版本、页码或表号、研究时期与适用人群。检查是否混用了统计与估计、不同研究版本、不能相加的分量，或把来源不足写成已知。

也可以提出一个非敏感现实问题，注明受影响主体、具体能力、退出或恢复通道与时间窗口。昂贵、缓慢不自动等于永久关闭；通道存在也不自动证明它对该主体有效。本轮不承诺完整个案建模或现实方案服务。

R0 可按约 5 分钟、R1 可按 10–15 分钟、R2 按 20–40 分钟、R3 按 15–30 分钟规划投入；这些是估计，不是已经测得的完成时间。

## 5. 反馈可以只写一句

> 模型遗漏了____，可能导致____，可用____检查。

运行类再附：提交号、系统/Python、命令、是否修改输入、预期与实际差异、最小日志。证据类再附：矩阵行号、来源版本和准确位置。请注明是否使用 AI、是否参与过实现，不要求透露个人身份或机构。

在 [Issue #49](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/49) 评论即可；较完整结果也可另开 issue 并链接回来。不能使用 GitHub 时，把这句话回给邀请发送者；转入公开记录须先取得你的同意。

不要提交凭证、个人资料、保密合同、内部订单或安全敏感操作细节。GitHub 评论本身公开；在其它材料中署名或转载须另获同意。不预先承诺论文署名、经费、合作机会或处理时限。反馈经核对后可记为复现、失败复现、证据更正、表示缺口、待补证或附理由的不采纳；未经核对的提交仍只是报告。

## 6. 这次公开了什么，尚未证明什么

公开的是固定研究代码的复算入口和证据检查任务，不是独立外部验证已经发生。维护者/AI 复跑、仓库 CI、外部独立复算、真实使用、有效改进分别留痕。样例中的两个 false 描述其来源，外部运行者不应自行改成 true；外部参与身份和证据在独立反馈中记录。

```text
empirical_frontier = NOT_CALIBRATED
independent_validation = false
external_evidence_state_changed = false
policy_recommendation = false
```

未列出的成本不等于零；完整成本覆盖、全局稳健性、论文结构模型复现及现实通道恢复均未由这个样例证明。本入口不输出中美政策推荐、国家总分或现实 S0–S3 排序。无需认同文明跃迁理论即可参与。

## English entry

**See who gains, who bears costs, and which assumptions change the result.**

This Round 1 challenge connects a source-linked evidence matrix with one executable, entirely synthetic cost-accounting example. It does not ask you to endorse a U.S.–China policy or CCM. The candidate code was unmerged when this entry was created; use the full pinned commit above, not default `main`.

**R0: read only.** No clone, installation or execution is needed. Read the pinned example and the English accounting summary above; identify one omitted or double-counted consequence.

**R1: reproduce.** Follow the commands in section 2 (Python 3.11–3.13; standard library). Report the unchanged output or failure. The three declared burdens are 2, 4 and UNKNOWN. Expected conditional frontiers are `[B]`, `[A,B]`, and no determinate frontier, respectively. A/B are mathematical fixtures, not political options.

**R2: challenge, with or without execution.** A static code-location / proposed-input counterexample is sufficient when marked “not run.” If executing, preserve the baseline, then supply one minimal changed input or diff and the actual trace. Test a wrong unit/horizon, unknown burden, within-actor trade-off, or hidden double counting between feedback and transition costs. The cost-aware entry point does not automatically fix lower-level callers or establish complete economic coverage.

**R3: check evidence, no code required.** Pick one of the sixteen K/C/U rows in the [English evidence excerpt](gc_t01/KNOWN_UNKNOWN_CONDITIONAL_MATRIX_EN_V0_1.md), with direct primary-source links, or name one missing actor and a concrete exit/recovery capability. Provide the source version, page/table, time period and population. Expensive restoration is not itself proof of irreversible closure. The matrix's section 5 is a pre-repair capability snapshot; the separate cost-accounting note describes this pinned implementation.

Effort estimates are R0 about 5, R1 10–15, R2 20–40 and R3 15–30 minutes, not measured guarantees. A single sentence is useful: **“The model omits ___; this could cause ___; it could be checked with ___.”**

**Private reply to the invitation sender / axdwzx@gmail.com, or [public Issue #49](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/49).** Private feedback is equally eligible for review; public release requires consent. For a run, add commit, OS/Python, command, input/diff and observed output; disclose AI assistance and implementation involvement without needing personal identity. Without GitHub, reply to the invitation sender; public relay requires consent. Do not disclose private contracts, credentials, personal data or security-sensitive details. Attribution outside your comment requires consent; no authorship, funding or response-time promise is made.

A CI pass is not independent validation. Keep the fixture's origin fields unchanged and report external participation separately. Empirical frontier: NOT_CALIBRATED; total cost coverage and global robustness: not established. No policy recommendation follows.

续读 / Further reading：[证据矩阵](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/blob/c822d1729bf4d4ed5a4c6c0f518c255c36cbf0ca/cases/real_gc_01/gc_t01/KNOWN_UNKNOWN_CONDITIONAL_MATRIX_V0_1.md) · [CCM 仓库](https://github.com/Civilization-Leap/computable-cooperation-mechanisms) · [文明跃迁网站](https://www.civitas.top/)


## 维护者入口校验 / Maintainer entry check

`python scripts/check_real_gc_01_entry.py --check-only` 检查本入口命令、固定提交和英文行号绑定；加 `--run` 后，另建临时目录，逐字执行上方 clone/checkout 与三条 Python 命令，并检查 JSON、20 项非空测试和固定 Git 对象。CI 使用同一脚本在 Linux/Bash 与 Windows/cmd 执行，日志是否成功以对应提交的实际 run 为准。此检查不同于语料版本检查 `corpus_lint`，也不证明现实研究成立。

上述维护者脚本不在固定旧代码提交中；须从本入口所属的新提交调用。参与者只需三条 Python 命令，或选择 R0/R3 完全不执行。旧入口 V0.1 是前序受控版本，既有固定链接保留；[Issue #49](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/49) 指向现行入口。
