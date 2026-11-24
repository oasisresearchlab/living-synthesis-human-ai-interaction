---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e92-253b-797f-bcdb-edabb64c22e7
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-25 W02 (2025-02-05)]]"
created: 2026-11-24
---
## Grounds
Claude:
> Joel Chan, explaining GAMs: they are like regressions, but additive, with a shape function per feature instead of a single weight; the shapes can be non-linear (U-shaped, plateaus). "This feels like a nice ... on the model side trade off between like a more complex model that theoretically would have like much higher predictive power and ... something that ... has nicer properties for like being able to reason about each individual feature ... by itself." (SP-25 W02, [00:03:03]–[00:06:18])
>
> "It's not like a giant neural network where you have these like uninterpretable weights ... they call it like a glass box model" (SP-25 W02, [00:04:02]).
> ![[YPjU_eux-7.png]]

## Other Notes
Claude:
> - Counter-consideration from the paper's case studies: the sepsis GAM still reached almost 90% AUC on the test set ([[EVD - it was possible for a two physicians to use ART - GAM Changer to edit a GAM model for sepsis risk prediction to account for possible issues with temperature, respiratory rate, and systolic blood]]), so the predictive cost may be small in some tasks.
> - S14 (🏺 Archaeologist, SP-25 W02 notes) pointed to Chang et al. (2021), "How Interpretable and Trustworthy are GAMs?" (KDD), https://dl.acm.org/doi/pdf/10.1145/3447548.3467453, on inductive bias in GAMs.

## Suggested relations
Claude:
> - consistent with → [[CLM - linear models are inherently more interpretable than deep neural network models]]
> - informs → [[PTN - Glass-box models]]
> - enables → [[PTN - interactive model editing]]: per-feature reasoning is what makes shape-function editing possible
