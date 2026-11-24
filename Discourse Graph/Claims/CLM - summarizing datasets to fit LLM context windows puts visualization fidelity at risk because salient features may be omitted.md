---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e91-1533-75f9-b6bf-7ec2f8d721e0
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-25 W12 (2025-04-16)]]"
created: 2026-11-24
---
## Grounds

Claude:
> - S01 (🚧 Safety Inspection Expert, SP-25 W12 notes): both the data summary and visualization rely on the [[ART - LIDA]] summarizer, which works around input limits "but also raises concerns about data fidelity and possible missing information. The final visualization quality now highly depends on Lida summarizer's performance."
> - In discussion: "when I do data visualization I want to preserve everything ... I would be concerned if during the summarization process, some interesting feature got omitted"; every input and interaction is based on the summary (SP-25 W12, [00:20:25]).
> - Context: the paper used GPT-3.5, so the whole dataset could not fit in context (SP-25 W12, [00:20:03]). LIDA summarizes data types, general statistics, and random samples per column, then enriches them (SP-25 W12, [00:22:27]).

## Other Notes

## Suggested relations
Claude:
> - informs → [[ART - LIDA]]
> - informs → [[QUE - How would the advantage of dynamically synthesized widgets over natural language editing change with stronger models and better prompting practices?]]: larger context windows may change this constraint (SP-25 W12, [00:20:03])
