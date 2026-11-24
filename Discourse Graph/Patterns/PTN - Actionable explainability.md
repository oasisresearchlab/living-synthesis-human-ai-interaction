---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e70-661f-703d-a81f-41fb1657db87
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/-yOVhZN1U
roamAuthor: "Joel Chan"
created: 2025-03-26
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Explainability and interpretability do more than increase users' understanding of how and why the machine makes decisions. If allowed, they can also signal to users how to **steer** the model in the direction they want. This pairs naturally with [[PTN - Direct Manipulation]]. (S01, SP-25 group discussion)

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - GAM Changer]] ([[@wangInterpretabilityThenWhat2022]]) lets users edit an interpretable model through continuous feedback and transparent, reversible edits. This was the context in which the pattern was named in the SP-25 seminar.

## Other Notes

Claude:
> **Risk: harmful edits.** If explainability is extended to let users customize the model, responsible and accountable model change needs support to avoid irreversible adversarial changes. Evidence from [[@wangInterpretabilityThenWhat2022]]: "... continuous feedback ... as well as transparent and reversible edits ... (h)owever ... do not guarantee to prevent users from overfitting the model, injecting harmful bias, or maliciously manipulating model predictions. This potential vulnerability warrants further study on how to audit and regulate model editing." Reversible edits can undo damage, but some monitoring mechanism is also needed to detect harmful edits, e.g., an LLM judge with a constitution that safeguards model integrity. (S01, SP-25)
