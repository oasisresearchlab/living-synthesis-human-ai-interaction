---
type: extraction-session
session: "SP-24 W06-07 Explainability and trust"
sources: [notes]
extractedBy: Claude
created: 2026-11-24
---
Claude:
> Two SP-24 sessions on explainability and trust. W06 read Lipton's "The Mythos of Model Interpretability" ([[@liptonMythosModelInterpretability2017]]): a warmup on how to vet an opaque educational ML system, a class ontology activity on what interpretability means, and debate over whether post-hoc interpretation is inherently misleading and whether interpretability comes in levels or in kinds. W07 read Ehsan et al., "The Who in Explainable AI" ([[@ehsanWhoExplainableAI2021a]]): unwarranted faith in numbers, appropriation of explanations, and the creator-consumer gap. The sharpest critiques targeted the study's methods: recruiting the AI and non-AI groups from different populations, and running grounded theory on one-shot responses.

## Nodes created
### Questions
- [[QUE - What can instructors or administrators do to interpret and vet an educational ML system whose workings the developer has not explained?]]
- [[QUE - How can we determine which decision contexts require which kinds of interpretability?]]
- [[QUE - Which interpretability desiderata do existing human-AI systems such as SMILY, ImageSense, and Graphologue target, and what do they miss?]]
- [[QUE - What kinds and levels of explanation do constituents need to hold government uses of ML accountable?]]
- [[QUE - Who should AI explanations be designed for?]]
- [[QUE - How do different AI explanations change how people of different backgrounds collaborate with AI on decision-making and creative tasks?]]
- [[QUE - Do human persuasion strategies carry over to the design of AI explanations?]]
- [[QUE - How do people's conceptions of intelligence, as part of AI literacy, shape how they read numerical AI explanations?]]

### Claims
- [[CLM - developers' unwillingness to share algorithms, features, training data, or validation data should lower confidence in a deployed ML system]]
- [[CLM - learning gains from an ML practice-problem system may reflect overlap between practice items and the test rather than transferable understanding]]
- [[CLM - post-hoc interpretations risk misleading but are not inherently misleading]]
- [[CLM - the interpretability a deployment needs varies by decision context and along distinct dimensions rather than as one overall level]]
- [[CLM - pursuing transparency to win user trust can conflict with the broader goals a deployed AI system serves]]
- [[CLM - interpretability desiderata describe information about a model that predictive performance metrics alone cannot convey]]
- [[CLM - legibility and predictability of an agent's behavior are distinct properties that can trade off against each other]]
- [[CLM - numerical explanations can inflate trust in an AI system without improving understanding of it]]
- [[CLM - AI explanations can be used as dark patterns to earn unwarranted trust]]
- [[CLM - AI explanations designed by developers for people like themselves widen the creator-consumer gap]]
- [[CLM - users appropriate AI explanations for purposes their designers did not intend]]
- [[CLM - comparing AI-background and non-AI-background groups recruited from different populations confounds AI background with recruitment differences]]
- [[CLM - one-shot open-ended survey responses are too shallow to support a full grounded theory analysis]]

### Evidence
- [[EVD - participants ranked a rationale-generating robot above an action-declaring robot, and both above a numerical-reasoning robot, on perceptions of its explanations - @ehsanWhoExplainableAI2021a]]
- [[EVD - participants with an AI background preferred numerical-reasoning explanations over action declarations more than participants without an AI background did - @ehsanWhoExplainableAI2021a]]
- [[EVD - both AI-background and non-AI-background participants showed unwarranted faith in numerical explanations, for different reasons - @ehsanWhoExplainableAI2021a]]
- [[EVD - participants read AI explanations as serving functions beyond their design, such as confirming normal operation or enabling debugging - @ehsanWhoExplainableAI2021a]]
- [[EVD - both AI-background and non-AI-background participants associated humanlike AI explanations with command of language - @ehsanWhoExplainableAI2021a]]
- [[EVD - a skim of citation statements to Lipton's Mythos of Model Interpretability found most used it as a generic citation that interpretability matters - @liptonMythosModelInterpretability2017]]

### Patterns
- [[PTN - Probing a black-box model with edge-case and out-of-distribution inputs]]
- [[PTN - Subgroup outcome analysis]]
- [[PTN - Explanatory needs elicitation]]
- [[PTN - Contestable algorithmic decisions]]
- [[PTN - Contrastive explanations]]
- [[PTN - Appropriation-aware explanation design]]
- [[PTN - Cognitive forcing functions]]

### Theories
- [[THE - Interpretive flexibility]]
- [[THE - Dual-process theory of cognition]]

## Bears on existing nodes
Claude:
> - [[QUE - Why is interpretability important?]]: already holds the Lipton and EU quotes and the S05 and S11 contestability responses. This session adds the warmup's concrete answers (subgroup equity, validation, generalization) and Joel's "informativeness beyond the performance metric" framing (SP-24 W06), now in [[CLM - interpretability desiderata describe information about a model that predictive performance metrics alone cannot convey]].
> - [[QUE - What is interpretability?]] and [[QUE - What are possible meanings of interpretability that we may constuct and find useful?]]: the class ontology activity is already recorded there. The levels-vs-kinds debate (S08 and Joel Chan, SP-24 W06) is now its own claim.
> - [[QUE - What is trust?]]: S05's ELI5 gloss adds that trust may be competence-based or benevolence-based and can be measured behaviorally, e.g., as willingness to relinquish control (SP-24 W06).
> - [[QUE - What constitutes transparency?]]: already holds the simulatability, decomposability, and algorithmic-transparency levels. The session adds Lipton's claim that "neither linear models, rule-based systems, nor decision trees are intrinsically interpretable" and the transparency-vs-broader-goals tension.
> - [[CLM - linear models are inherently more interpretable than deep neural network models]]: the session's notes record Lipton's counterpoint ("neither linear models, rule-based systems, nor decision trees are intrinsically interpretable"; deep models are "not necessarily less transparent") and the FICO and Experian logistic-regression gaming example (SP-24 W06). These oppose the claim.
> - [[PTN - post-hoc interpretability]]: the debate over whether post-hoc means misleading (Joel Chan, S13, S11, SP-24 W06) and the contrastive sub-pattern, now [[PTN - Contrastive explanations]].
> - [[PTN - Automated Rationale Generation]]: W07 supplies its reception data, since rationales were ranked highest and read as humanlike.
> - [[PTN - Seamful XAI]]: S06 (Archaeologist, SP-24 W07) traced it as the follow-up to the Ehsan paper. It is a natural partner to appropriation-aware design.
> - [[PTN - Shared Representation]], [[PTN - Predictive Interaction]]: these already record Joel's "eschew explanations, design affordances for sensemaking" connector note.
> - [[QUE - what are the effects of different types of explanations on how people with or without an AI background perceive AI agents?]] and [[QUE - how and why do differences in AI background result in different perceptions of explanations?]]: now answered by the five new EVD nodes.
> - [[ART - Auditing Ai]]: an instance of the outside-in auditing that the new probing pattern describes.

## Suggested relations
Claude:
> - [[EVD - both AI-background and non-AI-background participants showed unwarranted faith in numerical explanations, for different reasons - @ehsanWhoExplainableAI2021a]] — supports → [[CLM - numerical explanations can inflate trust in an AI system without improving understanding of it]]
> - [[EVD - participants with an AI background preferred numerical-reasoning explanations over action declarations more than participants without an AI background did - @ehsanWhoExplainableAI2021a]] — supports → [[CLM - AI explanations designed by developers for people like themselves widen the creator-consumer gap]]
> - [[EVD - participants read AI explanations as serving functions beyond their design, such as confirming normal operation or enabling debugging - @ehsanWhoExplainableAI2021a]] — supports → [[CLM - users appropriate AI explanations for purposes their designers did not intend]]
> - [[CLM - numerical explanations can inflate trust in an AI system without improving understanding of it]] — informs → [[CLM - AI explanations can be used as dark patterns to earn unwarranted trust]]
> - [[CLM - comparing AI-background and non-AI-background groups recruited from different populations confounds AI background with recruitment differences]] — informs → [[EVD - participants with an AI background preferred numerical-reasoning explanations over action declarations more than participants without an AI background did - @ehsanWhoExplainableAI2021a]]: qualifies the between-group difference
> - [[CLM - post-hoc interpretations risk misleading but are not inherently misleading]] — informs → [[PTN - post-hoc interpretability]]
> - [[PTN - Contrastive explanations]] — instantiates → [[PTN - post-hoc interpretability]]
> - [[PTN - Contrastive explanations]] — enables → [[PTN - Contestable algorithmic decisions]]
> - [[PTN - Appropriation-aware explanation design]] — consistent with → [[PTN - Seamful XAI]]
> - [[THE - Interpretive flexibility]] — informs → [[CLM - users appropriate AI explanations for purposes their designers did not intend]]
> - [[PTN - Cognitive forcing functions]] — derived from → [[THE - Dual-process theory of cognition]]
> - [[CLM - the interpretability a deployment needs varies by decision context and along distinct dimensions rather than as one overall level]] — opposes → [[CLM - linear models are inherently more interpretable than deep neural network models]]: Lipton's point that no model class is intrinsically interpretable

## Skipped or uncertain
Claude:
> - S16's Safety Inspection notes in W06 were for Feuston and Brubaker ([[@feustonPuttingToolsTheir2021]]), not Lipton. S16 flagged them as written for the wrong paper. They raise generalizability limits: participants mostly CSCW and HCI scholars with ML experience; a focus on early analysis stages (sampling, coding); short social-media texts only. Not extracted, since they belong with that paper's session.
> - S08's link from unwarranted faith to a prior result ("when presented with fully pre-populated suggestions" people made more mistakes) has no source in the notes. It is mentioned in the numerical-explanations claim but not made into an EVD.
> - Archaeologist leads not developed in discussion: Arrieta et al. (arXiv 1910.10045) XAI taxonomy, the DARPA XAI program, and the participatory XAI talk by Kim et al. (cited inside the creator-consumer gap claim).
> - Lipton's causality point (supervised associations aren't guaranteed causal; the race and loan recidivism example) and the "We = Zachary Lipton" stylistic aside were passing points with no discussion.
> - THE - Dual-process theory of cognition is thin: S11 listed only the term, tied to heuristics. Keep it or merge it as you see fit.
> - S11's ELI5 glosses (Mann-Whitney U with Bonferroni correction, within- vs. between-subjects designs, encoder-decoder rationale generation) are methods explanations, not claims, so they were not extracted.
> - The Upol Ehsan tweet about the paper's long review history (S06) was skipped as context only.
> - Names: Upol Ehsan, Zachary Lipton, and Karl Popper are public authors or researchers. No un-pseudonymized student names were seen.
