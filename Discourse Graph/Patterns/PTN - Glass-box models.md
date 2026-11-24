---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e70-661f-7edf-b536-c40868364e7a
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/TM51g9Zni
roamAuthor: "Joel Chan"
created: 2025-02-04
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.
Claude:
> A class of models whose internal structure is directly interpretable, such as GLMs and [[PTN - Generalized Additive Models (GAMS)]]. In the SP-25 seminar, GAMs came up as part of this class when discussing [[ART - GAM Changer]] ([[@wangInterpretabilityThenWhat2022]]).

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.
Claude:
> - [[ART - GAM Changer]] depends on glass-box models (GLMs/GAMs) to let domain experts edit models.

## Other Notes
Claude:
> - Joel Chan's working hypothesis from SP-25 Week 2: glass-box models enable richer, more effective direct manipulation-based steering of AI models.
> - A limit of that approach, from the 🚧 Safety Inspection Expert thread: S05 asked whether GAM Changer requires a supervised, prediction-based ML task with "well-understood features". S11 agreed: "This work is primarily for editing structured, 'well-understood features' that domain experts can align, because it depends on [[PTN - Glass-box models]] like GLMS/GAMs." (S05, S11, SP-25)
