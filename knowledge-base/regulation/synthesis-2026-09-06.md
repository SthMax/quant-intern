# Initial Regulatory / MRM Synthesis — 6 September 2026

> 2026-09-09复核更新：请优先阅读[逐条复核结果](review-results-2026-09-09.md)。本页是9月6日研究底稿；新增REG-013–016已补齐网络安全、数据安全、个人信息审计和AI标识。REG-011美国政策有过时引文，EU相关适用日期也已修订，不应沿用旧研究的当前状态描述。

> 本页为研究者分析，不是来源原文或官方翻译。请通过下方 REG 笔记查阅原语言条文和本地原始文件；完整目录见[原始来源档案](../sources/README.md)。

This synthesis organizes inspected provisions under the three assigned themes.
[Source matrix](index.md) · [Master register](../source-register.md).

It is a research draft. The cited source wording has been inspected; a complete
amendment/status sweep, institution-specific applicability and internal-policy
confirmation remain open. Human review has not yet occurred.

## Data privacy

Start with the processing activity and data category. The Personal Information
Protection Law provides multiple processing bases, entrusted-processing controls,
specific automated-decision protections, and impact-assessment duties.
[REG-002](REG-002-personal-information-protection-law.md)

The network-data regulation and CSRC security rules add relevant data-lifecycle,
institutional-accountability and investor-information provisions.
[REG-004](REG-004-network-data-security-regulations.md),
[REG-005](REG-005-csrc-network-information-security.md)

**Research implication:** the future architecture should make input data,
retrieval permissions, logs, outputs and third-party flows visible. “On-premise”
alone does not describe those flows. No institution-specific dataset has been classified in this
research.

## Model interpretability and governance

Three different source concepts must remain distinguishable:

| Source | What was verified | Correct use in the presentation |
|---|---|---|
| PIPL Article 24 | Explanation/transparency rights in defined personal-information automated-decision situations | State the processing/decision conditions |
| AMAC T/AMAC 0004-2026, 11.3(e) | Explainability and source-reference recommendations using “宜” | Label as association-standard recommendations; check adoption |
| April 2026 US MRM guidance, footnote 3 | Generative/agentic AI excluded from scope | Comparative governance context, with exclusion prominently stated |

Sources: [REG-002](REG-002-personal-information-protection-law.md),
[REG-010](REG-010-amac-llm-application-standard.md),
[REG-008](REG-008-fed-mrm-guidance-scope.md).

SR 26-2 replaces SR 11-7; the older letter should not be presented as the current
unqualified public US MRM authority.
[REG-007](REG-007-fed-sr-26-2-replacement.md)

The AMAC explainability paper is industry research. The September 9 citation
review found that its US discussion uses rescinded EO 14110 and does not report
the removal of the proposed ten-year state AI moratorium. Its EU discussion also
needs the subsequent formal amendment and staged application dates. Use the
dated review results rather than the paper as a current-law summary.
[REG-011](REG-011-amac-explainability-research.md)

**Research implication:** define which evidence makes a proposed output useful,
traceable and reviewable, then obtain the internal MRM control requirements.
Displaying a source or explanation does not by itself validate an answer.

## Outsourcing and deployment boundaries

The CSRC IT rule permits defined outsourcing while retaining institutional
responsibility and control, with particular restrictions for important systems.
Review/reporting, exit planning, agreements and vendor-data provisions need to be
assessed against the actual service arrangement.
[REG-003](REG-003-csrc-information-technology-management.md)

The AMAC standard discusses local, externally hosted institution-controlled, and
cloud-call arrangements. Its publication does not automatically establish
universal statutory compulsion: group-standard adoption has its own legal and
organizational basis.
[REG-009](REG-009-amac-llm-standard-publication.md),
[REG-010](REG-010-amac-llm-application-standard.md),
[REG-012](REG-012-standardization-law.md)

Cross-border provisions require a separate factual assessment of data location,
access and transfer conditions. They do not equate “API” with “overseas.”
[REG-006](REG-006-cross-border-data-provisions.md)

**Research implication:** distinguish model publisher, software supplier, managed
service provider, compute host and data processor. Investigate the standard's
model-filing clause and any internal adoption commitments before reaching a
procurement conclusion.

## A key applicability distinction

Article 2 of the generative-AI interim measures differentiates domestic-public
services from non-public organizational research/application. This is narrower
than a blanket exemption from Chinese regulation.
[REG-001](REG-001-generative-ai-interim-measures.md)

## Next verification priorities

1. Targeted public-source status checks and core law/audit/labelling review were
   completed on September 9; see the linked matrix and retrieval record.
2. Confirm internal MRM coverage, COD facts, data categories and AMAC adoption/filing.
3. Once the pilot is chosen, inspect the applicable technical standards in detail.
4. Human-check the material presentation claims and their source passages before release.
