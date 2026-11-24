---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e94-6dbd-783b-b8f2-ba836cbfdfe1
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W13-16 Evaluation and accountability]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> A human-in-the-loop arrangement where routine cases go through the algorithm and uncertain cases (or inputs it can't handle) go to a human expert. Joel Chan proposed it as "the obvious solution approach" to the gradability mismatch in the diabetic retinopathy deployment: nurses could read images the model rejected. (Joel Chan, Academic Researcher, SP-24 W13)
> - Background: https://en.wikipedia.org/wiki/Human-in-the-loop (Joel Chan, SP-24 W13)

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - Project Sidewalk (Makeability Lab), https://makeabilitylab.cs.washington.edu/project/sidewalk/, and Kurt Luther's crowd-plus-algorithm work were given as examples. (Joel Chan, SP-24 W13)
> - Proposed, not built, for the diabetic retinopathy screening system in [[@beede2020humancentered]].

## Other Notes

Claude:
> Boundary condition: Joel contrasted this with self-driving cars, where "only handing off to driver in certain unknown situations is recipe for disaster". See the companion claim on when deferral works.

## Suggested relations
Claude:
> - informs → [[CLM - deferring hard cases from an AI system to humans works better when the humans can handle those cases under suboptimal conditions and the handoff is not time-critical]]
> - informs → [[QUE - What criteria must a task meet to necessitate the collaboration of both algorithms and human expertise?]]: deferral is one answer to which cases need human expertise
> - informs → [[QUE - How do we understand which aspects of tasks are better tackled by AI systems vs. humans?]]
