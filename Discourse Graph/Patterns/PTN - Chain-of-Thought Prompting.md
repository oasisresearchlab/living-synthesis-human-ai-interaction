---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e70-661e-7326-b992-9bc83772d0c8
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/hm24TyiC6
roamAuthor: "Joel Chan"
created: 2025-02-11
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> - Elicit step-by-step reasoning from an LLM within a single few-shot prompt. Key source: [[@weiChainofThoughtPromptingElicits2022]] (https://arxiv.org/pdf/2201.11903).
> - It shares the "divide and conquer" philosophy of [[PTN - LLM Chains]]; "the major difference is CoT is not sequential. Instead it provides this step-by-step reasoning in one single few-shot prompt." (S01 as 🕸️ Connector, SP-25)
> - Now "part of most models today" (SP-25 notes, under [[QUE - To what extent do modern reasoning LLMs still struggle with complex tasks?]]).

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.
## Other Notes
Claude:
> Joel Chan's response to S01 in the SP-25 session on [[QUE - How can we optimize LLM performance on complex, real-world tasks?]]:
> - "GREAT connection. in fact, the COT paper cites this one!" The CoT paper fleshes out a family of related ideas, some reaching back quite a bit in time:
> ![[4_dgIJIppp.png]]
> ![[9FwOZ4eq-x.png]]
> - The paper also helps flesh out the idea that this chaining approach isn't just great for human control: it can make the overall model perform better.
> - That could contrast with approaches that try to align the *whole* model, which may trade off performance ([[QUE - What are the tradeoffs between LLM alignment and performance?]]; e.g., https://arxiv.org/abs/2401.16332, https://arxiv.org/abs/2406.04879).
> - It may also contrast with using CoT as *explanations*, which can be post-hoc rationalizations, rather than as a prospective way to decompose the task and control it better.
