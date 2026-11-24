---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e91-bb21-742e-9961-385172340f0b
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W14 (2025-04-30)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Introduced in [[@inanBetterSlowSorry2025]]: deliberately slowing a conversation at strategic moments (asking questions, revealing assumptions, pausing) so that the interaction is longer but has better long-term effects on goal alignment, modeling of the user's mental state, and task success. Joel Chan's gloss: "things that are intentionally slowing down an interaction that make it longer, but have positive long-term impact," which is "super ill defined" until it is cashed out from theory. (Joel Chan, SP-25 W14, [00:33:09])
> - The motivating contrast: current LLM response generation chases efficiency and low latency, which may hurt long-term goals. (SP-25 seminar discussion, SP-25 W14, [00:05:00])
> - The class read it as a version of conversational grounding and repair: "It's just conversational grounding" ([00:06:58]); "to me it's just Clark ... it's doing repair ... and checking for understanding" ([00:34:09]). See [[PTN - common ground]] and [[THE - conversational repair]].
> - Joel Chan connected friction to seamful design ([[PTN - Seamful XAI]]), slow search, and, further afield, epistemic action in distributed cognition (e.g., rotating Tetris pieces to build a mental model rather than to reach the goal directly). (Joel Chan, Connector thread, SP-25 W14)
> - S01's ELI5 framing linked it to System 2 (slow, effortful) vs. System 1 (fast, automatic) thinking. (S01, ELI5 linter, SP-25 W14)

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - positive friction ontology]]: the paper's typology of friction moves (Table 1).
> ![[-a1_xktn6N.png]]
> - Clarifying-scope questions in OpenAI Deep Research, and follow-up questions in commercial LLM chat products more generally. (S11, Connector, SP-25 W14)
> - Alexa-style clarification utterances ("Hmm, can you repeat that?") were raised as a possible precursor. (Connector thread, SP-25 W14)

## Other Notes

Claude:
> Contested in the session: whether friction helps depends on the user and the task framing ([[QUE - Under what task framings and for which users does positive friction in dialogue systems help rather than hurt?]]); whether the typology is too context-free ([[CLM - a context-free typology of friction utterances invites reward-hacked models that produce friction-like utterances without acting on them]]); and whether the paper's evidence supports its claims ([[EVD - positive friction annotations by 10 engineering undergraduates given a short lecture reached only low chance-adjusted agreement - @inanBetterSlowSorry2025]]).

## Suggested relations
Claude:
> - derived from → [[PTN - common ground]]: the paper frames friction as how dialogue systems build common ground (SP-25 W14, notes key question thread)
> - consistent with → [[PTN - Seamful XAI]]: both deliberately surface rather than hide gaps (Joel Chan, Connector, SP-25 W14)
> - informs → [[QUE - Under what task framings and for which users does positive friction in dialogue systems help rather than hurt?]]
