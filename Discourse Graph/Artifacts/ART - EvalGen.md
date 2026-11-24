---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e70-661e-7c21-a295-2f7df7ca0258
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/H4z11ZFmY
roamAuthor: "Joel Chan"
created: 2025-03-24
---
## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> Helps users generate, implement, and validate evaluation criteria for LLM outputs. (Archaeologist "looking forward" notes, SP-25 seminar, on [[@shankarWhoValidatesValidators2024]])

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.
Claude:
> 1. The LLM suggests criteria in natural language.
> 2. Users select whether to implement each one.
> 3. In parallel, users vote outputs good or bad while EvalGen generates and tests evaluators in the background. The system uses the human grades to select the assertions that best align with user preferences. Assertions are automated eval functions (validators), code-based or LLM-based, that check whether the evaluated LLM's output meets specific criteria.
> 4. A report card shows the alignment between the chosen assertions and the user's grades.

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

## Other Notes
Claude:
> - The authors validated the tool in a qualitative study with 9 practitioners, which revealed "criteria drift": users need criteria to grade outputs, but grading outputs helps users define criteria. This raises the question of whether evals depend on seeing LLM output, rather than being definable a priori. (SP-25 seminar)
