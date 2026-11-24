---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e91-c0ec-79c3-acd7-d3a48c07e207
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W14 (2025-04-30)]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> The paper calls its annotators "expert". Joel Chan: "engineering students after short lecture on linguistic / cognitive science of positive friction --> EXPERT ANNOTATORS?????" with kappa agreement of ~0.4 (notes). In class he described it as "like 30% agreement, adjusted for chance," below the average kappa of about 0.7-0.8 one would want for gold-standard labels: "they actually disagree more often than they agree" on whether a turn is positive friction and of what kind. (Joel Chan, SP-25 W14, notes and [00:45:07])
> ![[wAfFdRPQ9i.png]]
> ![[WglwwCgs53.png]]

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> Category labels of positive friction on dialogue turns; inter-annotator agreement (kappa).

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> Annotators received a short lecture on the linguistics and cognitive science of positive friction, then labeled turns. A student asked whether low agreement came from poorly defined categories; Joel Chan: "that's probably part of it," the other part being the annotators. (SP-25 seminar discussion, SP-25 W14, [00:45:29])

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> 10 engineering undergraduate students, annotating [[ART - Multi-Domain Wizard-of-Oz dataset (MultiWOZ)]] and [[ART - TEACh dataset]]. Nothing else is reported about them. (Joel Chan, SP-25 W14, [00:18:23])

## Other Notes

Claude:
> Consequence for the paper: "I have had a hard time trusting any of these results ... the sampling is so noisy that ... the error bars are hard for me to trust." (Joel Chan, SP-25 W14, [00:46:39]) S11 expected reviewers to raise the same concerns, since the paper was posted to arXiv before the ACL deadline and has not appeared in any *ACL proceedings. (S11, SP-25 W14)

## Suggested relations
Claude:
> - supports → [[CLM - who annotators are and what they know shapes model evaluations and training signals, yet NLP papers often treat annotators as black boxes]]
> - opposes → [[EVD - models predicted human-annotated user satisfaction on MultiWOZ dialogues differently when a sampled turn contained model-classified positive friction - @inanBetterSlowSorry2025]]: undermines trust in the downstream analyses that rely on these labels (Joel Chan, SP-25 W14, [00:46:39])
