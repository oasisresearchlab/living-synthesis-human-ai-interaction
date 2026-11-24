---
nodeTypeId: node_Gp7JMdrzm9DUuPfBzUptc
nodeInstanceId: 01a20e92-3eff-7a86-b7b1-f8ae31b71ee9
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 other weeks and synthesis]]"
created: 2026-11-24
---
## Context

Claude:
> Group 1 of the Week 9 synthesis noted that [[ART - GAM Changer]] uses commit logs so that edits can be reverted and audited by people with the relevant knowledge. That raised a governance question: once users can edit model behavior, what structure decides who is involved? Group 1 suggested, for example, "having an auditor/moderator to track and revert user-initiated commits." (SP-25 W09 synthesis, Group 1)
> - S01 added that reversible edits can undo damage, but something must also *detect* harmful edits, and floated "llm judge with constitution to safeguard model integrity." (S01, SP-25 W09 synthesis)
> - The worry comes from [[@wangInterpretabilityThenWhat2022]]: continuous feedback and reversible edits "do not guarantee to prevent users from overfitting the model, injecting harmful bias, or maliciously manipulating model predictions. This potential vulnerability warrants further study on how to audit and regulate model editing." (quoted by S01, SP-25 W09 synthesis)

## Other Notes

Claude:
> - Group 1 also asked "responsible edits? what knowledge is needed?", which ties governance to who has the expertise to judge an edit. (SP-25 W09 synthesis, Group 1)
> - Compare [[QUE - How might visual sensemaking LLM policy tools like ART - AI Policy Projector integrate into broader governance processes?]], which asks the same kind of question for LLM policy tools.

## Suggested relations

Claude:
> - informs → [[CLM - reversible, transparent model edits do not by themselves prevent harmful edits - interactive model editing also needs a way to detect and review harmful changes]]: the claim is a partial answer (reversibility is not enough) (SP-25 W09 synthesis)
> - consistent with → [[EVD - some data scientists cautioned about the need for (stronger) guardrails on model edits when using interactive editing tools like ART - GAM Changer - @wangInterpretabilityThenWhat2022]]: data scientists in the GAM Changer study also asked for guardrails (S01 citing @wangInterpretabilityThenWhat2022, SP-25 W09 synthesis)
> - informs → [[QUE - How might visual sensemaking LLM policy tools like ART - AI Policy Projector integrate into broader governance processes?]]: both ask how interactive model-steering tools fit into wider governance
> - informs → [[PTN - edit history with authorship and comments for accountable model editing]]: commit logs are the mechanism that makes tracking and reverting possible (Group 1, SP-25 W09 synthesis)
