---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e92-267c-748c-9b09-4efae1882baa
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W03 (2025-02-12)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Decompose a task into subgoals at run time and have the user inspect and verify (or edit) each step, such as a stated assumption plus the code for it, before the system continues. Key source: [[@kazemitabaarImprovingSteeringVerification2024]].
> - Joel Chan: "rather than having the model do the whole thing at once ... the model first like articulates an assumption and then generates some code and then you verify each step before proceeding. So this kind of like real time, almost like chaining ... quite laborious, but people found it to be the most useful for ... controlling what's happening" (SP-25 W03, [00:28:38]-[00:29:35]).
> - A participant had just suggested that "having things that could be available in real time, but then broken down into smaller steps" is valuable ([00:27:57]).

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - Stepwise and Phasewise]]

## Other Notes

Claude:
> A real-time, model-proposed relative of [[PTN - LLM Chains]], where the user authors the chain in advance.

## Suggested relations

Claude:
> - consistent with → [[PTN - LLM Chains]]
> - informs → [[QUE - How might interfaces make the intermediate steps of reasoning models visible and useful to people?]]
> - informs → [[QUE - How can we help users accomplish complex tasks with LLMs in a way that is more transparent and debuggable?]]
