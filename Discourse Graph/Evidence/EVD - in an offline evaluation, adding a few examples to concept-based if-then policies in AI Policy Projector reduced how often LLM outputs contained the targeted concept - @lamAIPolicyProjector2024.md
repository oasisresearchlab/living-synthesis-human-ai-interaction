---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e91-22f4-7baf-958c-561d85b3d5b9
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W07 (2025-03-12)]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> - Joel Chan's notes on Section 7 of [[@lamAIPolicyProjector2024]]: "neat validation of concept classification components, and then steering in offline study." (SP-25 W07 notes)
> ![[RiZw2ITBI8.png]]
> ![[94_sNJ_Swz.png]]
> - In discussion: "for this policy, for this concept ... it kind of works. We see less of the undesirable behavior once we add a few examples." (Joel Chan, SP-25 W07, [00:47:16]–[00:47:47])
> - A participant noticed that for graphic violence there was no change between the n=3 and n=5 conditions, while the other concepts kept improving. Joel Chan's reading: it is probabilistic, and after three examples there may be little of that concept left to remove. (SP-25 seminar discussion, [00:48:00]–[00:49:04])

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> Proportion of LLM outputs that contained the targeted concept (as judged by the system's concept classifiers), with error bars, across numbers of steering examples (e.g., 3 vs. 5). (SP-25 W07, [00:49:00]; see figure)

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> Offline evaluation. Concept-based if-then policies were applied with a varying number of added examples of the desired behavior. Steering was by prompting, not fine-tuning. (Joel Chan, SP-25 W07, [00:30:55], [00:49:04])

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> Offline, model-based; no human participants. Results depend on the underlying model. (Joel Chan, SP-25 W07 notes)

## Other Notes
Claude:
> "In the general case, we don't know under what conditions it's gonna succeed versus fail." (Joel Chan, SP-25 W07, [00:47:47])

## Suggested relations
Claude:
> - supports → [[CLM - concept-based if-then policy + easy access to more training examples may be a powerful combination for enabling better steering]]
> - supports → [[CLM - the same natural-language LLM policies can be enforced at the prompt level or by fine-tuning model weights, so policy design tools can be decoupled from the enforcement mechanism]]
> - informs → [[ART - AI Policy Projector]]
