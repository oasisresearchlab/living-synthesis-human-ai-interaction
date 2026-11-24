---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e91-15ac-7b8e-9026-c3861da283bf
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-25 W12 (2025-04-16)]]"
created: 2026-11-24
---
## Grounds

Claude:
> - Prompted by [[EVD - a PhD student using LLMs to generate time-series forecasting code ran into hallucinated or deprecated methods and incompatible packages]], the seminar looked up code-generation leaderboards on Papers with Code. On [[ART - HumanEval]] a top OpenAI o1-based entry reported about 99% one-shot accuracy (SP-25 W12, [00:33:45]) (ASR is noisy here; model names uncertain).
> - Participants questioned this: the problems "could be simple, they could be complicated," and "it's likely that data has been contaminated ... you're testing on the training set" (SP-25 W12, [00:34:00]).
> - Inspecting the dataset: "164 original programming problems," which looked like simple software-interview questions, e.g., "return the sum of all the odd elements that are in even positions"; "that's so easy" (SP-25 W12, [00:34:19]).

## Other Notes

## Suggested relations
Claude:
> - informs → [[CLM - programmatic validation of LLM-generated code is more dependable than prompting the model to produce valid code]]: benchmark scores alone do not justify skipping validation
> - consistent with → [[CLM - the reliability of LLM-generated code depends on how common and stable the target language or library is in web training data]]
