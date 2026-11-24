---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e94-69ab-7182-9b4c-48f10b013d7e
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W13-16 Evaluation and accountability]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> Some nurses dissuaded patients from participating, because a positive result could cause unnecessary hardship. At one clinic, nurses told patients that a positive result would mean referral to a hospital an hour away. (S11, Distiller, SP-24 W13)
> > "Some people aren't ready to go so won't join the research. 40-50% don't join because they think they have to go to the hospital." (P6)
> ![[EojEjWJgzv.png]]
> Nurses also sometimes urged patients not to follow the referral, with evidence for why the model's output shouldn't be trusted, which added to their own burden. (S11, Distiller, SP-24 W13)
> ![[3wVQqeC3A4.png]]

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> Observation of consent and referral conversations, and nurse interviews.

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> Post-deployment observation and interviews in the same field study (S11, Distiller, SP-24 W13).

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> Nurses and patients at clinics in Pathum Thani, Thailand.

## Other Notes

Claude:
> S05 (Safety Inspection Expert, SP-24 W13) tied this to the cost of false positives: referral brings financial, travel, and emotional costs for patients, which the paper's error trade-off did not fully discuss.

## Suggested relations
Claude:
> - supports → [[CLM - the real-world value of a clinical AI system depends as much on its fit with local workflows, environments, and infrastructure as on its model accuracy]]: travel costs and the referral pathway shaped whether the system was used at all
> - informs → [[QUE - How should the relative costs of false positives and false negatives in a clinical AI system be decided, and by whom?]]: the cost of a false positive was carried by patients, and nurses acted on it
> - informs → [[QUE - How can one evaluate deep learning models in clinical settings?]]: consent is itself shaped by local consequences
> - derived from → [[@beede2020humancentered]]
