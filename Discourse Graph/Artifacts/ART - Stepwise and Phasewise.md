---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e92-a4e4-7ff6-9acd-2067dfb50e12
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W03 (2025-02-12)]]"
created: 2026-11-24
---
## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> Improve steering and verification in AI-assisted data analysis programming ([[@kazemitabaarImprovingSteeringVerification2024]]).

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> Per the abstract: Stepwise "decomposes the problem into step-by-step subgoals with pairs of editable assumptions and code until task completion"; Phasewise "decomposes the entire problem into three editable, logical phases: structured input/output assumptions, execution plan, and code."
> See [[PTN - interactive task decomposition with step-by-step verification]].

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

Claude:
> A user doing data analysis checks the model's stated assumption and code at each step before proceeding (Joel Chan, SP-25 W03, [00:29:01]).

## Other Notes

Claude:
> Results: [[EVD - participants doing AI-assisted data analysis reported greater control with stepwise task decomposition than with a chat baseline - @kazemitabaarImprovingSteeringVerification2024]].

## Suggested relations

Claude:
> - instantiates → [[PTN - interactive task decomposition with step-by-step verification]]
