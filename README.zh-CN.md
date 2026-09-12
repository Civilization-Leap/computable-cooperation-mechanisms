# 竞争—合作可计算机制
## 最小开源参考实现

**当前发布目标：v0.1.1。只有固定 tag 与 GitHub Release 实际形成后，才视为正式发布。采用 Apache-2.0。**

**处境未变，判定翻转。** A、B 各节省 3 CU，C 损失 0.5 TU。只把 C 的损失上限从 0.5 调到 0.49，结果便由 `SATISFIED` 变为 `VIOLATED`，所有主体差值保持相同。计算可以准确执行一条保护线，却不能因此证明这条线画得正当。[阈值扫描、完整报告对照与中英文短稿](docs/THRESHOLD_SENSITIVITY.md)。

人类社会每天都在竞争、合作、结盟、形成阵营与共同体。**这些关系背后的机制，有多少能够被明确表达、检查、复算、证伪和改进？**

这是一个面向全球后续开发者的、刻意保持小型的可运行起点：给定主体、资源、结果和明确约束，计算候选安排相对基线的分项变化，并报告已声明约束是满足、违反还是信息不足。

本项目**不预设合作总是更优，不认证公平，不推断动机，不预测行为，不生成研究 H/T/L/RUN 状态，也不产生现实授权。**

关于项目目的、目标、方法、应用方式、范围、全球参与、商业独立关系与维护边界，详见：[中文项目总览](docs/PROJECT_OVERVIEW.zh-CN.md) · [Project Overview](docs/PROJECT_OVERVIEW.md)

## 五分钟试运行

以下下载方式需要 Git，运行需要 Python 3.11–3.13；计算器和测试都只使用 Python 标准库。**在解压后的仓库目录中运行，无需 `pip install`，也无需 `pip install -e .`。** v0.1.1 正式发布后，可从固定版本开始：

```bash
git clone --branch v0.1.1 --depth 1 https://github.com/Civilization-Leap/computable-cooperation-mechanisms.git
cd computable-cooperation-mechanisms
python -m mechanism_ref examples/shared_equipment_third_party_violation.json --out-dir outputs
python -m mechanism_ref examples/shared_equipment_unknown.json --out-dir outputs
python -m mechanism_ref examples/shared_equipment_ok.json --out-dir outputs
python -m unittest discover -s tests -v
```

依次输出 `VIOLATED`、`UNKNOWN`、`SATISFIED`。第一份报告同时显示：A/B 各节省 3 CU，但 C 损失 2 TU，超过已声明的 1 TU 上限。打开 `outputs/shared_equipment_third_party_violation.report.md` 即可查看。

做一次具体修改：复制满足约束的示例，把 ID 为 `THIRD-PARTY` 的约束从 `limit: 1` 调低为 `limit: 0.25`，保留 C 的损失 `0.5`。结果就会变成 `VIOLATED`，A/B 的节省保持相同。[精确复制修改命令、报告位置与全部四例](docs/FIVE_MINUTE_WALKTHROUGH.md)。取得源码后，运行无需账号、API 密钥、模型下载或托管服务。

完整当前复现路径可直接运行 `python scripts/reproduce_offline.py`。v0.1.1 发布工作流还会附加精确提交的离线源码归档及 SHA-256 校验文件。

历史 [v0.1.0 Release](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/releases/tag/v0.1.0) 与[源码 tag](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/tree/v0.1.0)继续冻结保留；v0.1.1 的固定入口以发布工作流实际完成为准。

## 独立第三方测试

