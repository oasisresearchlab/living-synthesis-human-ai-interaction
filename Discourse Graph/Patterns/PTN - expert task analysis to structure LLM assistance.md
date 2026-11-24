---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e92-25f1-778e-9b0f-33733c81a210
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W03 (2025-02-12)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Instead of asking an LLM to do a whole expert task at once, run a task analysis of how experts actually do it (e.g., from transcripts), then have the model work through those expert sub-steps in order.
> - Joel Chan on Rose Wang's tutoring work: "she did like a task analysis of what good tutors do when they're tutoring in math" from "actual chat transcripts of ... expert tutors", found recurring strategies like "first they try to identify the error and then they devise a strategy and then they describe ... intention", and had "the LLM sort of tune for each of these subtasks. So it doesn't do the whole thing at once" (SP-25 W03, [00:17:19]-[00:18:22]).
> - Contrasted with deriving primitives from LLM capability demos, as in AI Chains ([00:15:39]-[00:16:07]). In the notes, Joel Chan described this as "embed[ding] expert-like thinking in models" and wondered "how this compares to approach of cognitive modeling and knowledge components".

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - Tutor CoPilot]]
> - [[ART - Bridge (Wang et al. 2024)]]

## Other Notes

## Suggested relations

Claude:
> - informs → [[QUE - Should task decompositions for LLM chains come from catalogs of model capabilities or from task models of how experts actually do the task?]]
> - consistent with → [[PTN - LLM Chains]]: same decomposition, different source of the steps
> - consistent with → [[PTN - Articulation Work]]
