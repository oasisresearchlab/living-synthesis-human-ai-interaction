---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e70-661f-7341-9c4c-339654abbd8c
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/26rCzNuL7
roamAuthor: "Joel Chan"
created: 2024-03-06
---

## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Key source: [[@ehsanAutomatedRationaleGeneration2019]] (S08, 👩🏽‍🔬 Distiller, SP-24). Definition: "a process of producing a natural language explanation for agent behavior as if a human had performed the behavior and verbalized their inner monologue."
> - From the paper: an approach for real-time explanation generation in which a computational model learns to translate an autonomous agent's internal state and action representations into natural language. Training on human explanation data can let agents generate human-like explanations of their behavior. The rationales were produced with neural machine translation (NMT).

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - An agent that plays Frogger ([[@ehsanAutomatedRationaleGeneration2019]]): the authors collected a corpus of explanations, trained a neural rationale generator to produce different styles of rationales, and studied how people perceive them. Users perceived the intended differences between rationale styles, and, context permitting, preferred detailed rationales to form a stable mental model of the agent's behavior.

## Other Notes

Claude:
> - Automated Rationale Generation is an instance of [[PTN - post-hoc interpretability]]; cf. [[@liptonMythosModelInterpretability2017]] (Joel Chan, 🕸️ Connector, SP-24).
