---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e92-055c-704b-8a10-08faf076b92a
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W05 (2025-02-26)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Use a strong LLM to evaluate or critique other LLM outputs in place of (or alongside) human judges. Raised by S01 (Connector) under [[QUE - What is the effectiveness of LLM-generated critiques?]]: "Can LLM be a good judge?", citing Zheng et al. (2023), "Judging LLM-as-a-judge with MT-Bench and Chatbot Arena" (https://arxiv.org/pdf/2306.05685). (SP-25 W05 notes)


## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - The LLM-generated critiques and principle translations in [[ART - ConstitutionMaker]].
> - The LLM-based assertions (validators) in [[ART - EvalGen]], whose alignment with human grades must itself be checked ([[@shankarWhoValidatesValidators2024]]; S16, Archaeologist, SP-25 W05).

## Other Notes

Claude:
> - The "looking forward" paper ([[@shankarWhoValidatesValidators2024]]) frames the risk: LLM evaluators can inherit the same problems as the LLMs they evaluate, so someone has to validate the validators. (S16, SP-25 W05 notes)

## Suggested relations
Claude:
> - informs → [[QUE - What is the effectiveness of LLM-generated critiques?]]
> - supports → [[ART - EvalGen]]: EvalGen exists to check LLM-based evaluators against human grades
