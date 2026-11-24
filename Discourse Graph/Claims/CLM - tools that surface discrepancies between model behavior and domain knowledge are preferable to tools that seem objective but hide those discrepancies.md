---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e92-2673-725c-8f7d-1708c74502db
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-25 W02 (2025-02-05)]]"
created: 2026-11-24
---
## Grounds
Claude:
> "I would rather have a tool that makes us ask that question than a tool that feels objective that hides these things ... my bias of like, I like systems like this that like sort of reveal these discrepancies" (Joel Chan, SP-25 W02, [00:29:11]–[00:29:30]).
>
> The trade-offs then belong in a joint conversation: "maybe the accuracy goes up, but then we will harm 10 percent more patients by not treating them ... So we're going to be conservative ... Those are not decisions that should be done by the engineer alone or the domain expert alone ... This artifact can be a useful prop for those kinds of [conversations]." (SP-25 W02, [00:29:30]–[00:30:15])
>
> Case study example: the physician in the sepsis case study edited the temperature and blood pressure features with an eye to false negatives ([[EVD - it was possible for a two physicians to use ART - GAM Changer to edit a GAM model for sepsis risk prediction to account for possible issues with temperature, respiratory rate, and systolic blood]]).

## Other Notes
Claude:
> - Stated as Joel Chan's preference ("my bias"), not as a tested result.
> - [[ART - GAM Changer]]'s notes already include the related hypothesis that a benefit of direct manipulation tools is to elicit noticing and discussion of fine-grained discrepancies.

## Suggested relations
Claude:
> - informs → [[CLM - ART - GAM Changer or PTN - Direct Manipulation-based approaches to steering models are best used in collaborative teams with domain experts - end users and ML engineers]]
> - informs → [[PTN - boundary object(s)]]: the artifact as a "prop" for cross-expertise talk
> - uses → [[PTN - Shared Representation]]: shape functions are what make the discrepancies visible (SP-25 W02, [00:17:00])
