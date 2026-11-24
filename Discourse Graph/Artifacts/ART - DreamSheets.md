---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e70-661e-79bd-a135-201d59d81505
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/mCwT2FGUm
roamAuthor: "Joel Chan"
created: 2025-03-04
---
## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> - To help people make sense of text-to-image models: hypothesis [[CLM - ART - DreamSheets can enable sensemaking of text-to-image models by enabling users to construct reusable visual computational explorations of how prompt and parameter variations relate to image]] (SP-25, session on [[@almedaPromptingDiscoveryFlexible2024]]).
> - To support open-ended creative exploration. For open-ended or creative tasks, users usually want to know what they can do and to sense the basic landscape of the "solution space"; DreamSheets and [[ART - AI Policy Projector]] both visualize the mapping between inputs and that solution space, to help users understand utility and encourage further exploration. (S01, SP-25 Week 9 synthesis)
> - Possibly to help people learn effective AI art generation: [[CLM - sensemaking tools like ART - DreamSheets can be used to help people learn to do effective AI art generation]] (S14, SP-25).

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> - A spreadsheet: prompt and parameter variations laid out as rows and columns of generated images. The seminar asked "why spreadsheets instead of ... infinite canvas / networks, etc.?", and connected the answer to [[CLM - 2D matrix layouts like PTN - small multiples and PTN - contact sheets are used to support visual design space exploration in the visual arts]] (see also [[PTN - contact sheets]]).
> - Related claims: [[CLM - to reason about LLM behavior, you need to be able to (visually) compare outputs side by side]] (S01, SP-25).

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

Claude:
> Usage patterns from [[EVD - expert visual artists actually used ART - DreamSheets to independently construct a diverse range of powerful, reusable computational exploration structures that could be use make sense of useful]] (SP-25):
> - Naturally creating 2D "small multiples" and "contact sheets":
> ![[7hwXH36HsM.png]]
> - Parametric manipulation, both stochastic (e.g., random seed) and non-stochastic (e.g., cfg):
> ![[X3tpuy4UHc.png]]
> ![[AKKOgr4OMo.png]]
> - Semantic manipulation, both manual and generative (using an LLM to generate prompt variations and combinations):
> ![[9vTIA_p_aU.png]]
> ![[PWIpPFreXb.png]]
> - A summary of what was translated into design features in the mockups for "DreamSheets 2.0":
> ![[GSnT0oOnQm.png]]

Claude:
> Some participants used it only for manual variations: [[EVD - some participants used ART - DreamSheets to power exclusively -manual- variations in prompts and parameters - @almedaPromptingDiscoveryFlexible2024]]
> ![[Mp0NaAlckV.png]]
> ![[oaOn_Lb2VP.png]] (p. 11)

## Other Notes
Claude:
> **What helps people use it well.** [[CLM - meta-knowledge of how text-to-image models work enables richer hypothesis exploration in ART - DreamSheets]]. Joel Chan (SP-25): such knowledge "gives a richer source of hypotheses to test in dream sheets," because you could add them as rows or columns and see whether they change the output. One example from the discussion: the timeframe of the training data, since the language and metadata of images collected around 2020–2021 would differ from today's internet language.

Claude:
> **Questions and critiques (SP-25).**
> - S14 (🚧 Safety Inspection Expert): how much training did participants need before exploring? How will the tool be kept up to date? Why two views, and not a third that shows the user's final selection?
> - S01: 2D or 3D visualization is limited for representing high-dimensional things like natural language embeddings (cf. [[CLM - UMAP 2D projections do not produce meaningful global spatial separation]]). And if the prompts or operators used to explore the solution space don't produce consistent (deterministic) outputs, the tool is less useful, since users may want to reproduce outputs they liked.

Claude:
> **Connections.**
> - Similar to [[ART - ChainForge]] in its focus on making sense of your prompts (or policies) in conversation with cases; the same was said of the system behind [[QUE - how can we support users to reason about whether they have the right policies when steering LLMs with policy?]] (SP-25).
> - A subtle difference from [[ART - Patchview]] ([[@chungPatchviewLLMpoweredWorldbuilding2024]]): there the target of sensemaking is the generated world, not necessarily the model.
> - Named in the SP-25 Week 15 synthesis as a valuable in-the-wild example of the kind of deployment the seminar wanted to see more of.
