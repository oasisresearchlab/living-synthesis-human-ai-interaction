---
nodeTypeId: node_Gp7JMdrzm9DUuPfBzUptc
nodeInstanceId: 01a20e70-661c-70bd-b266-c0bcfde5bece
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/x7xO9RF63
roamAuthor: "Joel Chan"
created: 2025-02-05
---

## Context
Claude:
> First raised by Joel Chan (🚧 Safety Inspection Expert thread, SP-25 Week 2) on [[ART - GAM Changer]] ([[@wangInterpretabilityThenWhat2022]]): he wished the paper showed more about how overall model performance changed after edits. The paper's example (edit the age feature, then check consequences for fairness by gender) is an ok start, but it's unclear how often such effects can be detected, and what the fix is. The authors partly agree:
> ![[E2HR8OiLex.png]]
> They claim [[CLM - local edits to shape function of single features have minimal global impacts on generalized additive model performance]]. If true, Joel noted, that is another boundary condition on the usefulness of this approach. (Joel Chan, SP-25)
>
> The question recurred across later sessions:
> - **Cascading errors.** Responding to S01, Joel noted it seems related to the challenge of "cascading errors" raised in the paper's related work.
> ![[fWw9OqTqOF.png]]
> - **Systematic testing.** Related to whether scientific literacy is needed to benefit from tools like [[ART - ChainForge]].
> - **Principles for steering.** On a principle-based steering tool, Joel saw a big gap: no scaffolding for what counts as a good principle ([[QUE - How to support users to design effective principles for steering LLMs?]]) and no support for reasoning about interactions between principles. The paper also missed a chance to reflect on this in relation to [[ART - ChainForge]] and [[PTN - LLM Chains]] (it cites [[@wuAIChainsTransparent2022]], but only in passing).
> - **Feature steering.** The off-target effects in [[@durmusEvaluatingFeatureSteering2024]] (steering a gender-bias SAE feature also steered age bias) suggest the need to do more than steer individual features: there are complex higher-order interactions, even between monosemantic features.
> ![[pUrxUAIxba.png]]
> - **Dynamically generated widgets.** On S11's Connector link between Constitutional AI papers and dynamically generated UIs, Joel noted that Section 3.1, "Widgets as modular sub-components" (p. 5), seems to partially address the question. It also uses [[ART - Vega-Lite]] as an underlying [[PTN - Domain-Specific Language (DSL)]] for constraints.

## Other Notes
Claude:
> - [[ART - Patchview]] ([[@chungPatchviewLLMpoweredWorldbuilding2024]]) lets users construct higher-order structures that combine views, like a 2D plane visualization or parallel coordinates. The lit notes on the paper call this a neat step towards addressing the question.
