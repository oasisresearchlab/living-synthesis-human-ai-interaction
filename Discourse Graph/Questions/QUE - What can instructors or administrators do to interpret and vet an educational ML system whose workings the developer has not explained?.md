---
nodeTypeId: node_Gp7JMdrzm9DUuPfBzUptc
nodeInstanceId: 01a20e91-771e-78ae-8261-09c6f297e7ed
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W06-07 Explainability and trust]]"
created: 2026-11-24
---
## Context

Claude:
> The SP-24 W06 warmup (S13, Distiller, on [[@liptonMythosModelInterpretability2017]]): an ML program sequences practice problems; students using it score 75% on a test vs. 60% for students who learned from readings alone. As an instructor or administrator who must make sure it works "effectively, reliably, and fairly" without an explanation of *how* it works, what can you do?
> ![[Z-BEJkKx6g.png]]
> Responses clustered into several strategies:
> - probe the system with edge cases and "weird" test data (S08, S05) → [[PTN - Probing a black-box model with edge-case and out-of-distribution inputs]]
> - elicit stakeholders' mental models and remaining explanatory needs (S08) → [[PTN - Explanatory needs elicitation]]
> - check the comparison itself: overlap between practice items and the test (S11) → [[CLM - learning gains from an ML practice-problem system may reflect overlap between practice items and the test rather than transferable understanding]]
> - error analysis against misconception models and instructor "gold standard" sequences; subgroup outcomes; demand algorithms, data, and validation studies (Joel Chan) → [[PTN - Subgroup outcome analysis]], [[CLM - developers' unwillingness to share algorithms, features, training data, or validation data should lower confidence in a deployed ML system]]
> - feature-importance explanations and a simple model visualization, e.g., a decision path (S16)
> - qualitative study of what students learned, not the algorithm itself (S05)

## Other Notes

## Suggested relations
Claude:
> - informs → [[QUE - Why is interpretability important?]]: the warmup motivated the session's question of why interpretability matters (SP-24 W06)
> - informs → [[PTN - Probing a black-box model with edge-case and out-of-distribution inputs]], [[PTN - Subgroup outcome analysis]], [[PTN - Explanatory needs elicitation]]: these were the strategies proposed in response
