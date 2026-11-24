---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e90-8ba7-74f6-a102-d0cef2194bd0
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W10 (2025-04-02)]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> Some features (e.g., neutrality) had multifaceted steering effects, reducing a variety of undesirable biases at once (👩🏽‍🔬 Distiller thread, SP-25 W10).
> ![[QMoNf5_Qf-.png]]

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
> A positive counterpart to the off-target finding ([[EVD - steering a gender-bias SAE feature in an Anthropic LLM also shifted age bias, an off-target effect - @durmusEvaluatingFeatureSteering2024]]): cross-dimension effects are not always unwanted.

## Suggested relations
Claude:
> - informs → [[CLM - SAE features that are monosemantic in what they represent are not independent when used as steering knobs, because concepts are entangled in the model and in the world]]: features are not independent knobs, but their spillover can be beneficial
> - informs → [[PTN - feature steering]]: suggests broad features may be more useful steering targets than narrow ones
