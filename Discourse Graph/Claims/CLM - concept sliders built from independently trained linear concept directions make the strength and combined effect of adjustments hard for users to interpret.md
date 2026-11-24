---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e91-8a9d-70a6-b004-29d33fe0254f
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-24 W05 Explainability]]"
created: 2026-11-24
---
## Grounds
Claude:
> - S11 asked why [[ART - SMILY]] models the refinable concepts with independent linear classifiers when search results are returned collectively at inference time. It became a problem in use: a user wasn't sure about the "strength" of the slider, and the intensity of the shift could affect the overall search query. (S11, 🚧 Safety Inspection Expert, SP-24 W05; already noted on [[PTN - Concept Activation Vectors (CAVs)]])
> - S11 also flagged that the absence of a concept and a negative concept are different things, which a single slider may blur ([[QUE - How should concept-based steering interfaces distinguish the absence of a concept from its negation?]]). (S11, SP-24 W05)

## Other Notes
Claude:
> - Joel Chan linked the linearity worry to the discussion of linear models in [[@liptonMythosModelInterpretability2017]] (recorded on the CAVs node).

## Suggested relations
Claude:
> - opposes → [[CLM - linear models are inherently more interpretable than deep neural network models]]: linear concept directions can still be hard to interpret when combined (S11, SP-24 W05)
> - informs → [[PTN - Concept Activation Vectors (CAVs)]]
> - informs → [[PTN - feature steering]]: the same "dial strength" problem may arise for feature steering
