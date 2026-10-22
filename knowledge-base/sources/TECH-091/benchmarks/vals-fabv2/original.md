## Background

Finance Agent v2 builds on [Finance Agent v1.1](https://www.vals.ai/benchmarks/finance_agent) with 927 expert-reviewed questions across public, private validation, and held-out test splits. Dataset design, splits, and access are covered in [Methodology](#methodology).

The benchmark tests a model’s ability to perform the work of entry-level financial analysts — answering difficult questions on public company filings.

Automating analyst-grade financial research is valuable because the work is expensive, repetitive, and time-sensitive: analysts often need to move from filings and transcripts to a defensible model or investment memo under deadline. The work is also difficult because the answer depends on finding the right source, applying the right finance convention, and carrying precise intermediate numbers through several steps.

Finance Agent v2 measures how well AI can aid analysts in automating busy work so they can focus on higher-leverage tasks.

---

## Results

The Pareto chart above illustrates how model accuracy trades off against cost and latency. [Gemini 3.8 Flash](https://www.vals.ai/models/google_gemini-3.8-flash) leads at 61.44% at $2.00 per test. [Muse Spark 1.2](https://www.vals.ai/models/meta_muse_spark_1_2) follows at 60.60% and [Muse Spark 1.3 Max](https://www.vals.ai/models/meta_muse_spark_1_3_max) at 59.96%, each at roughly $0.77 per test, less than 40% of the leader’s cost. Muse Spark 1.3 Max is also the fastest of the three at about 3 minutes 19 seconds per task, narrowly ahead of Gemini 3.8 Flash, while Muse Spark 1.2 takes about 5 minutes.

The mid-tier models sit only a few points below the leaders at a fraction of the cost, suggesting the accuracy premium at the frontier is modest relative to the price gap.

### Where Models Stand

**Category Leaders** Hover for top three

Earnings Analysis

Gemini 4 Argon 84.8%

General Qualitative

Muse Spark 1.3 Max 83.4%

General Quantitative

Gemini 3.7 Flash 81.8%

Market Analysis

Gemini 4 Argon 79.7%

Disclosure Analysis

Gemini 4 Argon 74.5%

Adjustments

Gemini 4 Argon 60.5%

Comparables

Gemini 3.8 Flash 52.0%

Precedents

Gemini 4 Argon 49.8%

Financial Modeling

Muse Spark 1.2 34.5%

Categories ordered by leader accuracyBars scaled 0–100% accuracy · gridlines every 25%

The retrieval and summarization categories cluster at the top: General Quantitative, Earnings Analysis, General Qualitative, Market Analysis, and Disclosure Analysis all have category leaders above 70%. Adjustments tops out at 56.29%, while Comparables reaches 52.00% as cross-document reconciliation gets harder. Financial Modeling and Precedents remain the hardest categories, topping out at 34.52% and 36.37%, respectively.

**Partial Credit vs All-Pass**

PARTIAL CREDITALL-PASS

When measuring models on their ability to perfectly answer questions, scores fall substantially across the leaderboard compared with allowing partially complete responses.

The strongest model reaches 50.88% All-Pass accuracy, the next group sits in the mid-to-high 40s, and mid-tier models land in the low 30s. Models are still unable to execute financial tasks perfectly, often missing core details that real analysts would include.

**Tool Calls Analysis**

TURNSTOOL CALLSERRORS

The tool call analysis reveals how many steps the models take to produce an answer. Interestingly, the top performers also register relatively high numbers of tool calls. This suggests that their comparatively strong performance is partly due to leveraging the tools provided.

**Tool Usage**

4/80 models

The radar graph shows the per-model breakdown of tool calls across the six tools.

Calculator is the dominant tool for most frontier models. Higher-performing models tend to spend more of their tool budget on numerical resolution after finding the relevant source material. Lower-performing models lean harder on `web_search` and `retrieve_information`, making more exploratory calls that do not translate into correct answers. Across the models shown, `price_history` accounts for at most 4.22% of tool calls, matching its narrower role in Market Analysis questions.

---

## Model Output Examples

Question

### Did NYSE: CNC have to pay a rebate to policyholders in fiscal year 2025 or fiscal year 2020? If not, was the company closer to owing customers a rebate in 2025 or 2020? What were the medical loss ratios in each year?

\### Executive Summary  
  
1\. \*\*Did Centene Corporation (NYSE: CNC) have to pay a rebate to policyholders in FY 2025 or FY 2020?\*\*  
\* \*\*On a consolidated basis: No.\*\* Under the Affordable Care Act (ACA) and Centers for Medicare & Medicaid Services (CMS) regulations, health insurers must maintain a minimum Medical Loss Ratio (MLR) of \*\*80%\*\* (for individual and small group commercial plans) to \*\*85%\*\* (for large group commercial, Medicaid managed care, and Medicare Advantage/Part D plans). If an insurer’s MLR falls \*below\* the minimum threshold, it must pay rebates to policyholders or government program sponsors. In both fiscal year 2025 (\*\*91.92%\*\*, reported as \*\*91.9%\*\*) and fiscal year 2020 (\*\*86.22%\*\*, reported as \*\*86.2%\*\*), Centene’s consolidated MLR (which Centene reports as its \*\*Health Benefits Ratio\*\*, or \*\*HBR\*\*) exceeded both the 80% and 85% minimum thresholds.  
\* \*(Note on Plan-Level Footnote Disclosures: Because minimum MLR requirements are enforced at the individual state, legal entity, and product/contract level rather than on a consolidated basis, certain individual plans did accrue minimum MLR and return-of-premium payables in both periods—specifically, ACA minimum MLR payables of $294 million at year-end 2025 and $238 million at year-end 2020, recorded as reductions to premium revenue.)\*  
  
2\. \*\*Was the company closer to owing customers a rebate in 2025 or 2020?\*\*  
\* Centene was \*\*closer to owing customers a rebate in fiscal year 2020\*\*.  
\* Because rebates are owed when the MLR drops \*below\* the statutory minimum floor (85% or 80%), a \*\*lower\*\* MLR places the insurer closer to triggering a rebate. In \*\*2020\*\*, reduced medical utilization during the COVID-19 pandemic lowered Centene's consolidated MLR to \*\*86.22%\*\* (reported as \*\*86.2%\*\*), which was only \*\*1.22 percentage points\*\* (1.2 percentage points as reported) above the 85% minimum threshold (and 6.22 percentage points above the 80% threshold). In \*\*2025\*\*, elevated medical cost trends across Marketplace, Medicaid, and Medicare drove Centene’s consolidated MLR to \*\*91.92%\*\* (reported as \*\*91.9%\*\*), which was \*\*6.92 percentage points\*\* (6.9 percentage points as reported) above the 85% minimum threshold—\*\*5.71 percentage points\*\* (570 basis points as reported) further away from the rebate threshold than in 2020.  
  
3\. \*\*What were the Medical Loss Ratios in each year?\*\*  
\* \*\*Fiscal Year 2025:\*\* \*\*91.92%\*\* (explicitly reported in MD&A to one decimal place as \*\*91.9%\*\*), calculated as $\\$157,702\\text{ million}$ in medical costs divided by $\\$171,556\\text{ million}$ in premium revenues.  
\* \*\*Fiscal Year 2020:\*\* \*\*86.22%\*\* (explicitly reported in MD&A to one decimal place as \*\*86.2%\*\*), calculated as $\\$86,264\\text{ million}$ in medical costs divided by $\\$100,055\\text{ million}$ in premium revenues.  
  
\---  
  
\### Step-by-Step Analysis and Calculations  
  
\#### 1. Regulatory Minimum MLR and Rebate Mechanics  
Under the ACA and CMS managed care rules (as detailed in Item 1A, \*Risk Factors\*, and Note 2, \*Summary of Significant Accounting Policies\*, of Centene’s Form 10-K filings):  
\* \*\*ACA Commercial Plans (Individual / Marketplace & Small Group):\*\* Subject to a federal minimum MLR of \*\*80%\*\* (or \*\*85%\*\* for large group plans), taking into account risk adjustment transfers.  
\* \*\*Medicaid Managed Care & Medicare Advantage/Part D Plans:\*\* Subject to a federal minimum MLR standard of \*\*85%\*\* (established by CMS in the April 2016 Medicaid managed care final rule and Medicare regulations, with certain states imposing state-specific minimum MLRs or profit-sharing corridors).  
\* \*\*Rebate Trigger:\*\* An insurer owes a rebate (return of premium) to policyholders or state/federal agencies only when its medical costs (plus qualifying quality improvement expenses) as a percentage of premium revenues fall \*\*below\*\* the minimum threshold (e.g., $< 85\\%$ or $< 80\\%$).  
  
\---  
  
\#### 2. Centene’s Medical Loss Ratio (Health Benefits Ratio) Definition & Components  
In Item 7 (\*Management’s Discussion and Analysis of Financial Condition and Results of Operations\*) of both the FY 2025 and FY 2020 Form 10-K filings, Centene defines its primary medical loss ratio metric—the \*\*Health Benefits Ratio (HBR)\*\*—as follows:  
\> \*"The health benefits ratio (HBR) represents medical costs as a percentage of premium revenues, excluding premium tax \[and health insurer fee\] revenues that are separately billed, and reflects the direct relationship between the premiums received and the medical services provided."\*  
  
From the Consolidated Statements of Operations in Centene’s FY 2025 Form 10-K (page 71) and FY 2020 Form 10-K (page 67; unchanged in the FY 2022 Form 10-K, page 62):  
  
| Metric ($ in millions) | FY 2025 | FY 2020 |  
|---|---|---|  
| \*\*Medical costs\*\* (Numerator) | $\\$157,702$ | $\\$86,264$ |  
| \*\*Premium revenues\*\* (Denominator) | $\\$171,556$ | $\\$100,055$ |  
| \*\*Calculated Consolidated MLR / HBR (2 decimal places)\*\* | \*\*91.92%\*\* | \*\*86.22%\*\* |  
| \*\*Reported Consolidated HBR in Item 7 (MD&A)\*\* | \*\*91.9%\*\* | \*\*86.2%\*\* |  
| \*Distance above 85.00% Minimum MLR Threshold\* | \*+6.92% (+6.9%)\* | \*+1.22% (+1.2%)\* |  
| \*Distance above 80.00% Minimum MLR Threshold\* | \*+11.92% (+11.9%)\* | \*+6.22% (+6.2%)\* |  
  
\*\*Exact Calculations:\*\*  
\* \*\*FY 2025 Consolidated MLR (HBR):\*\*  
$$\\text{MLR}\_{2025} = \\frac{\\$157,702}{\\$171,556} = 0.91924503 \\approx \\mathbf{91.92\\%} \\quad (\\text{reported as } \\mathbf{91.9\\%})$$  
\*(Note: In FY 2025, per Note 19, Segment Information, every operating segment also exceeded the 85% threshold individually: Medicaid was $\\$84,450 / \\$90,137 = 93.69\\%$; Medicare was $\\$34,227 / \\$37,210 = 91.98\\%$; Commercial was $\\$36,902 / \\$42,001 = 87.86\\%$; and Other was $\\$2,123 / \\$2,208 = 96.15\\%$.)\*  
  
\* \*\*FY 2020 Consolidated MLR (HBR):\*\*  
$$\\text{MLR}\_{2020} = \\frac{\\$86,264}{\\$100,055} = 0.86216581 \\approx \\mathbf{86.22\\%} \\quad (\\text{reported as } \\mathbf{86.2\\%})$$  
  
\*(Note on Alternative Revenue Denominators: If medical costs were divided by combined "Premium and service revenues" of $\\$174,581\\text{ million}$ in 2025 and $\\$103,800\\text{ million}$ in 2020, the ratios would be \*\*90.33%\*\* in 2025 and \*\*83.11%\*\* in 2020. However, per GAAP and Centene's MD&A definition, service revenues and separately billed premium taxes/health insurer fees are excluded from the HBR/MLR calculation.)\*  
  
\---  
  
\#### 3. Comparison of 2025 vs. 2020 and Contract-Level Footnote Context  
\* \*\*Consolidated Comparison:\*\*  
In 2020, routine healthcare utilization dropped significantly due to COVID-19 stay-at-home orders and deferred elective procedures, causing Centene’s consolidated HBR to decline to \*\*86.22%\*\* (86.2%). In contrast, in 2025, Centene experienced sharp medical cost pressures (lower Marketplace risk adjustment revenue, higher Marketplace utilization, and elevated Medicaid behavioral health, home health, and specialty drug costs), pushing its consolidated HBR up to \*\*91.92%\*\* (91.9%). Consequently, on a consolidated basis, Centene did not owe a rebate in either year, and it was \*\*5.71 percentage points\*\* (570 basis points as reported) closer to the minimum MLR rebate threshold in \*\*2020\*\* than in \*\*2025\*\*.  
  
\* \*\*Plan-Level / Contract-Level Accounting Nuance:\*\*  
While consolidated ratios were above 85% in both years, MLR compliance is legally calculated at the state/contract/plan level, and estimated rebates or return-of-premium obligations for specific over-performing contracts are netted directly against \`Premium\` revenue in the period incurred (Note 2). Per Note 9 (\*Affordable Care Act\*) and the Consolidated Balance Sheets:  
\* \*\*ACA Minimum MLR Payable:\*\* Centene carried an ACA minimum MLR liability of \*\*$\\$294\\text{ million}$\*\* as of December 31, 2025 (down from $\\$688\\text{ million}$ at December 31, 2024) and \*\*$\\$238\\text{ million}$\*\* as of December 31, 2020 (down from $\\$367\\text{ million}$ at December 31, 2019).  
\* \*\*Total Return of Premium Payable (Balance Sheet):\*\* Centene reported current liabilities for \`Return of premium payable\` (spanning Medicaid state profit-sharing/minimum MLR corridors and commercial plans) of \*\*$\\$1,592\\text{ million}$\*\* at December 31, 2025, and \*\*$\\$1,458\\text{ million}$\*\* at

100

All checks passed.

The question above is a General Quantitative Analysis task: deciding whether Centene owed a rebate to policyholders in either fiscal year based on the medical loss ratio threshold, and reporting the underlying MLRs.

---

## Trajectory Comparison

The visualizations below show how a frontier model and a smaller, cheaper model approached the same Financial Modeling question of building a DCF model. Each row is one agent turn; bar width is wall-clock time per turn (model reasoning + tool execution).

[Claude Opus 4.7](https://www.vals.ai/models/anthropic_claude-opus-4-7) trajectory (passed most checks):

![Claude Opus 4.7 trajectory](https://www.vals.ai/benchmarks/fab/v2-opus47-traj.png)

The frontier model worked through the question in 12 turns: pull market data, fetch and parse the two filings, run `retrieve_information` to extract the inputs needed for the DCF, then step through bursts of parallel `calculator` calls to compute projections, terminal value, and discounted cash flows before submitting.

[GPT 5.4 Nano](https://www.vals.ai/models/openai_gpt-5.4-nano-2026-03-17) trajectory (zeroed on most checks):

![GPT-5.4-nano trajectory](https://www.vals.ai/benchmarks/fab/v2-nano-traj.png)

The smaller model needed 34 turns to reach an answer of similar shape — nearly 3x as many. After the retrieval phase, it hammers the `calculator` one operation at a time for the next 27 turns rather than fanning out parallel calls, and the resulting numbers land close to the rubric’s targets but not exactly enough to be rewarded.

---

## Methodology

Agents are all evaluated on a shared default harness with access to six tools: `edgar_search` (SEC EDGAR API), `web_search`, `parse_html_page` (download an HTML page), `retrieve_information` (query over fetched HTML), `calculator`, and `price_history`.

![Finance Agent v2 harness: the LLM iterates with search, process, and fetch tools, storing fetched documents in a database it can query on demand](https://www.vals.ai/benchmarks/fab/v2-agent-diagram.png)

### Time Limit

Each task has a two-hour time limit. An answer must be produced within the time limit, otherwise the task is scored as a zero. The time limit was chosen empirically by measuring how long current frontier models need to converge on these tasks and setting the limit comfortably above that ceiling. A fixed time budget also allows us to normalize and compare performance across different agent implementations.

### Grading

Each question is composed of weighted checks, and a subset are flagged as **dealbreakers**, load-bearing facts or numbers, that are required for a satisfactory answer. Failing any dealbreaker means the answer receives no credit for that question, regardless of the remaining content in the response. Two metrics are reported:

- **Partial Credit** (primary): the dealbreaker-gated, severity-weighted average of per-check scores. A response with a correct dealbreaker but a few peripheral misses scores below 100%; a response with any failed dealbreaker scores 0%.
- **All-Pass** (secondary): 100% only if every check passes, 0% otherwise.

All responses are graded by a three-judge LLM jury consisting of three frontier models: GPT-5.4, Gemini-3.1-Pro, and Claude Sonnet 4.6.

### Changes from v1.1

- **Step up in difficulty.** Even the best models reach only 61.44% with Partial Credit and 50.88% under All-Pass grading. Questions require connecting data across multiple documents, tighter numeric precision, and answers are expected to include insights that skilled analysts would include but are not explicitly stated in the question.
- **Expanded taxonomy.** The taxonomy was reorganized around real analyst workflows rather than retrieval tiers. v1.1’s easier retrieval-focused buckets (Quantitative Retrieval, Qualitative Retrieval, Numerical Reasoning, Complex Retrieval, Beat or Miss, Trends) are replaced with Comparables, Precedents, Earnings Analysis, Disclosure Analysis, and a split between General Qualitative and General Quantitative analysis.
- **New grading mechanism.** Dealbreaker-gated Partial Credit replaces v1.1’s flat per-question score, and All-Pass is reported alongside it as a strict secondary metric.
- **Stricter numeric tolerances.** Tighter thresholds on rounding and precision drift. Answers that previously passed under v1.1’s looser tolerance now fail.
- **Expanded harness.** Adds `calculator` and `price_history` on top of the v1.1 tools.
- **Multi-run aggregation.** Every model is run three times; reported scores are mean-of-runs with standard error of the mean.
- **Expanded test set.** Larger held-out test split for tighter measurement.

### Question Design

Questions target the analytical depth expected of a 2nd or 3rd-year investment banking analyst. Each question was designed to satisfy four criteria:

- **Determinism.** A single, unambiguous correct answer with no room for competing interpretations.
- **Multi-source synthesis.** Answers require chaining information across multiple filings or data sources rather than a single lookup.
- **Domain specificity.** Questions require implicit industry knowledge that follows sector convention rather than explicit instruction.
- **Forensic precision.** Critical information is frequently buried in footnotes, MD&A caveats, or accounting policy disclosures.

### Dataset

The dataset is divided into three parts: Public (27 open-source samples), Private Validation (450 samples available for license), and Test (450 samples).

- The Public set and agent harness are fully open in the [Finance Agent v2 GitHub repository](https://github.com/vals-ai/finance-agent-v2).
- The Private Validation set is available for license. Interested parties are encouraged to [contact us](mailto:contact@vals.ai) directly for access.
- The Test set will remain private. All results reported on this page are based solely on the Test set to prevent overfitting.

The dataset splits were sampled to preserve the distribution of question categories and difficulty.

### Question Taxonomy

Finance Agent v2 organizes questions into nine analytical categories reflecting real equity-research workflows.

#### General Qualitative Analysis

Summarization and comparison of fundamental filing sections: business model, risk factors, MD&A, and standard disclosures across companies.

> Compare Walmart, Costco, and Target’s capital allocation priorities across capex, dividends, share repurchases, and debt management.

#### General Quantitative Analysis

Extraction and calculation of reported financials such as revenue growth, CAGR, leverage ratios, and executive compensation — often requiring verification against restated historicals.

> Compare Home Depot and Lowe’s FY2024 inventory efficiency and calculate the difference in days inventory outstanding.

#### Market Analysis

Relative trading performance, total shareholder return, and how news cycles or guidance shifts drive stock volatility relative to sector indices.

> Measure Sun Communities’ stock reaction after the announced sale of Safe Harbor Marinas, then relate the move to the company’s stated use of proceeds.

#### Comparables

Building trading comps tables, calculating EV multiples, and normalizing enterprise value across peers by adjusting for off-balance-sheet items buried in footnotes.

> Rank major U.S. banks by excess CET1 ratio relative to their regulatory minimums.

#### Precedents

Analyzing M&A transaction multiples from S-4 filings and target financials, with industry-specific EBITDA normalization (e.g. exploration expense add-backs in Oil & Gas).

> Extract enterprise values and EV/EBITDA multiples for recent industrial distribution acquisitions and rank the transactions by pre-synergy multiple.

#### Adjustments

Bridging GAAP to non-GAAP or pro forma figures by reconciling SBC, acquired intangible amortization, and other non-cash items across the P&L and cash flow statement.

> Reconcile Honeywell’s GAAP operating income to segment profit across annual releases and identify newly introduced adjustment categories.

#### Earnings Analysis

Comparing reported results against consensus estimates and prior guidance, including non-GAAP reconciliations across consecutive quarterly reporting cycles.

> Compare Rapid7’s Q3 2025 actuals against prior revenue, non-GAAP operating income, and ARR guidance.

#### Disclosure Analysis

Tracking shifts in MD&A language, KPI definitions, and segment reporting methodology across multiple annual filings, then restating prior periods to reflect the new format.

> Track Boeing’s segment reporting and 787 cost-recovery disclosures across FY2022-FY2024 10-K filings.

#### Financial Modeling

Multi-step frameworks including DCF/NPV, LBO, and M&A accretion/dilution models built from historical ratios extracted from primary filings.

> Assess whether Ralph Lauren could justify a distressed acquisition of Capri under stated synergy, margin, and valuation assumptions.

---

## Acknowledgements

We would like to thank Andrew Schettino and all of the financial experts who worked on Finance Agent v2.

---

## Citation

If you use this benchmark in your research, please cite the [paper](https://arxiv.org/abs/2508.00828).

### Citation (BibTeX)

```
@misc{bigeard2025fab,
title        = {Finance Agent Benchmark: Benchmarking LLMs on Real-world Financial Research Tasks},
author       = {Bigeard, Antoine and Nashold, Langston and Krishnan, Rayan and Wu, Shirley},
year         = {2025},
month        = may,
howpublished = {Vals AI},
url          = {https://arxiv.org/abs/2508.00828},
}
```