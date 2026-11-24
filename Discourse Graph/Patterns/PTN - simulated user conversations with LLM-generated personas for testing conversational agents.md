---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e91-c488-793c-ae80-3ad6fb16342c
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W13 (2025-04-23)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> To test a conversational agent before deployment, the builder writes a prompt for a simulated user persona, puts the persona and the agent in a conversation, generates multiple dialogues, and refines the agent based on what goes wrong. From [[ART - AgentBuilder]] ([[@zhengEvaluatingNonAIExperts2025]], Figure 3).
> ![[Ab5FMlWGI-.png]]

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - AgentBuilder]]: "Elderly Library Patron" persona in a group chat with a "Library Policy Assistant".

## Other Notes

Claude:
> - Contested in discussion. Joel Chan: "This is controversial... My hypothesis is that using LLMs for personas, for designing for marginalized and diverse populations increases marginalization by stereotyping. And there's some evidence for that... especially for like earlier versions of models" (SP-25 W13, [00:20:12]). See [[CLM - LLM-generated personas can flatten and caricature marginalized identity groups]].
> - A participant connected this to a recent departmental brown-bag talk on LLMs' discriminatory tendencies toward people with disabilities: asking several LLMs to write a story about a person with a disability yields stereotyped outputs (SP-25 W13, [00:20:42]-[00:21:34]).
> - Counterpoint: see [[CLM - persona descriptions with specific behavioral characteristics may be less prone to stereotyping than category labels when LLMs simulate users]].

## Suggested relations
Claude:
> - informs → [[CLM - LLM-generated personas can flatten and caricature marginalized identity groups]]: the risk applies directly to this pattern (SP-25 W13, [00:20:12])
