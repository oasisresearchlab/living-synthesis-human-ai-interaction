---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e91-a5d6-7744-b7ae-86a4e3a138b0
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-25 W04 (2025-02-19)]]"
created: 2026-11-24
---
## Grounds
Claude:
> Joel Chan's account of ChainForge's "secret sauce": "you can do these like exploratory like comparisons, which then generate hypotheses that you can test systematically ... If you jump straight to here [the evaluators and plots], you don't know what the test [is]. If you stay here [inspecting responses], then you only have like anecdotes. The idea is to ... bridge between exploratory looking at stuff ... and then that hopefully then leads to hypotheses that you can then test systematically" (SP-25 W04, [00:15:45]–[00:16:35]).
> - Worked example: [[EVD - an instructor exploring a ChainForge example flow noticed through side-by-side comparison that one prompt preserved the docstring while another dropped it, which suggested a testable hypothesis]] — "which you may not know what to write over here before, like looking at the examples" (SP-25 W04, [00:15:45]).
> - A test like "is this valid JSON?" only becomes meaningful once a hypothesis ("if I change this prompt design, the response will be more likely to be well structured as JSON") exists (SP-25 W04, [00:18:49]–[00:19:11]).
## Other Notes
Claude:
> Contested in practice: the study found that users rarely made the second step (see suggested relations).
## Suggested relations
Claude:
> - consistent with → [[CLM - to reason about LLM behavior, you need to be able to (visually) compare outputs side by side]]: adds why the comparison matters — it feeds hypothesis generation
> - informs → [[QUE - How can we enable people to intuitively bridge exploring and systematically testing hypotheses about LLMs when developing LLM-powered systems?]]
> - informs → [[ART - ChainForge]]: its design rationale
> - inconsistent with → [[EVD - users --- including those with prior proramming experience --- infrequently transitioned to systematic testing with ART - ChainForge - @arawjoChainForgeVisualToolkit2024]]: the bridge is designed for but rarely crossed
