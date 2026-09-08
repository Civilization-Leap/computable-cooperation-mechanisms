# v0.1.0 Zenodo archive verification

Verified 2026-09-08 against the public Zenodo record, DataCite registry, the downloaded archive, and the GitHub annotated tag.

| Item | Verified value |
|---|---|
| Record | https://zenodo.org/records/22656544 |
| Version DOI | https://doi.org/10.5281/zenodo.22656544 |
| Concept DOI (all versions) | https://doi.org/10.5281/zenodo.22656543 |
| Publication state | Zenodo `published`; DataCite `findable`, active |
| Title | Computable Competition–Cooperation Mechanisms: Minimal Open Reference Implementation |
| Resource type / license | Software / Apache-2.0 |
| Uploaded archive | `computable-cooperation-mechanisms-0.1.0.zip` |
| Archive size | 49,027 bytes |
| Archive MD5 | `a530230bfa782128c689c711a5062fea` |
| Archive SHA-256 | `ea54358e0a3fa5fd479914e3a0d872def1d9a6a3777fc3d1bd22cd1833612a37` |
| Release tag | `v0.1.0` |
| Annotated tag object | `0960d01d73c73a6ad66644341e70a8cf8b10dd15` |
| Peeled release commit | `a811eccf0eae8c5120c6be1d5ac4b11c8319d377` |
| File comparison | 34 matches; 0 mismatches; 0 missing; 0 extra |

The comparison strips only the ZIP's outer repository directory, compares the complete file inventory, and compares every file's bytes with `git show v0.1.0:<path>`. Matching the archive filename alone was not treated as sufficient evidence. [Machine-readable verification](evidence/zenodo-22656544-verification.json).

The release's original publication date in CITATION.cff is 2026-09-06. The Zenodo archive was published on 2026-09-08. These describe different publication events.

## Metadata corrections completed

The record owner corrected and republished the metadata. The published Zenodo API was rechecked after the user's completion message; record modification time is `2026-09-08T08:54:38.585383+00:00`.

| Field | Previous value (history only) | Verified published value |
|---|---|---|
| Version | `0.10` | `0.1.0` |
| Creator | `zijinfu` | `Zijunfu` |

DataCite also confirms version `0.1.0`, creator `Zijunfu`, and state `findable` (updated `2026-09-08T08:54:39.000Z`).

The DOI, archive filename, size (49,027 bytes), and checksum are unchanged. The earlier 34-file byte comparison therefore remains the archive-content evidence. CITATION.cff agrees with the corrected canonical author/version. The owner performed the edit; this task verified it and closed the pending documentation item.

中文：两项更正已生效。Zenodo 公开记录显示版本 `0.1.0`、署名 `Zijunfu`；原 DOI 与归档文件保持不变。元数据更正待办已关闭。

## Citation scope and bidirectional links

Use version DOI `10.5281/zenodo.22656544` when citing the archived v0.1.0 implementation. Use concept DOI `10.5281/zenodo.22656543` when referencing the evolving release family. The concept DOI was read from the record's `conceptdoi` and confirmed by DataCite's IsVersionOf relation; it was not inferred from adjacent record numbers.

Zenodo's software repository field (`code:codeRepository`) already links to `https://github.com/Civilization-Leap/computable-cooperation-mechanisms`. Both READMEs and CITATION.cff in this candidate branch now link to the archive. Those GitHub changes become the default-branch entry only after the PR is merged.

The DOI does not archive PR #9's later additions: the five-limit sweep script, optional CLI exit gates, updated READMEs, or dissemination images. Refer to their actual branch/commit until a later release is archived. The frozen v0.1.0 tag was not moved.

## Sources

- [Zenodo API record](https://zenodo.org/api/records/22656544)
- [DataCite DOI registration](https://api.datacite.org/dois/10.5281/zenodo.22656544)
- [GitHub tag reference](https://api.github.com/repos/Civilization-Leap/computable-cooperation-mechanisms/git/ref/tags/v0.1.0)
- [GitHub annotated tag object](https://api.github.com/repos/Civilization-Leap/computable-cooperation-mechanisms/git/tags/0960d01d73c73a6ad66644341e70a8cf8b10dd15)
