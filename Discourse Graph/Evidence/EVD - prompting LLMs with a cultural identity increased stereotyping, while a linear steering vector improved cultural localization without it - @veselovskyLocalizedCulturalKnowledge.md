---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e91-55ef-72d3-8a3e-559fe0bedd50
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W12 (2025-04-16)]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> Shared by Joel Chan under "cool stuff" at the start of the session, from a tweet thread (Joel had "not read this paper in detail") (SP-25 W12, [00:02:23]).
> - Focal example: "What color is a pumpkin?" The answer is generally orange, but in Japan it is green (SP-25 W12, [00:01:18]).
> - You can prompt with "what color is a pumpkin in Japan?" or "say I'm a Japanese person," but this increases stereotyping and reduces the diversity of the model's generations (SP-25 W12, [00:01:30]).
> - Adding a linear steering vector improves cultural localization "without sacrificing like diversity" (SP-25 W12, [00:01:53]); the notes record a reported 40% improvement for cultural localization (SP-25 W12 notes).
> - Author summary (Veniamin Veselovsky on X): steered generations "stay more faithful, less stereotypical, and more diverse than explicit prompting," suggesting "cultural knowledge is conserved within LLMs without using prompting; we just need new ways of accessing it." https://x.com/VminVsky/status/1912174727868694783

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> Cultural localization accuracy, stereotyping, and diversity of generations (as summarized secondhand; measures not checked).

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> Comparison of explicit prompting with cultural context versus a linear steering vector added to the model (per the tweet thread).

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> LLM generations on culturally localized questions; details not read in the seminar.

## Other Notes

## Suggested relations
Claude:
> - supports → [[CLM - explicit prompting cannot be assumed to steer LLMs faithfully toward culturally local or marginal perspectives]]: prompting with identity context induced stereotyping (SP-25 W12, [00:04:10])
> - supports → [[CLM - LLM-generated personas can flatten and caricature marginalized identity groups]]: partial evidence, per Joel Chan (SP-25 W12, [00:02:44])
> - instantiates → [[PTN - feature steering]]: linear steering vector as the alternative to prompting (SP-25 W12, [00:00:28])
