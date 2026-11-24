---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e91-87e6-72a2-94d4-116b0dce13fe
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W05 Explainability]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Retrieve items (here, images) by similarity of their content features rather than by text metadata. In [[@caiHumanCenteredToolsCoping2019]] the technical affordance is CBIR over pathology images from previously diagnosed cases, used to support clinical decision-making. Its known weakness is the semantic gap ([[CLM - the semantic gap between what an algorithm extracts from an image and what a user means by it is a core obstacle for content-based retrieval in expert work]]). (S05, 👩🏽‍🔬 Distiller, SP-24 W05)
> - At the end of the introduction, the paper notes that its approach may extend to other domains via the general class of CBIR problems. (Joel Chan, replying to S11, SP-24 W05)

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - SMILY]]: returns visually similar images from past patients for a query tissue image. (S05, SP-24 W05)
> - [[ART - ImageSense]] does semantic image search for designers, which Joel Chan linked to SMILY in the same session.
## Other Notes

## Suggested relations
Claude:
> - instantiates ← [[ART - SMILY]] (S05, SP-24 W05)
> - informs → [[CLM - the semantic gap between what an algorithm extracts from an image and what a user means by it is a core obstacle for content-based retrieval in expert work]]: the semantic gap is a defining limitation of CBIR (S05, SP-24 W05)
