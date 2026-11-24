---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e94-8c41-7e8a-a6fc-9452e3d31ddd
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W13-16 Evaluation and accountability]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> For AAPF, "While the articles returned were overall much more relevant than the previous, general model, many were still false positives, despite few false positives on our internal dataset. Specifically, of the 37 cases returned between 12/07/21 and 12/24/21, 12 described cases of Black women killed by the police." (p. 675)
> ![[87vdRqQ9wJ.png]]
> Joel Chan (SP-24 W16): about a 67% false positive rate, i.e., Precision@37 of 0.32, "way less than the ~.9 they got in internal testing".

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> Number of returned articles describing relevant cases.

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> Stage 2 deployment on the Email Alerts system with contextual hybrid models, on unseen articles.

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> Articles returned for the AAPF project in December 2021.

## Other Notes

Claude:
> Fewer articles were returned overall than with the original model (p. 675). Joel asked whether the threshold stayed the same, and noted there's no clear quantitative comparison with the old false positive rate (SP-24 W16).

## Suggested relations
Claude:
> - supports → [[CLM - ML model performance measured on internal test data often drops substantially in real-world deployment]]
> - informs → [[ART - Email Alerts system for feminicide counterdata collection]]
> - informs → [[CLM - classifiers trained on news articles can perpetuate the erasure of marginalized victims because news coverage misgenders people and omits race]]: the paper ties this to the difficulty of logging feminicides for an intersectional subgroup
