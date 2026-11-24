---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e70-661e-77e1-bee0-9799d573ec8f
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/yvSXC-_4v
roamAuthor: "Joel Chan"
created: 2024-02-07
---
## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

![[Y5B7QXCSI4.png]]

Claude:
> The core technical contribution of [[@jiangGraphologueExploringLarge2023]]: an interaction medium that makes it easier for people to benefit from intelligent assistance. The hypothesis is that a dynamically created graph of LLM responses is more effective for people to learn from (in an information seeking task) AND is a more __controllable__ interaction medium. (Joel Chan, lit notes)

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> - [[PTN - prompt engineering]] with [[PTN - Large Language Models (LLMs)]] converts text to annotated nodes and links (marked by salience, with unique local IDs).
> ![[oTuu9BuaDj.png]] (p. 6)
>   - A very long prompt that uses [[PTN - few-shot in-context learning]]:
> ![[wngBOgKDrB.png]]
> ![[a_Xzp1XzhD.png]] (pp. 17-18)
>   - Plus error correction and saliency filtering.
>   - In this way the paper contributes back to the literature on text-to-graphical representations, or more generally "flexible representational transformation", which may be a neat design pattern.
> ![[tlSQpiB0jq.png]] (p. 3)
> - Various UI controls, including "tell me more" buttons for getting more output via "graph operations" (expand, explain, give examples, etc.).
> ![[5bJ4puNRhL.png]] (p. 9)
> ![[wT7J2spoE6.png]] (p. 10)
>
> (Joel Chan, lit notes on [[@jiangGraphologueExploringLarge2023]])

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

## Other Notes
Claude:
> - Joel Chan (🕸️ Connector, SP-24 seminar): the concept of [[PTN - Shared Representation]] nicely captures at least part of the secret sauce of both [[ART - ImageSense]] (the canvas, the ontology of mood words) and Graphologue (the knowledge graph). Is this why spreadsheets are so good for end-user programming? (see https://www.miramontes.com/writing/spreadsheet-eup/)
> ![[XJRveB7koI.png]]
> - Joel Chan (🕸️ Connector, SP-24 seminar) proposed analyzing it with Lipton's preliminary taxonomy of interpretability ([[@liptonMythosModelInterpretability2017]]): which interpretability desiderata does Graphologue target, compared with the [[PTN - Concept Activation Vectors (CAVs)]] in [[ART - SMILY]] or the slider in [[ART - ImageSense]]? Is anything missing?
> - Listed among the "systems we've seen" in Joel Chan's notes on properties of interpretability.
