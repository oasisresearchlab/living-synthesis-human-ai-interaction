---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e91-882a-7624-9759-f10914f95b22
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W05 Explainability]]"
created: 2026-11-24
---
## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> Make the predictions of any black-box classifier more interpretable and trustworthy by explaining individual predictions. Flagged as prior work to the SMILY paper, which places itself relative to work that "focuses on generating human-interpretable algorithmic explanations". Source: Ribeiro, Singh, and Guestrin (2016), "Why Should I Trust You?": Explaining the Predictions of Any Classifier, KDD '16, https://doi.org/10.1145/2939672.2939778 (no source note in the vault). (S16, 🏺 Archaeologist, SP-24 W05)

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> Approximates the classifier locally, around one prediction, with an interpretable model, and is model-agnostic. This makes it an instance of [[PTN - local explanations]] and [[PTN - post-hoc interpretability]]. (S16, SP-24 W05)

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

Claude:
> The paper's evaluation includes simulated and human-subject studies. Non-expert users could use LIME to make better decisions about which classifier is likely to generalize in the real world, and LIME can help with feature engineering by surfacing non-generalizable features. (S16, SP-24 W05)

## Other Notes
Claude:
> - Contrast with SMILY: LIME explains the model, while [[@caiHumanCenteredToolsCoping2019]] gives users controls to test it instead ([[CLM - interactive refinement can help users cope with opaque ML models by letting them test the algorithm, without explicit explanations of how it works]]). (Connection drawn from S16's framing of the paper as moving beyond "algorithmic transparency"; SP-24 W05)

## Suggested relations
Claude:
> - instantiates → [[PTN - local explanations]]: local, interpretable surrogate around one prediction (S16, SP-24 W05)
> - instantiates → [[PTN - post-hoc interpretability]] (S16, SP-24 W05)
> - instantiates → [[PTN - algorithmic transparency]]: listed under "improving algorithmic transparency" (S16, SP-24 W05)
