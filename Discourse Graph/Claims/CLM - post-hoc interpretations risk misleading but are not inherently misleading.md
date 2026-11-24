---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e91-7d24-770b-a29c-f2be34200b83
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-24 W06-07 Explainability and trust]]"
created: 2026-11-24
---
## Grounds
Claude:
> Distiller notes (S13, SP-24 W06) summarized a section of [[@liptonMythosModelInterpretability2017]] as "Post-hoc interpretations = misleadings" (examples: hiring and promotion). Joel Chan pushed back: "don't think Lipton is __equating__ post-hoc approaches to misleadings! there is certainly a risk, but not clear that post-hoc inherently misleads." S13: "Agreed!"
> S11 added an advantage: post-hoc interpretation "can be done by third-parties without model code" (SP-24 W06).

## Other Notes

Claude:
> Citation statements collected by Joel note that post-hoc interpretations "mostly do not show the exact inner workings of a model" but "we can interpret BB machine learning models after they have been created, without sacrificing their predictive power" (citing Lipton; from the axiomatic-framework paper, https://arxiv.org/abs/1808.05054).
> Lipton notes "the processes by which we humans make decisions and those by which we explain them may be distinct" (quoted in the SP-24 W06 notes), which is the root of the misleading risk.

## Suggested relations
Claude:
> - informs → [[PTN - post-hoc interpretability]]: sets the boundary condition on the pattern's risk (SP-24 W06)
> - consistent with → [[CLM - AI explanations can be used as dark patterns to earn unwarranted trust]]: the risk becomes a dark pattern when exploited deliberately
> - informs → [[PTN - Automated Rationale Generation]]: a post-hoc method whose rationales are not the agent's actual process
