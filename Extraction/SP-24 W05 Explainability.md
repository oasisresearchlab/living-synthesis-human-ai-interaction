---
type: extraction-session
session: "SP-24 W05 Explainability"
sources: [notes]
extractedBy: Claude
created: 2026-11-24
---
Claude:
> SP-24 Week 5 (February 21st, 2024) read Cai et al. (2019) on [[ART - SMILY]], a similar-image search tool that helps pathologists with differential diagnosis through interactive refinement (by region, example, and concept). S05 distilled the paper through Ackerman's social-technical gap. S11 pushed on confirmation bias, the linear-concept design of the sliders, and "absence vs. negative concept", which led Joel Chan to bring in a cluster of work on transformer models and negation and a recent result on fair classifiers and physician bias. Connector and Archaeologist threads tied the paper to algorithmic folk theories, LIME and TCAV, [[ART - ImageSense]], and [[PTN - Predictive Interaction]]. The main contested points were whether refinement can stand in for explanation, and whether the tool helps or hurts confirmation bias.

## Nodes created
### Questions
- [[QUE - How might we design AI decision aids so that experts use them to seek disconfirming evidence rather than to confirm their first hypothesis?]]
- [[QUE - Could AI diagnostic aids help clinicians learn to diagnose cases that were underrepresented in their own training?]]
- [[QUE - How should concept-based steering interfaces distinguish the absence of a concept from its negation?]]
- [[QUE - How do expert users attribute errors and responsibility between themselves and an AI tool when its results surprise them?]]
- [[QUE - How do users' folk theories of opaque AI tools shape how they use them, and can interface design cultivate better ones?]]

### Claims
- [[CLM - interactive refinement can help users cope with opaque ML models by letting them test the algorithm, without explicit explanations of how it works]]
- [[CLM - expert users' information needs shift moment to moment with their current hypothesis, so AI decision aids need user-controllable notions of similarity]]
- [[CLM - the semantic gap between what an algorithm extracts from an image and what a user means by it is a core obstacle for content-based retrieval in expert work]]
- [[CLM - multi-month iterative design with a few domain experts grounds human-AI tool design better than superficial breadth]]
- [[CLM - transformer language models, even large ones, systematically struggle with negation]]
- [[CLM - concept sliders built from independently trained linear concept directions make the strength and combined effect of adjustments hard for users to interpret]]
- [[CLM - the form of AI assistance shapes whether it narrows or broadens users' exploration of alternatives]]
- [[CLM - improving AI-assisted diagnostic accuracy does not by itself reduce clinician bias, even when the classifier is fair]]

### Evidence
- [[EVD - pathologists rated SMILY above a conventional interface on diagnostic utility, trust, mental support, and willingness to use, with lower effort - @caiHumanCenteredToolsCoping2019]]
- [[EVD - pathologists interleaved refine-by-region, refine-by-example, and refine-by-concept tools within a single diagnostic case in SMILY - @caiHumanCenteredToolsCoping2019]]
- [[EVD - pathologists used SMILY refinement tools to tell ML errors from their own by removing suspect variables and re-searching - @caiHumanCenteredToolsCoping2019]]
- [[EVD - pretrained language models did not distinguish negated from non-negated cloze probes - @kassnerNegatedMisprimedProbes2020]]
- [[EVD - language models from 125M to 175B parameters performed worse on negated prompts as they scaled - @jangCanLargeLanguage2022]]
- [[EVD - NLU corpora had few and often unimportant negations, and transformers trained on them did much worse when negation mattered - @hossainAnalysisNegationNatural2022]]
- [[EVD - humans used negatively answered questions in GuessWhat dialogues while language-model guessers struggled to ground negation - @testoniArtificialIntelligenceModels2022]]
- [[EVD - AI assistance from a skin-tone-fair classifier raised diagnostic accuracy for over 1000 dermatologists and primary care physicians but did not resolve physician bias - Groh et al 2024]]

### Patterns
- [[PTN - Interactive refinement]]
- [[PTN - Content-based image retrieval (CBIR)]]

### Artifacts
- [[ART - LIME (Local Interpretable Model-agnostic Explanations)]]

### Theories
- [[THE - Social-technical gap]]
- [[THE - Algorithmic folk theories]]

## Bears on existing nodes
Claude:
> - [[ART - SMILY]]: this session supplies its full mechanism (three refinement tools plus auxiliary tools; S05, Distiller) and its user-study results; see the new EVD nodes and [[PTN - Interactive refinement]].
> - [[PTN - Concept Activation Vectors (CAVs)]]: S11's linear-classifier critique, already in Other Notes, is now a standalone claim ([[CLM - concept sliders built from independently trained linear concept directions make the strength and combined effect of adjustments hard for users to interpret]]). The TCAV source and hacker links (S16, S13) are already recorded there.
> - [[QUE - What criteria must a task meet to necessitate the collaboration of both algorithms and human expertise?]]: S06's question, with the Bitter Lesson image, already exists. This session suggests one candidate criterion: hypothesis-driven work whose relevant features shift moment to moment.
> - [[QUE - Can AI models learn new concepts that even experts can learn from to advance knowledge of a domain?]]: S06's AlphaZero links are already recorded. The new Q2 on clinicians learning from AI aids is a sibling question.
> - [[PTN - Shared Representation]], [[PTN - Predictive Interaction]], [[ART - ImageSense]]: Joel Chan's Connector replies to S08 are already recorded on these nodes; they now point to [[PTN - Interactive refinement]].
> - [[ART - Predictive Translation Memory (PTM)]]: S11 contrasted SMILY's concepts making users "overthink" with PTM (Lilt) reducing translation diversity. This feeds [[CLM - the form of AI assistance shapes whether it narrows or broadens users' exploration of alternatives]].
> - [[@hosseiniUnderstandingUnderstandingNot2021]] and the other negation source notes: they now back [[CLM - transformer language models, even large ones, systematically struggle with negation]].
> - [[PTN - local explanations]], [[PTN - algorithmic transparency]]: LIME is now an instance (S16, Archaeologist).
> - [[QUE - What is trust?]]: the SMILY study splits trust into capability-based and benevolence-based trust, and the two moved differently.

## Suggested relations
Claude:
> - [[ART - SMILY]] — instantiates → [[PTN - Interactive refinement]]: refinement tools (S05, SP-24 W05)
> - [[ART - SMILY]] — instantiates → [[PTN - Content-based image retrieval (CBIR)]] (S05)
> - [[PTN - Interactive refinement]] — uses → [[PTN - Concept Activation Vectors (CAVs)]]
> - [[EVD - pathologists used SMILY refinement tools to tell ML errors from their own by removing suspect variables and re-searching - @caiHumanCenteredToolsCoping2019]] — supports → [[CLM - interactive refinement can help users cope with opaque ML models by letting them test the algorithm, without explicit explanations of how it works]]
> - [[EVD - pathologists interleaved refine-by-region, refine-by-example, and refine-by-concept tools within a single diagnostic case in SMILY - @caiHumanCenteredToolsCoping2019]] — supports → [[CLM - expert users' information needs shift moment to moment with their current hypothesis, so AI decision aids need user-controllable notions of similarity]]
> - [[EVD - pathologists rated SMILY above a conventional interface on diagnostic utility, trust, mental support, and willingness to use, with lower effort - @caiHumanCenteredToolsCoping2019]] — supports → [[PTN - Interactive refinement]]
> - The four negation EVDs — support → [[CLM - transformer language models, even large ones, systematically struggle with negation]]
> - [[CLM - transformer language models, even large ones, systematically struggle with negation]] — informs → [[QUE - How should concept-based steering interfaces distinguish the absence of a concept from its negation?]]
> - [[EVD - AI assistance from a skin-tone-fair classifier raised diagnostic accuracy for over 1000 dermatologists and primary care physicians but did not resolve physician bias - Groh et al 2024]] — supports → [[CLM - improving AI-assisted diagnostic accuracy does not by itself reduce clinician bias, even when the classifier is fair]]
> - [[CLM - concept sliders built from independently trained linear concept directions make the strength and combined effect of adjustments hard for users to interpret]] — opposes → [[CLM - linear models are inherently more interpretable than deep neural network models]]
> - [[CLM - interactive refinement can help users cope with opaque ML models by letting them test the algorithm, without explicit explanations of how it works]] — supports → [[PTN - Actionable explainability]]
> - [[ART - LIME (Local Interpretable Model-agnostic Explanations)]] — instantiates → [[PTN - local explanations]]
> - [[THE - Social-technical gap]] — informs → [[CLM - the semantic gap between what an algorithm extracts from an image and what a user means by it is a core obstacle for content-based retrieval in expert work]]
> - [[THE - Algorithmic folk theories]] — informs → [[QUE - How do users' folk theories of opaque AI tools shape how they use them, and can interface design cultivate better ones?]]

## Skipped or uncertain
Claude:
> - Notes only, no transcript, so the nodes reflect written role contributions and Joel Chan's replies, not the live discussion.
> - The EVD nodes on SMILY rest on figures and passages pasted into the notes. The participant count (12) is inferred from the Figure 6 caption ("half (6) the participants"). I didn't add accuracy results because the notes don't include them.
> - The negation EVDs rest only on abstracts pasted into the notes. I skipped separate EVDs for Ettinger, MAQA, Jang (2022, meaning-matching), Hosseini, Chaturvedi, Jumelet, and Laverghetta; the first five are cited inside the negation claim.
> - The Groh et al. (Nature Medicine 2024) EVD rests on two tweets, and the second is cut off ("led to increased differences in…"). There's no source note, so the title ends in "Groh et al 2024" instead of a citekey. Verify against the paper.
> - The folk-theories paper (https://dl.acm.org/doi/10.1145/3476046) is described only as a CSCW paper on TikTok's "For You" page; I didn't name its authors because the notes don't.
> - Skipped: the Archaeologist's pointer to Andersen et al. (2023, TOCHI special issue on human-centred AI in healthcare), which was a list of themes with no discussion; S13's code request to Google; the "Bitter Lesson" image (already on the existing S06 QUE); S11's unanswered question about other refine-by-example experiments (noted on [[PTN - Interactive refinement]]).
> - Names: the notes include public researchers (Carrie Cai, Been Kim, Matt Groh, Michael Ann DeVito, Arvind Narayanan, Shubham Toshniwal, Jos Rozen). I found no un-pseudonymized student names.
