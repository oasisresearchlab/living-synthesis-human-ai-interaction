---
nodeTypeId: node_Gp7JMdrzm9DUuPfBzUptc
nodeInstanceId: 01a20e70-661c-7311-8ddf-7a10ba250a90
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/TFGZQZyBj
roamAuthor: "Joel Chan"
created: 2025-02-04
---

## Context
Claude:
> - The key question of Week 2 of SP-25, on [[@wangInterpretabilityThenWhat2022]]. The paper proposes [[ART - GAM Changer]] as a way to empower users to audit and *edit* [[PTN - Generalized Additive Models (GAMS)]]. (SP-25 seminar, 👩🏽‍🔬 Distiller thread)
> - GAMs are very similar to generalized linear models. The main difference is that instead of a weight for each predictor, each predictor has a "shape function" that can be many kinds of function, not just multiplication. They are part of the class of [[PTN - Glass-box models]]. (Joel Chan, SP-25 seminar)
> ![[YPjU_eux-7.png]]
> - The question breaks into two challenges:
>   - the basic mechanics of actually editing the model
> ![[lQ4LXYFRSE.png]]
>   - reasoning about potential unintended negative consequences of modifications
> ![[x1tAMGdXMQ.png]]

## Other Notes
Claude:
> - Design patterns in GAM Changer that answer the question (SP-25 discussion of how GAM Changer works):
> ![[XzgMk4QHXR.png]]
>   - The shape functions are a [[PTN - Shared Representation]], probably far superior to a table: misalignments are easy to spot at a granular level, and users can edit the model directly. The paper doesn't name this pattern. (Joel Chan, SP-25 seminar)
>   - [[PTN - Direct Manipulation]] addresses the basic mechanics of editing for users without ML/software engineering expertise: users edit the model by directly editing its shape function, scaffolded by preset "modification types" like align and interpolate.
> ![[omkpng_BTY.png]]
>   - Continuous feedback and reversible actions address reasoning about unintended consequences. Continuous feedback: link + reorder to see correlated features. Reversible actions: inspired by [[ART - git version control]].
> ![[JO6PA2aLPZ.png]]
> ![[7Rq6xkBINP.png]]
> - The paper suggests GAM Changer instantiates a (new) class of [[PTN - interactive model editing]] tools. (SP-25 seminar)
> ![[BHR4HO5cBv.png]]
