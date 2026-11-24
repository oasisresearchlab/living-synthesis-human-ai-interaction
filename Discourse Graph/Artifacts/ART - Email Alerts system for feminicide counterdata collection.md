---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e94-8b47-7f5c-890c-5d04a8d09057
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W13-16 Evaluation and accountability]]"
created: 2026-11-24
---
## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> Helps activists who collect and monitor data about feminicide (gender-related killings of women and girls) find relevant news articles, so they don't have to comb through irrelevant ones by hand. (S08, Distiller, SP-24 W16, from Suresh et al. 2022)

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> ML classifiers deliver relevant news articles through an Email Alerts system. A general model worked for general cases but not for cases specific to people of color, so the team redesigned with two partners: the Sovereign Bodies Institute (SBI), tracking missing and murdered Indigenous women, girls, and two-spirit people (MMIWG2), and the African American Policy Forum (AAPF), monitoring police violence against Black women (#SayHerName). (S08, SP-24 W16)
> - Data collection shifted to previously collected relevant cases, even for negatives; articles got multiple annotations, so models "explicitly take into account the ways in which different systems of oppression manifest and interplay".
> - Model variants: joint, hybrid, contextual hybrid.
> ![[vv8d5dbMCL.png]]
> - Evaluation: cross-validation, then a monitoring phase on out-of-distribution data in deployment, and "extended, participatory evaluation with the partner organization".

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

Claude:
> Deployed contextual hybrid models for AAPF and SBI. See [[EVD - in deployment, a contextual hybrid classifier for police killings of Black women returned 12 relevant cases out of 37 articles, despite few false positives in internal testing - Suresh et al 2022]] and [[EVD - in deployment, a contextual hybrid classifier for missing and murdered Indigenous women returned 10 of 20 articles describing specific cases - Suresh et al 2022]].

## Other Notes

Claude:
> S08 didn't follow the modeling section; Joel Chan flagged "how they translate their theoretical perspectives to modeling details" as worth discussing (SP-24 W16).

## Suggested relations
Claude:
> - instantiates → [[PTN - co-designing datasets and ML models with affected communities]]
> - instantiates → [[PTN - participation as justice vs participation as work]]
> - derived from → [[THE - Data Feminism]]
