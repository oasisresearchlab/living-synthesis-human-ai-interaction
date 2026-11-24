---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e70-661e-75f4-aad1-12400da8dd7e
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/QevogpeDc
roamAuthor: "Joel Chan"
created: 2025-02-04
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> A case study in [[@wangInterpretabilityThenWhat2022]]: a physician and an ML researcher used [[ART - GAM Changer]] to edit a GAM for pneumonia risk prediction.
> - Editing the **age** feature, then checking the consequences for the overall model, including fairness by gender:
> ![[yjUpP5AUi7.png]]
> ![[iSmboABr6t.png]]
> - Editing the **asthma** feature:
> ![[3WbRvnSxxf.png]]

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> The edits made to the model and their effects on model behavior. The model had 19 continuous and 27 categorical features, with fairly high performance (AUC on the test set).

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> Case study of editing a trained GAM with the tool.

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> A physician and an ML researcher, working on a pneumonia risk prediction model.

## Other Notes
Claude:
> Discussed in the SP-25 seminar under "evidence of efficacy", alongside comments from the 🚧 Safety Inspection Expert role.
