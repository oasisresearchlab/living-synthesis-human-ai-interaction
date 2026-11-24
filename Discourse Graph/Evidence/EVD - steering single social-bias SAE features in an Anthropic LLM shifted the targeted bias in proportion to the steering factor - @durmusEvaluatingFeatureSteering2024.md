---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e90-c371-7593-b118-ce13c8e847c1
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W10 (2025-04-02)]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> Steering a feature expected to increase or reduce a target bias moved that target accordingly, in proportion to the steering factor (👩🏽‍🔬 Distiller thread, SP-25 W10).
> ![[Ja5Pz73HHr.png]]
> ![[sUF1K4bUqk.png]]
> ![[c-fwAiq1rz.png]]
> Joel Chan glossed the result: the hope was to find really specific knobs, and the quantitative curves show "when you reliably turn this up or down, it changes in this way" (SP-25 W10, [00:41:23]).

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
> This is the on-target half of the result. Read it with [[EVD - steering a gender-bias SAE feature in an Anthropic LLM also shifted age bias, an off-target effect - @durmusEvaluatingFeatureSteering2024]] and [[EVD - the amount of output change per unit of steering varied widely across the SAE features evaluated, with some features barely moving the outputs - @durmusEvaluatingFeatureSteering2024]]: on-target effects were present but not isolated, and not uniform across features.

## Suggested relations
Claude:
> - supports → [[CLM - prompting is a more accessible steering mechanism than feature steering for non-technical users, but feature steering may offer more predictable dose-response control]]: on-target dose-response curves are the basis for the claim that feature knobs could be more predictable than prompts (Joel Chan, [00:41:40])
> - informs → [[PTN - feature steering]]: first quantitative evaluation of how well the pattern works for social bias (seminar discussion, [00:40:21])
