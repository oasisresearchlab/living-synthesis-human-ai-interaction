---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-6620-7e24-90f4-e2dea22ff1ba
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/bnybOHn2H
roamAuthor: "Joel Chan"
created: 2025-01-23
---

- Title: Patchview: LLM-powered Worldbuilding with Generative Dust and Magnet Visualization
- Author(s): John Joon Young Chung, Max Kreminski
- Type: Conference paper
- Publication: Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology, 1–19
- URL: https://dl.acm.org/doi/10.1145/3654777.3676352
- Date Added: January 23rd, 2025
- Zotero links: [Local library](zotero://select/groups/2451508/items/RZVSQ8AT), [Web library](https://www.zotero.org/groups/2451508/items/RZVSQ8AT)
- PDF links: [Chung_Kreminski_2024_Patchview.pdf](zotero://open-pdf/groups/2451508/items/UC2JAIMS)

## Discussion notes
Claude:
> **Problem.** Read in Week 11 of SP-25 (April 9th, 2025). How can we enable users to steer LLM generations to align with verbally elusive or ambiguous concepts, especially when sensemaking during worldbuilding? (cf. [[THE - Sensemaking Theory]]) (Joel Chan, notes)
> ![[9W6DuG9c_a.png]] (p. 2)
> ![[Fz0rm_hyl4.png]] (p. 2)
> - The paper generalizes a bit beyond worldbuilding (section 3.1): worldbuilding is a *complex* creative task, making something very large and complex, with proximal issues of sensemaking, steering, and verbally elusive intent.
> ![[LsFn-LIvdn.png]]
> - A subtle difference from [[ART - DreamSheets]] and [[ART - ChainForge]]: the target of sensemaking is the (generated) world, not necessarily the model. (Joel Chan, notes)
> - S05 found section 3.1's "criteria" for which users and behaviors suit the tool helpful for sensemaking, though they personally had a hard time relating to worldbuilding as a use case. (S05, 🚧 Safety Inspection Expert role, SP-25)
> - Other scenarios raised in discussion: communication barriers for intent (e.g., English language learners might need non-verbal modalities); oral histories, where natural language may fail because an LLM might misinterpret content underrepresented in training data; making sense of your own life experience ("WORLDBUILDING YOUR LIFE"); and narrative qualitative data analysis as "worldbuilding", in contrast to [[ART - LLOOM]] (https://stanfordhci.github.io/lloom/), which better fits "taxonomizing" paradigms. (SP-25 seminar)
> ![[3huL0Q90Bw.png]]

Claude:
> **System and patterns.** (Joel Chan, notes)
> - The core pattern is [[PTN - Generative Dust and Magnet Visualization]].
> ![[8d0mwINZWp.png]]
> - It supports key interactions, framed by the gulfs of evaluation and execution: i1, evaluation support (make sense of AI outputs according to user-defined concepts); i2, specification alignment (steer generation of specific elements); i3, process alignment (steer the underlying model).
> ![[aVlNIlLIwd.png]]
> ![[phMsuJfrfh.png]]
> ![[gipf-sh7_N.png]]
> - Instantiated in the [[ART - Patchview]] prototype for worldbuilding. Each view is a single instance of the visualization, and maxes out at 3 concepts per view ("for ... geometric reasons?").
> ![[RiUs-xo6Pq.png]]
> ![[SdOrfBaV1B.png]]
> ![[i8iMHt9QyY.png]]
> - Users can link and anchor across views, and construct higher-order structures that combine views, like a 2D plane visualization or parallel coordinates. "Neat to see a step towards addressing [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]]!"
> ![[b7q_dEFJfs.png]]
> ![[I_vNppX_Ny.png]]
> - [[PTN - Direct Manipulation]] was flagged as a key pattern in discussion. S01 noted that visualizations can suffer from optical illusions (ambiguity, distortion, etc.), and that Patchview counters this by letting users "adjust the layout of concepts (Figure 4d), aligning their visual presentation with how they want to think about these concepts and elements", i.e., adjustable magnet locations. (S01, 🚧 Safety Inspection Expert role, SP-25)
> - Related work: S16 pointed to Kim, Lee, Chang, and Kim (2023), "Cells, Generators, and Lenses: Design Framework for Object-Oriented Interaction with Large Language Models" (UIST '23, https://doi.org/10.1145/3586183.3606833), cited alongside ChainForge as also using visualization nodes for steering model behavior. It is a "design framework that conceptualizes the components of generation configurations as interactive objects". Its relationships between inputs are more concrete than Patchview's, like object-oriented programming, which means less flexibility for control. (S16, 🏺 Archaeologist role, SP-25)
> ![[UxChwmNI3R.png]]
> - For the gulfs of evaluation and execution, S01 shared https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/ (🤔 ELI5 linter role), and a paper presentation with demo: https://www.youtube.com/watch?v=6Uk1NnLRSxw (👾 Hacker role). (S01, SP-25)
> ![[JLk2b8Xsfg.png]]

Claude:
> **Study and evidence.** (Joel Chan, notes)
> - Methods: participants answered sensemaking questions with the tool vs. a baseline, then tried the system to generate and steer worldbuilding while thinking aloud. Measures: speed and correctness on sensemaking questions of two kinds, landscape (distribution over concepts) and comparison (more/less for concept A vs. B); logs, think-aloud, and recordings; recognition errors; and steering errors.
> ![[aV2fksnWBZ.png]]
> ![[qwYrozcffN.png]]
> ![[ahik1DgqS3.png]]
> ![[k9k7UrDqf3.png]]
> ![[hCBgmTM-GC.png]]
> ![[NqQwMi0KZk.png]]
> - Participants were faster and more correct on landscape sensemaking questions with Patchview vs. the baseline.
> ![[wHZhko6ZgK.png]]
> - No difference in speed or correctness for comparison questions ("kudos for null result!").
> - Qualitative feedback: steering with the visualization felt intuitive, possibly more natural than natural-language prompting.
> ![[Om0lG7W-fU.png]]
> ![[b7zvnr4wHN.png]]
> - Recognition error went down with more usage (examples). Steering error showed no real change with more examples ("maybeeee slight increasing trend??").
> ![[Tdi6Jjs8gp.png]]
> - Participants created interesting views and structures.
> ![[7zSvFJk_lX.png]]
> ![[6vuwsZju2X.png]]
> ![[7IymKNWJnw.png]]
> ![[1X50mmsUI9.png]]

Claude:
> **Limitations and open questions.** (SP-25 seminar)
> - It doesn't handle time very well, and participants wanted it to.
> ![[IN-WTsyvRj.png]]
> - We wished we knew how it would work over a longer time period.
