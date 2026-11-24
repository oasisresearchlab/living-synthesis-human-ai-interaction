---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e70-661e-70e9-b81b-cfe180455140
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/813UpfXVv
roamAuthor: "Joel Chan"
created: 2024-01-31
---
## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> - An integrated environment for designers' visual ideation, proposed in [[@kochImageSenseIntelligentCollaborative2020]]. It addresses [[QUE - How to incorporate intelligent assistance into the ideation process, while leaving the human designer in control?]], which can be generalized to [[QUE - How to incorporate intelligent assistance into human knowledge work, while leaving the human in control?]]. (Joel Chan, lit-notes on ImageSense and [[@jiangGraphologueExploringLarge2023]])
> ![[h8povsaa8O.png]]

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> - Four key aspects (from the intro): 1) curations from other designers, 2) **semantic search** for images, 3) **AI suggestions** from an AI co-explorer for images, and 4) AI-generated image **tag clouds** at various levels of abstraction, for reflection and sensemaking support. (Joel Chan, lit-notes)
> ![[2L3oNLY_fg.png]] (p. 2)
> - **Semantic search**: semantic labels for images, from Google's Vision object recognition and semantic labeling API (https://cloud.google.com/vision/), help users refine their search intent.
> ![[aQH1Mf2NVu.png]] (p. 9)
> - **AI suggestions**: the same semantic labels explain suggestions, which users can also refine. Suggestions use [[PTN - cooperative contextual bandits]], extended from looking only at color to also looking at image semantics. The "Suggest-o-matic Dial" controls the explore/exploit balance: explore = (not) more like this, exploit = more like this.
> ![[sBa_VR4egO.png]] (p. 10)
> - **Tag clouds** of AI-generated image tags.
> ![[QXTfOv8Ezs.png]] (p. 12)
> - Under the hood: Google Vision semantic labels plus cooperative contextual bandits.
> ![[tPgq-3SCAR.png]] (p. 8)
> (Joel Chan, lit-notes on [[@kochImageSenseIntelligentCollaborative2020]])
>
> - Latent design patterns:
>   - The tag clouds may be an instance of [[PTN - representational talkback]]; see [[ART - ART system]] in [[@yamamotoRepresentationalTalkbackApproach1998]] for an early example. (Joel Chan, SP-24 consolidated notes)
> ![[SnCXb_rk5J.png]]
>   - [[PTN - Shared Representation]] (the canvas, the ontology of mood words) captures at least part of the secret sauce. (Joel Chan, 🕸️ Connector, SP-24)

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

## Other Notes
Claude:
> - As Distiller in SP-24, Joel Chan picked three AI-support features (semantic search, AI suggestions, tag clouds) to explore against the session's core question. (Joel Chan, SP-24 seminar)
> - The image-focused refine-by-concept interaction in [[ART - SMILY]] (from [[@caiHumanCenteredToolsCoping2019]]) reminded Joel Chan "very much" of ImageSense, though refine-by-concept seems like it might be tougher. (Joel Chan, responding to S08, SP-24)
> - Open question from the Lipton session: what interpretability desiderata does the ImageSense slider target, compared with the [[PTN - Concept Activation Vectors (CAVs)]] in [[ART - SMILY]] or [[ART - Graphologue]]? (Joel Chan, 🕸️ Connector, SP-24; see [[@liptonMythosModelInterpretability2017]])
