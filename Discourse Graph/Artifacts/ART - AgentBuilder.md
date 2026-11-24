---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e91-c1b5-7fa8-88bc-a172a5db5bc9
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W13 (2025-04-23)]]"
created: 2026-11-24
---
## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> A prototype that lets library professionals who don't code create, test and refine their own conversational agents for patrons, from [[@zhengEvaluatingNonAIExperts2025]]. Built to explore [[QUE - How to enable non-AI experts to design and customize conversational agents for their own use in their own communities (without coding)?]].
> - Context (Sections 2.1-2.2, as summarized in discussion): libraries face high volumes of recurring questions plus a long tail of diverse ones, with too few staff; rule-based chatbots handle only simple queries and must be customized; librarians are skeptical of commercial solutions because the agent must fit their own community (SP-25 W13, [00:09:09]-[00:10:16]).

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> Three design goals were named in discussion (SP-25 W13, [00:19:39]): establish service boundaries and keep control over the service scope; align with professionals' expectations; customize to their case (where role-play comes in).
> - **Boundary setting**: define the agent's role, customize it by prompt design ("you are a friendly..."), and add knowledge resources (SP-25 W13, [00:21:39]-[00:22:08]). Joel Chan: this is what programmers always do when setting up LLM calls, "but this is a nice, like, human friendly way to do it."
> - **Knowledge synchronization / source transparency**: shows where a given response comes from, with a step-by-step breakdown; under the hood this is [[PTN - Retrieval-Augmented Generation (RAG)]] over documents librarians upload, on GPT-3.5-turbo (SP-25 W13, [00:23:25], [00:26:01]-[00:26:50]).
> - **Persona simulation and iterative testing**: the builder crafts a patron persona, invites it and the agent into a group chat, "plays" simulated dialogues, then uses Show and Edit buttons to adjust the agent's replies (Figure 3). See [[PTN - simulated user conversations with LLM-generated personas for testing conversational agents]].
> ![[Ab5FMlWGI-.png]]

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

Claude:
> Figure 3's user journey: a librarian creates an "Elderly Library Patron" persona ("curious about what types of books the library purchases... no prior knowledge of the library's acquisition policy"), puts it in a group chat with a "Library Policy Assistant" agent, simulates dialogues, and edits the assistant's replies to better match the persona's needs.

## Other Notes

Claude:
> - The design and evaluation were done in summer 2023, about six months after ChatGPT launched, though the paper appeared at CHI 2025 (SP-25 W13, [00:22:45], [00:30:03]).
> - Joel Chan was unsure whether editing a reply changes the agent's later behavior or is a one-off fix (SP-25 W13, [00:24:04]-[00:25:13]); see [[CLM - one-off edits to an LLM agent's responses do not help users design the agent unless the edits persist into its future behavior]]. Figure 3 also shows a "[Rule]" button next to Show and Edit that the discussion did not address.

## Suggested relations
Claude:
> - instantiates → [[PTN - Retrieval-Augmented Generation (RAG)]]: knowledge upload plus source display (SP-25 W13, [00:26:01])
> - instantiates → [[PTN - simulated user conversations with LLM-generated personas for testing conversational agents]]: Figure 3 user journey
> - informs → [[QUE - How to enable non-AI experts to design and customize conversational agents for their own use in their own communities (without coding)?]]: the paper's prototype for this question
