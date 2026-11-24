---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-661f-71dd-9126-ed1d9c3fd79e
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/yZiA1zV7v
roamAuthor: "Joel Chan"
created: 2025-01-15
---

- Title: Prompting for Discovery: Flexible Sense-Making for AI Art-Making with Dreamsheets
- Author(s):: Shm Garanganao Almeda, J.D. Zamfirescu-Pereira, Kyu Won Kim, Pradeep Mani Rathnam, Bjoern Hartmann
- Type: Conference paper
- Publication: 
- URL : https://dl.acm.org/doi/10.1145/3613904.3642858
- Date Added: January 14th, 2025
- Zotero links: [Local library](zotero://select/groups/2451508/items/659U3F97), [Web library](https://www.zotero.org/groups/2451508/items/659U3F97)
- PDF links : [Almeda et al. - 2024 - Prompting for Discovery Flexible Sense-Making for.pdf](zotero://open-pdf/groups/2451508/items/68KI468N)

## Discussion notes
Claude:
> Read in Week 6 of the SP-25 seminar (March 5, 2025), listed under "Design examples". Citation: Almeda, S. G., Zamfirescu-Pereira, J. D., Kim, K. W., Mani Rathnam, P., & Hartmann, B. (2024). Prompting for Discovery: Flexible Sense-Making for AI Art-Making with Dreamsheets. *Proceedings of the CHI Conference on Human Factors in Computing Systems*, 1–17.

### The problem
Claude:
> Key question: [[QUE - How might new interfaces support users in sense-making for successful art making with text-to-image models?]]; more specifically, how users can build an understanding of the mapping between the prompt input space and the image output space.
> ![[_axYYSZtu8.png]]
> - [[PTN - Text-to-Image Latent Diffusion Model]] is a different class of model from [[PTN - Large Language Models (LLMs)]] or [[PTN - Generalized Additive Models (GAMS)]]. Prompts for text-to-image models look less like natural-language instructions (where something like [[ART - ConstitutionMaker]] makes sense) and more like long lists of keywords that are not very human-readable; this is partly an artifact of how the models use CLIP. See, e.g., the difference between prompts by experienced vs. novice prompt artists:
> ![[uSK7iJXp_U.png]]
> - Joel Chan framed this as a new kind of question for the seminar. Earlier readings asked how users express intent, assuming they know how the model works. This paper asks how users can build a model of a prompt-to-image mapping they don't know, framed as a sensemaking problem: not finer-grained control, but "a place from which you can decide ... how you want to control and steer it." It is partly a scientific question (what is the nature of these models?) and partly a user question. (Joel Chan, SP-25 seminar)
> - Joel also liked that the paper draws on community practice: forums and Midjourney's public Discord channels, where people share what works and what doesn't. (Joel Chan, SP-25 seminar)

### The artifact and its "secret sauce"
Claude:
> [[ART - DreamSheets]] ({{video: https://www.youtube.com/watch?v=x_9lm8ZaNtI}}):
> ![[_CShhSNsL6.png]]
> - The secret sauce is exploratory (visual) comparison:
> ![[BbJY2WLhZc.png]]
> ![[AFPtyDOPtT.png]]
> - Mechanism as discussed: rows and columns hold prompt fragments (with slots), and each cell combines the parts from its row and column into a prompt. Moving across a row gives variations along one vector; moving to the next row jumps to another level of variation. There are two models: the user steers the text-to-image model (Stability), while GPT is used to generate axes of exploration (e.g., points on a dimension like cat breeds). Only control of the text-to-image model is evaluated. (SP-25 seminar discussion)
> - The system also supports discovering and generating variations in prompt space, similar to how [[ART - ConstitutionMaker]] surfaces possible rules:
> ![[aek_LKftEn.png]]
> - The comparison approach is motivated by [[THE - Sensemaking Theory]] (Russell, Stefik, Pirolli, & Card, 1993, "The cost structure of sensemaking") and draws inspiration from [[PTN - Exploratory Search Interfaces]]:
> ![[Ldc6dvd3SX.png]]
> ![[ZBiCtbeixZ.png]]
> ![[34OrIAed44.png]]
> - Joel Chan's reading of the sensemaking link: in the learning loop complex, sensemaking loops between schemas/representations and data, with "residue" (surprises) driving refinement. The spreadsheet supports this loop: rows and columns are the representation, cell contents are the data. The paper itself cites Davis's creative sensemaking framework, which has a similar loop of reducing variance between one's model and sensory input. An information-foraging reading is also possible: images give "information scent" about which regions of prompt space are worth exploring. (Joel Chan, SP-25 seminar)
> - In a sense this is like [[ART - ChainForge]], "turned up to 100000 on the comparison/sensemaking dimension", and placed within creativity support tools. (Joel Chan, SP-25 seminar)

### Why spreadsheets?
Claude:
> - Joel Chan asked why spreadsheets rather than an infinite canvas or networks. His answer: 2D is easier than 3D, and 1D is too linear to compare, so the grid is a sweet spot between flexibility and structure. Related tools inspired by comparative sensemaking use free-form canvases for collaging; DreamSheets moves toward something more systematic. (Joel Chan, SP-25 seminar)
> - "I wonder if spreadsheets are more commonly used by novice designers. Also it seems like there are more functions (sort, filter, grouping, etc) that can be easily done through the grid format that spreadsheets provide." (S14, SP-25)
> - The paper grounds the grid in established visual-arts practice: [[CLM - 2D matrix layouts like PTN - small multiples and PTN - contact sheets are used to support visual design space exploration in the visual arts]], i.e., [[PTN - small multiples]] from Tufte and [[PTN - contact sheets]] in photography (https://petapixel.com/what-is-a-contact-sheet/).
> ![[jgRhk7JysV.png]]
> ![[ywJv4wbb6B.png]]
> - Hypothesis: [[CLM - ART - DreamSheets can enable sensemaking of text-to-image models by enabling users to construct reusable visual computational explorations of how prompt and parameter variations relate to image]]
> - S15 added [[CLM - A 2 x 2 matrix is visually efficient for our brains to detect contrasts and differences]], citing grid layouts of meters in nuclear control room design (Seminara et al., 1979, *Human factors methods for nuclear control room design*, EPRI-NP-1118-SY), and an AI-generated review of supporting theory: parallel visual processing, Gestalt grouping, pre-attentive salience of outliers, spatial memory and chunking, and comparative scanning. (S15, SP-25)
> ![[puuhtLLP3w.png]]
> - Joel Chan agreed the paper "didn't make the connection to this visual perception theory" but "got the right intuition", and that the connection would make the paper stronger. (Joel Chan, SP-25 seminar)
> - On novelty: a participant felt the idea was simple and not novel. Joel Chan's response: it is novel in *systematizing* a practice that pockets of people already use, and he likes that design pattern of identifying effective practices and building a tool that scaffolds them for others. He also praised the paper for paying homage to related tools rather than citing prior work derogatorily. (Joel Chan, SP-25 seminar)
> - Compared with a single prompt box plus regenerate (no comparison, no history) and chat (history, but hard to compare), the spreadsheet affords both history and comparison, plus reuse of good prompts. One participant described this as information infrastructure that organizes history for the user; Joel noted that users, not the system, do most of the organizing, often building multiple manual grids in one sheet. (SP-25 seminar discussion)

### Evidence of efficacy
Claude:
> - Joel Chan called the user study "INCREDIBLE" (similar to [[@arawjoChainForgeVisualToolkit2024]]): credible users and authentic usage over a deployment of about two weeks with expert artists who already use text-to-image as a medium, rather than novices. The data is what people *made* with the tool, not only what they said. (Joel Chan, SP-25 seminar)
> - Usage patterns: [[EVD - expert visual artists actually used ART - DreamSheets to independently construct a diverse range of powerful, reusable computational exploration structures that could be use make sense of useful]]
>     - naturally creating 2D "small multiples" and "contact sheets":
> ![[7hwXH36HsM.png]]
>     - parametric manipulation, both stochastic (e.g., random seed) and non-stochastic (e.g., cfg):
> ![[X3tpuy4UHc.png]]
> ![[AKKOgr4OMo.png]]
>     - semantic manipulation, both manual and generative (using an LLM to generate prompt variations and combinations):
> ![[9vTIA_p_aU.png]]
> ![[PWIpPFreXb.png]]
>     - a summary of what was translated into design features in the mockups for "DreamSheets 2.0":
> ![[GSnT0oOnQm.png]]
> - [[EVD - some participants used ART - DreamSheets to power exclusively -manual- variations in prompts and parameters - @almedaPromptingDiscoveryFlexible2024]] (p. 11):
> ![[Mp0NaAlckV.png]]
> ![[oaOn_Lb2VP.png]]
> - The kind of more direct evidence Joel wanted more of:
> ![[CfjD0ZMP9Q.png]]
> - "I really love the attribution and publicity for the expert artists who participated in Study 2 in Section 10, if they chose to de-anonymize themselves." (S11, SP-25)
> ![[iXY_Iwlz0B.png]]

### Critiques and limits of the evidence
Claude:
> - Joel Chan felt the study showed well that people *can* build small-multiples and contact-sheet exploration structures, but gave little direct evidence that the structures helped sensemaking: the experiments could all have "failed". The strongest evidence would be artists saying "I learned something" or "I found a space of things I love that I wouldn't have found with chat". One example: E1 used text generation to discover prompt modifiers such as monochromatic, watercolor, and pixel art. He put his confidence that DreamSheets helps sensemaking at 60–80%. (Joel Chan, SP-25 seminar)
> - Does the tool push people to think systematically, or did the experts already think this way? The paper notes experts already saved results and prompt modifiers in spreadsheets or Word documents, and that even novices developed strategies within 40 minutes, but the study was not set up to test this. Joel contrasted [[ART - ChainForge]], where the tool did not make people think systematically: perhaps DreamSheets works because it matches the existing (artistic, not scientific) sensemaking practices of its community, such as contact sheets and collages. (Joel Chan, SP-25 seminar)
> - There was no comparison condition, e.g., the same prompts without the grid; a content analysis of how prompts changed was suggested. (SP-25 seminar discussion)
> - Success is subjective in art, so the goal is to help each user make sense of the prompt-to-image mapping *they* care about, not objectively "good" regions of the space. (SP-25 seminar discussion)

### Prior knowledge and AI literacy
Claude:
> - [[CLM - meta-knowledge of how text-to-image models work enables richer hypothesis exploration in ART - DreamSheets]]: knowing what text is on the Internet next to images (captions, alt text, metadata, shaped by what sells and by SEO) is meta-knowledge that DreamSheets alone may not reveal. Joel Chan: it "gives a richer source of hypotheses to test in dream sheets ... you could like add those as like rows or columns" (e.g., when training data was collected and what slang it contains). (Joel Chan, SP-25 seminar)

### Open questions from the roles
Claude:
> - Replicability (🚧 Safety Inspection Expert): "How useful is this application if images cannot be replicated outside of Dreamsheet?" Even with the same prompt and hyperparameters, API calls may return different images. (S01, SP-25)
>     - S11: as with all closed-source AI applications, the onus may be on the user (like saving your work in Word); the value is exploring variation and assessing differences at that point in time. (S11, SP-25)
>     - S15: advances in mechanistic interpretability might let users "save" parameter values for high-fidelity replication. (S15, SP-25) Joel Chan noted the seminar would later read about sparse autoencoders and feature steering, and called this an open question. (Joel Chan, SP-25 seminar)
> - Learning: "I found the Dreamsheet to be an excellent tool that provides both scaffolding and guidance for novice and expert designers alike." See [[CLM - sensemaking tools like ART - DreamSheets can be used to help people learn to do effective AI art generation]]. S14 also asked how much training participants needed, how the tool would be kept up to date, and why there was no third view showing the user's final selection. (S14, SP-25)
> - Long-term reuse: a single session is useful, but months later, how do you find the prompt behind a past image? This points to a "DreamSheets 2.0" that saves favorite prompts and tokens. (SP-25 seminar discussion)
> - Extensions (🍜 Academic Researcher): exposing more hyperparameters, e.g., `style_preset` and text prompt weight in the Stability API (S01, SP-25); other shared media that offer spreadsheet affordances in line with Shneiderman's creativity-support principles (exploratory search, collaboration, rich history, low threshold/high ceiling/wide walls), such as storyboards, visual timelines, or chat (S11, SP-25); and integrating image-to-text with text-to-image so image edits are reflected in prompt space (S11, SP-25). A similar prompt generator, DreamStory (https://dream-xyz.github.io/dreamstory), was also shared:
> ![[l_zkLPvt9K.png]]
> - ELI5: a novelist who can't paint puts a character description into a spreadsheet and uses DreamSheets to bring the character to life. (🤔 ELI5 linter, SP-25)
> - [[QUE - How does cfg influence image generation?]]: higher CFG scale means more alignment with the prompt but possible distortion; lower means more creativity and quality but possible deviation from the prompt (https://blogs.novita.ai/understanding-cfg-scale-in-stable-diffusion/). (S01, SP-25)

### Later synthesis
Claude:
> In the later SP-25 synthesis, the DreamSheets evidence ([[EVD - expert visual artists actually used ART - DreamSheets to independently construct a diverse range of powerful, reusable computational exploration structures that could be use make sense of useful]]) was cited under open-ended creative task-space exploration (understanding what the model and users are capable of), and as an example of the in-the-wild deployments the seminar wanted more of.
