---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e91-886d-7265-bec5-25fd1ef51aba
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W06-07 Explainability and trust]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Design decisions so affected people can challenge them. The EU position quoted in [[@liptonMythosModelInterpretability2017]]: "individuals affected by algorithmic decisions have a right to explanation... algorithmic decisions should be contestable." This requires systems that (i) "present clear reasoning based on falsifiable propositions" and (ii) "offer some natural way of contesting these propositions and modifying the decisions appropriately if they are falsified" (S13, Distiller, SP-24 W06).
> S13 noted the Popperian flavor: it makes the model a "little scientist" that can be argued with like a human.

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> Seminar ideas (SP-24 W06):
> - expose weighted factors so the user can contest the weights; where several outputs are "correct," show how they differ and let the user decide (S05)
> - let users check whether the claimed factors are actually used, e.g., with [[PTN - Contrastive explanations]] (S11)

## Other Notes

## Suggested relations
Claude:
> - informs → [[QUE - Why is interpretability important?]]: contestability is one of the session's answers (the QUE already records the S05 and S11 responses)
> - uses → [[PTN - Contrastive explanations]]
