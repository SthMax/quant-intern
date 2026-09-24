# Initial Company-Landscape Synthesis — 6 September 2026

<!-- original-language-provenance:start -->
> [!important] 原文与研究者分析分离
> 本页保留的英文正文、分类及表格是研究者撰写的摘要、整理或分析，不是来源原文。请先阅读下方逐源链接中的原语言文本；中文来源保留中文，原本为英文的来源保留英文。本次未将英文摘要反译为所谓“中文原文”。
> 来源的一手／转载／媒体／供应商属性及证据限制仍按原登记保留；保存原文不等于核实全部研究结论。人工核验仍待完成。

## 原语言来源档案（逐源）

档案中的 `original.md` 是机械提取文本；页面排版、表格和提取缺失以下载文件为准。无法确认正文的响应不作为原文提供，详见元数据。来源标题沿用登记表，仅作定位。

| 来源 ID | 登记标题 | 原登记证据状态 | 原语言正文／下载文件／记录 |
|---|---|---|---|
| FUND-001 | 关于华夏基金管理有限公司采购结果的公告 | verified-primary | [原语言正文](../sources/FUND-001/original.md) · [下载文件](../sources/FUND-001/source.pdf) · [元数据与限制](../sources/FUND-001/metadata.json) · [登记网址](https://www.chinaamc.com/upload/resources/file/2025/12/31/442744.pdf) |
| FUND-002 | 华夏基金管理有限公司大模型云服务项目潜在供应商征集公告 | verified-primary | [原语言正文](../sources/FUND-002/original.md) · [下载文件](../sources/FUND-002/source.html) · [元数据与限制](../sources/FUND-002/metadata.json) · [登记网址](https://www.chinaamc.com/c/2026-02-05/926147.shtml) |
| FUND-004 | 『基金行业金融科技获奖成果宣传活动』易方达基金：基于数智赋能的指数业务一体化平台 | verified-primary | [原语言正文](../sources/FUND-004/original.md) · [下载文件](../sources/FUND-004/source.pdf) · [元数据与限制](../sources/FUND-004/metadata.json) · [登记网址](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337819827722.pdf) |
| FUND-007 | 『基金行业金融科技发展奖』富国基金：指数基金智能投资决策系统 | verified-primary | [原语言正文](../sources/FUND-007/original.md) · [下载文件](../sources/FUND-007/source.pdf) · [元数据与限制](../sources/FUND-007/metadata.json) · [登记网址](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337808067241.pdf) |
| FUND-009 | 广发基金智能理财助理服务协议 | verified-primary | [原语言正文](../sources/FUND-009/original.md) · [下载文件](../sources/FUND-009/source.pdf) · [元数据与限制](../sources/FUND-009/metadata.json) · [登记网址](https://cdnwww.gffunds.com.cn/gfjjnew/jjgg/lsgg/202603/W020260327646002876113.pdf) |
| FUND-011 | 『基金行业金融科技获奖成果宣传活动』兴证全球基金：千询固收智能交易平台 | verified-primary | [原语言正文](../sources/FUND-011/original.md) · [下载文件](../sources/FUND-011/source.pdf) · [元数据与限制](../sources/FUND-011/metadata.json) · [登记网址](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337841539992.pdf) |
| FUND-013 | 『基金行业金融科技获奖成果宣传活动』大成基金：固收全链路数智一体化平台 | verified-primary | [原语言正文](../sources/FUND-013/original.md) · [下载文件](../sources/FUND-013/source.pdf) · [元数据与限制](../sources/FUND-013/metadata.json) · [登记网址](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337853082516.pdf) |

## 研究者摘要／分析（保留原有正文）

**以下为研究者摘要/分析，不是原文。** 原有事实表述、引用定位、证据状态和局限一并保留，供对照原文复核。
<!-- original-language-provenance:end -->

Historical first-batch snapshot. The current size-first findings are in
[the expanded synthesis](large-fund-synthesis-2026-09-06.md).

Scope: six fund managers, seven primary-source initiatives, ten further candidates.
See [the database](index.md), [candidate queue](candidate-queue.md), and
[master sources](../source-register.md). This is an initial convenience sample
of verifiable disclosures; no industry adoption rate can be calculated from it.

## What the first sample supports

| Finding | Evidence | Boundary |
|---|---|---|
| LLM activity extends beyond generic experimentation in this sample | E Fund, Fullgoal, Industrial Securities Global, and Dacheng publish operational platform descriptions in AMAC project cases (FUND-004/007/011/013) | These are reported deployments; no independent system access or outcome audit |
| Internal research and transaction workflows provide concrete examples | Fullgoal local research/RAG, Qianxun transaction parsing, Dacheng NLP/千问 2.5 (FUND-007/011/013) | Human workflow roles and non-LLM platform components matter |
| Customer-facing and procurement pathways also appear | GF official assistant terms and ChinaAMC security/cloud procurement (FUND-001/002/009) | Terms/awards/solicitations are different maturity evidence |
| Supplier disclosure is uneven | ChinaAMC names a gateway awardee; GF credits model origins; AMAC cases disclose varying stack detail | An open-source package or named model is not necessarily a commercial partner |
| Outcomes are generally case-reported | Hours saved, platform reach and workflow duration appear in cases | Do not combine them into an average LLM ROI or infer causality from AUM growth |

## Asset-size interpretation

All six have sourced scale observations, but only Fullgoal and Dacheng currently
have separately captured public-fund AUM. Observations span June 2025 to March
2026 and differ in subsidiary/advisory/pension inclusion.

Use the database's dated raw figures and explicit scope labels in any early
presentation. A common-date public-fund comparison needs more collection.
Dacheng's “above RMB 700 billion” cannot be turned into an exact value or a
below-RMB-1-trillion category.

## Examples suitable for a discussion slide

- **Fullgoal:** a concrete research/RAG workflow with described source referencing
  and output checks. The reported duration change lacks an independent test.
- **Industrial Securities Global:** a fixed-income assistant integrated into
  quotation and instruction workflows, with human trader/manager roles retained.
- **ChinaAMC:** a procurement award gives a named security supplier without
  proving a foundation-model deployment.
- **GF:** official terms establish the documented assistant/model families while
  leaving topology and service availability untested.

These are examples of peer practice, not a ranking of proposed internal pilots.

## Claims to avoid

- “All large onshore fund houses are still only exploring AI.”
- “All surveyed firms run DeepSeek on-premise.”
- “Open-model use proves a vendor partnership.”
- “A trading assistant is an autonomous trader.”
- “Reported platform productivity is independently measured LLM ROI.”
- “The fund named in a news repost has made a separately verified primary disclosure.”

The overview in the final project brief is project context. Update the evidence
narrative from this research without changing the confirmed project objectives.

## Next pass

Prioritize the ten-company candidate queue, common-cut-off public-fund AUM,
missing publication dates, and a direct compliance-review case. Complete manual
review and reconcile the missing numerical company target before calling the
Phase 1 database finished.
