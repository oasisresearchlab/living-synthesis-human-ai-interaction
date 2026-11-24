---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-661f-78f7-a06f-2be19b089ba8
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/vjYCRDhI6
roamAuthor: "Joel Chan"
created: 2024-01-24
---

- Title: Agency plus automation: Designing artificial intelligence into interactive systems
- Author(s): Jeffrey Heer
- Abstract: Much contemporary rhetoric regards the prospects and pitfalls of using artificial intelligence techniques to automate an increasing range of tasks, especially those once considered the purview of people alone. These accounts are often wildly optimistic, understating outstanding challenges while turning a blind eye to the human labor that undergirds and sustains ostensibly “automated” services. This long-standing focus on purely automated methods unnecessarily cedes a promising design space: one in which computational assistance augments and enriches, rather than replaces, people’s intellectual work. This tension between human agency and machine automation poses vital challenges for design and engineering. In this work, we consider the design of systems that enable rich, adaptive interaction between people and algorithms. We seek to balance the often-complementary strengths and weaknesses of each, while promoting human control and skillful action. We share case studies of interactive systems we have developed in three arenas—data wrangling, exploratory analysis, and natural language translation—that integrate proactive computational support into interactive systems. To improve outcomes and support learning by both people and machines, we describe the use of shared representations of tasks augmented with predictive models of human capabilities and actions. We conclude with a discussion of future prospects and scientific frontiers for intelligence augmentation research.
- Type: Article
- Publication: Proceedings of the National Academy of Sciences
- URL: https://www.pnas.org/content/116/6/1844
- Date Added: February 19th, 2020
- Zotero links: [Local library](zotero://select/groups/2451508/items/VBWQLYLA), [Web library](https://www.zotero.org/groups/2451508/items/VBWQLYLA)
- PDF links: [Heer_2019_Agency plus automation.pdf](zotero://open-pdf/groups/2451508/items/39CIXEFV)

## Discussion notes
Claude:
> **The vision.** Read in Week 4 of SP-24 (February 14th, 2024). Joel Chan returned to it in SP-25 as a statement of his interest in interaction as a core part of the "secret sauce" of human-AI systems: it "articulates this vision quite well in a way that resonates with me, drawing connections back to cybernetics too". (Joel Chan, SP-25 seminar)
> > "Although sharing overlapping origins in midcentury computer science, research programs in intelligence augmentation (IA; using computers to extend people’s ability to process information and reason about complex problems) and artificial intelligence (AI; developing computational methods for perception, reasoning, and action) have to date charted largely separate trajectories." (p. 1)
> - Instead of fully automated methods that imitate human actions, the paper proposes human-AI collaboration: "design of shared representations about people's tasks alongside interfaces with which people can review, select, revise, or dismiss algorithmic suggestions" (e.g., spellcheck, autocomplete), to "productively employ AI methods while ensuring that people remain in control". (S13, SP-24 notes)
> - The central pattern is [[PTN - Shared Representation]]. Joel Chan had foreshadowed it in Week 3, noting it was "really curious" that the previous week's reading did not describe shared representations. (Joel Chan, SP-24 consolidated notes)

Claude:
> **Case studies.** (S13, SP-24 notes)
> - Data wrangling: the shared representation is the Wrangle programming language, a high-level domain-specific language. [[PTN - Predictive Interaction]]: simple user selections guide automatic predictions of which transformations to apply.
> - Exploratory analysis: the shared representation is Vega-Lite. [[ART - Voyager]] blends manual and automated chart specification for both open-ended exploration and targeted question answering. One participant quote cuts the other way: "These related views are so good but it's also spoiling that i start thinking less. I'm not sure if that's really a good thing."
> - Natural language translation: the shared representation is digital text, in the [[ART - Predictive Translation Memory (PTM)]] project. Translators reported downsides: "the translator is less susceptible to be creative"; "[MT] distracts from my own original translation process by putting words in [my] head". The paper's conclusion: "neither automated suggestions nor direct manipulation play a strictly dominant role. Rather, we have observed that a fluent interleaving of both modalities can enable more productive, yet flexible, work."

Claude:
> **Critiques and open questions.**
> - The paper references few cognitive science ideas. This led S13 to pose [[QUE - What are the relevant cognitive science theories of agency, control, and problem-solving that could help predict the appropriate balance of agency and automation in a system?]], in response to Heer's question of whether "might we predict an appropriate balance of agency vs. automation based on the nature of the task". (S13, SP-24)
> - Joel Chan remained "stuck on the idea of agency being undefined". (Joel Chan, SP-24)
> - Contrast from the following week: in [[@caiHumanCenteredToolsCoping2019]], refine-by-concept led users to "overthink", the opposite of the PTM case here, where the tool limited diverse translations. (SP-24 seminar)

Claude:
> **Resources.** Talk video: [Colloquium on Creativity, National Academy of Sciences](https://www.youtube.com/watch?v=ouIFSDQwkQM&list=PLGJm1x3XQeK140JC2g7EzGO2NEK3a2I4l&index=23) (www.nasonline.org/Cybernetic_Serendipity). Altmetrics show the paper [cited in policy documents](https://pnas.altmetric.com/details/54958505/policy-documents) and [in patents](https://pnas.altmetric.com/details/54958505/patents). Voyager demo: https://vega.github.io/voyager/. (Joel Chan, SP-24 seminar)
