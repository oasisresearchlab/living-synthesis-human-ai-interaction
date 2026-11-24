---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e94-8bc7-7fa5-a154-7477b3448d66
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W13-16 Evaluation and accountability]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> "in internal testing w/ 5-fold cross-validation, hybrid and contextual hybrid seem better than a naive joint on AUC-ish metrics, but not really for Precision @K" (Joel Chan, SP-24 W16). AAPF: AUPRC 0.881/0.902/0.921 and AUROC 0.913/0.931/0.944 for joint/hybrid/contextual hybrid; Precision@50 was 1, 0.98, 0.98. (Table 3, p. 675)
> ![[N2pq3P-BeT.png]]

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> AUPRC, AUROC, Precision@50, and Precision@100 per model variant. Precision@K is asserted to be the key metric for downstream use (p. 674).
> ![[-MfS2b_AJK.png]]

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> 5-fold cross-validation on the collected datasets.

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> News article datasets for AAPF (police violence against Black women) and SBI (MMIWG2).

## Other Notes

Claude:
> Joel Chan (Safety Inspection Expert, SP-24 W16): on Precision@K "that seemed like a wash, and in any case, the numbers are super close". The joint model is claimed to equal the single-label baseline, but he wanted a direct comparison with the general model before Stage 1.

## Suggested relations
Claude:
> - opposes → [[CLM - designing AI with affected communities from the start is preferable to relying on retroactive audits of potentially flawed systems]]: weak evidence that the intersectional approach produces a better model
> - informs → [[ART - Email Alerts system for feminicide counterdata collection]]
