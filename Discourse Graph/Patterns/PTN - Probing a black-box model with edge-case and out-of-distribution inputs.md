---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e91-869f-7d8f-966b-18c75d4987e9
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W06-07 Explainability and trust]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> When a model's internals are unavailable, learn its scope and the features it responds to by feeding it unusual inputs and watching the outputs: an informal audit.
> - S05 (SP-24 W06): play with the system by providing "**weird** test data" ("informal audit of the model"); if patterns in the test data produce different outputs, examine those inputs for the features the model may be picking up.
> - S08 (SP-24 W06): test **edge cases**, e.g., problems that are more complex or unsolvable, to understand the model's scope.
> - Joel Chan (SP-24 W06): feed the model new practice problems or concepts and check how recommendation quality changes, to ensure it isn't "just indexing surface features."

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - Auditing Ai]] collects tools for auditing AI systems.

## Other Notes

## Suggested relations
Claude:
> - informs → [[QUE - What can instructors or administrators do to interpret and vet an educational ML system whose workings the developer has not explained?]]
> - consistent with → [[CLM - learning gains from an ML practice-problem system may reflect overlap between practice items and the test rather than transferable understanding]]
> - consistent with → [[PTN - post-hoc interpretability]]: interpretation from outside the model
