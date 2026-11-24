---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e92-04da-7955-b270-3559b153e5cb
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W05 (2025-02-26)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Use an LLM to compare user-authored principles pairwise, flag pairs that are at odds, and suggest a resolution. Proposed by the authors of [[@petridisConstitutionMakerInteractivelyCritiquing2024]] as future work: "One way to prevent potential principle conflicts is to leverage an LLM to conduct a pairwise comparison of principles to assess if any two are at odds, and then suggest a solution." (quoted by S14, Safety Inspection Expert thread, SP-25 W05 notes)
> - S14 flagged it as important and linked it to inter-rater reliability. (S14, SP-25 W05)


## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - Proposed, not built, for [[ART - ConstitutionMaker]].

## Other Notes

Claude:
> - Motivated by the finding that participants wrote conflicting principles even when working alone (Joel Chan, SP-25 W05, [00:40:47]–[00:41:00]).
> - It relies on the same unverified LLM judgment as the rest of the pipeline; see [[PTN - LLM-as-a-judge]] and [[QUE - What is the effectiveness of LLM-generated critiques?]].

## Suggested relations
Claude:
> - informs → [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]]: one concrete mechanism for reasoning about interactions between edits
> - informs → [[QUE - How to support users to design effective principles for steering LLMs?]]
> - uses → [[PTN - LLM-as-a-judge]]
