---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e91-8c00-7bd5-84a7-52cf3b4e269f
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W05 Explainability]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> From [[@caiHumanCenteredToolsCoping2019]], "Disambiguating ML Errors from Self Errors": when faced with surprising results, pathologists wondered whether the algorithm was noisy or had seen something they missed ("I don't know why it's picking up PIN [Prostatic Intraepithelial Neoplasia] so much! Now I'm questioning myself"). "To test if the error was due to ML, pathologists removed variables they thought were leading the algorithm astray and repeated the search. Over time, some tried to remove these variables *preventatively*, by cropping out areas known to introduce noise. Thus, without providing an explicit explanation about how the algorithm works, SMILY implicitly gave users some insight by allowing them to test the algorithm."
> ![[2ILIVGnSjf.png]]
> (Shared by S05 under "Attribution of errors and responsibilities", SP-24 W05)

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> Qualitative observations and participant quotes during diagnosis with SMILY.

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> Within-subjects study: each pathologist completed 6 diagnosis cases covering 3 image types, 3 with SMILY and 3 with conventional tools, with conditions counterbalanced. Subjective measures were collected after each trial. (S05, 👩🏽‍🔬 Distiller, SP-24 W05)

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> Practicing pathologists. The tool-usage figure shows "half (6)" of participants because of counterbalancing, which implies 12 participants. (S05, SP-24 W05)

## Other Notes
Claude:
> - S05 also noted that participants developed a mental model of the ML, and asked about the "coupling" of human and ML in attributing errors and responsibility. (S05, SP-24 W05)

## Suggested relations
Claude:
> - supports → [[CLM - interactive refinement can help users cope with opaque ML models by letting them test the algorithm, without explicit explanations of how it works]]
> - informs → [[QUE - How do expert users attribute errors and responsibility between themselves and an AI tool when its results surprise them?]]
> - informs → [[THE - Algorithmic folk theories]]: users built a working model of the algorithm by testing it
