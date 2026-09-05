# Project Overview

## Purpose

This project explores how multi-actor competition, cooperation, alliance, bloc, and community relationships can be expressed as explicit, inspectable, and recomputable mechanisms rather than treated only as narrative claims or opaque judgments.

The immediate goal is deliberately modest: provide a small open reference implementation that lowers the cost for researchers, developers, institutions, and independent teams to test, criticize, replace, and extend mechanism ideas.

The project does **not** assume that cooperation is always preferable, that agreement proves fairness, or that a computable result is automatically legitimate. Failure, conflict, hard constraints, third-party burdens, and insufficient information are first-class outcomes.

## Core research question

Given actors with different interests, capabilities, information, time horizons, dependencies, and exit options, what changes when the rules of interaction change? Which effects are beneficial, which burdens are transferred, which hard constraints are crossed, what remains unknown, and under what conditions does a claimed improvement fail?

## Objectives

The reference implementation aims to make a limited subset of these questions machine-checkable:

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

The current release candidate supports a small local Python/JSON workflow for synthetic cases, deterministic comparison, hard-constraint checks, explicit unknowns, machine-readable JSON output, human-readable Markdown reports, and automated tests.

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
