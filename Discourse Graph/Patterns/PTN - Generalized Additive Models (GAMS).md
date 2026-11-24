---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e70-661f-7cb1-ba7b-9f572454a42e
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/6_GCztd-9
roamAuthor: "Joel Chan"
created: 2025-02-04
---

## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Very similar to a generalized linear model. The main difference is that instead of a weight for each predictor, each predictor gets a "shape function," which can be a variety of functions other than simple multiplication. GAMs belong to the class of [[PTN - Glass-box models]]. (Joel Chan, SP-25, discussing [[@wangInterpretabilityThenWhat2022]])
> ![[YPjU_eux-7.png]]

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - GAM Changer]] ([[@wangInterpretabilityThenWhat2022]]) lets users audit *and edit* GAMs, toward [[QUE - How might we empower users to act on model interpretations when they lack expertise in ML and software engineering?]] Key design patterns discussed in SP-25 (Joel Chan):
>   - The shape functions act as a [[PTN - Shared Representation]], probably far superior to a table: misalignments are easy to spot at a granular level, and the model can be edited directly.
>   - [[PTN - Direct Manipulation]] addresses the basic mechanics of editing for users without ML or software engineering expertise: you edit the model by editing its shape function, scaffolded by preset modification types like align and interpolate.
> ![[omkpng_BTY.png]]
>   - Continuous feedback (e.g., link + reorder to see correlated features) and reversible actions (inspired by [[ART - git version control]]) address the challenge of reasoning about unintended consequences of edits.
> ![[JO6PA2aLPZ.png]]
> ![[7Rq6xkBINP.png]]
>   - The authors suggest GAM Changer instantiates a new class of [[PTN - interactive model editing]] tools.
> ![[BHR4HO5cBv.png]]
## Other Notes
Claude:
> - GAMs are a different class of model than [[PTN - Large Language Models (LLMs)]] or [[PTN - Text-to-Image Latent Diffusion Model]], which shapes what kinds of steering make sense. (SP-25)
> - See [[CLM - local edits to shape function of single features have minimal global impacts on generalized additive model performance]]
