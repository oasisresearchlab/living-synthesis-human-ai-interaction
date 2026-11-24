---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e91-890f-72cd-a3e3-6f6f92a18fc5
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-24 W05 Explainability]]"
created: 2026-11-24
---
## Grounds
Claude:
> - [[@caiHumanCenteredToolsCoping2019]] reports that "without providing an explicit explanation about how the algorithm works, SMILY implicitly gave users some insight by allowing them to test the algorithm." See [[EVD - pathologists used SMILY refinement tools to tell ML errors from their own by removing suspect variables and re-searching - @caiHumanCenteredToolsCoping2019]].
> ![[2ILIVGnSjf.png]]
> - S05 listed "refinement to aid sense-making of opaque ML models" among the paper's broader implications, and named its contribution as going beyond algorithmic feedback. (S05, 👩🏽‍🔬 Distiller, SP-24 W05)
> - S16 placed the paper against the line of work on "improving algorithmic transparency", which focuses on generating human-interpretable explanations, such as [[ART - LIME (Local Interpretable Model-agnostic Explanations)]]. (S16, 🏺 Archaeologist, SP-24 W05)

## Other Notes
Claude:
> - Boundary condition: the evidence comes from expert users (pathologists) with strong domain models; it's not clear that novices could test an algorithm as effectively.
> - Joel Chan has elsewhere asked whether we could "eschew explanations altogether" and design affordances for sensemaking instead (see [[PTN - Predictive Interaction]]); this claim is evidence for that direction.

## Suggested relations
Claude:
> - derived from → [[EVD - pathologists used SMILY refinement tools to tell ML errors from their own by removing suspect variables and re-searching - @caiHumanCenteredToolsCoping2019]]: the paper's own conclusion from the error-disambiguation finding
> - supports → [[PTN - Actionable explainability]]: interaction that both probes and steers the model (SP-24 W05)
> - informs → [[QUE - How to incorporate intelligent assistance into human knowledge work, while leaving the human in control?]]
