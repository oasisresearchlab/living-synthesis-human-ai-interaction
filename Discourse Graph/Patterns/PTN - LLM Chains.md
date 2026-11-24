---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e70-661e-7027-b5cd-4e7a6befb269
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/gEEFknLn3
roamAuthor: "Joel Chan"
created: 2025-02-11
---

## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Key source: [[@wuAIChainsTransparent2022]] (SP-25 Distiller notes).
> ![[NxSYURAfl9.png]]
> ![[T8Ynos6mPc.png]]
> - Core idea: **decompose** a large complex task into smaller, well-scoped subtasks that map to one of 8 curated LLM primitive operations, and provide a way to **chain** these subtasks together.
> ![[x_dHv3BwcZ.png]]
> - The 8 primitives were mined from 73 online demos of LLMs.
> ![[PlF6DsnFyk.png]]
> ![[5Bpq7CEy1C.png]]
> ![[DhIKnKa8RR.png]]
> - Inspired by [[PTN - crowdsourcing pipelines]].
> ![[mpkwHijZps.png]]
> ![[z73I6yeDPY.png]]
> - Each chain step is basically an LLM call with a prompt design, with slots that can take outputs from a previous step as input.
> ![[2h3OM8vaB4.png]]

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - The interface in [[@wuAIChainsTransparent2022]] lets users make and control chains: a visual representation of the chains; local and global control; direct editing of each step's prompts and outputs; and global connections between chains via [[PTN - Visual Programming]].
> ![[W6P6txCsD1.png]]
> ![[VOGBnfknpA.png]]
> - [[ART - ChainForge]] "is a direct extension of" LLM Chains (SP-25 Distiller notes on [[@arawjoChainForgeVisualToolkit2024]]).
> ![[_2X4qvEqX7.png]]

## Other Notes

Claude:
> - Joel Chan (SP-25, on ConstitutionMaker): testing principles is not well supported there relative to [[ART - ChainForge]] or LLM Chains; a missed opportunity to reflect on such UIs, since it cites [[@wuAIChainsTransparent2022]] only in passing in related work.
> - S05 (SP-25, Group 1): LLM Chains and ChainForge offer "technical resources" of a different kind than [[ART - GAM Changer]]: less about directly manipulating a glassbox model, more about giving people "cognitive (or thinking?) resources" to examine LLM behavior against multiple changing prompt parameters and formulate rules or principles (similarly ConstitutionMaker and [[ART - AI Policy Projector]]). S05 also suggested tools like GAM Changer and LLM Chains can offer "Task Resources": support for how people or groups plan and discuss how to use AI tools for the task at hand.
