---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e91-8bac-777f-9f96-e354dbe2380d
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W05 Explainability]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> Figure 6 of [[@caiHumanCenteredToolsCoping2019]]: "Participants interleaved between different refinement tools, using a variety of strategies to emphasize and de-emphasize clinical features." It shows how 6 participants used refine-by-region, refine-by-example, and refine-by-concept over about 1000 seconds on the same prostate cancer case.
> ![[1VIJKBzhhf.png]]
> (Shared by S05 under "Tool usage and pattern", SP-24 W05)
> The paper also describes pathologists using refinement to iteratively track the likelihood of a hypothesis and to generate new ideas. (S05, SP-24 W05)

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> Time-stamped refinement tool uses per participant, by tool type.

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> Within-subjects study: each pathologist completed 6 diagnosis cases covering 3 image types, 3 with SMILY and 3 with conventional tools, with conditions counterbalanced. Subjective measures were collected after each trial. (S05, 👩🏽‍🔬 Distiller, SP-24 W05)

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> Practicing pathologists. The tool-usage figure shows "half (6)" of participants because of counterbalancing, which implies 12 participants. (S05, SP-24 W05)

## Other Notes


## Suggested relations
Claude:
> - supports → [[CLM - expert users' information needs shift moment to moment with their current hypothesis, so AI decision aids need user-controllable notions of similarity]]: tool use shifted within a single case
> - supports → [[PTN - Interactive refinement]]
