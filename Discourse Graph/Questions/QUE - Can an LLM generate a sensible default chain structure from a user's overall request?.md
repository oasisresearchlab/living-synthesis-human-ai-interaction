---
nodeTypeId: node_Gp7JMdrzm9DUuPfBzUptc
nodeInstanceId: 01a20e92-1b6c-75b2-be23-36d552fcb261
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W03 (2025-02-12)]]"
created: 2026-11-24
---
## Context

Claude:
> S01 (Safety Inspection Expert, SP-25 W03 notes): "I am very curious about how the default chain structure is generated. I doubt the authors have prefixed a set of chain structures since there will be 8^2 combinations for a 2-step chain. And it will be even harder to match any of these default to a complex natural language question. If the default chain is randomly created, it will be less helpful other than providing a visual guide on how to manipulate the chain. I am wondering could we ask LLM to pre-generate a default chain based on users' overall requests?"
> - Joel Chan raised the same "where did these sub steps come from" question in class (SP-25 W03, [00:15:18]).

## Other Notes

Claude:
> S01 also noted that the claimed controllability depends on users' ability to divide the problem efficiently ([[CLM - the controllability benefits of LLM chaining depend on the user's ability to decompose the problem well]]); an LLM-proposed default could lower that bar, at some cost to user agency (see [[QUE - how do you balance foolproof automation and freedom of controllability?]]).

## Suggested relations

Claude:
> - informs → [[QUE - how can end user effectively author their own LLM chains?]]: model-proposed chains as a starting point for end-user authoring
> - informs → [[CLM - the controllability benefits of LLM chaining depend on the user's ability to decompose the problem well]]
