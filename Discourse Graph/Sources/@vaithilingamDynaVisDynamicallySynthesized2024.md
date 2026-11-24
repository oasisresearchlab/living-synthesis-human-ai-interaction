---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-6620-7654-ab9c-6333c23bc995
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/5iCQmJtQ7
roamAuthor: "Joel Chan"
created: 2025-03-12
---

- Title: DynaVis: Dynamically Synthesized UI Widgets for Visualization Editing
- Author(s):: Priyan Vaithilingam, Elena L. Glassman, Jeevana Priya Inala, Chenglong Wang
- Abstract: Users often rely on GUIs to edit and interact with visualizations — a daunting task due to the large space of editing options. As a result, users are either overwhelmed by a complex UI or constrained by a custom UI with a tailored, fixed subset of options with limited editing flexibility. Natural Language Interfaces (NLIs) are emerging as a feasible alternative for users to specify edits. However, NLIs forgo the advantages of traditional GUI: the ability to explore and repeat edits and see instant visual feedback. We introduce DynaVis, which blends natural language and dynamically synthesized UI widgets. As the user describes an editing task in natural language, DynaVis performs the edit and synthesizes a persistent widget that the user can interact with to make further modifications. Study participants (n=24) preferred DynaVis over the NLI-only interface citing ease of further edits and editing confidence due to immediate visual feedback.
- Type: Conference paper
- Publication: 
- URL : https://dl.acm.org/doi/10.1145/3613904.3642639
- Date Added: May 25th, 2024
- Zotero links: [Local library](zotero://select/groups/2451508/items/7BAR6M63), [Web library](https://www.zotero.org/groups/2451508/items/7BAR6M63)
- Tags: Usability Study User Experience Design Visualization
- PDF links : [Vaithilingam et al_2024_DynaVis.pdf](zotero://open-pdf/groups/2451508/items/E55ZFEFV)

## Discussion notes
Claude:
> Read in SP-25, Week 12 (April 16th, 2025).

Claude:
> **The problem.** How to balance natural language interfaces (NLI) and GUIs for making visualizations without programming directly.
> - With an NLI you can often get 80% of the way, but then you want to explore lots of fine-grained tweaks, which are hard to discover or control through an NLI.
> - Starting with a GUI gives maximal control, but is too overwhelming as a starting point.
> - Framed in the intro (section 1) via the gulfs of evaluation and execution. The usage scenario (section 2, esp. the remarks at the end, p. 5) and the tasks in 4.3 are worth reading with an eye to how you might do them with an NLI alone.
> - Analogous situations: world-building (make a world, then do lots of fine-grained tweaks to characters and elements) and post-editing in translation.

Claude:
> **The artifact and its "secret sauce."** [[ART - DynaVis]] introduces dynamic widgets: "small modular UI components that focus on a particular edit or interaction task at hand. The edit can involve simple changes to one or multiple chart properties, such as changing the position of the legend or slicing, or can involve a data transformation operation executed on the data before chart rendering, such as filtering specific ranges on the axes." (p. 5)
> ![[UC73cBwERO.png]]
> ![[OomTePMxWa.png]]
> - It uses [[ART - Vega-Lite]] as an underlying [[PTN - Domain-Specific Language (DSL)]] for constraints (Joel Chan).
> - The related-work section "Customizable and dynamic user interfaces" (section 7) gives context for the deeper design pattern. A talk on the design space around this concept (there called "dynamic UIs") was also shared: https://www.youtube.com/watch?v=if9YEO5yty0

Claude:
> **Evidence of efficacy.**
> - Participants: "We recruited 24 participants (13 female, 10 male, 1 chose not to disclose) through the mailing lists of two research universities." Most worked with visualizations at least monthly (2 daily, 4 weekly, 14 at least monthly, 4 occasionally). (p. 8)
> - About 4x more natural language prompts in the baseline (roughly 8 vs. 2).
> - Participants self-rated the task as easier to complete with DynaVis than with the baseline.
> ![[jpnI52Ew74.png]]
> - No significant differences on cognitive load (NASA TLX).
> - Seminar hypothesis: for more exploratory, larger-scale changes, NLI may beat DynaVis; DynaVis is best when you have lots of small, annoying tweaks to make and iterate on.

Claude:
> **Critiques and connections (SP-25 roles).**
> - S01 (🚧 Safety Inspection Expert): both the data summary and the visualization rely on the LIDA summarizer. This works around LLM input limits but raises concerns about data fidelity and missing information; final quality depends heavily on the summarizer. S01 also wondered how DynaVis handles the different vocabularies users bring from different visualization grammars (e.g., ggplot2's aesthetics and facets vs. matplotlib's figure and axis, or tools like Tableau with no grammar).
> - S11 (🕸️ Connector): connects to the Constitutional AI readings through the pattern of dynamically generated structures that materialize from the system's inference of user intent (here, widgets; there, policies people author and refine). The pattern makes concrete the edits people want to do, but hinges on the LLM getting it right and assumes simple usage; interacting or conflicting edits make the interaction space complex. Joel Chan linked this to [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]], noting that 3.1 "Widgets as modular sub-components" (p. 5) partially addresses it.
> - S16 (🍜 Academic Researcher): the paper informed S16's own project on a collaboration system for expert tutors and LLMs to inductively explore and refine constructs from education discourse data (similar at a high level to [[ART - LLOOM]]). It suggested adding an NLI for memoing: users describe a new construct in natural language, retrieve examples and visualizations of its prevalence, then tweak inclusion and exclusion criteria.
