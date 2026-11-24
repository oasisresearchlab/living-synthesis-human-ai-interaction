---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e91-8cb6-7fde-a6bd-f21ba8e1c012
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W05 Explainability]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> From the abstract of [[@hossainAnalysisNegationNatural2022]]: eight popular corpora spanning six NLU tasks "have few negations compared to general-purpose English, and ... the few negations in them are often unimportant". State-of-the-art transformers trained on them "obtain substantially worse results with instances that contain negation, especially if the negations are important".

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> Frequency and importance of negations in corpora; model results on instances with and without (important) negation.

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> Corpus analysis plus model experiments.

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> Eight NLU corpora; state-of-the-art transformers trained on them.

## Other Notes
Claude:
> - Shared by Joel Chan in a reply about "absence of concept versus negative concept" in SMILY's refine-by-concept tool (S11 and Joel Chan, SP-24 W05). Grounded only in the abstract as pasted into the seminar notes.
> - Suggests a data explanation: models rarely see negation that matters.

## Suggested relations
Claude:
> - supports → [[CLM - transformer language models, even large ones, systematically struggle with negation]]
