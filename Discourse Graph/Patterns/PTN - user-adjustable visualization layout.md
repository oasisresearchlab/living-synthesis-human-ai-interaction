---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e91-8810-7534-bebf-8521d362e864
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W11 (2025-04-09)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Let users rearrange a visualization so it matches how they think about the content, instead of fixing the layout. S01 (🚧 Safety Inspection Expert, SP-25 W11): visualization helps make sense of models but can suffer optical illusions such as ambiguity and distortion; Patchview counters this by letting users "adjust the layout of concepts (Figure 4d), aligning their visual presentation with how they want to think about these concepts and elements" ([[@chungPatchviewLLMpoweredWorldbuilding2024]]). S01 tagged it "PTN adjustable magnet location".

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - Patchview]]: users can move concept magnets around a view.

## Other Notes
Claude:
> Related to the vault's concern about fixed projections: [[CLM - UMAP 2D projections do not produce meaningful global spatial separation]].

## Suggested relations
Claude:
> - instantiates ← [[ART - Patchview]]: Patchview instantiates this pattern
> - informs → [[PTN - Direct Manipulation]]
> - informs → [[CLM - UMAP 2D projections do not produce meaningful global spatial separation]]: user control over layout is one answer to misleading spatial positions
