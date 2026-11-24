---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e90-8b4b-7366-ac46-7c498bc54f07
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W10 (2025-04-02)]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> Steering for a gender-bias SAE feature also ended up steering toward age bias (👩🏽‍🔬 Distiller thread, SP-25 W10).
> ![[ZZtfjI83-c.png]]
> ![[hLLDv2qDDj.png]]
> The authors' own limitations section: "Our steering experiments showed complex interactions and unexpected cross-domain effects, suggesting that individual features do not operate in isolation." (quoted by S11, 🍜 Academic Researcher, SP-25 W10)
> In discussion: "as you like tune it up... it also makes it more age biased" (SP-25 W10, [00:17:35]).

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
> Joel Chan's note on this result: it suggests the need to do more than individual feature steering, since there are complex higher-order interactions even between monosemantic features.
> ![[pUrxUAIxba.png]]

## Suggested relations
Claude:
> - supports → [[CLM - SAE features that are monosemantic in what they represent are not independent when used as steering knobs, because concepts are entangled in the model and in the world]]: direct empirical case of a monosemantic feature producing off-target effects
> - supports → [[CLM - feature steering is not yet reliable enough to give users precise, production-ready control over model behavior]]: off-target effects undercut confidence that a knob changes only one thing (Joel Chan, [00:20:00])
> - informs → [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]]: canonical example in that question's context
> - informs → [[QUE - How might interactions among model features (circuits) be modeled when the number of possible interactions is combinatorially large?]]: the authors propose circuits as the next step because of this result
