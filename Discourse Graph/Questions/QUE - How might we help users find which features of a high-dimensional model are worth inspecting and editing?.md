---
nodeTypeId: node_Gp7JMdrzm9DUuPfBzUptc
nodeInstanceId: 01a20e92-22fc-7443-b368-27271919ea61
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W02 (2025-02-05)]]"
created: 2026-11-24
---
## Context
Claude:
> S15 (🚧 Safety Inspection Expert, SP-25 W02 notes) doubted the practicality of the use case: "In the wild, models that meet real world objectives have high dimensionality. Can humans actually browse through these models to find the features or covariates that lead to insight?"
>
> Joel Chan replied that perhaps another tool, process, or person is needed to *identify* potentially problematic (clusters of) features. The problem [[ART - GAM Changer]] solves is: given a problematic feature, how to reason about and modify the model. The tool does not address finding the feature in the first place. (Joel Chan, SP-25 W02 notes)

## Other Notes
Claude:
> - Scale for reference: the sepsis model had 7 continuous and 83 categorical features ([[EVD - it was possible for a two physicians to use ART - GAM Changer to edit a GAM model for sepsis risk prediction to account for possible issues with temperature, respiratory rate, and systolic blood]]).
> - Companion to [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]], which asks about the consequences of an edit once a feature is chosen.
> - Joel Chan noted that GAMs are additive, without higher-order interactions between features, which partly bounds S15's concern (SP-25 W02, [00:03:24]).

## Suggested relations
Claude:
> - informs → [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]]: same thread, before vs. after choosing a feature (Joel Chan, SP-25 W02 notes)
> - informs → [[QUE - How might we empower users to act on model interpretations when they lack expertise in ML and software engineering?]]
> - derived from → [[QUE - What properties must a machine learning task and its features have for interactive model editing to be feasible?]]: both probe the bounds of the approach
