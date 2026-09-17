# Project Plan — Final

**Status:** Final — mentor-confirmed version supplied by the user on 6 September 2026.

**Duration:** Two-month internship, organized into Weeks 1–8.

**Authority:** This document supersedes earlier project plans and phase schedules.

The confirmed brief is reproduced below with Markdown formatting normalized.
Original wording, including the missing company-count number, is retained.
Execution plans and wording questions are maintained separately in
[the Week 2 plan](weekly/week-02-plan.md) and the current
[Weeks 3–5 plan](weekly/week-03-05-plan.md). The overview is supplied project
context; its industry claims require research citations before use as findings.

## 1. Project Overview

The rapid advancement of LLM has opened transformative possibilities for the
asset management industry. While global leaders such as BlackRock, Goldman Sachs
and JPM have already proprietary LLMs into their research, compliance, and
client-service workflows, Onshore mutual fund is still in the early stages of
exploration. This project aims ti conduct a systematic feasibility study on
locally deploying (on-premise) LLMs within MSIM China, complemented by a
comprehensive survey of existing AI adoption cases across the industry.

The project is designed for a summer quantitative intern and will produce a
structured research report that provides actionable insights for our departments’
technology roadmap.

## 2. Project Objectives

### Primary Objective

Evaluate the technical, financial, and regulatory feasibility of deploying
open-source or commercial LLMs on-premise with MSIM China/COD infrastructure,
covering model selection, hardware requirements, data security and compliance
with Morgan Stanley and CSRC guidelines.

### Secondary Objective

Conduct a landscape survey of AI/LLM adoption cases among China’s top tier fund
houses, including specific use cases, technology stacks, and observed outcomes.

Identify high-impact, low risk pilot applications suitable for a quant research
desk, such as earnings-call summarization, research report drafting assistance,
sentiment analysis on financial news, model building vibe coding, and automated
compliance checking for fund outcomes.

Benchmark available open source LLMs on metrics relevant to financial NLP tasks,
including named entity recognition, financial question answering, and
multi-document summarization.

Estimate total cost of ownership (TCO) for a production-grade on-premise
deployment, including GPU server procurement, electricity, cooling, maintenance,
and personnel costs.

## 3. Scope of Work

### Phase 1: Week 1 / Week 2: Industry Research

Compile a structured database of at least onshore mutual fund companies that
have publicly disclosed AI/LLM initiatives, categorizing then by asset size, use
case (research, trading, risk, marketing, compliance), and technology partner.

Summarize key regulatory filings and MRM/CSRC guidance on AI usage in financial
institutions, with emphasis on data privacy, model interpretability, and
outsourcing restrictions.

### Phase 2: Week 3 - Week 5: Technical Feasibility Assessment

Survey and compare 5-8 open-source LLMs with language proficiency, evaluating them
on model size, inference speed, fine-tuning requirements, and community support.

Design a reference architecture for on-premise deployment, covering hardware
specifications (GPU Cluster, storage, networking), software stack (inference
engine, vector database, orchestration), and network security considerations.

Conduct a small-scale proof-of-concept: deploy one open-source model on a local
GPU workstation, test inference latency, and run a sample financial NLP task.

### Phase 3: Week 6 - Week 8: Cost-benefit Analysis & Recommendations

Build a TCO model comparing on-premise deployment versus API-based consumption of
commercial LLM services (such as OAI, anthropic, Deepseek etc) over a 3-year
horizon, incorporating volume-based pricing, data egress fees, and security
premiums.

Identify 3-5 pilot project candidates with clear ROI metrics, prioritized by
implementation complexity and regulatory risk.

Produce a final research report with executive summary, methodology, findings
and recommended next steps.

## 4. Expected Outcomes

Upon completion, the department will obtain:

- A structured knowledge base of AI/LLM practices across onshore mutual fund
  industry, enabling benchmarking and competitive intelligence.
- A technical reference architecture with hardware and software specifications
  for on-premise LLM deployment, tailored to the constraints of MSIMC/COD IT
  environment.
- A TCO comparison model that quantifies the financial trade-offs between
  on-premise LLM deployment and cloud-based LLM consumption.
- A prioritized pilot roadmap with 2-5 concrete project proposals, each with
  estimated effort, cost, and expected impact.
- A reusable evaluation framework for assessing future LLM models and
  infrastructure options.

## Mentor Clarifications

- COD infrastructure is the infrastructure used in MSIM.
- MRM is model risk management.
