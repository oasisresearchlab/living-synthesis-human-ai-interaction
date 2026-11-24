---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e92-2a74-7ed7-aa74-de4f601a327d
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W02 (2025-02-05)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> While a user edits a model, the interface continuously shows how the edit changes overall performance and related parts of the model, so that consequences are visible before committing. In [[ART - GAM Changer]] this was one of two patterns (with reversible actions) addressing the challenge of "reasoning about potential unintended negative consequences of modifications" (Distiller thread, SP-25 W02 notes).

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - GAM Changer]]: a metric panel (accuracy, precision, etc.) and "link + reorder" to see correlated features:
> ![[JO6PA2aLPZ.png]]
> - Pneumonia case: after editing age, checking consequences for fairness by gender ([[EVD - it was possible for a physician and ML researcher to use ART - GAM Changer to edit a GAM model for pneumonia risk prediction to account for possible issues with age and asthma predictors - @wang]]).

## Other Notes
Claude:
> - Limits raised in the seminar: metrics show *that* performance changed but not *what* changed in the function (SP-25 W02, [00:35:08]; [[QUE - How might interactive model editing tools show first-time users what a direct manipulation edit does to the underlying model function?]]); and it is unclear how often higher-order consequences can be detected, or what the fix is (Joel Chan, notes; [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]]).

## Suggested relations
Claude:
> - (reverse) [[ART - GAM Changer]] instantiates this pattern
> - informs → [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]]
> - informs → [[QUE - How might interactive model editing tools show first-time users what a direct manipulation edit does to the underlying model function?]]
