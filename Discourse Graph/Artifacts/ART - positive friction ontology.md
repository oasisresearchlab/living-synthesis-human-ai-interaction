---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e91-be64-7e84-8d13-33554ec6c3e8
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W14 (2025-04-30)]]"
created: 2026-11-24
---
## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> A typology (Table 1 of [[@inanBetterSlowSorry2025]]) that names concrete kinds of "positive friction" a dialogue system can produce, so the concept can be annotated, tested, and trained for. (Joel Chan, SP-25 W14, [00:30:00])

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> Draws on discourse and cognitive science theory to list friction moves with example utterances. The class's sanity check found that the categories make sense at a conceptual level but use different terms from the grounding literature: they cover repair, checking for understanding, and revealing the agent's understanding or assumptions. The student was unsure whether anything was missing or whether the clustering was accurate. (SP-25 seminar discussion, SP-25 W14, [00:34:09]-[00:34:56])
> ![[-a1_xktn6N.png]]
> ![[PcLTeyun33.png]]
> - Key difference from Clark and Wilkes-Gibbs's framework: the table has no prior context. It says "this kind of utterance is this kind of friction," whereas the source theory says an utterance is a kind of move *if it follows a prior context* where the interlocutors are in a given state. (Joel Chan, SP-25 W14, [00:37:10]-[00:37:35])

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

Claude:
> - Used in [[@inanBetterSlowSorry2025]] to annotate turns in [[ART - Multi-Domain Wizard-of-Oz dataset (MultiWOZ)]] and [[ART - TEACh dataset]].
> - Joel Chan imagined using it to build a "positive friction agent," refactor it into specialized dialogue agents, or curate a training dataset of examples. (Joel Chan, SP-25 W14, [00:31:08])

## Other Notes

Claude:
> Joel Chan's closing take: "the more I look at this table, the less I like it for the lack of context." He recommended looking at Tables 1 and 3 from Clark and Wilkes-Gibbs instead. (Joel Chan, SP-25 W14, [00:48:58]-[00:50:08]) See [[CLM - a context-free typology of friction utterances invites reward-hacked models that produce friction-like utterances without acting on them]].

## Suggested relations
Claude:
> - instantiates → [[PTN - positive friction in dialogue systems]]
> - derived from → [[THE - conversational repair]]
> - informs → [[CLM - translating a theory-derived concept like positive friction into a typology of concrete dialogue moves makes its effects testable and trainable]]
> - informs → [[CLM - a context-free typology of friction utterances invites reward-hacked models that produce friction-like utterances without acting on them]]
