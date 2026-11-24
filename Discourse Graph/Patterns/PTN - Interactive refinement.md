---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e91-87a5-7e6c-855b-ec46ef14a957
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W05 Explainability]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Give users lightweight controls to reshape what an ML system returns, so they can steer and probe it toward their current goal instead of accepting a single fixed output. [[@caiHumanCenteredToolsCoping2019]] proposes interactive refinement as its answer to the gap between what pathologists need and what content-based image retrieval affords: it goes "beyond algorithmic feedback" to help users make sense of and leverage ML algorithms. (S05, 👩🏽‍🔬 Distiller, SP-24 W05)
> - Refine by region: crop the image to isolate features in a specific region.
> - Refine by example: select a subset of the search results as reference images, for concepts that can't be pinpointed to one region.
> - Refine by concept: slide the presence of clinical concepts up or down (implemented with [[PTN - Concept Activation Vectors (CAVs)]]); the initial concept list came from the pathologists.
> - Auxiliary tools: narrow hypothesis, augment variety, visualize refinement.
> ![[pAjx87sm8q.png]]

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - SMILY]] ([[@caiHumanCenteredToolsCoping2019]]). (S05, SP-24 W05)
> - Joel Chan saw a family resemblance to [[ART - ImageSense]] (especially refine-by-concept), to [[PTN - Predictive Interaction]], and to [[PTN - Shared Representation]], since the image-focused refinement tools work on a representation both the user and the model act on. (Joel Chan, replying to S08 🕸️ Connector, SP-24 W05)
## Other Notes
Claude:
> - The paper frames refinement as a way to aid sensemaking of opaque models; see [[CLM - interactive refinement can help users cope with opaque ML models by letting them test the algorithm, without explicit explanations of how it works]]. (S05, SP-24 W05)
> - S11 questioned two design choices: modeling concepts with independent linear classifiers (see [[CLM - concept sliders built from independently trained linear concept directions make the strength and combined effect of adjustments hard for users to interpret]]), and why refine-by-example takes the average of all selected examples, and what other experiments were tried. (S11, 🚧 Safety Inspection Expert, SP-24 W05)

## Suggested relations
Claude:
> - instantiates ← [[ART - SMILY]]: SMILY's three refinement tools are the paper's instance of the pattern (S05, SP-24 W05)
> - uses → [[PTN - Concept Activation Vectors (CAVs)]]: refine-by-concept is built on CAVs (existing SMILY node; S11, SP-24 W05)
> - consistent with → [[PTN - Predictive Interaction]]: Joel Chan saw the two as "similar or related" (SP-24 W05)
> - consistent with → [[PTN - Shared Representation]]: image refinement tools as a shared representation (Joel Chan, SP-24 W05)
