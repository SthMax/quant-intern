---
company_id: COMP-019
evidence_state: verified-primary
accessed: 2026-09-06
reviewed_by: Codex research subagent
human_check_status: pending
---

# Maxwealth / 永赢基金管理有限公司

<!-- original-language-provenance:start -->
> [!important] 原文与研究者分析分离
> 本页保留的英文正文、分类及表格是研究者撰写的摘要、整理或分析，不是来源原文。请先阅读下方逐源链接中的原语言文本；中文来源保留中文，原本为英文的来源保留英文。本次未将英文摘要反译为所谓“中文原文”。
> 来源的一手／转载／媒体／供应商属性及证据限制仍按原登记保留；保存原文不等于核实全部研究结论。人工核验仍待完成。

## 原语言来源档案（逐源）

档案中的 `original.md` 是机械提取文本；页面排版、表格和提取缺失以下载文件为准。无法确认正文的响应不作为原文提供，详见元数据。来源标题沿用登记表，仅作定位。

| 来源 ID | 登记标题 | 原登记证据状态 | 原语言正文／下载文件／记录 |
|---|---|---|---|
| FUND-350 | 基金公司鏖战AI | candidate | [原语言正文](../sources/FUND-350/original.md) · [下载文件](../sources/FUND-350/source.html) · [元数据与限制](../sources/FUND-350/metadata.json) · [登记网址](https://m.21jingji.com/article/20250305/4afe229674c12f385cee84f64f3debc8.html) |
| FUND-352 | AI筑牢邮件安全防线 永赢基金以大模型守护金融数字资产 | verified-primary | [原语言正文](../sources/FUND-352/original.md) · [下载文件](../sources/FUND-352/source.pdf) · [元数据与限制](../sources/FUND-352/metadata.json) · [登记网址](https://www.amac.org.cn/xwfb/hydt/202607/P020260701319545695145.pdf) |
| FUND-353 | 行业动态 | verified-primary | [原语言正文](../sources/FUND-353/original.md) · [下载文件](../sources/FUND-353/source.html) · [元数据与限制](../sources/FUND-353/metadata.json) · [登记网址](https://www.amac.org.cn/xwfb/hydt/index.html) |

## 研究者摘要／分析（保留原有正文）

**以下为研究者摘要/分析，不是原文。** 原有事实表述、引用定位、证据状态和局限一并保留，供对照原文复核。
<!-- original-language-provenance:end -->

## Verified operational disclosure

An original two-page company case hosted by AMAC describes **安全GPT钓鱼检测大模型**
in an operational email-security workflow (FUND-352). AMAC's original index
links the exact PDF and dates the listing **1 July 2026** (FUND-353). The PDF
itself has no publication date.

| Field | Narrow case disclosure | Locator |
|---|---|---|
| Function | Cybersecurity / email-risk screening | PDF p. 1 |
| Inputs | Email text, attachments, URLs, QR codes and HTML pages | PDF p. 1 |
| AI task | Context/intent assessment to identify impersonation and phishing | PDF p. 1 |
| Tools / agents | Agents coordinate detection tools, attack assessment, severity treatment and chain reconstruction | PDF pp. 1–2 |
| Stage | The case explicitly reports performance since going live | PDF p. 2 |
| Reported results | >93% detection of high-adversarial phishing; <0.28% false-positive rate; >80% reduction in manual review work | PDF p. 2 |

These are case-reported measures. Evaluation dataset, sample size, operating
period, adversarial-test design, baseline denominators and independent audit
are not provided. They cannot be presented as general model accuracy or copied
into the host organization's expected ROI assumptions.

## Architecture and governance limits

“安全GPT” is the disclosed system/model label. It does **not** identify OpenAI
as the provider, a specific GPT foundation model, or the underlying vendor.
Parameter count, GPU specification, inference framework and hosting topology
are not stated. The case does not establish whether message content leaves
the company's network or how reviewers override/appeal a classification.

The reported reduction in manual review does not mean complete removal of
human review. This is a cybersecurity use case; it is not proof of automated
fund-product compliance approval or an investment-research LLM deployment.

## Asset size and other leads

Manager selection is recorded in the [size-first universe](large-fund-universe-2026q2.md).
No new company-origin AUM was verified in this pass. A March 2025 media survey
also lists Maxwealth among private DeepSeek deployers (FUND-350), but that
separate claim remains secondary and is not used to infer the mail system's
model or hosting.

## Verification and sources

Codex downloaded the original PDF, inspected its complete text and visually
checked both pages, including metric inequalities. The AMAC index's exact link
and date were read from original HTML. Human checks remain pending.

- **FUND-352** — [AI筑牢邮件安全防线 永赢基金以大模型守护金融数字资产](https://www.amac.org.cn/xwfb/hydt/202607/P020260701319545695145.pdf). Original company case on AMAC; PDF pp. 1–2; operational claims and self-reported outcomes.
- **FUND-353** — [行业动态](https://www.amac.org.cn/xwfb/hydt/index.html). Original AMAC index; linked entry 2026-07-01; pagination may change.
- **FUND-350** — [基金公司鏖战AI](https://m.21jingji.com/article/20250305/4afe229674c12f385cee84f64f3debc8.html), 2025-03-05. Additional DeepSeek lead; secondary, not confirmation of the mail system's foundation model.
