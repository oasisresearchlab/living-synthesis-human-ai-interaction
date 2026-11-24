---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e91-1efa-7ddb-9b47-7227ab556842
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-25 W07 (2025-03-12)]]"
created: 2026-11-24
---
## Grounds
Claude:
> - Joel Chan framed the "secret sauce" of [[ART - AI Policy Projector]] ([[@lamAIPolicyProjector2024]]): "you don't wanna just work in policy land ... say rules without looking at the actual cases, 'cause the world is messy," and you want to "go back and forth between like, how does the model behave under these conditions? How do the like different concepts interact?" (SP-25 W07, [00:21:59])
> - The paper's own framing contrasts this with approaches like [[PTN - Constitutional AI]], which assume we already know the policy and focus on getting the model to execute it (the "forward pass"). Deciding whether we have the right policies is the "backward pass". (Joel Chan, Distiller thread, SP-25 W07; SP-25 W07, [00:14:42])
> - Domain-specific support comes from "criteria drift" in [[@shankarWhoValidatesValidators2024]]: users need criteria to grade outputs, but grading outputs helps them define criteria (S16, SP-25 W07). See [[EVD - practitioners using EvalGen showed criteria drift, needing criteria to grade LLM outputs but refining those criteria by grading outputs - @shankarWhoValidatesValidators2024]].
> - S05 (🕸️ Connector) saw concepts, cases, and if-then logic as a way to help users "factorize a fuzzy problem or phenomenon to distill principles or rules based on specific factors." Joel Chan linked this to cautions from expertise research about over-indexing on principles: cases keep principles and schemas flexible enough for unseen problems ([[THE - Cognitive Flexibility Theory (CFT)]]). (SP-25 W07 notes)

## Other Notes
Claude:
> Joel Chan noted that this result is "kinda obvious a priori" from [[THE - Sensemaking Theory]], but that domain-specific validation is still useful. (SP-25 W07 notes)

## Suggested relations
Claude:
> - supports → [[QUE - how can we support users to reason about whether they have the right policies when steering LLMs with policy?]]: the claim answers the QUE's "need cases" intuition (SP-25 W07 notes)
> - derived from → [[THE - Cognitive Flexibility Theory (CFT)]]: cases keep principles flexible (Joel Chan, SP-25 W07 notes)
> - consistent with → [[THE - Sensemaking Theory]]
> - [[EVD - practitioners using EvalGen showed criteria drift, needing criteria to grade LLM outputs but refining those criteria by grading outputs - @shankarWhoValidatesValidators2024]] — supports → this node
> - informs → [[ART - AI Policy Projector]]
