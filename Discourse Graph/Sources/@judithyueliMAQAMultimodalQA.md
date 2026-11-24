---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-661f-712f-bcec-905daeaaf544
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/tIv_yJiu7
roamAuthor: "Joel Chan"
created: 2024-02-21
---

- Title: MAQA: A Multimodal QA Benchmark for Negation
- Author(s): Judith Yue Li
- Zotero link: [Zotero Link](zotero://select/items/6_G2B6VB8L)
- Abstract: Multimodal learning can benefit from the representation power of pretrained Large Language Models (LLMs). However, state-of-the-art transformer based LLMs often ignore negations in natural language and there is no existing benchmark to quantitatively evaluate whether multimodal transformers inherit this weakness. In this study, we present a new multimodal question answering (QA) benchmark adapted from labeled music videos in AudioSet (Gemmeke et al., 2017) with the goal of systematically evaluating if multimodal transformers can perform complex reasoning to recognize new concepts as negation of previously learned concepts. We show that with standard fine-tuning approach multimodal transformers are still incapable of correctly interpreting negation irrespective of model size. However, our experiments demonstrate that augmenting the original training task distributions with negated QA examples allow the model to reliably reason with negation. To do this, we describe a novel data generation procedure that prompts the 540B-parameter PaLM model to automatically generate negated QA examples as compositions of easily accessible video tags. The generated examples contain more natural linguistic patterns and the gains compared to template-based task augmentation approach are significant.

## Discussion notes
Claude:
> Shared by Joel Chan in the SP-24 seminar in reply to a comment that "absence of concept versus negative concept is interesting". He noted that it reminded him of work he had collected on how even large transformer models struggle with negation. This paper is one example: multimodal transformers fail to interpret negation regardless of model size, unless training is augmented with negated examples. See also [[@jangDistributionalHypothesisLet2022]], shared in the same reply.
