---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-661f-72f3-bcac-a414a9c02aa5
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/CEAdBi8AU
roamAuthor: "Joel Chan"
created: 2024-02-21
---

- Title: Can Large Language Models Truly Understand Prompts? A Case Study with Negated Prompts
- Author(s): Joel Jang, Seonghyeon Ye, Minjoon Seo
- Year: 2022
- Zotero link: [Zotero Link](zotero://select/items/6_Q26GFPEB)
- URL: https://arxiv.org/abs/2209.12711
- Abstract: Previous work has shown that there exists a scaling law between the size of Language Models (LMs) and their zero-shot performance on different downstream NLP tasks. In this work, we show that this phenomenon does not hold when evaluating large LMs on tasks with negated prompts, but instead shows an inverse scaling law. We evaluate 9 different tasks with negated prompts on (1) pretrained LMs (OPT & GPT-3) of varying sizes (125M - 175B), (2) LMs further pretrained to generalize to novel prompts (InstructGPT), (3) LMs provided with few-shot examples, and (4) LMs fine-tuned specifically on negated prompts; all LM types perform worse on negated prompts as they scale and show a huge performance gap between the human performance when comparing the average score on both original and negated prompts. By highlighting a critical limitation of existing LMs and methods, we urge the community to develop new approaches of developing LMs that actually follow the given instructions. We provide the code and the datasets to explore negated prompts at this link.

## Discussion notes
Claude:
> - Came up in the SP-24 seminar thread "Absence of concept versus negative concept is interesting": Joel Chan pointed to it, alongside [[@truongNotAnotherNegation2022]], as part of work showing that even large transformer models struggle with negation. Its headline finding is an inverse scaling law: models perform worse on negated prompts as they get larger. (Joel Chan, SP-24 seminar)
