---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-6620-706b-a4c3-9517a53fbb6b
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/qAXZCpmXb
roamAuthor: "Joel Chan"
created: 2024-01-24
---

- Title: Graphologue: Exploring Large Language Model Responses with Interactive Diagrams
- Author(s):: Peiling Jiang, Jude Rayan, Steven P. Dow, Haijun Xia
- Abstract: Large language models (LLMs) have recently soared in popularity due to their ease of access and the unprecedented ability to synthesize text responses to diverse user questions. However, LLMs like ChatGPT present significant limitations in supporting complex information tasks due to the insufficient affordances of the text-based medium and linear conversational structure. Through a formative study with ten participants, we found that LLM interfaces often present long-winded responses, making it difficult for people to quickly comprehend and interact flexibly with various pieces of information, particularly during more complex tasks. We present Graphologue, an interactive system that converts text-based responses from LLMs into graphical diagrams to facilitate information-seeking and question-answering tasks. Graphologue employs novel prompting strategies and interface designs to extract entities and relationships from LLM responses and constructs node-link diagrams in real-time. Further, users can interact with the diagrams to flexibly adjust the graphical presentation and to submit context-specific prompts to obtain more information. Utilizing diagrams, Graphologue enables graphical, non-linear dialogues between humans and LLMs, facilitating information exploration, organization, and comprehension.
- Type: Preprint
- URL : http://arxiv.org/abs/2305.11473
- Date Added: October 12th, 2023
- Zotero links: [Local library](zotero://select/groups/2451508/items/Z4282NFR), [Web library](https://www.zotero.org/groups/2451508/items/Z4282NFR)
- Tags: Computer Science - Artificial Intelligence Computer Science - Computation and Language Computer Science - Human-Computer Interaction
- PDF links : [Jiang et al_2023_Graphologue.pdf](zotero://open-pdf/groups/2451508/items/8T4H4356)

## Discussion notes
Claude:
> Read in Week 3 of the SP-24 seminar (February 7th, 2024, "Interaction / agency"); also listed among the design-example readings (https://doi.org/10.1145/3586183.3606737). Notes below are from Joel Chan's lit-notes unless marked.
>
> **Key question**
> - At a high level the core question is similar to [[ART - ImageSense]] re: control: [[QUE - How to incorporate intelligent assistance into the ideation process, while leaving the human designer in control?]], which generalizes to [[QUE - How to incorporate intelligent assistance into human knowledge work, while leaving the human in control?]]. Here it is in the context of information-seeking tasks.
> - Core subproblems (mostly Section 2.1 and the formative study): linear chat is a suboptimal medium for people to **benefit** from intelligent assistance (unstructured info is hard to make sense of), and to **control** it. See the concept of [[PTN - Direct Manipulation]] (Hutchins, Hollan & Norman, 1985), though it was not referenced directly.
> ![[GeakXX1Nq2.png]] (p. 3)
>
> **Artifact and "secret sauce"**
> - [[ART - Graphologue]] creates an interaction medium that is easier to benefit from and control. Hypothesis: a dynamically created graph of responses is more effective for learning in an information-seeking task AND a more *controllable* interaction medium.
> ![[Y5B7QXCSI4.png]]
> - Technically enabled by [[PTN - prompt engineering]] + [[PTN - Large Language Models (LLMs)]]: converting text to annotated nodes and links (marked by salience, with unique local IDs), with error correction and saliency filtering. The prompt is "super long" and uses [[PTN - few-shot in-context learning]].
> ![[oTuu9BuaDj.png]] (p. 6)
> ![[wngBOgKDrB.png]]
> ![[a_Xzp1XzhD.png]] (pp. 17-18)
> - In this way it contributes to the literature on text-to-graphical representations, or more generally "flexible representational transformation", which may be a neat design pattern.
> ![[tlSQpiB0jq.png]] (p. 3)
> - UI controls include "tell me more" buttons for graph operations (expand, explain, give examples, etc.).
> ![[5bJ4puNRhL.png]] (p. 9)
> ![[wT7J2spoE6.png]] (p. 10)
>
> **Evidence**
> - Formative study: information in linear chat form was hard to make sense of, and (more interestingly) the chat medium was harder to control for information-seeking operations.
> ![[d3LXLYYWy1.png]] (p. 4)
> ![[eG1cusx0aV.png]] (p. 4)
> ![[_EPFJT-h0Q.png]]
> - Technical audit: F-score of ~.95 for annotating nodes and ~.85 for annotating edges from text with GPT-4, on responses to 50 simulated information-seeking queries.
> ![[QuzXkrkDDs.png]]
> - Qualitative user evaluation with 7 experienced ChatGPT users. The most interesting result was in 9.4.3, validating the hypothesis that the graph is a more natural medium for *controllable* intelligent assistance.
> ![[RUqvDqrrQU.png]]
> ![[yFnHdLRd8h.png]] (p. 13)
>
> **Critiques (flagged for 🚧 Safety Inspection Expert)**
> - No inter-rater reliability reported for the technical audit (p. 11).
> - Scope of applicability unclear: no clear listing of domains tested, and technical performance not audited in the user study (pp. 10, 12).
> ![[XAREAWN45A.png]] (p. 11)
> ![[6WkuBvYT-A.png]] (p. 10)
> ![[HZU86yMCcU.png]] (p. 12)
> - The user-study scenario ("use ChatGPT for 20 mins to help you prep for a lecture as a prof") is "kinda sus".
> ![[Yd_LgTxmxn.png]] (p. 12)
> - Unclear how to interpret the Fig. 9 Likert results; general positive vibes in 9.4.1, but not a ton of detail.
> ![[jax-CNhAmm.png]]
> ![[_joxd_HfnS.png]] (p. 13)
>
> **Contrast with domain-anchored work**
> - When S11 (🚧 Safety Inspection Expert, SP-24) flagged that a later paper's focus on supporting medical diagnosis "immediately triggers some flags", Joel Chan noted a notable contrast with Graphologue: that paper anchored in the domain from the beginning, with concrete details about differential diagnosis as the main task, and only toward the end of the intro suggested extension to other domains via the class of content-based image retrieval problems.
