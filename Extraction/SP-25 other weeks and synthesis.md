---
type: extraction-session
session: "SP-25 other weeks and synthesis"
sources: [notes]
extractedBy: Claude
created: 2026-11-24
---
Claude:
> The source covers the SP-25 intro week (participants' metaphors for AI and their most hated and favorite uses), the seminar framing (why the reading list centers concrete interactive systems with human-centered evaluation, and the discourse-graph method), the Week 9 and Week 15 synthesis discussions, the Index and Synthesis query page, and a reading backlog. Week 9 is the richest part. S05 proposed technical, cognitive, and task "resources" for agency. S01 raised solution-space maps, actionable explainability, and the risks of user edits. Group 1 raised governance of model edits. S14, S16, S15, and Group 3 critiqued the readings: who is missing from the studies, that the papers presuppose AI is the tool, that tools come before users, and that most tools are for technical users. Week 15 settled on a meta-strategy (scope down to subcomponents) and named next steps: tools for "the rest of us," and larger compositions tested in the wild.

## Nodes created
### Questions
- [[QUE - How should user-initiated edits to AI models be governed, and who should audit, track, and revert them?]]
- [[QUE - How reliable are interactive steering tools when they rely on LLMs to make judgments, and where must a human stay in the loop?]]
- [[QUE - Should non-technical users' access to technical resources for directly editing models be limited?]]
- [[QUE - How can we tell whether an interaction design actually sustains users' agency, beyond short lab user studies?]]
- [[QUE - Can intuitive sandbox-style interaction with generative models, as in DreamSheets, transfer to domains like games, music, and writing?]]
- [[QUE - Does letting users customize AI systems lead to individualization?]]
- [[QUE - What prior knowledge do users need to engage effectively with interactive human-AI tools, and can non-technical users acquire it?]]
- [[QUE - How can AI literacy frameworks address gaps in knowledge, privilege, and access between research teams, their study participants, and the general population?]]
- [[QUE - How should we frame a task and choose its boundary object before deciding whether to infuse AI into it?]]
- [[QUE - How might interaction-oriented components for sensemaking, editing, and evaluating models compose into larger workflows in the wild?]]

### Claims
- [[CLM - reversible, transparent model edits do not by themselves prevent harmful edits - interactive model editing also needs a way to detect and review harmful changes]]
- [[CLM - interaction designs for steering AI give users distinct kinds of resources for agency - technical, cognitive, and task resources]]
- [[CLM - visualizing the mapping between inputs and the space of possible outputs helps users of open-ended tasks see what is possible and encourages further exploration]]
- [[CLM - non-deterministic input-output mappings make exploration tools less useful because users want to reproduce outputs they liked]]
- [[CLM - interaction-oriented human-centered AI research mostly presupposes that an AI model has already been chosen as the tool for the task]]
- [[CLM - interactive human-centered AI tools are so far mostly designed for and tested with technically skilled users rather than -the rest of us-]]
- [[CLM - human-centered AI tool papers tend to build a tool first and then find users to test it, rather than starting from users' needs and current practices]]
- [[CLM - human-centered AI research teams rarely represent the communities most affected by their work, so positionality and power dynamics in participatory design need explicit attention]]
- [[CLM - visual interactions with AI models tend to impose lower cognitive load than text-based interactions]]
- [[CLM - giving end users leverage over model outputs makes AI feel more like a tool than an omniscient being, a first step toward trustworthiness that leaves training-data concerns unaddressed]]
- [[CLM - scoping human-centered AI down to specific subcomponents such as sensemaking, editing models, and evaluating models is a productive strategy for generating design ideas]]
- [[CLM - interaction-oriented approaches to AI have more potential than static explanation methods to support augmentative rather than automated AI systems]]
- [[CLM - a discourse graph is a kind of shared representation that can support AI-assisted scholarly synthesis]]
- [[CLM - people want AI to automate the tasks they don't value, not the creative work they do value]]

### Patterns
- [[PTN - Intelligence Augmentation (IA)]]

### Artifacts
- [[ART - Discourse Graphs]]

## Bears on existing nodes
Claude:
> - [[QUE - What is the design space of --interaction-oriented-- approaches to Human-Centered AI?]]: its Other Notes already summarize the Week 9 and Week 15 synthesis. The new nodes above break that summary into separate questions and claims. Week 15 also adds the "things are possible" list (spreadsheet, compile feedback into rules, map, GUI for chains, sliders and controls) and the wish for in-the-wild, "rest of us"-led work.
> - [[QUE - What types of resources are these interaction designs offering to users to sustain agency? How effective are these resources, and why the selection of these resources in a given context?]] and [[CLM - human-AI interaction designs can maximize human-agency by providing -task resources- to elaborate and improve their task model]]: the three-way taxonomy is now its own claim. S05's follow-up questions about access and measurement are now their own questions. (S05, W09)
> - [[PTN - Actionable explainability]]: Group 1 asked "Is explainability just transparency?" S01's risk note is now a standalone claim about reversible edits. (W09)
> - [[PTN - edit history with authorship and comments for accountable model editing]] (from another session): the same pattern as Group 1's "nice use of commit logs to enable reverting, auditing by people with relevant knowledge" for [[ART - GAM Changer]]. I created a duplicate (PTN - commit log of model edits), then deleted it and pointed my links here. Add Group 1's W09 framing to this node.
> - [[QUE - how do we enable people with less scientific literacy to benefit from systematic tools like ART - ChainForge?]]: Week 15 restated it as wanting tools for "the rest of us," people who are not "thinking like a scientist." (W15)
> - [[EVD - expert visual artists actually used ART - DreamSheets to independently construct a diverse range of powerful, reusable computational exploration structures that could be use make sense of useful]], [[EVD - data scientists successfully used ART - ChainForge to do systematic testing of their LLM pipelines - @arawjoChainForgeVisualToolkit2024]], [[EVD - it was possible for a two physicians to use ART - GAM Changer to edit a GAM model for sepsis risk prediction to account for possible issues with temperature, respiratory rate, and systolic blood]]: Week 15 treated these as the few in-the-wild or realistic deployments the seminar saw, and as models for future work. (W15)
> - [[@heerAgencyAutomationDesigning2019]]: already records Joel Chan's SP-25 use of it. The new IA pattern node quotes the same passage.
> - [[QUE - How might we design AI-infused systems that augment — rather than replace — human intelligence and work?]]: the framing section restates that the focal question is a sub-question of this one. Nothing new beyond the new claim on interactive vs. static explanation.

## Suggested relations
Claude:
> - [[EVD - DynaVis and an NLI-only baseline showed no statistically significant differences in NASA TLX cognitive load or task completion time - @vaithilingamDynaVisDynamicallySynthesized2024]] — opposes → [[CLM - visual interactions with AI models tend to impose lower cognitive load than text-based interactions]]: the one measured comparison in the graph found no difference in cognitive load
> - [[EVD - participants self-rated visualization editing tasks as easier to complete with DynaVis than with an NLI-only baseline - @vaithilingamDynaVisDynamicallySynthesized2024]] — supports → [[CLM - visual interactions with AI models tend to impose lower cognitive load than text-based interactions]]: weakly, via perceived ease
> - [[CLM - interactive model editing tools do not correct for editors' own biases, so safeguards against biased edits must come from social and process mechanisms]] — consistent with → [[CLM - reversible, transparent model edits do not by themselves prevent harmful edits - interactive model editing also needs a way to detect and review harmful changes]]
> - [[PTN - LLM-as-a-judge]] — informs → [[QUE - How reliable are interactive steering tools when they rely on LLMs to make judgments, and where must a human stay in the loop?]]: S01 proposed an LLM judge to catch harmful edits
> - [[QUE - How might chain-based LLM tools be made usable by non-technical people, and should the tools be simplified or the users educated to meet them?]] — consistent with → [[QUE - What prior knowledge do users need to engage effectively with interactive human-AI tools, and can non-technical users acquire it?]]
> - [[CLM - translating an intuitive construct into a trustworthy metric is a scientific-thinking meta-skill that is a precondition for benefiting from systematic LLM testing tools]] — supports → [[CLM - interactive human-centered AI tools are so far mostly designed for and tested with technically skilled users rather than -the rest of us-]]
> - [[CLM - the levers for human control in human-AI interaction depend on the model class - glass-box models expose editable components, while LLMs mainly expose the prompt]] — consistent with → [[CLM - interaction designs for steering AI give users distinct kinds of resources for agency - technical, cognitive, and task resources]]: S05 also noted technical resources differ for GAMs vs. LLMs
> - [[CLM - interaction designs that increase user agency by requiring more resource involvement can impose costs on the user's primary task]] — informs → [[QUE - How can we tell whether an interaction design actually sustains users' agency, beyond short lab user studies?]]
> - [[CLM - knowledge of a text-to-image model's training data is AI literacy that complements, and cannot easily be gained from, exploring outputs in tools like DreamSheets]] — informs → [[QUE - What prior knowledge do users need to engage effectively with interactive human-AI tools, and can non-technical users acquire it?]]
> - [[EVD - worldbuilders answered landscape (distribution) questions about a generated world faster and more accurately with Patchview than with a list-only baseline - @chungPatchviewLLMpoweredWorldbuilding2024]] — supports → [[CLM - visualizing the mapping between inputs and the space of possible outputs helps users of open-ended tasks see what is possible and encourages further exploration]]
> - [[EVD - AI policy practitioners expressed that bridging a map view of concepts and policies w- examples was helpful for reasoning about their LLM policies - @lamAIPolicyProjector2024]] — supports → [[CLM - visualizing the mapping between inputs and the space of possible outputs helps users of open-ended tasks see what is possible and encourages further exploration]]
> - [[CLM - interaction-oriented human-centered AI research mostly presupposes that an AI model has already been chosen as the tool for the task]] — consistent with → [[CLM - human-centered AI tool papers tend to build a tool first and then find users to test it, rather than starting from users' needs and current practices]]
> - Each node's own Suggested relations section lists more.

## Skipped or uncertain
Claude:
> - Most Week 1 introduction content (individual research interests, metaphors such as "garden," "statistician that double majored in creative writing," "digestive system," "blind boxes") was not developed into discussion. Only the converging "automate what I don't value" theme became a claim. The "bicycle for the mind" metaphor appears in the IA pattern.
> - Environment setup, the Roam query-block configurations on the Index and Synthesis page, and the description of seminar roles were skipped as logistics. A role-based reading method could become a pedagogy node, but it falls outside this vault's human–AI design scope.
> - Reading backlog: Cocoa, GenQuery, Canvil, and most of the other papers already have source or ART nodes. The Buçinca et al. (2020) paper on proxy tasks and subjective measures in XAI evaluation has no source note and was only listed, so I did not extract it. It would bear on the claims about how these tools are evaluated.
> - S04's UIST 2024 game paper ("What's the Game, then? ...") is cited in plain text inside the sandbox question. I did not create an ART node because the notes don't name the system. S09's AI game link (a Creative Bloq article) was also left as context only.
> - S09's remark about Claude's memory and context limits, and S12's personal hallucination anecdote, were skipped as passing mentions or too personal.
> - Week 9 Group 2's synthesis block and S02's and S27's entries were empty.
> - The individualization question (S14) is a one-line prompt. The possible readings in its Other Notes are my interpretation, and are marked as such.
> - No transcript was available for these weeks, so all grounding comes from written notes.
