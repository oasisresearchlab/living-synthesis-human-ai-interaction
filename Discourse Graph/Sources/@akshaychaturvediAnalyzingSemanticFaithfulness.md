---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-6620-75f5-8065-d5080526a73b
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/X_U5V8ieo
roamAuthor: "Joel Chan"
created: 2024-02-21
---

Claude:
> - Title: Analyzing Semantic Faithfulness of Language Models via Input Intervention on Conversational Question Answering
> - Author(s): Akshay Chaturvedi, Swarnadeep Bhar, Soumadeep Saha, U. Garain, Nicholas M. Asher
> - Zotero link: [Zotero Link](zotero://select/items/6_DLZTE5GJ)
> - Abstract: Transformer-based language models have been shown to be highly effective for several NLP tasks. In this paper, we consider three transformer models, BERT, RoBERTa, and XLNet, in both small and large version, and investigate how faithful their representations are with respect to the semantic content of texts. We formalize a notion of semantic faithfulness, in which the semantic content of a text should causally figure in a model’s inferences in question answering. We then test this notion by observing a model’s behavior on answering questions about a story after performing two novel semantic interventions—deletion intervention and negation intervention. While transformer models achieve high performance on standard question answering tasks, we show that they fail to be semantically faithful once we perform these interventions for a significant number of cases ( 50% for deletion intervention, and 20% drop in accuracy for negation intervention). We then propose an intervention-based training regime that can mitigate the undesirable effects for deletion intervention by a significant margin (from 50% to 6% ). We analyze the inner-workings of the models to better understand the effectiveness of intervention-based training for deletion intervention. But we show that this training does not attenuate other aspects of semantic unfaithfulness such as the models’ inability to deal with negation intervention or to capture the predicate-argument structure of texts. We also test InstructGPT, via prompting, for its ability to handle the two interventions and to capture predicate-argument structure. While InstructGPT models do achieve very high performance on predicate-argument structure task, they fail to respond adequately to our deletion and negation interventions.

## Discussion notes
Claude:
> - Came up in an SP-24 thread on how "absence of concept versus negative concept is interesting". Joel Chan noted that this reminded him of work he had collected on how (even large) transformer models struggle with negation, and shared this paper alongside [[@hosseiniUnderstandingUnderstandingNot2021]]. (Joel Chan, SP-24 seminar)
