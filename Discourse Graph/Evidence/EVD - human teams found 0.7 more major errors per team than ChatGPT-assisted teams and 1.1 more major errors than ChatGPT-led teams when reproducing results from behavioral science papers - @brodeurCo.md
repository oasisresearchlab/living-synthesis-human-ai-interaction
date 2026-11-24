---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e70-661d-7d5d-83a5-5f8a09336eb5
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/8EmtQhx-6
roamAuthor: "Joel Chan"
created: 2025-02-05
---

## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> Human-only teams found more major errors than ChatGPT-assisted or ChatGPT-led teams (Institute for Replication (I4R); [[@brodeurComparingHumanOnlyAIAssisted2025]]). From I4R on X: "human teams were also particularly effective at identifying serious major errors compared to both AI-assisted and AI-led teams. Specifically, human teams found 0.7 more major errors per team than AI-assisted teams and 1.1 more major errors than AI-led teams." (https://x.com/I4Replication/status/1881889414315688344)
> ![[HnbrK9XYpd.png]]
> ![[lFDwa4gr7A.png]]
> - Paper: https://www.econstor.eu/bitstream/10419/308508/1/I4R-DP195.pdf

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> - Reproduction of numerical results.
> - Coding errors and data irregularities detected, classified as major or minor (major = could have an impact on the claims tested).
> ![[ccxNAqclZm.png]] (p. 12)

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> - Three conditions: human-only (no ChatGPT); AI-assisted (ChatGPT plus access to the original papers; access to GPT-4 and GPT-4o but not o1-mini; teams got 1 hour of training on ChatGPT); AI-led (no access to the original paper, work only in ChatGPT).
> ![[9mxDZLbSyD.png]]
> ![[1CuBE0z-nm.png]]
> ![[M5a9kQBoxP.png]]
> - Analysis: OLS regression.
> - Data and code: https://osf.io/sz2g8/

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> - 103 teams (roughly 30-ish per condition), working on a sample of behavioral science papers published in "leading journals".
> ![[Rti8H2QKlu.png]]
> ![[eIHIbIwFcH.png]] (p. 10)

## Other Notes

Claude:
> Joel Chan shared this in an SP-25 seminar discussion of a model that performed well (~90% AUC on its test set), as "kinda related and i think a counterexample to the claimed general trend".
