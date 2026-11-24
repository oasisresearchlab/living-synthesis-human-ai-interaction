---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e91-1ffe-7356-a92e-90a9e96f1b86
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-25 W07 (2025-03-12)]]"
created: 2026-11-24
---
## Grounds
Claude:
> - S01 (🚧 Safety Inspection Expert) questioned the authors' choice to add concept and policy embeddings because Sentence Transformer embeddings alone separated cases poorly: shouldn't raw sentence embeddings already reflect concepts? S01 suggested an ablation study. (SP-25 W07 notes)
> - Joel Chan's reading: sentence transformers embed the "whole" semantics of a case, which has many things in it, so any one concept is "diluted alongside the other stuff"; the concept embedding is added to *weight* the overall embedding toward the concept. (SP-25 W07 notes)
> - In discussion, Joel Chan conceded a point from S17: "when people define concepts, that gets added as a landmark, and then the spatial separation is influenced by not just the semantics of the case, also the embedding for the concept. So in that way you can modify the layout." (SP-25 W07, [00:25:28])

## Other Notes
Claude:
> Open: no ablation reported in the discussion; the size of the effect is unknown. (S01, SP-25 W07 notes)

## Suggested relations
Claude:
> - informs → [[ART - AI Policy Projector]]: explains its layout mechanism
> - consistent with → [[CLM - LLM-generated and custom-defined natural language concepts --- with mappings to example LLM outputs that contain those concepts --- support interpretable exploration of LLM output patterns]]
> - informs → [[CLM - map-like projections of high-dimensional embeddings need to communicate what their layout distorts, not just that information is lost]]: user concepts are one known source of layout distortion
