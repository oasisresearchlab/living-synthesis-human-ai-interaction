---
nodeTypeId: node_Gp7JMdrzm9DUuPfBzUptc
nodeInstanceId: 01a20e70-661c-71b7-9003-42986289bd73
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/Hr3XeF_W9
roamAuthor: "Joel Chan"
created: 2025-01-23
---

## Context
Claude:
> The focal question of the SP-25 seminar. Joel Chan chose to focus on "**concrete example systems** that emphasize **interaction as a core component of the 'secret sauce'** that are paired with some **human-centered evaluation**," to work toward a synthesis for this question. It is a focused sub-question of [[QUE - How might we design AI-infused systems that augment — rather than replace — human intelligence and work?]]
>
> The seminar returned to it in two synthesis discussions: Week 9 (March 26th, 2025), reflecting on the first six weeks of readings, and Week 15 (May 7th, 2025).

## Other Notes
Claude:
> **Week 9 synthesis: Group 1.**
> - *Responsible edits and needed knowledge*: [[ART - GAM Changer]]'s commit logs enable reverting and auditing by people with relevant knowledge.
> - *Actionable explainability*: is explainability just transparency, or can people take actions to adjust and shape model behavior? (S01, connecting S05's types of resources with S04's emphasis on intuitive interaction.)
> - *Open questions*: how reliable are these interactions when they rely on LLMs to make judgments (requiring a human in the loop)? What "governance" structure is needed for human involvement, e.g., an auditor or moderator to track and revert user-initiated commits?

Claude:
> **Resources for agency (S05).** S05 framed agency (drawing on Bandura's social cognitive theory) as people's ability to influence AI outputs toward desired outcomes, and asked [[QUE - What types of resources are these interaction designs offering to users to sustain agency? How effective are these resources, and why the selection of these resources in a given context?]]
> - **Technical resources**: [[ART - GAM Changer]] via [[PTN - Shared Representation]] and [[PTN - Direct Manipulation]]. Open question: is non-experts' use of such resources reasonable, and should access be limited?
> - **Cognitive resources**: [[PTN - LLM Chains]], [[ART - ChainForge]], ConstitutionMaker, and [[ART - AI Policy Projector]] help people examine LLM behavior across changing prompt parameters and formulate rules or principles.
> - **Task resources**: tools like GAM Changer and LLM chains may also support how people plan tasks and collaborate around AI use. S05 focuses on these most: [[CLM - human-AI interaction designs can maximize human-agency by providing -task resources- to elaborate and improve their task model]]
> - Open questions: do these distinctions make sense; how to track the effectiveness of these resources beyond user studies; what other resources exist?

Claude:
> **Exploring the solution space (S01).**
> - For open-ended or creative tasks, users want to know what they can do and to sense the landscape of the "solution space." [[ART - DreamSheets]] and [[ART - AI Policy Projector]] visualize the mapping between inputs and that space. Related: [[CLM - to reason about LLM behavior, you need to be able to (visually) compare outputs side by side]], [[EVD - expert visual artists actually used ART - DreamSheets to independently construct a diverse range of powerful, reusable computational exploration structures that could be use make sense of useful]], and the AI Policy Projector claim that its "map visualization provides a holistic overview of the concepts and policies, which supports users in surveying the terrain of possible model behaviors and iterating on policy designs."
> ![[fQAvl0A9ex.png]]
> ![[0E7K4Wt1yp.png]]
> - Challenges: 2D or 3D visualizations of high-dimensional things like language embeddings are limited ([[CLM - UMAP 2D projections do not produce meaningful global spatial separation]]); and non-deterministic mappings make it hard to reproduce outputs users liked.
> - [[PTN - Actionable explainability]] with [[PTN - Direct Manipulation]]: explanations can also be signals for users to steer the model. But if users can customize models, responsible and accountable change must be supported. Quoting [[@wangInterpretabilityThenWhat2022]]: continuous feedback and reversible edits "do not guarantee to prevent users from overfitting the model, injecting harmful bias, or maliciously manipulating model predictions." S01 suggested monitoring for harmful edits, e.g., an LLM judge with a constitution.

Claude:
> **Other Week 9 perspectives.**
> - S04: DreamSheets felt like an intuitive "sandbox" for co-creating art with AI without coding. Can this kind of intuitive interaction carry over to games, music, or writing? S04 pointed to a UIST 2024 paper on runtime behavior generation in games ("What's the Game, then? Opportunities and Challenges for Runtime Behavior Generation," https://dl.acm.org/doi/10.1145/3654777.3676358).
> ![[DkiEtfzfrO.png]]
> - S09: DreamSheets could serve design fields such as game design and UX/UI, e.g., exploring prompts for a character or interface design.
> - Group 3: start from users, their needs, and how they currently use technology, and only then build an AI tool; the papers tend to build a tool and then find people to test it, "over generalize" on usability, and leave scalability open.
> - S14: who is missing from these studies? Research teams should offer positionality statements, and participatory design should attend more to power dynamics. Non-technical perspectives are lacking, which limits transferability. Questions: does customization lead to individualization? What prior knowledge do users need, and can non-technical users acquire it? How can AI literacy frameworks address gaps in knowledge, privilege, and access between research teams, their often homogeneous participants, and the general population?
> - S12: worries about training data (diversity, bias, sampling, misinformation, misrepresentation of cultures and languages) are only partly allayed by tools that give end users leverage over outputs (prompt engineering tools, ConstitutionMaker, DreamSheets). Still, giving users leverage is "a good first step" toward trustworthy AI, making it seem "less like an omniscient, omnipotent, intelligent being and more like a slightly complicated piece of code."
> - S16: these papers presuppose that an LLM or ML model is already the chosen tool (e.g., Policy Projector, AI Chains, ChainForge, ConstitutionMaker). For many domains, the design space should start from a non-AI boundary object for the task, and ask how to frame problems *before* deciding to infuse AI.
> - S15: these are early attempts to bring a user-centered approach to foundation models, requiring deep interdisciplinary HCI skill and still far from tools for a wide range of users. Visual interactions tend to have lower cognitive load than text; voice prompts that an LLM turns into more precise prompts might lower it further, and visual reasoning transparency can aid understanding.

Claude:
> **Week 15 synthesis: what have we learned?**
> - A useful meta-strategy: scope the big question of human-centered AI down to concepts and ideas for specific subcomponents, like sensemaking, editing models, and evaluating models. These can then connect to other theories, disciplines, and artifacts.
> - Things we now know are possible: use a spreadsheet; compile feedback into rules; make a map; make a "GUI" for a chain; make sliders and controls.
> - What next: more things we are confident work for "the rest of us" (people without a technical or programming background, not used to thinking like a scientist; cf. [[QUE - how do we enable people with less scientific literacy to benefit from systematic tools like ART - ChainForge?]]), tested with and designed with or led by such people.
> - More thinking about how components compose into larger workflows "in the wild," e.g., [[EVD - expert visual artists actually used ART - DreamSheets to independently construct a diverse range of powerful, reusable computational exploration structures that could be use make sense of useful]], [[EVD - data scientists successfully used ART - ChainForge to do systematic testing of their LLM pipelines - @arawjoChainForgeVisualToolkit2024]], and [[EVD - it was possible for a two physicians to use ART - GAM Changer to edit a GAM model for sepsis risk prediction to account for possible issues with temperature, respiratory rate, and systolic blood]].
