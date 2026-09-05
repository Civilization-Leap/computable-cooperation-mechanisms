# Project Overview

## In one sentence

**We want to move the question of how people compete, cooperate, and build larger forms of coordination from something judged mainly by position, intuition, or slogans toward something whose conditions can be stated clearly, whose costs can be seen, whose alternatives can be compared, whose failures can be found, and whose mechanisms can be improved.**

That is also the shared task of participants in this project. The aim is not to prove that one form of cooperation is always right. It is to jointly discover, test, criticize, and improve interaction mechanisms that can help more actors pursue their real interests while reducing avoidable harm, domination, escalation, and cost-shifting to third parties.

## Shared purpose

Individuals, firms, institutions, states, and communities all have their own interests, capabilities, constraints, information, and risks. Competition will not disappear, and self-interest cannot be removed by moral instruction. But different rules of interaction can lead the same actors toward very different outcomes:

- some competition improves efficiency and innovation;
- some competition escalates until all sides bear larger losses;
- some cooperation works only by shifting costs to weaker or third parties;
- some cooperation creates durable mutual gains without requiring participants to become selfless first;
- some alliances, blocs, and communities expand coordination capacity while also creating new exclusion, dependency, or systemic risk.

The shared purpose of this project is to **make the mechanisms behind these differences as explicit, inspectable, and recomputable as possible, so people can see earlier what conditions improve a relationship, who actually benefits, who bears the burden, which boundaries ordinary gains cannot override, what remains unknown, and under what conditions an apparent improvement fails.**

If these questions can be expressed and tested more clearly, people have a better chance of finding ways to pursue their interests that are preferable to unbounded confrontation, one-sided domination, or hidden cost transfer.

## Shared goals for participants

Participation does not require prior acceptance of a complete theory. Researchers, developers, domain experts, institutions, and independent teams can all work toward the following shared goals:

1. **Make mechanisms explicit.** Separate actors, interests, capabilities, resources, time conditions, constraints, third-party effects, and unknowns from vague narrative claims.
2. **See the whole result.** Do not ask only whether the aggregate result looks better; ask who improves, who loses, who is omitted, and which hard boundaries are crossed.
3. **Compare alternatives.** Evaluate different interaction rules under the same declared conditions instead of presenting only one preferred outcome.
4. **Search for failure conditions.** Find counterexamples, hidden burdens, unreachable states, boundary cases, and reversal conditions rather than collecting only supportive examples.
5. **Make judgments recomputable and challengeable.** Wherever possible, let others independently inspect and repeat results from public inputs, rules, and code.
6. **Enable continued development.** Keep methods, examples, and code open enough for independent teams to improve, replace, fork, or apply them in their own domains.
7. **Do not turn a research tool into real-world authority.** Software outputs do not automatically become fairness certification, policy decisions, legal conclusions, permissions, prohibitions, or scores of people.

For that reason, a participant does not contribute only by “proving the project right.” **Showing that a mechanism fails, identifying an important reality the current model cannot represent, proposing a better formalization, or building a better independent implementation are equally valid ways of advancing the project.**

## Core research question

Given actors with different interests, capabilities, information, time horizons, dependencies, and exit options, what changes when the rules of interaction change? Which effects are beneficial, which burdens are transferred, which hard constraints are crossed, what remains unknown, and under what conditions does a claimed improvement fail?

## Current software objective

The current software is only one small building block within that wider research purpose. It does not try to solve the full problem. It first makes a limited subset machine-checkable:

- represent actors, baseline arrangements, candidate arrangements, outcomes, resources, and explicit constraints;
- compare like-for-like outcome dimensions without collapsing them into a universal fairness score;
- keep ordinary gains separate from hard constraints and third-party protections;
- preserve explicit `UNKNOWN` rather than silently filling missing facts with optimistic assumptions or zero;
- make input errors distinguishable from legitimate unknowns;
- produce deterministic, inspectable outputs that can be independently recomputed;
- provide a minimal extension path for new scenarios and future mechanism modules.

## Method

