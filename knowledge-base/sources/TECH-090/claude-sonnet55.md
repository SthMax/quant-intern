# Claude Sonnet 5.5
URL: https://platform.claude.com/docs/en/models/sonnet-5-5/overview

Latest. Released September 28, 2026.

The best combination of speed and intelligence

Model ID: `claude-sonnet-5-5`

Context window: 1M tokens · Max output: 128K tokens · Input pricing: $2 / MTok · Output pricing: $10 / MTok

Announcement · What’s new · Migration guide

## Overview

Claude Sonnet 5.5 offers the best combination of speed and intelligence. Five breaking changes affect code already running on Claude Sonnet 5:

- Turn off up-front thinking with `between_tools`.
- Forced tool use returns an error.
- Thinking blocks are tied to the model and the conversation.
- On the Claude API and Google Cloud, the earlier `computer_20251124` computer use tool is not accepted.
- The advisor tool rejects Claude Opus 4.8, Claude Opus 4.7, Claude Sonnet 5, and Claude Haiku 5.5 as advisors.

One more change alters the response shape without failing any request: text between tool calls comes back in `thinking` blocks. An application that streams that text to its users goes quiet between tool calls until it sets a `display` value that returns the text, or turns off up-front thinking with `between_tools`.

What's new in Claude Sonnet 5.5

## How it compares

| Model | Context | Max output | Price / MTok | Latency | Thinking | Default effort | Knowledge cutoff |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Fable 5.1 | 1M | 128K | $10 / $50 | Slower | Adaptive (always on) | `high` | Jun 2026 |
| Claude Opus 5.5 | 1M | 128K | $4 / $20 | Moderate | Adaptive (always on) | `medium` | Jun 2026 |
| Claude Sonnet 5.5 (this model) | 1M | 128K | $2 / $10 | Fast | Adaptive | `high` | Jun 2026 |
| Claude Haiku 5.5 | 1M | 128K | From $0.10 / $0.50 | Fastest | Adaptive | `medium` | Jun 2026 |

- Context: 1M tokens is roughly 555k words or 2.5M Unicode characters on the current tokenizer (introduced with Claude Opus 4.7); models before it fit about 750k words in 1M tokens. 200k tokens is roughly 150k words.
- Max output: Synchronous Messages API limit. On the Message Batches API, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, Claude Sonnet 5, Claude Haiku 5.5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6 support up to 300k output tokens with the output-300k-2026-03-24 beta header.
- Price / MTok: Input / output, base price per million tokens. Batch API requests are 50% off; prompt caching reads cost 10% of the base input price (2.5% on Claude Fable 5.1 and Claude Mythos 5.1, 5% on Claude Opus 5.5 and Claude Sonnet 5.5). See Pricing for the full list.
- Latency: Comparative latency, relative to the current lineup, as published in the models overview. Actual latency depends on prompt length, output length, and thinking effort.
- Thinking: Adaptive thinking lets the model decide how much to think, steered by effort. Extended thinking is the manual budget_tokens mode on earlier models.
- Default effort: The effort parameter’s default on the Claude API. Models without a value don’t support the parameter.
- Knowledge cutoff: Reliable knowledge cutoff: the date through which the model’s knowledge is most extensive and reliable.

## Specifications

### Model IDs

| Platform | Model ID |
| --- | --- |
| Claude API | `claude-sonnet-5-5` |
| Amazon Bedrock | `anthropic.claude-sonnet-5-5` |
| Google Cloud | `claude-sonnet-5-5` |
| Microsoft Foundry | `claude-sonnet-5-5` |
| Claude Platform on AWS | `claude-sonnet-5-5` |

### Pricing

| Feature | Value |
| --- | --- |
| Input | $2 / MTok |
| Output | $10 / MTok |
| 5m cache write | $2.50 / MTok |
| 1h cache write | $4 / MTok |
| Cache read | $0.10 / MTok |
| Batch API | 50% discount on input and output |

Full price list

### Capabilities

| Feature | Value |
| --- | --- |
| Context window | 1M tokens |
| Max output | 128K tokens |
| Max output (Batch API, beta) | 300K tokens |
| Thinking | Adaptive |
| Default effort | `high` |
| Comparative latency | Fast |
| Input → output | Text and images → text |
| Reliable knowledge cutoff | Jun 2026 |
| Training data cutoff | Jun 2026 |

### Availability

| Feature | Value |
| --- | --- |
| Status | Active (latest) |
| Released | September 28, 2026 |
| Retirement | Not sooner than September 28, 2027 |
| Platforms | Claude API, Amazon Bedrock, Google Cloud, Microsoft Foundry, Claude Platform on AWS |

## Good to know

- Adaptive thinking is on by default. The lowest thinking setting is `between_tools`, which turns off up-front thinking. It works at `high` effort or below. See What's new in Claude Sonnet 5.5.
- Setting `temperature`, `top_p`, or `top_k` to a non-default value returns a 400 error.
- The minimum cacheable prompt length is 512 tokens. See Prompt caching.
- On the Message Batches API, Claude Sonnet 5.5 supports up to 300k output tokens with the `output-300k-2026-03-24` beta header.
- Query limits and capabilities programmatically with the Models API.

## Resources

## Prompting Claude Sonnet 5.5

Behavioral differences and prompting patterns specific to Claude Sonnet 5.5.

## Effort

The control for thinking depth, latency, and cost. Choose a level per workload.

## Adaptive thinking

How adaptive thinking works, which thinking settings each model accepts, and how thinking blocks are preserved.

## Reference

## System prompt

The system prompt Claude Sonnet 5.5 uses on claude.ai and the Claude apps.

## System card

Safety evaluations and deployment decisions for Claude Sonnet 5.5.

## Pricing

Full price list, including batch discounts and prompt caching rates.

## Model IDs and versioning

How model IDs, aliases, and pinned snapshots work.

## Model deprecations

Lifecycle status and retirement commitments for every Claude model.
