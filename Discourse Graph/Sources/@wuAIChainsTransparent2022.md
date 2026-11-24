---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-6620-7327-8d25-4fc9ba2874fb
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/-UME0_lWI
roamAuthor: "Joel Chan"
created: 2025-01-23
---

- Title: AI Chains: Transparent and Controllable Human-AI Interaction by Chaining Large Language Model Prompts
- Author(s):: Tongshuang Wu, Michael Terry, Carrie Jun Cai
- Abstract: Although large language models (LLMs) have demonstrated impressive potential on simple tasks, their breadth of scope, lack of transparency, and insufficient controllability can make them less effective when assisting humans on more complex tasks. In response, we introduce the concept of Chaining LLM steps together, where the output of one step becomes the input for the next, thus aggregating the gains per step. We first define a set of LLM primitive operations useful for Chain construction, then present an interactive system where users can modify these Chains, along with their intermediate results, in a modular way. In a 20-person user study, we found that Chaining not only improved the quality of task outcomes, but also significantly enhanced system transparency, controllability, and sense of collaboration. Additionally, we saw that users developed new ways of interacting with LLMs through Chains: they leveraged sub-tasks to calibrate model expectations, compared and contrasted alternative strategies by observing parallel downstream effects, and debugged unexpected model outputs by “unit-testing” sub-components of a Chain. In two case studies, we further explore how LLM Chains may be used in future applications.
- Type: Conference paper
- Publication: 
- URL : https://dl.acm.org/doi/10.1145/3491102.3517582
- Date Added: January 23rd, 2025
- Zotero links: [Local library](zotero://select/groups/2451508/items/X5CG7PLX), [Web library](https://www.zotero.org/groups/2451508/items/X5CG7PLX)
- PDF links : [Wu et al_2022_AI Chains.pdf](zotero://open-pdf/groups/2451508/items/HMNISAH2)

## Discussion notes
Claude:
> Discussed in Week 3 of the SP-25 seminar (February 12th, 2025).
>
> **Key question / problem**
> - Key question: [[QUE - How can we optimize LLM performance on complex, real-world tasks?]], with the sub-question of most interest to the seminar: [[QUE - How can we help users accomplish complex tasks with LLMs in a way that is more transparent and debuggable?]] The authors don't like mining prompts and [[PTN - prompt engineering]] in general, because they are less transparent and controllable. (SP-25 seminar, Distiller notes)
> - ![[Jaa1CCAbNt.png]]
> - The paper reviews challenges of LLMs with complex tasks circa 2021; the seminar wondered how many still hold today ([[QUE - To what extent do modern reasoning LLMs still struggle with complex tasks?]]). Today you can stuff a lot of information and examples into the context window, or even fine-tune, and [[PTN - Chain-of-Thought Prompting]] is part of most models. (SP-25 seminar, Distiller notes)
> - ![[1gc5y7kbrT.png]]
> - Brainstormed complex tasks where this matters: enhancing critical thinking; tutoring (e.g., Rose Wang's work on embedding expert-like thinking in models, such as Bridge, https://aclanthology.org/2024.naacl-long.120.pdf, and Tutor CoPilot, https://arxiv.org/pdf/2410.03017, where lower-rated and less experienced tutors benefited most); complex, nonlinear, iterative sensemaking; and translation that accounts for cultural nuance, where chains might help people evaluate translation outputs by articulating the key aspects of the task. (SP-25 seminar, Distiller notes)
>
> **The artifact and its "secret sauce"**
> - [[PTN - LLM Chains]]: **decompose** a large complex task into smaller, well-scoped subtasks that each map to one of 8 curated LLM primitive operations, and provide a way to **chain** these subtasks together. Each chain step is basically an LLM call with a prompt design, with slots that take outputs from a previous step as input. (SP-25 seminar, Distiller notes)
> - The 8 primitive operations were mined from 73 online demos of LLMs. The approach is inspired by [[PTN - crowdsourcing pipelines]].
> - ![[x_dHv3BwcZ.png]]
> - ![[PlF6DsnFyk.png]]
> - ![[5Bpq7CEy1C.png]]
> - ![[DhIKnKa8RR.png]]
> - ![[mpkwHijZps.png]]
> - ![[z73I6yeDPY.png]]
> - ![[2h3OM8vaB4.png]]
> - The interface gives a visual representation of chains, with local and global control: direct editing of each step's prompts and outputs, plus connections between steps at a global level via [[PTN - Visual Programming]].
> - ![[NxSYURAfl9.png]]
> - ![[W6P6txCsD1.png]]
> - ![[VOGBnfknpA.png]]
> - The paper also includes case studies in debugging visualization code and assisted text entry.
> - ![[mGB5EdEuSG.png]]
>
> **Evidence of efficacy**
> - Methods: a within-subjects user study comparing Chaining with "Sandbox", "an interface that looks aesthetically similar to the Chaining interface, but without the Chaining functionality," based on the GPT-3 playground (Wu et al., 2022, p. 8; quoted by S09, SP-25). The Sandbox was basically equivalent to [[ART - GPT-3 Playground]] and came with default prompts. The model was [[ART - LaMDA]], roughly equivalent in size to [[ART - GPT-3]].
> - 20 participants at a large software company, about half without prompting experience. Two tasks: peer review writing and personalized flashcard creation. A 30-minute tutorial, then counterbalanced trials of up to 25 minutes each in each condition. Two non-participants made pairwise choices between Sandbox and Chain outputs.
> - ![[6_uuGQkAH2.png]]
> - ![[mUV8pOHVYW.png]]
> - ![[BVAECileJy.png]]
> - ![[qHakfmBGBY.png]]
> - ![[GmHky7VGjy.png]]
> - ![[YwKyckx0Qj.png]]
> - User survey results:
>   - [[EVD - higher overall subjective ratings of quality of output with chains vs. sandbox - @wuAIChainsTransparent2022]]
>   - [[EVD - higher rates of preferring chain outputs vs. sandbox outputs by two independent raters - @wuAIChainsTransparent2022]]
>   - [[EVD - higher subjective ratings of transparency for chains vs. sandbox - @wuAIChainsTransparent2022]]
>   - [[EVD - higher subjective ratings of controllability for chains vs. sandbox - @wuAIChainsTransparent2022]]
>   - [[EVD - higher subjective perception of helping them think through the task for chains vs. sandbox - @wuAIChainsTransparent2022]]
> - ![[w3tqXAOr3X.png]]
> - ![[gbkTL4kFbZ.png]]
> - Qualitative log analysis:
>   - [[EVD - more manual edits between runs with chains vs. sandbox - @wuAIChainsTransparent2022]]
>   - [[EVD - more curation or model outputs vs. deleting or creating new content entirely - @wuAIChainsTransparent2022]]
>   - [[EVD - some difficulty reasoning about the big picture and how it changes when zooming in on steps - @wuAIChainsTransparent2022]]
> - ![[vks7Gn0_hN.png]]
> - ![[4A4Fr2BW4n.png]]
>
> **Critiques and unmet needs**
> - How is the default chain structure generated? With 8 primitives there are many possible combinations even for a 2-step chain, and matching a default to a complex natural-language request is hard. Could an LLM pre-generate a default chain from the user's overall request? (S01, SP-25, 🚧 Safety Inspection Expert)
> - Two valid but unmet user needs: seeing how a tweak to an intermediate step affects the final output (mentioned in the paper), and rolling back to a previous output after regenerating, e.g., via a log of historical outputs. (S01, SP-25, 🚧 Safety Inspection Expert) Joel Chan tied this to higher-order effects of controlling models ([[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]]) and to the "cascading errors" challenge raised in the paper's related work.
> - ![[fWw9OqTqOF.png]]
> - The claimed controllability depends on users' ability to divide problems efficiently, and some questions may be too simple for subtasks: [[QUE - how do you balance foolproof automation and freedom of controllability?]] (S01, SP-25)
> - The participants were all technical or tech-adjacent. What scaffolds would broader populations (minors, the elderly, low-income users) need, and should we simplify tools or raise people's knowledge to meet them? (S14, SP-25)
> - The authors could do more with the lexical and extra-linguistic interpretation of words: e.g., "needs more bullet points" may not be specific enough without a number or range. Coarse-grained chaining could be followed by finer-grained responses, and the UI could let users highlight and interact with a response. (S15, SP-25, 🍜 Academic Researcher)
>
> **Connections**
> - Older work: the "Workflows in Crowdsourcing" related-work section seemed random to S11; ideas from software engineering (parallelization, modularization) might apply more directly, as in Tongshuang Wu's earlier CheckList work on behavioral testing of NLP models (https://arxiv.org/abs/2005.04118). (S11, SP-25, 🏺 Archaeologist)
> - Newer work: [[@weiChainofThoughtPromptingElicits2022]] ([[PTN - Chain-of-Thought Prompting]]) shares the "divide and conquer" philosophy but is not sequential: it gives step-by-step reasoning in a single few-shot prompt. (S01, SP-25, 🕸️ Connector) The CoT paper cites this one, and together they show that decomposition isn't just good for human control; it can make the model perform better. That contrasts with aligning the *whole* model, which may trade off performance ([[QUE - What are the tradeoffs between LLM alignment and performance?]]), and with using CoT as explanations, which can be post-hoc rationalizations. (Joel Chan, SP-25 seminar)
> - ![[4_dgIJIppp.png]]
> - ![[9FwOZ4eq-x.png]]
> - Newer work: "Post Hoc Explanations of Language Models Can Improve Language Models" (https://dl.acm.org/doi/10.5555/3666122.3668979). [[PTN - Post-hoc explanations of language models]] improve accuracy and complement CoT by automatically generating rationales from attribution scores, in line with this paper's intuition of simplifying problems into subproblems the model can digest. (S11, SP-25, 🏺 Archaeologist)
> - ![[VxKQZp377w.png]]
> - Decomposition and human-human collaboration: [[CLM - the underlying idea of decomposition of complex task into smaller steps can be an interesting angle to facilitate human-human collaboration (or human-agent collaboration?)]]. In a related study of multilingual co-writing (shared in the seminar), treating "writing" as one task made low-proficiency participants seem to contribute almost nothing; dissecting it into subcomponents (e.g., ideation vs. wording) showed they contributed to ideation when given a "protected" space. Joel Chan noted this recalls [[PTN - Articulation Work]]. (S05, SP-25, 🍜 Academic Researcher)
> - This raised [[QUE - Can LLM chaining be a tool-model-reference for human collaborators to consider the underlying components of a complex task and better coordinate among people (e.g., considering everyone's expert]] (e.g., an ethnographic study of teams using a chaining tool, or an experiment on team planning with vs. without one) and the authors' own future-work question, [[QUE - how can end user effectively author their own LLM chains?]] (S05, SP-25)
> - Resources: a talk video, https://www.youtube.com/watch?v=brCo42DoMu0 (shared by S01 and S09, SP-25).
> - The ChainForge paper ([[@arawjoChainForgeVisualToolkit2024]]) was moved up to the following week because it is similar. In a later SP-25 session, Joel Chan noted a missed opportunity in another paper to reflect on its relation to [[ART - ChainForge]] and [[PTN - LLM Chains]]: it cites this paper only in passing in related work.
