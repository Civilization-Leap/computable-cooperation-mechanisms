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

Verified: the public GitHub release is [`v0.1.0`](https://github.com/Civilization-Leap/computable-cooperation-mechanisms/releases/tag/v0.1.0), commit `0960d01d73c73a6ad66644341e70a8cf8b10dd15`. Current README and `CITATION.cff` have no Zenodo DOI. No matching Zenodo record was verified from the sources available in this task. That is not proof that no record exists.

Once the existing record is identified, compare its title, creator, version, uploaded archive, and repository relationship. Then:

1. On GitHub, add the verified record/DOI link in both READMEs and citation metadata, clearly distinguishing the archived release from changing main-branch documentation.
2. On Zenodo, add the repository URL and exact tagged release as related software/source links, choosing the relation that matches the actual archived object. If the record archives the theoretical manuscript instead of this software, link it as related research and do not assign its DOI to the software's `CITATION.cff`.
3. If distinct concept and version DOIs exist, label the former as all versions and use the correct version DOI when citing a particular release.

Do not invent a DOI, silently create a duplicate record, or move the frozen release tag to include documentation updates.

## Status at preparation

The browser was signed out of GitHub; topics and custom-preview installation are pending authenticated settings access. The existing DOI/record identity is also pending verification. These account-level settings are not completed by this documentation change. Email and HN publication remain unsent.
