---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e70-661f-797f-b484-45e7f12143ec
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/GVduP03Sq
roamAuthor: "Joel Chan"
created: 2024-02-07
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Shaping the behavior of [[PTN - Large Language Models (LLMs)]] by crafting the input prompt (instructions, examples, output formats), rather than changing the model itself. Often paired with [[PTN - few-shot in-context learning]].
> - Critique noted in the SP-25 seminar on [[@wuAIChainsTransparent2022]]: the authors don't like "mine" prompts and prompt engineering in general because it is less transparent and controllable, which motivates their chaining approach. (Joel Chan, SP-25 seminar)
> ![[Jaa1CCAbNt.png]]

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - Graphologue]] ([[@jiangGraphologueExploringLarge2023]]) is technically enabled by prompt engineering on top of LLMs: it converts text into annotated nodes and links (marked by salience, with unique local IDs), then does error correction and saliency filtering. (Joel Chan, lit-notes)
>   - ![[oTuu9BuaDj.png]] (p. 6)
>   - The prompt is "super long" and uses [[PTN - few-shot in-context learning]]:
>   - ![[wngBOgKDrB.png]]
>   - ![[a_Xzp1XzhD.png]] (pp. 17-18)
>   - In this way the paper contributes back to the literature on text-to-graphical representations (or, more generally, "flexible representational transformation", which may be a design pattern in its own right).
>   - ![[tlSQpiB0jq.png]] (p. 3)

## Other Notes

Claude:
> - Comparison point for steering: in the SP-25 session on [[@durmusEvaluatingFeatureSteering2024]], while comparing feature steering to the steering available in [[ART - AI Policy Projector]], the seminar noted it is important to compare these approaches with prompt engineering. Changing prompts may be easier for end users, but its reliability is unclear, and the effects may be comparable. (SP-25 seminar)
