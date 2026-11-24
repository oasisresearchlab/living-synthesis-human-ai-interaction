---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e92-1e2f-76c2-b313-3e46947712d0
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W06 (2025-03-05)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Lay out prompt fragments along rows and columns of a grid, and have each cell compose its row and column fragments (often into slots of a base prompt) and render the model's output. The grid then shows how output varies along two dimensions at once.
> - How the seminar reconstructed [[ART - DreamSheets]]: "you get parts from the row and then parts from the column and you stuff it together into the prompt"; a participant refined this to a main prompt ("a smiling dog") with slots defined in it. (SP-25 W06, [00:17:41]–[00:18:40])
> - One participant described the two axes as "inter-differentiation and intra-differentiation": variations along a row drift further from the original, and moving to the next row applies another level of variation along the same vector. (SP-25 W06, [00:16:59]–[00:17:41])
> - Recompute on change: DreamSheets' "power cell" reruns the dependent grid when a cell's value is modified (SP-25 W06, [00:19:00]). Someone noted this "seems expensive" ([00:19:43]).
> - Source: [[@almedaPromptingDiscoveryFlexible2024]]

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - DreamSheets]] (spreadsheet formulas composing prompts for a text-to-image model)
> - [[ART - ChainForge]] has a related mechanism: prompt templates with variables crossed against inputs and models.

## Other Notes
Claude:
> - A computational version of [[PTN - small multiples]] and [[PTN - contact sheets]].

## Suggested relations
Claude:
> - [[ART - DreamSheets]] — instantiates → this pattern
> - derived from → [[PTN - small multiples]]
> - enables → [[CLM - ART - DreamSheets can enable sensemaking of text-to-image models by enabling users to construct reusable visual computational explorations of how prompt and parameter variations relate to image]]
