---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e91-11af-7e02-9da2-ca6de5279075
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-25 W12 (2025-04-16)]]"
created: 2026-11-24
---
## Grounds

Claude:
> - S11 (🕸️ Connector, SP-25 W12 notes): the pattern "hinges a lot on LLM ability for getting this right, AND it assumes simplistic usage in practice," since policies (or edits) can conflict or interact.
> - With a pure NLI, "make this axis smaller" has the LLM regenerate the whole spec with "no guarantee that it's not gonna change anything else" (SP-25 W12, [00:24:51]).
> - [[ART - DynaVis]] enforces modular widgets: "One of the main design [goals of] our system is to ensure modular widgets, so edits from two different widgets do not conflict or manipulate the chart in an unexpected [way]" (section 3.1, read aloud (SP-25 W12, [00:26:42])).
> - Joel Chan: "we're gonna use a domain specific language to constrain what is possible ... that helps overcome the conflicting stuff. But it does reduce the space of modifications. How much is an open question" (SP-25 W12, [00:27:12]).
> - A seminar participant flagged this as a limitation: the DSL "forces people to make their NLI statements basically at that level," e.g. you can't necessarily say "I wanna do this and that" (SP-25 W12, [00:25:17]). Joel called it "a good safety inspection thing" (SP-25 W12, [00:25:44]).
> - Asked whether letting the model generate freely would be better: "I think it would be terrible" (SP-25 W12, [00:27:55]).

## Other Notes

## Suggested relations
Claude:
> - informs → [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]]: modularity partly addresses it (Joel Chan, SP-25 W12 notes)
> - uses → [[PTN - Domain-Specific Language (DSL)]] and [[ART - Vega-Lite]]
> - informs → [[PTN - dynamically synthesized UI widgets]]
