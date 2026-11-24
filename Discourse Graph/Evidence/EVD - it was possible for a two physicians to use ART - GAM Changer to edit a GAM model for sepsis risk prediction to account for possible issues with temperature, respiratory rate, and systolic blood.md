---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e70-661e-7c2e-b811-03b9cef3e3e2
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/2AwZIy0Vs
roamAuthor: "Joel Chan"
created: 2025-02-04
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> - A case study in [[@wangInterpretabilityThenWhat2022]]: physicians used [[ART - GAM Changer]] to edit a sepsis risk prediction model. (SP-25 seminar, discussion of evidence of efficacy with the 🚧 Safety Inspection Expert role)
> - Temperature: the shape function revealed granular misalignments in the curve, and the edits aimed to reduce potential false negatives related to temperature. The physician noted why weeding out these errors is so important in high-stakes clinical settings like this one.
> ![[gx0Dmlv_-l.png]]
> ![[vwjd7TIXFC.png]]
> - Respiratory rate (difference from age norm): the shape function's overall distribution seemed to match clinical knowledge. There was no physiological explanation for the dip below -21, so it was smoothed out, using a monotonic increase rather than smoothing (changing the shape function entirely) in order to keep a plateau that does have a physiological explanation.
> ![[JPuPLzpQFI.png]]
> - Systolic blood pressure: edits again considered minimizing the false negative rate.
> ![[-MSe8IQQkp.png]]
> ![[pd5w5aZpYX.png]]

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> - The edits physicians made to the model's shape functions, and their clinical rationale for each edit. (SP-25 seminar)

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> - Case study. The physician made the edits based on a random subset of 5k records (about 1/4 of the data), in discussion with the ML research team (the paper's authors). (SP-25 seminar)
> - The model: 7 continuous and 83(!) categorical features, with boosted trees as shape functions. It is fairly accurate overall (almost 90% AUC on the test set). (SP-25 seminar)
> ![[edOrKqTgI3.png]]
> ![[bHbMMTyQus.png]]

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> - Physicians (two, per the evidence statement), working with a sepsis risk prediction model. (SP-25 seminar)

## Other Notes
Claude:
> - "This diff between the consequences of a monotonic increase vs. linear interpolation seems super significant, but i wonder if the physician alone would have noticed it: seems **super** important that the discussion was with physician *and* ML research team (from the authors)! probably a requirement for usefulness in real-world settings" (Joel Chan, SP-25 seminar)
> - Cited later in SP-25, alongside [[EVD - data scientists successfully used ART - ChainForge to do systematic testing of their LLM pipelines - @arawjoChainForgeVisualToolkit2024]], as an example of the more in-the-wild deployments the seminar wanted to see. (SP-25 seminar)
