---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e91-895f-713e-8d81-cb778d31340c
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-24 W05 Explainability]]"
created: 2026-11-24
---
## Grounds
Claude:
> - In [[@caiHumanCenteredToolsCoping2019]], pathologists make a differential diagnosis by hypothesis testing: they look for the most likely diagnosis and try to rule out alternatives that share image features (a process of elimination). The ML support they need is control over which kinds of similarity to focus on, at different moments. Needs shift with the current goal, e.g., focusing on one region. (S05, 👩🏽‍🔬 Distiller, SP-24 W05)
> - These needs came out of a multi-month iterative design process with 3 pathologists ([[CLM - multi-month iterative design with a few domain experts grounds human-AI tool design better than superficial breadth]]). (S05, SP-24 W05)
> - In the study, pathologists used refinement to track a hypothesis's likelihood and generate new ones, and switched between tools within one case ([[EVD - pathologists interleaved refine-by-region, refine-by-example, and refine-by-concept tools within a single diagnostic case in SMILY - @caiHumanCenteredToolsCoping2019]]). (S05, SP-24 W05)

## Other Notes
Claude:
> - Generalization: likely to hold wherever expert work is hypothesis-driven and the relevant features change as hypotheses change; the paper suggests CBIR problems in other domains. (Joel Chan, SP-24 W05)

## Suggested relations
Claude:
> - supports → [[PTN - Interactive refinement]]: user-controllable similarity is what refinement provides
> - derived from → [[EVD - pathologists interleaved refine-by-region, refine-by-example, and refine-by-concept tools within a single diagnostic case in SMILY - @caiHumanCenteredToolsCoping2019]]
> - informs → [[QUE - What criteria must a task meet to necessitate the collaboration of both algorithms and human expertise?]]: shifting, hypothesis-driven needs are one candidate criterion (S06's question, SP-24 W05)
