---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e92-0338-71a4-bfa3-9273f1bc4809
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W05 (2025-02-26)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Use a model (an ML model or another LLM) to explore variations of a prompt and return the one that best produces the desired behavior, so the human does not have to find a good prompt by hand. Raised in the session as the opposite design choice from [[PTN - interactive natural language critique]]: there the human discovers and articulates what to change; here the search is automated. (SP-25 W05, Joel Chan, [00:11:51]–[00:12:38])
> - Motivation: prompt engineering is "still like a dark art", and prompts that work well for text-to-image models can be "almost like programs" rather than natural language ([00:12:30]–[00:12:38]).


## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - DSPy]] ([00:12:08])

## Other Notes

## Suggested relations
Claude:
> - informs → [[PTN - prompt engineering]]: automates the search that prompt engineering does by hand
> - inconsistent with → [[PTN - interactive natural language critique]]: the human is taken out of the loop rather than scaffolded within it (SP-25 W05, [00:12:08])
