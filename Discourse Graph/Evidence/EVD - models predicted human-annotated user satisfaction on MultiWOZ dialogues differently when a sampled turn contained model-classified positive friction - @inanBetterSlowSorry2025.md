---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e91-c16f-759c-acf8-4fd3a113d88b
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W14 (2025-04-30)]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> Section 4.2 holds the claims the authors are most excited about. Joel Chan's reading of the satisfaction experiment (Section 4.1), offered because S01 and S05 found it confusing: "the claim is that model predictions of user satisfaction got worse," with satisfaction estimated by human annotators rather than measured algorithmically. (Joel Chan, Safety Inspection Expert thread, SP-25 W14)
> ![[dczM0R1ZP-.png]]
> ![[-fSzq1526a.png]]
> ![[_RuBI8xO8Q.png]]

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> How well a model's predictions match human-annotated user-satisfaction scores (1-5, per turn and per dialogue), compared across dialogues with and without model-classified positive friction in a randomly sampled turn.

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> 1. Take the subset of [[ART - Multi-Domain Wizard-of-Oz dataset (MultiWOZ)]] annotated for user satisfaction in [[@sunSimulatingUserSatisfaction2021]] (40 annotators; Fleiss kappa ~0.574).
> 2. Have a model predict those scores for a given conversation (prompting language models "to infer the intensity of user beliefs on a continuous scale").
> 3. Compare alignment with the human scores depending on whether a sampled turn contains positive friction, as classified by a model.
> (Joel Chan, SP-25 W14)
> ![[ivMd7X57Ew.png]]
> ![[vg4lZTg0Qy.png]]

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> Crowdsourced MultiWOZ dialogues; satisfaction labels from [[@sunSimulatingUserSatisfaction2021]]'s annotators.

## Other Notes

Claude:
> S01 asked where "the average anticipated user satisfaction of the annotation cohort" comes from and how it relates to LM-inferred scores. S05 asked how user satisfaction could be "measured algorithmically" and was misled by the word "experimental" into expecting a study with participants. (S01, S05, SP-25 W14) Treat this node's wording as Joel Chan's interpretation, not a verified reading of the paper.

## Suggested relations
Claude:
> - informs → [[CLM - LLM-simulated users are defensible for theorizing only when clearly distinguished from empirical observation of the people one wants to make claims about]]: an example of model-estimated outcomes standing in for user experience
