---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e70-661e-7b31-aadc-14983a7dfab8
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/3FZL2txwg
roamAuthor: "Joel Chan"
created: 2024-02-18
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> - Foundational source: Kim et al., "Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors (TCAV)", https://proceedings.mlr.press/v80/kim18d.html. (S16, 🏺 Archaeologist role, SP-24)
> - Interactive examples for building intuition (in theory! a bit tough to follow along):
>   - Interpretable Machine Learning, 10.3 Detecting Concepts: https://christophm.github.io/interpretable-ml-book/detecting-concepts.html
>   - Performing Global Model Analysis with TCAV: https://pair-code.github.io/lit/tutorials/tcav/
> (S13 and Joel Chan, 👾 Hacker role, SP-24)

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - The key secret sauce for refine-by-concept in [[ART - SMILY]] ([[@caiHumanCenteredToolsCoping2019]]). (Joel Chan, notes)
> ![[eANNWS0r00.png]]
> ![[8LF_fN_d2K.png]] (pp. 3-4)
> ![[WGhsHWWcY2.png]]
## Other Notes
Claude:
> - Critique: S11 worried about the linear assumptions in SMILY's implementation: "Why use linear classifiers to model the refinable concepts independently, when at inference time search results are returned collectively?" This even became an issue when a user wasn't sure about the "strength" of the slider, since the intensity of the shift could affect the overall search query. Joel Chan noted that [[@liptonMythosModelInterpretability2017]]'s focus on linear models complements this worry. (S11 and Joel Chan, SP-24)
> - Open question: what interpretability desiderata (Lipton, section 2) do CAVs in [[ART - SMILY]] target? (Joel Chan, 🕸️ Connector, SP-24)
> - Follow-up work by Been Kim, first author of the original CAV paper, sparked [[QUE - Can AI models learn new concepts that even experts can learn from to advance knowledge of a domain?]], on concepts learned by [[ART - AlphaZero]]. (S06, SP-24)
> - In SP-25, a reading whose secret sauce was natural-language definitions of "concepts" that can be used to group and steer was connected back to CAVs. (SP-25 seminar)
