---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e91-1344-7899-aeab-afbee5d4bdf7
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-25 W12 (2025-04-16)]]"
created: 2026-11-24
---
## Grounds

Claude:
> - Joel Chan's heuristic: "If you see lots of stuff on Stack Overflow, you're probably fine ... it's really about how common this is on the web, what's the training data." Esoteric languages (e.g., Clojure) discussed in closed forums are riskier, while standard matplotlib widgets have "so much training data and it is fairly stable" (SP-25 W12, [00:30:37]).
> - He would not use LLMs for a new library meant to replace pandas, but ggplot "has been around forever" (SP-25 W12, [00:31:58]).
> - Vega-Lite "has been around for a while" with a fair amount of documentation (SP-25 W12, [00:31:00]).
> - Proposed measure: correlate Google or Stack Overflow hit counts with how likely generated code is to be valid (SP-25 W12, [00:32:00]).

## Other Notes

## Suggested relations
Claude:
> - consistent with → [[CLM - programmatic validation of LLM-generated code is more dependable than prompting the model to produce valid code]]: when coverage is thin, add validation
