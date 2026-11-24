---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-6620-7aa6-9385-fceb575e8c50
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/nXOJK6geM
roamAuthor: "Joel Chan"
created: 2024-02-21
---

- Title: Beyond Distributional Hypothesis: Let Language Models Learn Meaning-Text Correspondence
- Author(s): Myeongjun Jang, Frank Mtumbuka, Thomas Lukasiewicz
- Year: 2022
- Publication: Findings of the Association for Computational Linguistics: NAACL 2022
- Zotero link: [Zotero Link](zotero://select/items/6_B9GK8BDF)
- URL: http://dx.doi.org/10.18653/v1/2022.findings-naacl.156
- Abstract: The logical negation property (LNP), which implies generating different predictions for semantically opposite inputs ( p is true iff  p is false), is an important property that a trustworthy language model must satisfy. However, much re-cent evidence shows that large-size pre-trained language models (PLMs) do not satisfy this property. In this paper, we perform experiments using probing tasks to assess PLMs’ LNP understanding. Unlike previous studies that only examined negation expressions, we expand the boundary of the investigation to lexical semantics. Through experiments, we observe that PLMs violate the LNP frequently. To alleviate the issue, we propose a novel intermediate training task, named meaning-matching , designed to directly learn a meaning-text correspondence, instead of relying on the distributional hypothesis. Through multiple experiments, we find that the task enables PLMs to learn lexical semantic information. Also, through fine-tuning experiments on 7 GLUE tasks, we confirm that it is a safe intermediate task that guarantees a similar or better performance of downstream tasks. Finally, we observe that our proposed approach 1 outperforms our previous counterparts despite its time and resource efficiency.

## Discussion notes
Claude:
> Shared by Joel Chan in the SP-24 seminar in reply to a comment that "absence of concept versus negative concept is interesting". He noted that it reminded him of work he had collected on how even large transformer models struggle with negation. This paper is one example: pre-trained language models frequently violate the logical negation property.