**复现它、击破它或独立重写它；不要求背书。** 可选择 5–15 分钟冻结版本复现、固定开发挑战、独立实现，或 10–30 分钟不写代码的方法审阅。详见[第三方测试指南](docs/THIRD_PARTY_TESTING.md)，结果可回传至 [Issue #14](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/14)。复现失败、不兼容与反例同样是有效结果。

## 双方都获益，谁还在付出代价？

在共享设备的两份教学输入中，A、B 的成本都从 8 降至 5 CU，节省完全相同。但 C 的预留时段损失从 0.5 变为 2 TU，越过已声明的 1 TU 上限，结果便从 `SATISFIED` 变为 `VIOLATED`。相同的双方收益，可以伴随不同的约束结果。

这是**合成输入下对已声明规则的可复算演示**，不是真实收益测量或新的实证发现。[查看对照与边界](docs/SHARED_EQUIPMENT_COMPARISON.md)，或[指出当前表示无法表达的问题](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/5)。

## 独立实现挑战｜Independent Implementation Challenge

**用另一种语言复现公开语义，欢迎建立独立仓库。** 从 [Issue #8](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/8) 开始。

对熟悉所选语言和 JSON 工具的开发者，最小四例语义实现可先按 **8–16 小时**安排；包含非法输入检查、差异说明与可复现命令的版本，可按**合计 16–32 小时**安排。这是尚未经参与者实测的规划估计；与 Python 完全一致的输入哈希可能需要额外工作。

范围包括解析、校验、可比差值、独立硬约束检查、未知保留与确定性输出。[工作量拆分、预期结果和提交格式](docs/INDEPENDENT_IMPLEMENTATION.md)。提供仓库链接与发现的差异即可，不要求合并回上游或承担持续服务。

## 请尝试击破、扩展或独立重写它

我们不要求参与者先认同这套框架。以下都属于有价值的贡献：

- 找到一个当前表示方式无法表达的纯合成协调问题；
- 提出能够击中当前建模假设的强反例；
- 新增一个无需场景特判的同类示例；
- 提出更好的显式不确定性表示；
- 用另一种编程语言独立实现；
- 在其他领域建立完全独立的 fork 或下游项目。

可以从公开的 [贡献与研究挑战](../../issues) 开始，特别是标记为 `good first issue` 或 `help wanted` 的任务。即使独立 fork 或下游实现永远不合并回主仓库，也视为项目扩散成功。

## 当前已实现的方法纪律

- 主体、维度、单位分列，不生成“公平总分”；
- 只对主体＋维度＋单位一致的基线／候选结果计算差值；
- 硬约束独立检查，普通收益不能抵销第三方硬约束；
- 明确 `UNKNOWN` 不补零；
- 非法引用、未声明单位等输入错误直接拒绝，不伪装成 `UNKNOWN`；
- 未支持的顶层字段直接拒绝：添加 `id` 会报 `unsupported fields: ['id']`；案例标识字段应为 `case_id`；
- 计算具确定性，并验证不会修改原始输入；
- 输出包含输入复算哈希和解释边界。

## 四个原创教学变体

1. `shared_equipment_ok.json`：已声明约束满足；
2. `shared_equipment_third_party_violation.json`：A/B 普通成本下降，但 C 的保护门被违反；
3. `shared_equipment_unknown.json`：当前资源被明确标记为未知，因此相应硬检查保持 `UNKNOWN`；
4. `shared_equipment_capacity_violation.json`：同类场景扩展，仅通过更换输入触发资源容量违反，不在内核中写场景特判。

## 可选 CI 门禁

默认退出码 0 表示报告生成成功，包括违反和未知结果。v0.1.1 中，`--fail-on-violation` 在总体硬约束违反时返回 1；`--fail-on-unknown` 在总体未知时返回 3。CI 若要求只有 SATISFIED 才继续，应**同时使用两项**。有效输入先写完报告再返回门禁退出码；输入错误仍返回 2。[退出码表与命令](docs/CLI_EXIT_CODES.md)。历史 v0.1.0 tag 不含这两项参数。

## 验证

冻结的 v0.1.0 含原始 12 项测试；v0.1.1 共 18 项，即原始 12 项、5 项 CLI 子进程测试及 1 项阈值扫描测试。CI 在 Python 3.11、3.12、3.13 上运行测试，把 `ResourceWarning` 当作错误，实际运行四个教学变体，并执行离线复现路径。正式发布工作流会在创建版本标签和 GitHub Release 之前，再对精确发布提交执行一次验证。

用户此前报告已在 **Python 3.12.3** 独立复现冻结的 v0.1.0 材料：13 个原始源码／元数据文件哈希一致、原始 12 项测试在 ResourceWarning 作为错误时通过、四例通过且无需 pip。这里不把该证据静默升级为 v0.1.1 的独立验证。[证据记录与范围](docs/THRESHOLD_SENSITIVITY.md#reproduction-provenance)。

## 范围边界

本实现是教学／参考实现，不是正式 R1 B2B 盲测夹具，也不是 WP-01-A 或更大研究体系的完整软件化。正式与受控研究材料继续保持隔离。竞争、合作、联盟、阵营、共同体也不被编码为单向价值阶梯。

软件检查的是**已声明输入与已声明约束**。它不证明输入事实真实，不证明机制公平或正当，也不证明现实部署安全或已经获得授权。

## 二次开发

可以按同一 JSON 合同新增同类场景。新增约束语义必须显式修改代码、测试和文档，不允许静默解释。独立团队可依据 Apache-2.0 分叉与扩展本项目，不需要依赖一个中心持续运营的服务。

详见 [CONTRIBUTING.md](CONTRIBUTING.md)、[全球传播复用包](docs/OUTREACH_KIT.md)、[发布就绪检查表](docs/RELEASE_CHECKLIST.md) 与 [v0.1.1 发布说明](docs/RELEASE_NOTES_v0.1.1.md)。

## 引用已归档版本

冻结的 **v0.1.0 归档**版本 DOI 为 [10.5281/zenodo.22656544](https://doi.org/10.5281/zenodo.22656544)；[全版本 DOI](https://doi.org/10.5281/zenodo.22656543) 对应整个版本族。它们不是 v0.1.1 的版本 DOI。若建立 v0.1.1 独立归档，应在归档核验后另行登记其版本 DOI。

归档的 34 个文件与 v0.1.0 标签内容逐字节一致。Zenodo 的版本 `0.1.0`、署名 `Zijunfu` 均已核验正确。[归档核验及元数据更正记录](docs/ZENODO_ARCHIVE.md)。

仓库中的 [`CITATION.cff`](CITATION.cff) 在新的归档版本完成绑定前，继续指向已经核验的 v0.1.0 归档。

## 许可证与商业使用

本仓库统一采用 **Apache License, Version 2.0**。除非具体文件另有说明，本仓库原创代码、文档、合成教学示例、测试和实施支持文件均受该许可证覆盖。详见 [`LICENSE`](LICENSE) 与 [`LICENSE_SCOPE.md`](LICENSE_SCOPE.md)。

Apache-2.0 允许商业和独立下游开发。下游产品或服务应当独立承担其宣传、数据、验证、安全、部署、支持、法律义务和现实后果责任。

使用本项目不意味着获得项目背书、公平认证、研究有效性认定或现实授权。未进入本仓库的研究母稿、受控研究夹具、受限材料和其他资产，不因本仓库采用 Apache-2.0 而自动获得许可。

## 维护方式

本仓库是开放研究起点，不是持续托管服务、无限技术支持、固定路线图或长期兼容承诺。下游服务主体可以独立作出自己的服务承诺。
