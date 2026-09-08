# Repository discovery settings

Prepared 2026-09-08 for `Civilization-Leap/computable-cooperation-mechanisms`.

## Topics

The GitHub repository API returned `topics: []` at inspection. Proposed set:

```text
mechanism-design
competition
cooperation
automated-negotiation
computational-social-science
multi-agent-systems
constraint-validation
reproducible-research
reference-implementation
python
```

These describe research relevance and the reference implementation. They do not claim that this release includes a multi-agent simulator or negotiation engine. Avoid adding `norm-emergence`, `reinforcement-learning`, or `agi-alignment` as descriptions of implemented capabilities.

GitHub documents topics as a way to discover related repositories. The repository owner/admin can set them through the About gear → Topics → Save changes. Browser editing avoids API-token setup but still requires a signed-in account with repository authority. [Official instructions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics).

## Social preview

Asset: [`assets/social-preview.jpg`](../assets/social-preview.jpg). Headline: **Both sides gain. Who else pays?** This connects the shared-equipment comparison to a question worth inspecting.

The opaque JPEG is 1774 × 887 pixels (2:1), 194,351 bytes. It was created with the built-in image-generation tool, visually checked, and converted from PNG to JPEG for GitHub's under-1-MB limit; the composition and pixel dimensions were retained. GitHub recommends at least 640 × 320, with 1280 × 640 for best display. [Official instructions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview).

Install under repository Settings → General → Social preview → Edit → Upload an image. Merely committing this file does not activate the preview. Platform rendering and cache behavior vary, so do not promise that every shared link will immediately display it or that it increases forwarding by a known amount.

## GitHub ↔ Zenodo

Verified 2026-09-08: [Zenodo record 22656544](https://zenodo.org/records/22656544) is published, its [version DOI](https://doi.org/10.5281/zenodo.22656544) is registered and findable in DataCite, and the [concept DOI](https://doi.org/10.5281/zenodo.22656543) represents all versions.

All 34 files in `computable-cooperation-mechanisms-0.1.0.zip` match GitHub tag `v0.1.0` byte-for-byte. The annotated tag object is `0960d01d73c73a6ad66644341e70a8cf8b10dd15`; it points to release commit `a811eccf0eae8c5120c6be1d5ac4b11c8319d377`. The previously described "commit 0960..." was the annotated tag object, not the peeled commit.

Zenodo's `code:codeRepository` already points to this repository. The reverse link has been added to both READMEs and CITATION.cff in this candidate branch. This DOI identifies the archived release, not unreleased branch additions.

The record owner completed both metadata corrections: version `0.10` → `0.1.0`; creator `zijinfu` → `Zijunfu`. The published Zenodo API now confirms both canonical values. Archive size/checksum and DOI are unchanged. [Verification evidence and correction history](ZENODO_ARCHIVE.md).

## Status at preparation

The browser was signed out of GitHub; topics and custom-preview installation are pending authenticated settings access. The DOI identity and archive contents are now verified; the two Zenodo metadata corrections above are complete and verified. These account-level settings are not completed by this documentation change. Email and HN publication remain unsent.
