---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e91-886d-72fd-8444-a724a112433a
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W11 (2025-04-09)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Treat the parts of an LLM generation setup as interactive objects that users can compose and act on. Key source (no source note yet): Kim, T. S., Lee, Y., Chang, M., & Kim, J. (2023). Cells, Generators, and Lenses: Design Framework for Object-Oriented Interaction with Large Language Models. UIST '23. https://doi.org/10.1145/3586183.3606833
> S16 (🏺 Archaeologist, SP-25 W11) quoted it as a "design framework that conceptualizes the components of generation configurations as interactive objects. The framework describes how to design interfaces that encapsulate these objects and the interactions that can be supported on and between these objects".
> ![[UxChwmNI3R.png]]

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - Cells, Generators, and Lenses (Kim et al., 2023), cited in [[@chungPatchviewLLMpoweredWorldbuilding2024]] alongside [[ART - ChainForge]] as using visualization nodes for steering model behavior (S16, SP-25 W11).

## Other Notes
Claude:
> S16's contrast with [[ART - Patchview]]: relationships between inputs are "more concrete than Patchview, like in object-oriented programming -> less flexibility for control" (S16, SP-25 W11). Joel Chan placed it in a broader family of visual ways to interact with generative AI, along with [[ART - ChainForge]], [[ART - Graphologue]], Luminate, and TaleBrush, "as opposed to ... the kind of policy, natural language prompting rule base kind of approach" (SP-25 W11, [00:36:31]–[00:37:00]).

## Suggested relations
Claude:
> - informs → [[QUE - What is the design space of --interaction-oriented-- approaches to Human-Centered AI?]]
> - consistent with → [[ART - ChainForge]]: both use node-based composition
