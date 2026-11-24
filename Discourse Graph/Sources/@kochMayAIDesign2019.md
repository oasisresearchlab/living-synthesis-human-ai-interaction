---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-6620-75ec-8d10-66dec500ca32
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/bQuLpeNH1
roamAuthor: "S06"
created: 2024-01-31
---

- Title: May AI?: Design Ideation with Cooperative Contextual Bandits
- Author(s):: Janin Koch, Andrés Lucero, Lena Hegemann, Antti Oulasvirta
- Abstract: Design ideation is a prime creative activity in design. However, it is challenging to support computationally due to its quickly evolving and exploratory nature. The paper presents cooperative contextual bandits (CCB) as a machine-learning method for interactive ideation support. A CCB can learn to propose domain-relevant contributions and adapt their exploration/exploitation strategy. We developed a CCB for an interactive design ideation tool that 1) suggests inspirational and situationally relevant materials ("may AI?"); 2) explores and exploits inspirational materials with the designer; and 3) explains its suggestions to aid reflection. The application case of digital mood board design is presented, wherein visual inspirational materials are collected and curated in collages. In a controlled study, 14 of 16 professional designers preferred the CCB-augmented tool. The CCB approach holds promise for ideation activities wherein adaptive and steerable support is welcome but designers must retain full outcome control.
- Type: Conference paper
- Publication: 
- URL : http://doi.acm.org/10.1145/3290605.3300863
- Date Added: July 31st, 2021
- Zotero links: [Local library](zotero://select/groups/2451508/items/PXP8IUXP), [Local library](https://www.zotero.org/groups/2451508/items/PXP8IUXP)
- Tags: creativity support tools, ideation support, interactive machine-learning, mood board design
- key question: how to support *cooperation* (augmentation) rather than automation in computational support for ideation (specifically here for visual desgin ideation)
  - ![[S5_NkOT5Tr.png]] (p. 1)
- related question: how to support designers collecting and curating materials
  - ![[NA6_0o9pV5.png]] (p. 2)
- how to identify and provide inspirational materials in a situationally appropriate manner?
- patterns
  - contextual example recommendation 
    - ![[CU5GaYv3dD.png]] (p. 2)
    - using cooperative contextual bandits
    - strategy selection
      - ![[U6pMn88lto.png]]
    - adapting to changes in design criterion
      - ![[m4mhPpvNQt.png]]
    - in the context of the UI
      - ![[fKU6Ysz0U6.png]]
  - explainable example recommendation

## Discussion notes
Claude:
> **Lineage.** The SP-24 🏺 Archaeologist (S06) brought it in as previous work by Janin Koch, first author of [[@kochImageSenseIntelligentCollaborative2020]]. It introduces the idea of integrating contextual bandits into design: the key question is how to support *cooperation* (augmentation) rather than automation in computational support for visual design ideation. (S06, SP-24)
>
> **Pattern.** The core pattern is contextual example recommendation using [[PTN - cooperative contextual bandits]], with strategy selection and adaptation to changes in design criteria, plus explainable example recommendation.
>
> **Connection to interactive model editing.** In the SP-25 seminar (🕸️ Connector thread), it was cited as earlier interactive machine learning, in response to [[ART - GAM Changer]]'s claim to be the first [[PTN - interactive model editing]] tool.
