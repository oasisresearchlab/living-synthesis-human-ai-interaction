---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e91-0f12-79e8-bc87-d37c3a39aa4a
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W12 (2025-04-16)]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> The paper includes a latency analysis (section 5.5): each query to the model adds about 1.47 seconds (SP-25 W12, [00:17:00]). As the seminar read it, the authors logged study actions and replayed them after the study to measure model response time ("we performed a ... analysis to measure the latency due to the model response time") (SP-25 W12, [00:18:54]).
> - Joel Chan used the number to frame the trade-off: "what's the likelihood that as a skilled programmer, you can make the edit that you want in about a second?" (SP-25 W12, [00:17:30])

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> Model response latency per query.

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> Post-hoc replay of logged study actions against the model to time responses (as interpreted in the seminar; the transcript is uncertain on details).

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> Study sessions from the 24-participant DynaVis evaluation; model was GPT-3.5 {W % '00:20:25'}.

## Other Notes

## Suggested relations
Claude:
> - supports → [[CLM - synthesizing persistent GUI widgets from natural language edits removes the LLM round trip from later tweaks, which cuts the latency of iterative editing]]: once a widget exists, tweaks avoid this per-query cost (SP-25 W12, [00:28:50])
> - supports → [[CLM - for programmers fluent in the underlying specification language, editing code directly can be faster than LLM-mediated editing]]: the latency is the bar a fluent programmer has to beat (SP-25 W12, [00:17:30])
