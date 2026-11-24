---
nodeTypeId: node_Gp7JMdrzm9DUuPfBzUptc
nodeInstanceId: 01a20e92-1970-77a7-85ec-0677309fda15
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W03 (2025-02-12)]]"
created: 2026-11-24
---
## Context

Claude:
> Raised early in the SP-25 W03 discussion of [[@wuAIChainsTransparent2022]]: "is chaining like the right abstraction to be used to ... depict how we can complete a task using LLM"; the tasks in the paper "are still quite straightforward" and the structure "looks ... a little unidimensional", i.e., linear (SP-25 W03, [00:07:32]-[00:08:34]).
> - Joel Chan tied it to the previous week's discussion of local vs. global control: for "more iterative ... or complex task structures, is this going to be sufficient?" ([00:21:01]-[00:21:34]).
> - A participant pointed to a Miro board on how to write the discussion section of a CHI paper as an example of a decomposition that "doesn't just look linear ... there are a lot of interdependencies ... I don't see any directionality" ([00:21:34]-[00:22:35]).
> - The same participant asked whether linear vs. nonlinear decompositions map onto informational (textbook-like, linear) vs. procedural tasks ("multiple ways in doing it") ([00:22:35]-[00:23:37]).
> - Joel Chan connected this to the crowdsourcing literature's move away from fixed micro-task workflows for interdependent work ([00:23:41]-[00:25:00]); see [[CLM - micro-task workflow decomposition breaks down for complex work with many interdependencies that requires open-ended adaptation]].
> - Proposed direction: "maybe we have to do something drastic to the UI or task model to handle like more complex non linear tasks where we have to reason about interdependencies" (Joel Chan, [00:26:01]).

## Other Notes

Claude:
> The SP-25 notes also list "complex tasks that are nonlinear, iterative?" as a candidate class of tasks under [[QUE - How can we optimize LLM performance on complex, real-world tasks?]].

## Suggested relations

Claude:
> - informs → [[PTN - LLM Chains]]: questions the sequential structure of the pattern (SP-25 W03, [00:07:32])
> - informs → [[QUE - How can we help users accomplish complex tasks with LLMs in a way that is more transparent and debuggable?]]: a boundary condition on chaining as the answer
> - consistent with → [[CLM - micro-task workflow decomposition breaks down for complex work with many interdependencies that requires open-ended adaptation]]: same limit, raised for crowdsourcing workflows (Joel Chan, [00:24:09])
