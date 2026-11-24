---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e91-c25e-704a-b2e0-a18433bbf16b
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W13 (2025-04-23)]]"
created: 2026-11-24
---
## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> A programming library for building workflows around language models. Joel Chan described it as "agent builder for programmers" and a "blast from the past" that "was like really hot for a while... in the AI building space" (SP-25 W13, [00:30:37]-[00:31:00]). It came up because AgentBuilder's interface (Figure 3) labels agents with "lang chain(Upload your docs)".

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> Boilerplate and quality-of-life abstractions for common LLM patterns: "you often want to like add examples or you often wanna do a rag kind of thing. And so there's a bunch of code that you don't have to write" (SP-25 W13, [00:31:14]). See [[PTN - few-shot in-context learning]] and [[PTN - Retrieval-Augmented Generation (RAG)]].

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

## Other Notes

Claude:
> - "It is not for non-programmers. It is for programmers." (Joel Chan, SP-25 W13, [00:31:37]). The contrast is the point: [[ART - AgentBuilder]] puts a no-code interface over the same kinds of operations.

## Suggested relations
Claude:
> - uses → [[PTN - Retrieval-Augmented Generation (RAG)]]: packages RAG boilerplate (SP-25 W13, [00:31:14])
> - uses → [[PTN - few-shot in-context learning]]: packages adding examples (SP-25 W13, [00:31:14])
