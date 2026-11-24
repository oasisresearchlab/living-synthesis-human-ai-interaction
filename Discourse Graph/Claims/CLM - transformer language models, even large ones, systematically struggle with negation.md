---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e91-8a5c-7e0d-9f00-37bf589788a3
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-24 W05 Explainability]]"
created: 2026-11-24
---
## Grounds
Claude:
> Joel Chan raised this in reply to S11's point that "absence of concept versus negative concept is interesting", noting work he'd collected "on how (even large) transformer models struggle with negation". (Joel Chan, SP-24 W05) The papers' abstracts:
> - [[EVD - pretrained language models did not distinguish negated from non-negated cloze probes - @kassnerNegatedMisprimedProbes2020]] ([[@kassnerNegatedMisprimedProbes2020]])
> - [[EVD - language models from 125M to 175B parameters performed worse on negated prompts as they scaled - @jangCanLargeLanguage2022]] ([[@jangCanLargeLanguage2022]])
> - [[EVD - NLU corpora had few and often unimportant negations, and transformers trained on them did much worse when negation mattered - @hossainAnalysisNegationNatural2022]] ([[@hossainAnalysisNegationNatural2022]])
> - [[EVD - humans used negatively answered questions in GuessWhat dialogues while language-model guessers struggled to ground negation - @testoniArtificialIntelligenceModels2022]] ([[@testoniArtificialIntelligenceModels2022]])
> - BERT "shows clear insensitivity to the contextual impacts of negation" ([[@ettingerWhatBERTNot2020]]).
> - Multimodal transformers with standard fine-tuning failed to interpret negation regardless of size ([[@judithyueliMAQAMultimodalQA]]).
> - PLMs often violate the logical negation property ([[@jangDistributionalHypothesisLet2022]]); state-of-the-art PLMs often handle negation incorrectly ([[@hosseiniUnderstandingUnderstandingNot2021]]); InstructGPT failed to respond adequately to negation interventions ([[@akshaychaturvediAnalyzingSemanticFaithfulness]]).

## Other Notes
Claude:
> - Several of these papers report partial fixes (unlikelihood training, negated-example augmentation, meaning-matching), so the claim is about default pretrained behavior, not an impossibility.
> - Most evidence is from 2018-2022 models; whether it holds for current frontier LLMs is open.

## Suggested relations
Claude:
> - informs → [[QUE - How should concept-based steering interfaces distinguish the absence of a concept from its negation?]]: if models struggle with negation, "negative concept" controls may not do what users expect (Joel Chan, SP-24 W05)
