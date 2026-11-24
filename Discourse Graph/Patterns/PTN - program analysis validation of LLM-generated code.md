---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e91-192d-7c6e-bfe0-453445255da5
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W12 (2025-04-16)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Check LLM-generated code with programming-language tooling (parsing to a syntax tree, linting, schema validation) before running or rendering it, rather than relying on instructions in the prompt to produce valid output.
> - In [[@vaithilingamDynaVisDynamicallySynthesized2024]], generated Vega-Lite is parsed and linted to ensure validity (SP-25 W12, [00:23:00]).
> - Joel Chan: instead of "please generate valid code ... all bets are off," have a checker (SP-25 W12, [00:31:32]).

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - DynaVis]] (static analysis of synthesized Vega-Lite specs).

## Other Notes

## Suggested relations
Claude:
> - consistent with → [[PTN - Domain-Specific Language (DSL)]]: a grammar makes the output checkable
