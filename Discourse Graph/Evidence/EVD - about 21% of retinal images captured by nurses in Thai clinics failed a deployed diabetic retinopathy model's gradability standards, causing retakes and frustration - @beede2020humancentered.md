---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e94-6750-7e0d-8900-fa83d237cfd6
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W13-16 Evaluation and accountability]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> Of the images nurses captured for the deep learning diabetic retinopathy (DR) system, 21% didn't meet its gradability standards. Non-darkened rooms and clinics not using dilation drops contributed. Nurses had to retake images even when they could read them themselves. (S11, Distiller, SP-24 W13)
> > "It gives guaranteed results, but it has some limitations. Some images are blurry, and I can still read it, but [the system] can't." (P6, p. 8; quoted by Joel Chan, Academic Researcher, SP-24 W13)
> ![[itLdNBgKVX.png]]

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> Observed screening sessions, nurse interviews, system logs, and model predictions/usage data from 1838 image uploads. (S11, Distiller, SP-24 W13)

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> Prospective, human-centered observational field study of a deployed system, before and after deployment; affinity notes written daily and affinity mapping of interview and observation data. (S11, Distiller, SP-24 W13)

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> Nurses and a camera technician running eye screening at clinics in Pathum Thani and Chiang Mai, Thailand. Post-deployment: 12 hours observing about 50 patients at 3 clinics, plus 7 hours of interviews with 5 nurses and a camera technician, via a Thai interpreter. (S11, Distiller, SP-24 W13)

## Other Notes

Claude:
> The system rejected lower-quality images by design, for patient safety: it was meant to decrease the chance of an incorrect assessment. (S11, Distiller, SP-24 W13)

## Suggested relations
Claude:
> - supports → [[CLM - input-quality thresholds tuned for accuracy in controlled settings can clash with real-world capture conditions and shift extra work onto frontline users]]: the strict threshold clashed with clinic conditions and added retakes
> - supports → [[CLM - the real-world value of a clinical AI system depends as much on its fit with local workflows, environments, and infrastructure as on its model accuracy]]: model accuracy didn't translate into a smooth screening workflow
> - informs → [[PTN - selective deferral to human experts for uncertain or low-quality inputs]]: nurses could read images the system rejected (Joel Chan, SP-24 W13)
> - derived from → [[@beede2020humancentered]]
