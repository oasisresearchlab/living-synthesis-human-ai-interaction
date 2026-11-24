---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e91-8c79-7ea7-b19e-7df5007927c6
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W05 Explainability]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> From the abstract of [[@jangCanLargeLanguage2022]]: on 9 tasks with negated prompts, the scaling law between LM size and zero-shot performance did not hold and instead showed "an inverse scaling law". All LM types "perform worse on negated prompts as they scale", with "a huge performance gap" compared with human performance.

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> Task performance on original vs. negated prompts across model sizes.

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> 9 tasks with negated prompts, comparing pretrained, instruction-tuned, few-shot, and negation-fine-tuned LMs.

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> OPT and GPT-3 (125M-175B), InstructGPT, plus human baselines.

## Other Notes
Claude:
> - Shared by Joel Chan in a reply about "absence of concept versus negative concept" in SMILY's refine-by-concept tool (S11 and Joel Chan, SP-24 W05). Grounded only in the abstract as pasted into the seminar notes.

## Suggested relations
Claude:
> - supports → [[CLM - transformer language models, even large ones, systematically struggle with negation]]
