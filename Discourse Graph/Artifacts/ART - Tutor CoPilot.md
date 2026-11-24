---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e92-27dc-7d45-ad0a-4922d48c44a8
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W03 (2025-02-12)]]"
created: 2026-11-24
---
## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> Help human tutors respond to students more like expert tutors, raising "the floor of existing human tutors" (Joel Chan's notes, SP-25 W03). Wang et al. 2024, https://arxiv.org/pdf/2410.03017.

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> - An LLM tuned to follow sub-steps from a task analysis of expert tutor chat transcripts (e.g., identify the error, choose a strategy, describe the intention) instead of producing a tutor response in one shot (Joel Chan, SP-25 W03, [00:17:19]-[00:18:22]). See [[PTN - expert task analysis to structure LLM assistance]].
> - Suggestions go to a human tutor, not directly to students ([00:18:22]). See [[PTN - AI copilot that scaffolds a human practitioner instead of replacing them]].
> ![[VrvtHNXKzt.png]]

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

Claude:
> Human tutors working with students (math, per Joel Chan in class) get real-time suggested moves during a session. Presented at an HCIL brown-bag talk by Rose Wang.

## Other Notes

Claude:
> Results: [[EVD - lower-rated and less experienced human tutors benefited most from LLM-generated Tutor CoPilot guidance, even though more experienced tutors clicked on it more (Wang et al. 2024)]].

## Suggested relations

Claude:
> - instantiates → [[PTN - expert task analysis to structure LLM assistance]]
> - instantiates → [[PTN - AI copilot that scaffolds a human practitioner instead of replacing them]]
