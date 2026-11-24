---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-6620-77a6-ab69-99ca25b93375
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/8FY5PHNdz
roamAuthor: "Joel Chan"
created: 2025-02-11
---

- Title: Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
- Author(s):: Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc V. Le, Denny Zhou
- Type: Conference paper
- Publication: 
- URL : https://proceedings.neurips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html
- Date Added: February 11th, 2025
- Zotero links: [Local library](zotero://select/groups/2451508/items/CSIUMTJV), [Web library](https://www.zotero.org/groups/2451508/items/CSIUMTJV)
- PDF links : [Wei et al_2022_Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.pdf](zotero://open-pdf/groups/2451508/items/WVVN2JNW)

## Discussion notes
Claude:
> **What it is and how it relates to chaining**
> - This is the canonical paper for [[PTN - Chain-of-Thought Prompting]]. It came up in the SP-25 session on [[@wuAIChainsTransparent2022]] (AI Chains): CoT shares the "divide and conquer" philosophy of chaining, but it is not sequential; it provides step-by-step reasoning in a single few-shot prompt. (S01, SP-25, 🕸️ Connector)
> - The CoT paper cites the AI Chains paper, and together they flesh out a family of related ideas, some stretching back quite a bit in time. (Joel Chan, SP-25 seminar)
> - ![[4_dgIJIppp.png]]
> - ![[9FwOZ4eq-x.png]]
>
> **Decomposition for performance, not only control**
> - The paper helps flesh out the idea that decomposition isn't just good for human control: it can make the model perform better. That contrasts with approaches that try to align the *whole* model, which may lead to performance tradeoffs (see [[QUE - What are the tradeoffs between LLM alignment and performance?]], e.g., https://arxiv.org/abs/2401.16332 and https://arxiv.org/abs/2406.04879). (Joel Chan, SP-25 seminar)
> - It may also contrast with using CoT as *explanations*, which can be post-hoc rationalizations, rather than as a prospective way to decompose the task and control it better. (Joel Chan, SP-25 seminar)
