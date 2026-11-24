---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e70-661e-7555-8796-9fae40460d89
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/MY0938Mi5
roamAuthor: "Joel Chan"
created: 2025-01-14
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Train a separate model that "compresses" the original giant network in the LLM, such that individual "neurons" in the new model are "monosemantic": each corresponds to a human-interpretable feature (though the features still need to be labeled). (Joel Chan, SP-25 seminar)
> - Key source: Anthropic's "Towards Monosemanticity" work on feature extraction with sparse autoencoders: https://transformer-circuits.pub/2023/monosemantic-features
> - The 👾 Hacker thread (SP-25) strongly recommended playing with its interactive visualization of features to build intuition: https://transformer-circuits.pub/2023/monosemantic-features/index.html#setup-interface
> ![[iqViD8ma5h.png]]
> ![[kH8fH0m62n.png]]

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - Feature steering in [[@durmusEvaluatingFeatureSteering2024]] uses SAE features (the SAE dictionary learning method from the Anthropic work).
> - Linus Lee has explored SAEs on the UX side, e.g., https://thesephist.com/posts/prism/#future-work and https://thesephist.com/posts/synth/ (🕸️ Connector thread, SP-25)
> ![[AS05PfuV7g.png]]
> - An interactive explainer by Ian Johnson on using SAE features to steer similarity search, for finer-grained control over search systems that rely on [[PTN - Large Language Models (LLMs)]] embeddings: https://x.com/enjalot/status/1913237189988598170 and "Navigating by Similarity | Latent Scope": https://latent.estate/essays/nav-by-sim (shared by Joel Chan, SP-25 Week 13)

## Other Notes
Claude:
> - Alternatives: S11 (🏺 Archaeologist, SP-25) noted that although steering remains "preparadigmatic", NLP has proposed many interventions for distinct tasks besides SAE dictionary learning:
>   - data-driven extraction of features in decoder models: https://aclanthology.org/2022.findings-acl.48/
>   - activation scaling: https://aclanthology.org/2024.findings-emnlp.479.pdf
>   - style transfer via data-driven extraction of style vectors from training data: https://aclanthology.org/2024.findings-eacl.52.pdf
> - Flagged as a "look ahead" in the SP-25 discussion of [[ART - AI Policy Projector]], whose secret sauce is natural language definitions of "concepts" that can be used to group and steer outputs. The Connector thread later compared SAE-based steering to what Policy Projector offered.
> - Listed by Joel Chan under interactive interpretability/explainability when workshopping SP-25 readings.
