---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e91-88fb-7d0b-8d10-df3ea4f49e53
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W06-07 Explainability and trust]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Explain why the model produced this output *rather than* another, expected one. S11 (SP-24 W06): contrastive rationales, e.g., "region → tumor likely, but it's not something else," citing "Contrastive Explanations for Model Interpretability" (https://arxiv.org/abs/2103.01378).
> ![[GC_OKMYKzW.png]]
> A citation statement Joel collected (from https://arxiv.org/abs/1808.05054, citing Lipton) states the rationale: "people usually do not ask why a specific prediction was made, but rather why this prediction was made instead of another one, namely the one we expected... if our mortgage application gets rejected, we are more interested in knowing the factors that need to change to get it accepted."

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - the contrastive explanation method in arXiv 2103.01378 (figure above)

## Other Notes

## Suggested relations
Claude:
> - instantiates → [[PTN - post-hoc interpretability]]: listed among its sub-patterns in that node
> - enables → [[PTN - Contestable algorithmic decisions]]
