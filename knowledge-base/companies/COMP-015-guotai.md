---
company_id: COMP-015
evidence_state: verified-primary
evidence_scope: Original AI/LLM project disclosure; current screening rank is secondary
accessed: 2026-09-06
reviewed_by: Codex
human_check_status: pending
---

# Guotai / 国泰基金管理有限公司

<!-- original-language-provenance:start -->
> [!important] 原文与研究者分析分离
> 本页保留的英文正文、分类及表格是研究者撰写的摘要、整理或分析，不是来源原文。请先阅读下方逐源链接中的原语言文本；中文来源保留中文，原本为英文的来源保留英文。本次未将英文摘要反译为所谓“中文原文”。
> 来源的一手／转载／媒体／供应商属性及证据限制仍按原登记保留；保存原文不等于核实全部研究结论。人工核验仍待完成。

## 原语言来源档案（逐源）

档案中的 `original.md` 是机械提取文本；页面排版、表格和提取缺失以下载文件为准。无法确认正文的响应不作为原文提供，详见元数据。来源标题沿用登记表，仅作定位。

| 来源 ID | 登记标题 | 原登记证据状态 | 原语言正文／下载文件／记录 |
|---|---|---|---|
| FUND-400 | 公募非货规模最新座次出炉，万亿公募增至3家，中段座次重排 | candidate | [原语言正文](../sources/FUND-400/original.md) · [下载文件](../sources/FUND-400/source.html) · [元数据与限制](../sources/FUND-400/metadata.json) · [登记网址](https://www.cls.cn/detail/2432695) |
| FUND-401 | 基金管理机构非货币公募基金月均规模（20家）（2024年三季度） | verified-primary | [原语言正文](../sources/FUND-401/original.md) · [下载文件](../sources/FUND-401/source.pdf) · [元数据与限制](../sources/FUND-401/metadata.json) · [登记网址](https://www.amac.org.cn/sjtj/datastatistics/assetmanagementdata/smzg_ywpm/202411/P020241106606145403776.pdf) |
| FUND-403 | 『基金行业金融科技获奖成果宣传活动』国泰基金：基金组合管理平台建设 | verified-primary | [原语言正文](../sources/FUND-403/original.md) · [下载文件](../sources/FUND-403/source.pdf) · [元数据与限制](../sources/FUND-403/metadata.json) · [登记网址](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337808791393.pdf) |
| FUND-405 | 国泰基金管理有限公司旗下部分基金2025年年度报告提示性公告 | verified-primary | [原语言正文](../sources/FUND-405/original.md) · [下载文件](../sources/FUND-405/source.pdf) · [元数据与限制](../sources/FUND-405/metadata.json) · [登记网址](https://st.gtfund.com/GSGG/2026/03/30/828175006116.PDF)；辅助阅读，不进入主阅读集 |

## 研究者摘要／分析（保留原有正文）

**以下为研究者摘要/分析，不是原文。** 原有事实表述、引用定位、证据状态和局限一并保留，供对照原文复核。
<!-- original-language-provenance:end -->

## Why this manager is in scope

Guotai is in the reported 2026-Q2 large-fund screen (rank 12; non-money public-fund
AUM RMB 6,238.11亿元 excluding ETF feeders, FUND-400). Keep that source-attributed
screen separate from primary AUM confirmation. AMAC's older 2024-Q3 official
table records 3,436.59亿元 of quarterly-mean non-money AUM (FUND-401); the two
period/metric definitions cannot be used for a growth calculation.

An official 30 March 2026 notice for 294 funds' annual reports establishes current
public-fund-manager activity (FUND-405). It does not supply aggregate AUM.

## Verifiable platform details

FUND-403 is an original company project case hosted by AMAC. Physical PDF page
is printed page + 1. The PDF is undated; no precise production launch is inferred.

| Area | Source disclosure | Locator |
|---|---|---|
| Hardware | Huawei Atlas800, Ascend 910B NPU, Kunpeng 920 CPU | PDF p. 4 / printed p. 3 |
| Runtime | MindSpore and CANN; serving/unified model management layer | PDF p. 4 |
| Data/application stack | Hadoop/CDH, ETL, SpringCloud/Java, Nacos, Vue/jQuery | PDF pp. 5, 7 |
| Document RAG | Table/image recognition and a vision-language conversion route; vectors and graph data feed retrieval | Figure 3, PDF p. 6 |
| Generative model | **DeepSeek模型** is labelled at the answer-generation node of Figure 3 | PDF p. 6, visually checked |
| Transaction NLP | Regex preprocessing → BERT → BiLSTM → CRF, joint entity/relation extraction, post-checks | PDF p. 6 text and Figure 4 p. 7 |
| Control design | Permission controls and review rules for business flow/output; traceability and contingency arrangements | PDF pp. 8, 10 |

The DeepSeek label is in the diagram and was absent from plain text extraction.
No specific DeepSeek version, parameter count, accelerator quantity, inference
benchmark or implementation contract is given. Hardware/framework names disclose
components; they do not establish the scope of a paid Huawei contract.

The transaction NLP pipeline is not the same mechanism as generative DeepSeek
RAG. It is particularly useful to distinguish these methods when examining
financial named-entity extraction.

## Reported outcomes and limits

The case describes production use across investment/trading, risk/compliance and
operations. It reports portfolio work moving from hours to minutes, without a
specified benchmark task, observation window or isolated LLM effect (PDF p. 8).
The wider platform's efficiency and investment claims are not causal LLM ROI.

Private hardware does not establish an air gap, and described permission rules
are not independent evidence of tested control effectiveness. No internal
policy or deployment approval is inferred.

## Source trail

- **FUND-403** — [『基金行业金融科技获奖成果宣传活动』国泰基金：基金组合管理平台建设](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337808791393.pdf). Complete text read; Figure 3 and surrounding NLP pipeline on PDF p. 6 visually inspected.
- **FUND-405** — [国泰基金管理有限公司旗下部分基金2025年年度报告提示性公告](https://st.gtfund.com/GSGG/2026/03/30/828175006116.PDF). Dated 2026-03-30; PDF p. 1.
- **FUND-400/401** — [Size-screening evidence and definitions](large-fund-universe-2026q2.md).

Human review remains pending. Next: obtain the exact deployed model, task-specific
quality/latency metrics, current official comparable AUM and dated system release.
