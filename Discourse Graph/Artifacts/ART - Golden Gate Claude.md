---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e90-90b5-7f72-bca2-a59e6f93c8ed
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W10 (2025-04-02)]]"
created: 2026-11-24
---
## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> A demonstration of feature steering: a version of Claude in which a Golden Gate Bridge feature is amplified, so the model behaves as if it were the bridge. Discussed in the seminar as evidence that steering gives humans a handle on model behavior and as a hint of creative uses.

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> Clamp the Golden Gate Bridge SAE feature to a high activation during generation ([[PTN - feature steering]], [[PTN - Sparse Autoencoders (SAEs)]]).

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

Claude:
> A participant showed a screenshot: asked "what is your physical form?", the original model says it is an AI without a physical form, while the steered model says it has a physical form because it is a bridge (SP-25 seminar discussion, W10, [00:37:12]-[00:38:02]).

## Other Notes
Claude:
> Proposed baseline: put "I'm the Golden Gate Bridge" in the prompt instead (SP-25 seminar discussion, W10, [00:39:23]); see [[CLM - prompting is a more accessible steering mechanism than feature steering for non-technical users, but feature steering may offer more predictable dose-response control]].

## Suggested relations
Claude:
> - instantiates → [[PTN - feature steering]]
> - supports → [[CLM - feature steering may suit stylistic and creative control, where unexpected interactions are tolerable, better than control of contextual social constructs like bias]]
