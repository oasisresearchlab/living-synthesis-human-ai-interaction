---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e92-02b8-7890-869b-b572f5152d76
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W05 (2025-02-26)]]"
created: 2026-11-24
---
## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> Automatically searches for prompts that make a language model do what you want, with no human in the loop of finding the prompt. Came up in the seminar as a counterpoint to [[ART - ConstitutionMaker]], where a human discovers and writes the steering text. (SP-25 W05, [00:11:51]–[00:12:30])



## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> As described in the session: a machine learning model or language model explores variations of a prompt and returns the prompt that does what you want (SP-25 W05, [00:12:00]). "Is it DSPy? Yeah. Yeah, I think so." ([00:12:08]; the transcript renders it "DS pi").
> - The session did not go into DSPy's internals; this note records only how it was positioned.


## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

## Other Notes

Claude:
> - Joel Chan framed it as "a counterpoint to that, where the human is not involved in the process of finding a good prompt", and connected it to text-to-image prompts (Midjourney, Stable Diffusion) that get good results while looking "nothing like natural language... almost like programs" (SP-25 W05, [00:12:08]–[00:12:38]).

## Suggested relations
Claude:
> - instantiates → [[PTN - automatic prompt optimization]]: DSPy was the named example (SP-25 W05, [00:12:08])
> - informs → [[PTN - prompt engineering]]: an automated alternative to human prompt engineering
