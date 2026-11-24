---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e91-8cf2-7fbd-9613-b75824cc5891
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W05 Explainability]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> From the abstract of [[@testoniArtificialIntelligenceModels2022]]: in the GuessWhat?! visually grounded guessing game, "humans profit from negatively answered questions to solve the task, models struggle in grounding negation, and some of them barely use it". When the language signal is poorly informative, visual features help encode the negative information.

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> Guessing performance after negatively vs. positively answered polar questions.

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> Evaluation of LM-based guessers plus a crowdsourcing experiment with humans on a controlled sample of games, in the same settings.

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> Guessers built on pretrained language models; crowd workers.

## Other Notes
Claude:
> - Shared by Joel Chan in a reply about "absence of concept versus negative concept" in SMILY's refine-by-concept tool (S11 and Joel Chan, SP-24 W05). Grounded only in the abstract as pasted into the seminar notes.
> - Relevant to SMILY's image setting: visual context may make negation easier to process, for people and partly for models.

## Suggested relations
Claude:
> - supports → [[CLM - transformer language models, even large ones, systematically struggle with negation]]
> - informs → [[QUE - How should concept-based steering interfaces distinguish the absence of a concept from its negation?]]
