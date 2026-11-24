---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e92-03bb-7c8c-873d-3d19e2922a02
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W05 (2025-02-26)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> When people don't always know what they want to change about an AI's output, have an LLM generate candidate feedback (and candidate rationales for it) that the user can pick from, edit, or replace with their own. This lowers the cost of articulating feedback and helps users notice things to critique.
> - In [[ART - ConstitutionMaker]]: "to address the thing where people don't always know what they want, they get an LM to generate examples of kudos, critiques, and rewrites. The user can pick from those and rewrite their own." Then the selected rationale is sent to a second LLM call that converts it into a principle. (Joel Chan, SP-25 W05, [00:30:56]–[00:31:26])
> - From [[@petridisConstitutionMakerInteractivelyCritiquing2024]]'s formative study, one need was to support users to identify things to critique. Joel Chan noted this "feels similar to the comparison stuff in chain forge". (SP-25 W05 notes, Distiller thread)
> ![[m9rTOPKOHK.png]]
> ![[tjDCpzCnrS.png]]


## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - ConstitutionMaker]] ([[@petridisConstitutionMakerInteractivelyCritiquing2024]])
> - [[ART - EvalGen]], where the LLM suggests evaluation criteria in natural language and users choose which to implement (S16, Archaeologist, SP-25 W05)

## Other Notes

Claude:
> - Open concern: how good are the LLM-generated suggestions and translations? Joel Chan: "I'm also really... really.... really wondering how good the translations are." (SP-25 W05 notes). See [[QUE - What is the effectiveness of LLM-generated critiques?]].

## Suggested relations
Claude:
> - enables → [[PTN - interactive natural language critique]]: makes it easier to produce critiques in the first place (SP-25 W05, [00:30:56])
> - informs → [[QUE - What is the effectiveness of LLM-generated critiques?]]: the quality of the suggestions is the open question
