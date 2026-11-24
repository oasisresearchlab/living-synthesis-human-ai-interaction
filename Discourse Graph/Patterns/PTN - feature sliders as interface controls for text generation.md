---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e90-901e-7e25-8896-d8c3d2de93ae
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W10 (2025-04-02)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Expose interpretable model features (e.g., from [[PTN - Sparse Autoencoders (SAEs)]]) as continuous controls, like sliders or knobs, so users can turn a concept up or down while generating or editing text, instead of (or alongside) prompting.
> - Joel Chan: "there's this interesting... UI designs that I've seen that I feel pretty inspired by... kind of taking the knobs thing pretty seriously... imagining... there's a narrative feature and I can sort of make it go up or down, or like quotes feature or technical feature when I'm trying to do like sort of text editing or creative writing." Unlike the if-then rules of [[ART - AI Policy Projector]], this "globally gives you that control" (SP-25 W10, [00:42:01]-[00:42:47]).
> - Quantitative steering curves are what would make such knobs trustworthy: "if they proved to be quite reliable, then we could use them for things like this" (Joel Chan, SP-25 W10, [00:42:47]-[00:43:00]).

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - Linus Lee's experiments with SAEs on the UX side (🕸️ Connector thread, SP-25 W10): https://thesephist.com/posts/prism/#future-work and https://thesephist.com/posts/synth/
> ![[AS05PfuV7g.png]]
> - [[ART - Golden Gate Claude]] is a fixed, single-setting version of the idea.

## Other Notes
Claude:
> Open issues raised in the same session: per-feature calibration ([[EVD - the amount of output change per unit of steering varied widely across the SAE features evaluated, with some features barely moving the outputs - @durmusEvaluatingFeatureSteering2024]]), off-target effects ([[EVD - steering a gender-bias SAE feature in an Anthropic LLM also shifted age bias, an off-target effect - @durmusEvaluatingFeatureSteering2024]]), and safety of user access ([[QUE - How much feature-level control over an LLM can be given to end users without opening attacks on its safety safeguards?]]).

## Suggested relations
Claude:
> - uses → [[PTN - feature steering]]
> - uses → [[PTN - Sparse Autoencoders (SAEs)]]
> - informs → [[ART - AI Policy Projector]]: contrast between global knobs and concept-based if-then policies
