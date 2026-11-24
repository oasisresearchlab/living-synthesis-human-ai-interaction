---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e70-661e-7055-82a3-3ea93eb338da
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/FFtVW3h_-
roamAuthor: "Joel Chan"
created: 2025-02-25
---

## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> - Lets users steer an LLM chatbot by turning their critiques of its responses into principles, from [[@petridisConstitutionMakerInteractivelyCritiquing2024]]. (SP-25 seminar)
> ![[CM-Onc0iD7.png]]

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> - An LLM-powered "suggest → compile" step turns critiques into principles. (SP-25, 👩🏽‍🔬 Distiller thread)
> ![[tjDCpzCnrS.png]]
> ![[JWlSOseMSf.png]]
> - "Constitution Maker, users can provide either positive or negative feedback in natural language, select auto-generated feedback, or rewrite the chatbot's response; each mode of feedback automatically generates a principle that is inserted into the chatbot's prompt." (Petridis et al., 2024, p. 854; quoted by S09, SP-25)
> - The prompt structure discussed: a system prompt that always stays (e.g., "you are friendly and helpful"), prior conversational turns (the part that gets truncated), and the user's actual text (e.g., "what is genAI?"). Principles go into the prompt alongside these. (SP-25)

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

## Other Notes
Claude:
> - Critiques from Joel Chan (SP-25): "i'm kinda aghast that it's hard coded to be specific and conditional: no wonder they later find that things conflict!" and "I'm also really... really.... really wondering how good the translations are" (from critique to principle).
> - Open problem: no support for reasoning about interactions between principles, which connects to [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]] A later paper in SP-25 explicitly cited ConstitutionMaker and, in theory, targets this problem, under the question [[QUE - how can we support users to reason about whether they have the right policies when steering LLMs with policy?]]
> ![[q-sl_43qs5.png]]
> - Another SP-25 reading that helps users discover and generate variations in prompt space was noted as doing something similar to ConstitutionMaker's surfacing of possible rules.
