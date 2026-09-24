# Knowledge Base

> 2026-09-08 微信范围修正：4篇相关研究文章中3篇已完整入库，仅华泰柏瑞待补全文；3条文末无关推荐已排除。见[相关文章目录](sources/wechat-articles/README.md)及[范围核对](audits/2026-09-08-wechat-scope/README.md)。

提取质量与分析风险：[本次核查、微信Skill测试及更清晰的阅读副本](audits/2026-09-07-extraction-quality/README.md)。

最新来源恢复：[内部浏览器与深搜复核结果](audits/2026-09-07-source-recovery/README.md)。

This folder holds research findings and their evidence. Project scope is
controlled by [the final project plan](../PROJECT_PLAN.md). Execution is tracked
in [the Week 2 plan](../weekly/week-02-plan.md).

## 原始来源与研究分析 / Original sources and analysis

**来源按原语言保存：中文原文保留中文，英文原文保留英文。英文摘要、翻译和研究者分析均不能代替原始来源。**

The [original-source archive](sources/README.md) holds downloaded source files,
original-language text extractions and per-source retrieval metadata. The
[7 September audit and complete change table](audits/2026-09-07-language-audit/changes.md)
records every baseline file and registered source, including unavailable originals.

- `sources/<source_id>/source.pdf` or `source.html`: downloaded original bytes;
  HTTP compression may be decoded by curl. PDFs preserve figures and page layout.
- `original.md`: mechanically extracted original-language text, never a back-translation.
  It may lose layout, images, footnotes or dynamic content; the source file governs.
- `metadata.json`: exact requested/final URLs, retrieval time, SHA-256, extraction
  method, original evidence state, access/quality limits and pending human review.
- `retrieval-response.*`: an error, challenge or wrong-page response, **not** an
  archived original. A failed request does not disprove a prior disclosure.
- Company dossiers, synthesis documents and plans are authored research. Their
  labelled summaries and interpretations are separate from the linked originals.

Source availability and provenance are separate. Archiving a media report or
repost preserves that publication; it does not verify an inaccessible company
original, establish a primary deployment claim, or complete legal-status review.
English originals remain English. Do not manufacture Chinese “originals” by
translating our earlier English notes.

## Phase ownership

| Folder | Phase | Purpose |
|---|---|---|
| companies/ | 1 — Weeks 1–2 | Onshore AI/LLM disclosures, size categories, use cases, partners, and reported outcomes |
| regulation/ | 1 — Weeks 1–2; maintained later | Public regulatory evidence and model risk management questions |
| models/ | 2 — Weeks 3–5 | 5–8-model survey, reusable evaluation framework, one-model GPU proof of concept |
| infrastructure/ | 2 and 3 | Phase 2 reference architecture; Phase 3 three-year on-premise/API TCO |
| pilots/ | 3 — Weeks 6–8 | 3–5 candidates and roadmap with 2–5 concrete proposals |
| templates/ | All | Evidence recording and review |

## Evidence states

- **candidate:** discovered but not checked against the original source.
- **verified-primary:** original primary material was opened and the specific
  claim, identity, date, and location were checked.
- **corroborated:** verified-primary evidence with an additional independent
  supporting source.
- **unresolved:** ambiguous, inaccessible, superseded, or conflicting evidence
  prevents the proposed claim from being verified.

Only verified-primary and corroborated claims may appear as facts in the main
presentation. A primary vendor source supports what the vendor reported; it does
not automatically establish independently measured customer outcomes.

Record who checked the source. Agent inspection and user/manual verification are
separate: use a human-check status and date without implying human review
occurred merely because a link is available.

## Required citation fields

Each source in [source-register.md](source-register.md) needs:

- Stable source ID, exact title, issuer, and source/instrument type.
- Publication date; for rules, effective date and amendment/current status.
- Direct primary URL and access date.
- Relevant article, section, page, or timestamp.
- Narrow supported claim and limitations.
- Evidence state and a link to the detailed evidence note.
- In that note, reviewer/method and human-check status.

Use “not stated” or “not yet verified” for absent or unresolved dates. Never infer
an effective date or legal force from the publication date or document title.

## Workflow

1. Log a candidate and its discovery source.
2. Open the original source and check the exact claim and its context.
3. Save the source file and original-language extraction under `sources/<source_id>/`;
   record retrieval metadata and check that the cited passage survives extraction.
   Save an evidence note using [the template](templates/evidence-note.md), then
   update the source register and relevant index.
4. Record findings as research proceeds, so slides never become the only record.
5. Keep source wording, interpretation, and open applicability questions explicit.
6. Before presentation release, follow every material claim's links to the
   original passage; record reviewer and result.
7. Update counts and report unresolved/manual-review items honestly.

The overview supplied in the final project plan is project context, not a
verified industry research finding. Source its claims before reusing them as
evidence.

## Citation discipline

- Prefer authoritative Chinese originals; translations are aids.
- Search snippets and reposts may support discovery, not legal conclusions.
- Distinguish law/rules, regulator guidance, drafts, industry material, vendor
  claims, and internal requirements.
- Verify instrument status and applicability separately.
- Preserve exact source wording and section/page pointers. Use selected original
  passages in evidence notes and link the full archived original; summaries and
  translations must be labelled as authored research.
- Record AUM unit, metric, entity scope, date, and source. Compare compatible
  measurements and label gaps.
- Distinguish announcement, pilot, and production use.
- Absence of a disclosure does not establish absence of adoption.

## Data handling

Use public information in this repository. Do not place confidential internal,
client, personal, portfolio/position, or licensed research data here without the
user's explicit direction and an authorized storage basis. Track internal-policy
questions without copying restricted text. COD is the host organization's infrastructure; MRM
means model risk management. Those clarifications do not supply architecture
specifications or internal policy content.
