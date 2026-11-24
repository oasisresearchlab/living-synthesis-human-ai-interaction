---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e91-7c9c-7460-bc68-949b4c3468e1
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-24 W06-07 Explainability and trust]]"
created: 2026-11-24
---
## Grounds
Claude:
> S11, warmup response (SP-24 W06): compare the content of the readings with the practice problems, and the generated practice problems with the test, "to ensure the overlap isn't too large". The goal is to ask "what added value come from the ML practice test? Is this even a fair comparison? Is it only because the practice problem is incredibly similar to the test, and students are learning how to do those specific questions or are they understanding the content? (This would be like 'model overfitting')." S13 named the distinction: memory vs. transfer.
> Joel Chan made a parallel point about the model itself: feed it new practice problems or concepts "to ensure that the model isn't just indexing surface features of the existing practice problems" (SP-24 W06).

## Other Notes

Claude:
> S11 also suggested going past the 75% average to see how the system affects individual students.

## Suggested relations
Claude:
> - informs → [[QUE - What can instructors or administrators do to interpret and vet an educational ML system whose workings the developer has not explained?]]: checking the comparison is a prerequisite to interpreting the system
> - consistent with → [[PTN - Probing a black-box model with edge-case and out-of-distribution inputs]]: both test generalization beyond the training distribution
