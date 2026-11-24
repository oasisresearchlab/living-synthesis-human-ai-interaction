---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e91-13bd-72cf-b7d3-04354fce7c09
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-25 W12 (2025-04-16)]]"
created: 2026-11-24
---
## Grounds

Claude:
> - [[ART - DynaVis]] parses generated Vega-Lite into a syntax tree and lints it to ensure the generated code is valid: "this is like a programming languages kind of thing" (SP-25 W12, [00:23:00]). With GPT-3.5 it was common for the model to generate invalid code (SP-25 W12, [00:23:24]).
> - Joel Chan: "you have that sort of checker that is valid, instead of just relying on prompt and say, please generate valid code, or make sure that it is JSON ... all bets are off" (SP-25 W12, [00:31:32]).
> - Even with a well-documented grammar, the authors "still add that static analysis stuff," which Joel recommended for anyone concerned about code validity (SP-25 W12, [00:31:17]).

## Other Notes

## Suggested relations
Claude:
> - informs → [[PTN - program analysis validation of LLM-generated code]]
> - consistent with → [[QUE - How good are LLMs at following instructions in prompts?]]
