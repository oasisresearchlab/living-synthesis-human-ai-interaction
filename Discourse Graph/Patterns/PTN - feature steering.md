---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e70-661f-7c44-b635-22db89900208
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/4-548YFRg
roamAuthor: "Joel Chan"
created: 2025-04-02
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> - "Briefly, feature steering works as follows. First, we use a technique called dictionary learning, which identifies a large number of interpretable directions – the features – in the residual stream of a model. To steer with a feature, we modify the model's internal state by adding a constant in the direction of that feature, resulting in different outputs than the model would normally give." (quoted from the Anthropic blog post read in SP-25, 👩🏽‍🔬 Distiller thread)
> ![[jDny9FvRC9.png]]
> - In more technical terms: decompose the residual stream activity **x** into the sum of the SAE reconstruction SAE(**x**) and the reconstruction error error(**x**). Then replace SAE(**x**) with a modified "reconstruction" in which one feature's activity is clamped to a specific value, leave the error term unchanged, and run the forward pass in downstream layers with this modified activity, for every input and token position. Source: [Scaling Monosemanticity, appendix on steering methods](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html#appendix-methods-steering). (SP-25 seminar)
> - Intuitively, it works like a "dial" on a concept. (SP-25 seminar)

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.
## Other Notes
Claude:
> - S11 gave context: steering remains "preparadigmatic". Many interventions have been proposed in NLP for distinct tasks, beyond the [[PTN - Sparse Autoencoders (SAEs)]] dictionary-learning method used in the Anthropic blog post. (S11, SP-25)
