---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e91-112f-70b4-b2c7-525577dce4d9
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-25 W12 (2025-04-16)]]"
created: 2026-11-24
---
## Grounds

Claude:
> - Joel Chan: "once you synthesize a widget, your changes don't require a model to regenerate code anymore because they basically generate a JavaScript thing that modifies ... that part of the specification" (SP-25 W12, [00:28:21]).
> - "Each time you make that request is a round trip to the language model. But once you make a GUI, like the little widget, then you don't need the LLM anymore ... So it's gonna be way faster" (SP-25 W12, [00:28:50]).
> - The paper measured about 1.47 s per model query ([[EVD - each LLM query in DynaVis added about 1.47 seconds of latency in a post-hoc replay of study sessions - @vaithilingamDynaVisDynamicallySynthesized2024]]).

## Other Notes

## Suggested relations
Claude:
> - informs → [[PTN - dynamically synthesized UI widgets]]: a core benefit of the pattern
> - consistent with → [[CLM - dynamic widgets add the most value for iterative fine-grained tweaking, while natural language suits known end states and larger exploratory changes]]: latency matters most when many small iterations are needed (SP-25 W12, [00:44:15])
