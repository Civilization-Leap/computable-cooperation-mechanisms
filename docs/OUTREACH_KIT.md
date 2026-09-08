# Global Outreach Kit

This file is a reusable, low-maintenance dissemination kit for the project. The canonical destination is always the GitHub repository and its tagged releases.

## Core message

Human societies constantly compete, cooperate, form alliances, blocs, and communities. But how many of the mechanisms behind those relationships are explicit enough to inspect, recompute, falsify, and improve?

**Computable Competition–Cooperation Mechanisms** is a deliberately small open-source starting point. It turns declared actors, resources, outcomes, constraints, and unknowns into a deterministic, inspectable computation. It does not assume cooperation is always better, collapse everything into a universal fairness score, or claim to predict human behavior.

The first release, `v0.1.0`, includes strict JSON validation, baseline/candidate comparisons, independent hard-constraint checks, explicit `UNKNOWN` handling, four synthetic teaching cases, and automated tests across Python 3.11–3.13.

The project is Apache-2.0 licensed. Independent research, forks, alternative formalizations, and commercial downstream development are welcome. Downstream products remain responsible for their own claims, validation, deployment, and consequences.

We are not asking people to endorse the framework. We are looking for strong counterexamples, missing variables, alternative representations, independent implementations, and real coordination problems that the current model cannot represent.

Repository: https://github.com/Civilization-Leap/computable-cooperation-mechanisms

## Result-led developer entry

Lead with the [threshold-sensitivity experiment](THRESHOLD_SENSITIVITY.md): all three outcome deltas stay fixed while changing only the declared ceiling flips the hard-check result. That page contains English/Chinese copy and complete report comparison images. The status, input hash, and check reason change; do not claim the reports differ only in status or that C was proven to have been excluded from rule-setting. These texts are reusable on channels that permit assisted writing. The [original teaching-case comparison](SHARED_EQUIPMENT_COMPARISON.md) remains available as a separate experiment that changes C's loss instead of the threshold. Link directly to the [five-minute walkthrough](FIVE_MINUTE_WALKTHROUGH.md).

The result is a synthetic demonstration of chosen semantics. Do not describe it as a new empirical finding, a prediction of the benefits of cooperation, or a comparison with a competing solver that was never run.

## Show HN preparation notes — author-written submission required

Checked 2026-09-08: the [HN guidelines](https://news.ycombinator.com/newsguidelines.html) prohibit generated or AI-edited text in comments. The [Show HN guidelines](https://news.ycombinator.com/showhn.html) call for something people can try, a creator available to discuss it, and easy access without signup. This section is technical preparation, not a ready-to-post HN submission or comment script. The person posting should write the title, introduction, and replies independently in their own words.

Title direction: identify the runnable constraint checker and the concrete question it exposes—whether the parties' gains hide a third-party cost. Keep the required `Show HN:` prefix. Put the specific invitation to challenge the representation in the author's explanation; avoid a combative or clickbait title.

Useful facts for the author's own account:

- Python standard-library implementation; Git + Python 3.11–3.13 needed; no model or API required.
- Four variants of one synthetic domain, not four validated application domains.
- In the threshold sweep, all A/B/C outcomes stay fixed; only the declared ceiling changes. The separate original pair changes C's loss instead.
- The record does not establish who selected the threshold or whether C participated.
- A missing affected actor or omitted protection will not be discovered automatically.
- Unknown values remain explicit; this is not probabilistic uncertainty calibration.
- The program neither searches for a deal nor predicts negotiation behavior.
- [Issue #5](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/5) invites representational counterexamples; [Issue #8](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/issues/8) invites independent implementations.

A two-hour availability window after posting is a practical suggestion, not a proven response-rate rule or a promise of live monitoring. Afterward, answer substantive reproducible reports when feasible; there is no need to maintain a daily promotional schedule. Do not solicit votes or coordinated comments. No HN post or monitoring task has been created by preparing these notes.

## Researcher outreach

Choose a person and one paper before composing a message. [Five paper-specific conversation candidates](RESEARCH_DIALOGUES.md) replace institution inboxes as the starting point. Their methodological differences are invitations to compare scope, not claims that this project solves those papers' limitations.

The following common description is supporting material, not a complete personalized message:

**Subject:** Open computational starting point for competition/cooperation mechanisms — counterexamples welcome

We have released a small Apache-2.0 reference implementation for making declared multi-actor mechanism conditions inspectable and recomputable.

The current implementation is intentionally limited: it separates actors/dimensions/units, compares declared baseline and candidate arrangements, checks hard constraints independently, and preserves explicit unknowns. It does not claim a universal fairness metric, behavioral prediction, or real-world validity.

We are not asking you to endorse the framework. We would value strong counterexamples, alternative formalizations, or examples from your field that the current representation cannot capture.

Repository: https://github.com/Civilization-Leap/computable-cooperation-mechanisms

## Domain-builder draft

**Challenge:** bring a coordination problem this model cannot represent.

The project is a minimal open-source reference for expressing actors, resources, outcomes, constraints, and unknowns, then recomputing what changes under an alternative arrangement.

If you work in civic tech, supply chains, negotiation systems, cooperative platforms, AI governance, labor, public-resource allocation, or institutional design, try mapping a synthetic version of a problem from your field. If the schema fails, that failure is useful evidence: open an issue describing what cannot be represented.

Repository: https://github.com/Civilization-Leap/computable-cooperation-mechanisms

## Suggested one-line descriptions

- **Developer:** A tiny deterministic reference implementation for inspectable multi-actor mechanism conditions—fork it, break it, or replace it.
- **Research:** An open computational object for testing representations of competition/cooperation mechanisms, with explicit unknowns and no universal fairness score.
- **Domain use:** A starting point for asking whether a coordination problem can be expressed as actors, constraints, burdens, outcomes, and unknowns before claiming a solution.

## Dissemination discipline

1. Link to the canonical repository or a tagged release rather than copying code into platform-specific posts.
2. Prefer invitations to falsify, extend, or independently implement over requests for endorsement.
3. Do not claim fairness certification, research validation, behavioral prediction, policy approval, or real-world authorization.
4. Do not publish controlled research fixtures or restricted materials as outreach examples.
5. Treat forks and independent downstream implementations as successful diffusion even when they do not contribute back upstream.
6. Do not create a standing obligation to post frequently or operate a community service.

## Repository discovery and citation

[Metadata settings and archive verification](DISCOVERY_SETTINGS.md) record the proposed topics, social preview asset, and verified v0.1.0 archive. Cite [10.5281/zenodo.22656544](https://doi.org/10.5281/zenodo.22656544) for that exact release. The [concept DOI](https://doi.org/10.5281/zenodo.22656543) represents all versions. The code repository backlink is present on Zenodo; the GitHub backlink is included in this candidate branch. The corrected version and creator metadata are verified in the [archive record](ZENODO_ARCHIVE.md). A committed image is still not an installed GitHub social preview, and the v0.1.0 archive does not include later candidate features.
