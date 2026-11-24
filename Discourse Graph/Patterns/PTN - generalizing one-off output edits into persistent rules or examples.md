---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e91-c3fe-704f-b189-10240bed0b77
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W13 (2025-04-23)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> When a user corrects one bad model output, the interface offers to generalize the correction into something that persists: a rule added to the prompt, a stored few-shot example, or a steering vector.
> - Joel Chan: "we know different ways that you could persist the edits, right? You can craft rules around them, you can make them in examples. You can... get the vectors out of them and then steer the... prompt responses... maybe you can add like a little button here, like make a rule out of this" (SP-25 W13, [00:27:39]-[00:28:17]).

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - ConstitutionMaker]]: "You see a thing you don't like, you edit it and then you can generalize that to say, make this a rule, and then it got stuffed into the prompt" (SP-25 W13, [00:28:17]). (Initially misremembered in discussion as "policy crafter", [00:29:04].)
> - Possible in [[ART - AgentBuilder]]: Figure 3 shows a "[Rule]" button, though the discussion didn't establish what it does.

## Other Notes

Claude:
> - Proposed as an easy future-work addition to AgentBuilder, which was designed in summer 2023, before ConstitutionMaker (2024) (SP-25 W13, [00:29:04]-[00:30:03]).

## Suggested relations
Claude:
> - uses → [[PTN - few-shot in-context learning]]: one way to persist an edit
> - uses → [[PTN - feature steering]]: steering vectors as another way (SP-25 W13, [00:27:58])
> - informs → [[CLM - one-off edits to an LLM agent's responses do not help users design the agent unless the edits persist into its future behavior]]: the remedy for non-persistent edits
