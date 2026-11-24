---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-661f-7cc2-bcab-3bd502a6c747
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/3G12foNAR
roamAuthor: "Joel Chan"
created: 2024-01-24
---

- Title: ImageSense: An Intelligent Collaborative Ideation Tool to Support Diverse Human-Computer Partnerships
- Author(s):: Janin Koch, Nicolas Taffin, Michel Beaudouin-Lafon, Markku Laine, Andrés Lucero, Wendy E. Mackay
- Abstract: Professional designers create mood boards to explore, visualize, and communicate hard-to-express ideas. We present ImageSense, an intelligent, collaborative ideation tool that combines individual and shared work spaces, as well as collaboration with multiple forms of intelligent agents. In the collection phase, ImageSense offers fluid transitions between serendipitous discovery of curated images via ImageCascade, combined text- and image-based Semantic search, and intelligent AI suggestions for finding new images. For later composition and reflection, ImageSense provides semantic labels, generated color palettes, and multiple tag clouds to help communicate the intent of the mood board. A study of nine professional designers revealed nuances in designers’ preferences for designer-led, system-led, and mixed-initiative approaches that evolve throughout the design process. We discuss the challenges in creating effective human-computer partnerships for creative activities, and suggest directions for future research.
- Type: Article
- Publication: Proceedings of the ACM on Human-Computer Interaction, 4(CSCW1), 1–27
- URL : https://dl.acm.org/doi/10.1145/3392850
- Date Added: December 13th, 2021
- Zotero links: [Local library](zotero://select/groups/2451508/items/JJG4PQWJ), [Web library](https://www.zotero.org/groups/2451508/items/JJG4PQWJ)
- PDF links : [Koch et al. - 2020 - ImageSense An Intelligent Collaborative Ideation .pdf](zotero://open-pdf/groups/2451508/items/RXYR7CN9)
- 📝 lit-notes
  - what are the questions from this paper that overlap with / connect to ours?
    - [[QUE - How to incorporate intelligent assistance into the ideation process, while leaving the human designer in control?]]
      - ![[50FgyKhvNV.png]] (p. 2)
    - some design problems for the mood board context (some HCAI problems) that unpack this
      - ![[64-Uga3f8-.png]] (p. 3: Digital Ideation Context Section)
      - need diverse types of inspiration support (hmm not really the core thing here)
      - accurately understanding designers' current context/intent
        - isn't supported in existing systems (at the time); need better ways to help designers express vague, nonverbal intents!
          - ![[xwVjcxVDV6.png]] (p. 4: Related Work)
      - non-intrusiveness (don't break flow) - also maybe not the core thing that interests us
  - [[ART - ImageSense]] as a way to address the questions/problems
    - ![[h8povsaa8O.png]]
    - is an integrated environment that has a bunch of components in it
      - from intro: four key aspects: 1) curations from other designers, 2) **Semantic Search** for images, 3) **AI Suggestions** AI co-explorer for images, and 4) AI-generated (image) **tag clouds** at various levels of abstraction for reflection/sensemaking support (unclear what this is at this point)
        - ![[2L3oNLY_fg.png]] (p. 2)
      - **Semantic Search** for images
        - ![[aQH1Mf2NVu.png]] (p. 9)
          - semantic labels for images from Google vision object recognition and semantic labeling API to help refine (intent for) search
      - **AI Suggestions** AI co-explorer for images
        - ![[sBa_VR4egO.png]] (p. 10)
          - uses semantic labels for images from Google vision object recognition and semantic labeling API to provide explanations for suggestions (can also refine)
          - uses [[PTN - cooperative contextual bandits]], enhanced from just looking at color, to also looking at semantics (analyzed from the images)
          - the Suggest-o-matic Dial is a way to control the explore/exploit balance: explore = (not) more like this / exploit = more like this
      - AI-generated (image) **tag clouds** at various levels of abstraction for reflection/sensemaking support
        - ![[QXTfOv8Ezs.png]] (p. 12)
    - technical under the hood
      - semantic labels for images from Google vision object recognition and semantic labeling API
        - ![[tPgq-3SCAR.png]] (p. 8)
        - https://cloud.google.com/vision/
      - [[PTN - cooperative contextual bandits]]
  - evidence of efficacy? anything learned from user eval?
    - lots of stuff in 8.3 that validates design hypotheses around accurately understanding designers' current context/intent (including helping the designers themselves!)

## Discussion notes
Claude:
> **Where it sat.** Listed among the design examples in the seminar readings, and assigned in Week 2 (January 31st, 2024) of the SP-24 seminar under "Interaction / agency".
>
> **The question.** Joel Chan's lit notes frame it as addressing [[QUE - How to incorporate intelligent assistance into the ideation process, while leaving the human designer in control?]]. The most relevant design problem is accurately understanding designers' current context and intent, including helping designers express vague, nonverbal intents, which existing systems did not support at the time.
>
> **The system.** [[ART - ImageSense]] is an integrated environment with four parts: curations from other designers, semantic image search, an AI co-explorer that suggests images, and AI-generated tag clouds at several levels of abstraction for reflection. Under the hood it uses Google Vision semantic labels and [[PTN - cooperative contextual bandits]] (extended from color to semantics). The Suggest-o-matic Dial lets designers control the explore/exploit balance.
>
> **Patterns noticed in discussion.**
> - Joel Chan (🕸️ Connector, SP-24) saw [[PTN - Shared Representation]] as part of the secret sauce of both ImageSense (the canvas, the ontology of mood words) and [[ART - Graphologue]] (the knowledge graph).
> - Lineage: it builds on the first author's earlier [[@kochMayAIDesign2019]], which introduced cooperative contextual bandits for design ideation.
>
> **Evidence of efficacy.** Section 8.3 has a lot that validates the design hypotheses about accurately understanding designers' current context and intent, including helping designers themselves understand it. (Joel Chan, lit notes)
