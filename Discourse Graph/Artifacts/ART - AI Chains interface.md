---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e92-2aba-7c8a-8856-3eea618bec00
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W03 (2025-02-12)]]"
created: 2026-11-24
---
## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> Let users build, run, and debug [[PTN - LLM Chains]] so that complex tasks with LLMs are more transparent and controllable ([[@wuAIChainsTransparent2022]]).

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> A visual representation of chains, with global control over connections between steps ([[PTN - Visual Programming]]) and local control to directly edit each step's prompt and output (SP-25 Distiller notes; Joel Chan, SP-25 W03, [00:20:39]-[00:21:01]). Each step uses one of 8 LLM primitive operations mined from 73 online LLM demos.
> ![[NxSYURAfl9.png]]
> ![[W6P6txCsD1.png]]
> ![[VOGBnfknpA.png]]

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

Claude:
> Writing a constructive peer review: identify issues, split them into sub-problems, ideate suggestions for each, then compose a paragraph (Joel Chan, [00:04:16]). The paper also shows personalized flashcard creation, visualization-code debugging, and assisted text entry.

## Other Notes

Claude:
> Evaluated with [[ART - LaMDA]] against a sandbox modeled on [[ART - GPT-3 Playground]]. No hosted demo was available ([[EVD - PhD seminar participants found the AI Chains paper hard to understand without a hosted demo, and a recorded walkthrough of the system helped]]). S01 (notes) flagged unmet needs: seeing how an edit to an intermediate step affects the final output, and rolling back to previous outputs after regenerating (cf. [[EVD - some difficulty reasoning about the big picture and how it changes when zooming in on steps - @wuAIChainsTransparent2022]]).

## Suggested relations

Claude:
> - instantiates → [[PTN - LLM Chains]]
> - uses → [[PTN - Visual Programming]]
> - informs → [[ART - ChainForge]]: ChainForge extends this line of work
