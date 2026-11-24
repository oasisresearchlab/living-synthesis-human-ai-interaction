---
nodeTypeId: node_Gp7JMdrzm9DUuPfBzUptc
nodeInstanceId: 01a20e70-661c-7604-9041-ac07ea757aae
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/WT6wCgWuD
roamAuthor: "Joel Chan"
created: 2025-03-24
---

## Context
Claude:
> Raised in the SP-25 seminar discussion of [[@petridisConstitutionMakerInteractivelyCritiquing2024]] ([[ART - ConstitutionMaker]]), from the 🚧 Safety Inspection Expert role.
> - Joel Chan named a "big gap": the tool offers no scaffolding for what counts as a "good" or "effective" principle. It also offers no support for reasoning about *interactions* between principles, which links back to [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]]. He saw a missed chance to reflect on this against other UIs such as [[ART - ChainForge]] and [[PTN - LLM Chains]]; the paper cites [[@wuAIChainsTransparent2022]] only in passing in related work. (Joel Chan, SP-25 seminar)
> - On interactions between principles: the system design did not anticipate conflicting principles, but a participant (P2) raised them, and P8 suggested a workflow change (S11, SP-25):
> ![[4GEZBl1cbw.png]]
> - S11 proposed authoring principles at the level of the *conversation* rather than per response: review the whole conversation, then rate each response. (S11, SP-25)
>     - Pro: more context goes into developing general principles, which may reduce (1) conflicting principles and (2) compositional principles that stack on each other.
>     - Con: risk that future AI responses drift "unaligned", making the whole conversation useless.
> - Section 7.4 of the paper (limits of principles) suggests design directions for authoring principles, e.g., visualizing conversation arcs (P14) or structured UI elements instead of natural language (P13). (S11, SP-25)
