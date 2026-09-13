# Start Here｜Theory + Tool + Use Path

This project should not be understood as theory alone or software alone. Its practical unit is:

**Theory → Actor purpose → Problem framing → Candidate arrangements → Computable checks → Human judgment / negotiation / authorization → Real-world action**

## 1. Theory

Read the public idea guide first:

- 中文：[`我们能否学会更好地竞争与合作？`](PUBLIC_IDEA_GUIDE_ZH.md)
- English: [`Can We Learn to Compete and Cooperate Better?`](PUBLIC_IDEA_GUIDE_EN.md)

Core question:

> What does cooperation gain and cost? What does non-cooperation gain and cost? Who benefits, who bears the burden, and who was never at the table?

The theory does not assume cooperation is always better. It asks whether interests, constraints, third-party effects, unknowns, exit conditions, and irreversible consequences can become visible earlier.

## 2. Start from the actor's purpose

The actor defines the goal. The project does not.

Examples:

- Business: profit, cash flow, supply security, control, growth;
- Workers: income, safety, dignity, career continuity, exit rights;
- Platforms: efficiency, ecosystem stability, user/creator sustainability;
- Public institutions: service quality, stability, risk, innovation, resilience;
- AI / AGI governance: capability benefits, safety, competitive position, irreversible-risk reduction;
- International actors: security, deterrence, sovereignty, crisis stability.

## 3. Turn the real problem into a comparable structure

At minimum identify:

1. actors;
2. each actor's objective;
3. current positions;
4. underlying interests and constraints;
5. affected third parties;
6. cooperation candidate;
7. non-cooperation candidate;
8. optional third paths;
9. outcomes and units;
10. hard constraints;
11. unknowns;
12. irreversible consequences.

## 4. Use the reference tool only for the computable part

Current public baseline: `v0.1.1`.

```bash
git clone --branch v0.1.1 --depth 1 https://github.com/Civilization-Leap/computable-cooperation-mechanisms.git
cd computable-cooperation-mechanisms
python scripts/reproduce_offline.py
```

The tool can compare declared outcomes, compute matching deltas, check declared hard constraints, preserve UNKNOWN, and produce deterministic output.

It cannot decide legitimacy, truth, fairness, motives, or authorization.

## 5. Return to judgment and action

After computation, ask:

- Why is this threshold here?
- Who set it?
- Who bears the consequence?
- Does a small parameter change flip the verdict?
- Which unknown should be verified first?
- Can the next step be staged, reversible, and easy to exit?

## 6. Application guides

- 中文：[`如何把竞争—合作可计算机制用于真实问题`](APPLICATION_GUIDE_ZH.md)
- English: [`How to Use Computable Competition–Cooperation Mechanisms on Real Problems`](APPLICATION_GUIDE_EN.md)

These guides show how firms, workers, platforms, public institutions, AI/AGI governance teams, researchers, and international-policy actors can bring their own objectives into the framework.

## 7. Public testing

- [`THIRD_PARTY_TESTING.md`](THIRD_PARTY_TESTING.md)
- Results / counterexamples: GitHub Issue #14

The project asks users to reproduce, break, extend, or independently reimplement the mechanism—not to endorse it.

---

# 中文说明｜理论 + 工具 + 使用路径

这个项目不应被理解为“只有理论”或“只有软件”。真正有现实意义的完整单元是：

**理论 → 主体目的 → 问题定义 → 候选方案 → 可计算核验 → 人的判断 / 谈判 / 授权 → 现实行动**

主体首先明确自己的目的，再把合作、不合作及第三路径同时带入比较；工具只负责对已声明、可计算的部分进行显式化和复算；价值判断、阈值正当性、谈判、授权与行动始终由真实主体承担。

因此，对外介绍这个项目时，应同时给出：

1. 为什么需要更文明地理解竞争与合作；
2. 这个工具目前到底能算什么；
3. 不同主体为了实现自己的目的，应该怎样把真实问题带进来；
4. 计算结果之后，怎样继续谈判、验证、试验、退出或修改路径。

> **理论解释为什么这样看；工具负责把部分结构运行出来；使用方法把两者连接到真实主体的现实目的。**
