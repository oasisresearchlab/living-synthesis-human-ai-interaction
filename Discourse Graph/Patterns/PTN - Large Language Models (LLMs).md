---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e70-661f-71fd-bfa2-e463087ed690
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/yr5kdQMQ1
roamAuthor: "Joel Chan"
created: 2024-02-07
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> [[ART - Graphologue]] ([[@jiangGraphologueExploringLarge2023]]) is technically enabled by [[PTN - prompt engineering]] plus LLMs:
> - The LLM converts text into annotated nodes and links (marked by salience, with unique local IDs).
> ![[oTuu9BuaDj.png]] (p. 6)
> - It uses a very long prompt with [[PTN - few-shot in-context learning]].
> ![[wngBOgKDrB.png]]
> ![[a_Xzp1XzhD.png]] (pp. 17-18)
> - The pipeline adds error correction and saliency filtering.
> - In this way the paper contributes back to the literature on text-to-graphical representations (or, more generally, "flexible representational transformation," which may be a neat design pattern).
> ![[tlSQpiB0jq.png]] (p. 3)

## Other Notes
Claude:
> - In SP-25, the seminar paused to note that [[PTN - Text-to-Image Latent Diffusion Model]] is a different class of model from LLMs or [[PTN - Generalized Additive Models (GAMS)]]. For example, prompts by experienced and novice prompt artists differ, partly as an artifact of how the model uses CLIP.
> ![[uSK7iJXp_U.png]]
> - SP-25 Week 13 (housekeeping): a neat interactive explainer on using [[PTN - Sparse Autoencoders (SAEs)]] to get more fine-grained control over search systems that rely on embeddings from LLMs: Ian Johnson's post (https://x.com/enjalot/status/1913237189988598170) and essay "Navigating by Similarity" (https://latent.estate/essays/nav-by-sim).
