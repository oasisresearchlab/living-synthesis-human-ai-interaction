---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e70-661d-7d8d-b994-4ffb6280bff5
NodeFormality: draft
TruthValue: 0.5
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/Zpesacem6
roamAuthor: "Joel Chan"
created: 2025-03-24
---
## Grounds

Claude:
> From the offline evaluation in [[@lamAIPolicyProjector2024]] ([[ART - AI Policy Projector]]): a neat validation of the concept classification components, and then of steering. Adding a few examples to a concept-based if-then policy reduced the undesirable concept in outputs. (Joel Chan, SP-25 seminar)
> ![[94_sNJ_Swz.png]]
> - Take with a grain of salt: results depend on the underlying model, and the key contribution is the interactive framework, which can (at least theoretically) plug and play different models under the hood.
> ![[RiZw2ITBI8.png]]
> - In discussion, a student noticed that for "graphic violence" there was no change between 3 and 5 examples while other concepts kept improving. The reading offered in discussion: it is probabilistic, and after 3 examples there may not be much more of that concept left to remove. Implicit in the design: you give the principle (the if-then rule) and can additionally provide examples showing what the behavior looks like. (SP-25 seminar discussion)
> - Caveat: to what extent LLMs can actually be aligned via prompting is a live research question; the results show it "kind of works" for these policies and concepts, but not under what conditions it will succeed or fail in general. (SP-25 seminar discussion)

## Other Notes

Claude:
> Related: [[CLM - If-then statements support transparent and interpretable LLM policy formulation]] and [[CLM - LLM-generated and custom-defined natural language concepts --- with mappings to example LLM outputs that contain those concepts --- support interpretable exploration of LLM output patterns]].
