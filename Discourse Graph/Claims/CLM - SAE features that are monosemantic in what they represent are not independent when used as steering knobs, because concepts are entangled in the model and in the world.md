---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e90-8cfe-7a2c-9bbb-48aa614c49f1
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-25 W10 (2025-04-02)]]"
created: 2026-11-24
---
## Grounds
Claude:
> - S11 (🍜 Academic Researcher, SP-25 W10): an LLM's internal feature representations are intertwined in practice, as the age x gender bias amplification shows. "This is also true in real life -> real-world concepts are entangled and a long text that might have gender bias will likely have a degree of other biases as well. Clamping a single feature will inevitably shift the text towards other types of biases as well."
> - Seminar discussion: "mono semantic features as learned from a model are not exactly like mono semantic, right? Because they... interact very highly with each other" (SP-25 W10, [00:16:43]-[00:17:09]).
> - Refined in the same turn: "the features themselves are actually mono semantic in that they correspond to a specific thing, but then when you try to use it to steer... it ends up having like more than one effect" (SP-25 W10, [00:18:30]-[00:19:00]).
> - Empirical basis: [[EVD - steering a gender-bias SAE feature in an Anthropic LLM also shifted age bias, an off-target effect - @durmusEvaluatingFeatureSteering2024]].

## Other Notes
Claude:
> The distinction matters: monosemanticity is a claim about what activates a feature (representation), not about what changing it does (intervention). Joel Chan: the hope was "make this less biased towards older people and nothing else changes," and mathematically there were reasons to think that could work, but the experiments show otherwise (SP-25 W10, [00:19:33]-[00:20:19]).

## Suggested relations
Claude:
> - derived from → [[EVD - steering a gender-bias SAE feature in an Anthropic LLM also shifted age bias, an off-target effect - @durmusEvaluatingFeatureSteering2024]]
> - informs → [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]]
> - informs → [[QUE - How might interactions among model features (circuits) be modeled when the number of possible interactions is combinatorially large?]]
> - inconsistent with → [[CLM - local edits to shape function of single features have minimal global impacts on generalized additive model performance]]: the GAM claim assumes single-feature edits stay local; SAE feature steering in LLMs did not