The current software follows five methodological rules.

1. **Declare before computing.** The program evaluates stated actors, values, units, resources, and constraints. It does not infer hidden motives, true preferences, legal rights, or social facts.
2. **Keep dimensions separate.** Outcomes are compared only when actor, dimension, and unit match. The implementation does not generate a universal fairness, welfare, cooperation, or civilization score.
3. **Hard constraints do not disappear inside averages.** Ordinary gains cannot automatically compensate for a violated hard constraint or an explicitly protected third-party burden.
4. **Unknown is a valid result.** A legal input with a critical value explicitly unknown yields `UNKNOWN`; an invalid reference or undeclared unit is rejected instead of being disguised as uncertainty.
5. **Recomputation is part of the result.** The same valid input and software version should produce the same core result, and the input is hashed for reproducibility.

## How to use it

The current reference implementation is intended for:

- teaching and demonstration;
- synthetic mechanism experiments;
- reproducible research prototypes;
- software extension by independent teams;
- comparison of alternative explicit rule sets;
- development of domain-specific tools that perform their own validation and governance.

A typical workflow is:

`describe case -> declare baseline and candidate -> declare constraints -> run evaluator -> inspect SATISFIED / VIOLATED / UNKNOWN -> change assumptions -> recompute`

## Scope

### In scope now

The current release supports a small local Python/JSON workflow for synthetic cases, deterministic comparison, hard-constraint checks, explicit unknowns, machine-readable JSON output, human-readable Markdown reports, and automated tests.

### Research directions, not current software claims

The wider research program may later examine bargaining, supply chains, labor arrangements, platform governance, public projects, alliances, blocs, communities, public goods, capability development, externalities, correction, exit, and other multi-actor mechanisms.

Those domains do not share one universal institutional design. A successful synthetic example in this repository does not validate a real-world mechanism or justify cross-domain generalization.

### Explicitly out of scope for this reference implementation

This repository does not provide:

- fairness certification;
- legal, policy, investment, employment, negotiation, or public-authority decisions;
- behavioral or motive prediction;
- personality, loyalty, cooperation, ideology, or reputation scoring;
- automatic optimal-policy search;
- a universal bargaining or governance system;
- real-world authorization, enforcement, arbitration, or representation;
- guarantees that a declared input is true, complete, legitimate, or ethically acceptable.

Formal research manuscripts, controlled blind fixtures, restricted research materials, personal data, and other assets not included in this repository remain outside the repository license and software scope.

## Commercial and independent downstream development

Commercial use is permitted under Apache-2.0. Independent teams may build products, services, private extensions, research tools, hosted systems, integrations, or domain-specific implementations, subject to the license terms.

The public research project and any downstream commercial implementation are separate responsibilities. A downstream team is responsible for its own claims, data, validation, security, legal compliance, deployment, customer support, and real-world consequences.

Using this repository does not imply endorsement by the project, fairness certification, validation of a downstream mechanism, or authorization to act on behalf of any person or institution.

## Global participation model

The project is designed to be forkable rather than centrally dependent. Contributors do not need to accept every theoretical proposition before testing or extending the software.

Useful contributions include:

- counterexamples and failure cases;
- stricter validators;
- clearer schemas and documentation;
- reproducibility improvements;
- new synthetic examples;
- alternative mechanism modules;
- domain-specific implementations kept clearly separate from universal claims;
- translations and accessibility improvements.

The maintainers may accept, reject, or defer contributions to the canonical repository, but downstream work does not require central approval where Apache-2.0 permits independent use.

## Maintenance boundary

This project is an open research starting point, not a promise of continuous hosted service or unlimited maintainer support. No uptime, response-time, roadmap, compatibility, or customization commitment is implied unless separately agreed by a responsible downstream provider.

## License

Unless a file states otherwise, repository code, documentation, original synthetic teaching examples, tests, and repository support files authored for this project are licensed under the Apache License, Version 2.0. See [`../LICENSE`](../LICENSE) and [`../LICENSE_SCOPE.md`](../LICENSE_SCOPE.md).
