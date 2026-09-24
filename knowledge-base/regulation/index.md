# Regulatory and Model Risk Management Evidence Map

> 2026-09-09 已执行：[监管与研究复核结果](review-results-2026-09-09.md)，含12份既有材料、4份新增法规、9项研究引文核验、EU正式修法日期链及内部待确认项。[复核方案](review-plan-2026-09-09.md)保留执行安排。

> 本页为研究者编制的索引和摘要，不是法规原文。各 REG 证据笔记已分别链接原始文件和原语言提取文本；完整目录见[原始来源档案](../sources/README.md)。英文分析不代替中文法规原文。

**Phase 1 — Weeks 1–2.** Research batch dated **6 September 2026**.
COD means the infrastructure used in the host organization; MRM means model risk management.

Sixteen official law, regulatory, standard, MRM, and research sources have now
been inspected at the cited locations. These are not sixteen binding AI rules.
Read [the thematic synthesis](synthesis-2026-09-06.md) with the source notes.

## Source-to-theme matrix

| Theme | Source | Type / status established | Exact locator | Supported content | Applicability / interpretation limit |
|---|---|---|---|---|---|
| Service boundary | [REG-001](REG-001-generative-ai-interim-measures.md) | CAC joint measures; original commencement checked | Article 2; 4(5) | Domestic-public service scope and non-public organizational exclusion | Hosting and audience are separate; other rules may still apply |
| Privacy / automated decisions | [REG-002](REG-002-personal-information-protection-law.md) | PRC law; 2021 text/commencement inspected | Articles 13, 21, 24, 28, 55–56 | Lawful basis, entrusted processing, specific explanation rights, assessment | Depends on personal information and decision use; not universal LLM explainability |
| Outsourcing / IT governance | [REG-003](REG-003-csrc-information-technology-management.md) | CSRC consolidated 2021-amended rule inspected | Articles 2–3, 14, 21, 43–45, 51 | Accountability, internal review, important-system control and vendor limits | Determine defined service role/system scope; exceptions matter |
| Network-data lifecycle | [REG-004](REG-004-network-data-security-regulations.md) | State Council regulation; effective 2025-01-01 | Articles 2, 9, 12, 19, 31, 37 | Safeguards, entrusted-data records, training-data and important-data provisions | Data category and processor/service role must be established |
| Investor information / sector security | [REG-005](REG-005-csrc-network-information-security.md) | CSRC Order 218; effective 2023-05-01 | Articles 2, 4, 29–34, 75 | Institutional security responsibility and investor-data safeguards | Evaluate actual system boundaries and third-party flows |
| Cross-border processing | [REG-006](REG-006-cross-border-data-provisions.md) | CAC Order 16; effective 2024-03-22 | Articles 2–8, 10–14 | Conditional routes/exemptions and residual obligations | No institution-specific transfer-volume or exemption determination made |
| MRM currency | [REG-007](REG-007-fed-sr-26-2-replacement.md) | US supervisory letter, 2026-04-17 | Applicability / Supersedes | Replaces SR 11-7 and SR 21-8 | Not CSRC law or unpublished firm policy |
| MRM scope | [REG-008](REG-008-fed-mrm-guidance-scope.md) | US guidance | Sections I–VII; footnote 3 | Generative/agentic AI excluded; comparative governance context | Internal LLM controls require an internal source |
| AMAC standard publication | [REG-009](REG-009-amac-llm-standard-publication.md) | Association notice, 2026-04-03 | Announcement / attachment | T/AMAC 0004-2026 publication and commencement | Notice does not establish universal legal compulsion |
| LLM-specific sector specification | [REG-010](REG-010-amac-llm-application-standard.md) | Group standard; cover/date checked | 9.1, 9.2, 11.2, 11.3(e), Annex B.2 | Deployment options, evaluation, data isolation, explainability recommendations | Preserve “应/宜” distinctions and check adoption/basis of filing clause |
| Explainability research | [REG-011](REG-011-amac-explainability-research.md) | Industry research issue dated 2026-04-01 | PDF pp. 1, 12 | Governance discussion | Recommendations and foreign-law summaries are not binding rules |
| Standard classification | [REG-012](REG-012-standardization-law.md) | PRC Standardization Law, 2017 revision | Articles 2, 18, 45 | Group-standard adoption route | Member agreements/incorporation/internal adoption need checking |
| Network security / current numbering | [REG-013](REG-013-cybersecurity-law-2025-amendment.md) | PRC Cybersecurity Law, 2025 amendment effective 2026-01-01 | Articles 2, 20, 23, 27, 33, 39, 42 | General network safeguards and classification; amendment date | COD system/MLPS/CII classification remains unknown |
| Data-security baseline | [REG-014](REG-014-data-security-law.md) | PRC Data Security Law, effective 2021-09-01 | Articles 2–3, 21, 27, 29–32, 36 | Broader-than-personal data lifecycle controls | Important-data status and actual flows require evidence |
| Personal-information auditing | [REG-015](REG-015-personal-information-compliance-audit.md) | CAC Order 18, effective 2025-05-01 | Articles 3–6 and annex 6, 9, 23 | Periodic audit; over 10 million subjects: at least every two years | Processor-level threshold, not PoC row count; not a model validation |
| AI-content labels | [REG-016](REG-016-ai-generated-content-labelling.md) | Joint normative document, effective 2025-09-01 | Articles 2, 4–6, 9–12; GB 45438 status | Provider/platform/publisher roles and labelling | Internal vs public distribution requires separate determination |

Targeted official-source amendment/repeal checks and review of presentation-relevant
passages were performed on 2026-09-09; this is not an exhaustive legal clearance.
REG-011 contains outdated US-policy discussion and needs the corrections in the
review results. Institution-specific application and human review remain pending.

## Questions for authorized internal owners

| Area | Question | Evidence informing the question | Status |
|---|---|---|---|
| Internal MRM | Which policy covers generative/agentic AI and what validation tier applies? | REG-007/008 distinguish current US guidance from internal policy | Open |
| AMAC adoption | What association/member/internal commitments apply to T/AMAC 0004-2026? How is 9.1.1(d) interpreted? | REG-009/010/012 | Open |
| Privacy/data owner | Which inputs/logs are personal, sensitive, important, or restricted research data? | REG-002/004/005 | Open |
| IT / outsourcing | Which systems/services fall within relevant CSRC definitions and what review/reporting applies? | REG-003/005 | Open |
| COD infrastructure | What outbound connections, shared services, support access, and data boundaries exist? | REG-003/005/006/010 | Phase 2 input |
| Legal/compliance | Which version/status and applicability conclusions can be confirmed? | Entire source matrix | Open |

## Remaining scoped checks

The Cybersecurity Law, Data Security Law, personal-information audit measures and
AI-content labelling rules have now been added as REG-013–016. GB 45438-2025's
current mandatory-standard status was verified; detailed format compliance and
other standards referenced by AMAC remain scoped follow-ups after the pilot and
architecture are chosen. Sales/suitability rules for a customer-facing service are
outside this internal-research pilot review.
