---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-6620-7c05-a2fc-fa0b746d8a85
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/5L_bsOLSk
roamAuthor: "Joel Chan"
created: 2025-01-23
---

- Title: ChainForge: A Visual Toolkit for Prompt Engineering and LLM Hypothesis Testing
- Author(s):: Ian Arawjo, Chelse Swoopes, Priyan Vaithilingam, Martin Wattenberg, Elena L. Glassman
- Abstract: Evaluating outputs of large language models (LLMs) is challenging, requiring making—and making sense of—many responses. Yet tools that go beyond basic prompting tend to require knowledge of programming APIs, focus on narrow domains, or are closed-source. We present ChainForge, an open-source visual toolkit for prompt engineering and on-demand hypothesis testing of text generation LLMs. ChainForge provides a graphical interface for comparison of responses across models and prompt variations. Our system was designed to support three tasks: model selection, prompt template design, and hypothesis testing (e.g., auditing). We released ChainForge early in its development and iterated on its design with academics and online users. Through in-lab and interview studies, we find that a range of people could use ChainForge to investigate hypotheses that matter to them, including in real-world settings. We identify three modes of prompt engineering and LLM hypothesis testing: opportunistic exploration, limited evaluation, and iterative refinement.
- Type: Conference paper
- Publication: 
- URL : https://dl.acm.org/doi/10.1145/3613904.3642016
- Date Added: January 23rd, 2025
- Zotero links: [Local library](zotero://select/groups/2451508/items/QGYYNWKI), [Web library](https://www.zotero.org/groups/2451508/items/QGYYNWKI)
- PDF links : [Arawjo et al_2024_ChainForge.pdf](zotero://open-pdf/groups/2451508/items/XHCEP933)

## Discussion notes
Claude:
> **The key question.** Discussed in Week 4 of the SP-25 seminar (February 19, 2025), framed by the 👩🏽‍🔬 Distiller as [[QUE - How can we enable people to intuitively bridge exploring and systematically testing hypotheses about LLMs when developing LLM-powered systems?]]
> - "LLM hypothesis testing" here does not mean using an LLM to test statistical hypotheses. It means making sense of the LLM itself; Section 3 is where this became concrete. (S05, SP-25)
> - The target audience is not the everyday person: the motivating scenario is a developer. (Joel Chan, SP-25)
> ![[f8-t2tGij-.png]]
> ![[bsoEJrdcBT.png]]

Claude:
> **What the system is and its "secret sauce."** [[ART - ChainForge]] is a visual programming interface and a direct extension of [[PTN - LLM Chains]]. Unlike the previous week's chaining paper, its nodes are steps of an *evaluation* workflow, not steps of an LLM task workflow. (Joel Chan, SP-25)
> ![[_2X4qvEqX7.png]]
> - A student first described it as direct manipulation that saves people from programming. Joel Chan pushed back: in [[ART - GAM Changer]] you directly manipulate how the model relates one variable to another by changing a shape function, whereas in ChainForge you aren't editing the thing itself, so it is better described as visual programming. Design concepts like [[PTN - Direct Manipulation]] lack formal definitions, so you compare against canonical examples.
> - Another student likened it to the validation step of ML model development: it makes it visually easier to vary models and prompt templates and see the effects all at once (cf. the paper's Table 1 of design goals).
> - The deeper secret sauce is comparison ([[CLM - to reason about LLM behavior, you need to be able to (visually) compare outputs side by side]]). Looking at outputs and prompt designs side by side lets you notice differences and generate hypotheses, which you can then formalize in an evaluator node (written as code or, in later designs, as an LLM-based evaluator) and test systematically. "If you jump straight to here, you don't know what to test... If you stay here, then you only have anecdotes." Joel Chan's own example: in the HumanEval coding-benchmark example flow, one prompt design preserved the docstring and the other dropped it, which suggests a hypothesis about anchoring on the original problem's intent. (Joel Chan, SP-25)
> - Why visual rather than a programming interface? It overlaps with notebook-style and other exploratory interfaces for sensemaking, and the authors cite differentiation and enrichment theories of learning: [[THE - Variation Theory]] and [[THE - Analogical Learning Theory]]. (Joel Chan, SP-25)
> ![[SCvMu1Aljg.png]]
> - "How do these theories come into the design of ChainForge?" (S01, 🚧 Safety Inspection Expert, SP-25). S11 noted that LLM applications connect naturally to Variation Theory because they can easily be sampled with different parameters (prompt perturbations, temperature, etc.): "you don't want to run it just once." (S11, 🕸️ Connector, SP-25)

Claude:
> **Modes of use.** The paper identifies three modes: opportunistic exploration, limited evaluation, and iterative refinement. Asked whether these were defined beforehand or derived from the data, Joel Chan read them as coming from the data, since they are presented as observed usage patterns, though the authors came in with a schema (people explore, then need to get to systematic testing). The modes map well onto models of sensemaking, exploration vs. exploitation, and opportunistic design, and resemble the exploration vs. acceleration modes found for Copilot in [[@barkeGroundedCopilotHow2023]]. (Joel Chan, SP-25)

Claude:
> **Evidence of efficacy and its limits.**
> - Meta-point on evaluation: [[CLM - controlled usabiltiy tests are not appropriate for evaluating HCI toolkit contributions]]. The authors used tasks as demo and training and put more analysis on free exploration.
> ![[AP5l_J0Crr.png]]
> - [[EVD - users --- including those with prior proramming experience --- infrequently transitioned to systematic testing with ART - ChainForge - @arawjoChainForgeVisualToolkit2024]]: the authors were surprised and disappointed by this; Joel Chan called it "an important negative result" that helps define the conditions under which the tool is useful.
> - [[EVD - data scientists successfully used ART - ChainForge to do systematic testing of their LLM pipelines - @arawjoChainForgeVisualToolkit2024]], flagged by Joel Chan as a key insight for synthesis. The real-world interview study was later held up as a gold standard of authentic usage with credible users, and the case studies in the appendix give context for how people actually used it.
> - [[EVD - phd student reading ChainForge paper found it difficult to formalize intuitive sense on different dimensions when comparing into metrics that can be studied systematically]]
> - Synthesis (tentative): scientific literacy may be necessary to benefit from tools like ChainForge. Translating a construct into an operationalization is a fundamental meta-skill of scientific thinking that the tool does not support. Without it you never get to systematic testing, and "even if you make charts, they don't mean anything." Data scientists in the real-world study have this skill because it is their job. (Joel Chan, SP-25) This led to [[QUE - how do we enable people with less scientific literacy to benefit from systematic tools like ART - ChainForge?]] and connects to [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]]
> - Related claims from discussion: [[CLM - experience as a creator (vs. producer) is an important precursor for being able to understand tools like LLMs]] and [[CLM - tools like ART - ChainForge can impact users of LLMs by empowering developers to design better LLM-powered systems]]
> - Joel Chan drew a parallel to GAM Changer: he would be cautious about deploying it apart from a team of engineers and domain experts, since direct model edits need both statistical and domain knowledge (cf. [[CLM - ART - GAM Changer or PTN - Direct Manipulation-based approaches to steering models are best used in collaborative teams with domain experts - end users and ML engineers]]). Open-ended evaluations with people outside the authors' circle are what surface such preconditions; a clean controlled lab study would not.

Claude:
> **Open questions and critiques.**
> - One case study switched between English and Indonesian prompts. A student asked how to handle language bias from models trained mostly on English, e.g., for language learners. Joel Chan noted that you can vary prompts in ChainForge but can't really test hypotheses about the training data, and pointed to NLP work on low-resource languages. (SP-25)
> - S11 asked, more broadly, how to use and quantify the variation in GenAI outputs to help human-AI teams with overreliance, learning, or decision correctness. They pointed to RELIC (verifying correctness via contradicting vs. supporting evidence in atomic claims: https://www.semanticscholar.org/paper/RELIC%3A-Investigating-Large-Language-Model-Responses-Cheng-Zouhar/edbfa8e27cf1065a30e6386a7a6313607503ea7e) and "One vs. Many" (https://dl.acm.org/doi/pdf/10.1145/3630106.3662681) as an overreliance mitigation technique. (S11, 🕸️ Connector, SP-25)

Claude:
> **Connections.**
> - [[@zamfirescu-pereiraWhyJohnnyCant2023]] is frequently cited, and its results echo the lack of bridging to systematic testing. (🕸️ Connector, SP-25)
> ![[mSiK3FEbNQ.png]]
> ![[lReili6dYj.png]]
> - On [[PTN - Direct Manipulation]] tradeoffs for novices: the 1990s debate between Ben Shneiderman and Pattie Maes on direct manipulation vs. interface agents ([[@shneidermanDirectManipulationVs1997]]). Maes argued that growing complexity and non-computer-trained users will require delegating some tasks to agents, as a complement to visualization and direct manipulation, not a replacement, with users able to understand and bypass the agent. Also [[@maayanHowDomainExperts2020]]: experts making conceptual diagrams use neither direct manipulation nor programming exclusively; DM offers faster feedback and global control, programming offers abstraction and local control. (Joel Chan, SP-25)
> ![[p443b9ZFR7.png]]

Claude:
> **Resources.** Try it at https://www.chainforge.ai/. S09 found a talk video showing it in use, including what it is and isn't for: https://www.youtube.com/watch?v=Slb3unllD74. Joel Chan recommended looking up conference talk recordings for papers, since they are often clearer than the paper or the pre-recorded ACM video. (SP-25)
