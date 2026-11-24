---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e90-8c67-7707-acbf-ad04b7de53ac
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W10 (2025-04-02)]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> Joel Chan, reading the on-target curves: "the sort of relationship between how much you're amping it up and how much is changing varies by particular knob, right? So like some of these like change a lot and some of them don't really change at all" (SP-25 W10, [00:24:41]).
> The seminar also noted that steering factors do not scale linearly: "if you do like negative seven five versus negative four five could result... it doesn't scale like that necessarily" (SP-25 W10, [00:24:00]).
> ![[sUF1K4bUqk.png]]

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> Bias scores on a social bias evaluation, plus off-target bias dimensions and general capability measures, as a function of the steering factor applied to each feature (see the evaluation overview figure below).
> ![[f7NQPZ1Wf-.png]]

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> Feature steering: clamp the activation of a single SAE feature to a multiple of its usual value (the seminar noted a range of roughly -5 to 5 steering factors; SP-25 W10, [00:23:55]) and measure how model outputs change on target and off target. Features came from SAE dictionary learning on the model's residual stream ([[PTN - Sparse Autoencoders (SAEs)]], [[PTN - feature steering]]).

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> An Anthropic production LLM and a set of 29 SAE features related to social bias, selected out of the very large number of features the SAE learned (Joel Chan, SP-25 W10, [00:46:00]).

## Other Notes
Claude:
> This observation is the seminar's reading of the paper's figures, not a statistic the authors reported. Joel Chan linked it to a similar pattern in [[ART - AI Policy Projector]], where some concepts improved after one round of added examples and others kept changing (SP-25 W10, [00:24:17]).

## Suggested relations
Claude:
> - supports → [[CLM - exposing model features as user-facing knobs requires users to understand both what a feature means and how output will change as its activation is scaled]]: users would need a per-feature expectation of how output responds
> - informs → [[PTN - feature sliders as interface controls for text generation]]: sliders would need per-feature calibration
