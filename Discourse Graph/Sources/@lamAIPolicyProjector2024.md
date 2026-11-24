---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-6620-741e-b2ed-c1a233c1ada9
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/WFb6jLguu
roamAuthor: "Joel Chan"
created: 2025-01-23
---

- Title: AI Policy Projector: Grounding LLM Policy Design in Iterative Mapmaking
- Author(s):: Michelle S. Lam, Fred Hohman, Dominik Moritz, Jeffrey P. Bigham, Kenneth Holstein, Mary Beth Kery
- Abstract: Whether a large language model policy is an explicit constitution or an implicit reward model, it is challenging to assess coverage over the unbounded set of real-world situations that a policy must contend with. We introduce an AI policy design process inspired by mapmaking, which has developed tactics for visualizing and iterating on maps even when full coverage is not possible. With Policy Projector, policy designers can survey the landscape of model input-output pairs, define custom regions (e.g., "violence"), and navigate these regions with rules that can be applied to LLM outputs (e.g., if output contains "violence" and "graphic details," then rewrite without "graphic details"). Policy Projector supports interactive policy authoring using LLM classification and steering and a map visualization reflecting the policy designer's work. In an evaluation with 12 AI safety experts, our system helps policy designers to address problematic model behaviors extending beyond an existing, comprehensive harm taxonomy.
- Type: Preprint
- Publication: 
- URL : http://arxiv.org/abs/2409.18203
- Date Added: January 23rd, 2025
- Zotero links: [Local library](zotero://select/groups/2451508/items/RXLBWWZI), [Web library](https://www.zotero.org/groups/2451508/items/RXLBWWZI)
- Tags: Computer Science - Artificial Intelligence Computer Science - Computation and Language Computer Science - Human-Computer Interaction Computer Science - Machine Learning
- PDF links : [Lam et al_2024_AI Policy Projector.pdf](zotero://open-pdf/groups/2451508/items/UN3KLD6L)

## Discussion notes

### Key question/problem

Claude:
> Read in Week 7 of the SP-25 HCAI Reading Seminar (March 12th, 2025).
>
> - The paper explicitly contrasts itself with [[PTN - Constitutional AI]] ([[@baiConstitutionalAIHarmlessness2022]]). The claim is that such approaches focus on enabling LLMs to *execute* policy, assuming we already know what we want: the "forward pass". (Joel Chan as Distiller, SP-25 seminar)
>   - ![[9QHV90dXH9.png]]
>   - ![[QYt8YcUMh6.png]]
> - Left open: how do we know if we have the right policies? This is the "backward pass": [[QUE - how can we support users to reason about whether they have the right policies when steering LLMs with policy?]]
>   - ![[aXEqzqg2um.png]]
>   - Key claim: we need cases (lots of them, systematically, in conversation with concepts/principles).
>   - Motivated by the "criteria drift" finding from [[@shankarWhoValidatesValidators2024]] ([[ART - EvalGen]]): users need criteria to grade outputs, but grading outputs helps users define criteria. Joel Chan: "kinda obvious a priori" from [[THE - Sensemaking Theory]], but good to have domain-specific validation.
> - "AI policy for LLMs does not appear as any centralized "policy" artifact, but rather a blend of different alignment techniques documents safeguards, and product or feature-specific decisions that form the AI's implicit learned policy. Part of the goal of this paper is to create more discussion around explicit, interpretable, and inspectable representations of an AI's learned policy." (Lam et al., 2024, p. 3)
> - What "AI policy" means here (ELI5 linter, SP-25): a specification of desired model behavior that is used to shape that behavior. It is *not* policy documents *about* AI made by governments, and *not* a reinforcement learning policy. S16 noted they first read "policy" in the title as government AI policy.
>   - ![[1FZuM8dAz2.png]]
>   - ![[G0YsFInSHg.png]]
> - In discussion, Constitutional AI was described as going a step further than [[ART - ConstitutionMaker]]: rather than modifying the prompt for a single turn, the collection of policies is used to tune the whole model. Today's chatbots are tuned in a similar spirit, but via opaque preference judgments ("I like this, I don't like this") from underpaid workers rather than explicit principles. (SP-25 seminar discussion)

### The artifact and its "secret sauce"

Claude:
> [[ART - AI Policy Projector]]: "Our mapmaking approach grants policy designers a global view of policy to understand how a large set of policies and cases interact and provides nuanced control with concepts to iterate and resolve conflicts in policy" (Lam et al., 2024, p. 4)
> ![[-ThVdAGMsg.png]]
> ![[R3KU6TB0RJ.png]]
> ![[RSyPDE2Lp1.png]]
> ![[Sqb27SIU1n.png]]
> ![[DOS0nsyxuR.png]]
>
> - Secret sauce: natural language definitions of "concepts" (classifiers that say whether a case contains, e.g., "property crime and vandalism") that can be used to group cases on the map and to steer. (Joel Chan, SP-25 seminar)
>   - ![[EtjH7jJAwt.png]]
>   - ![[cQU2qxt_sz.png]]
>   - Claim: [[CLM - LLM-generated and custom-defined natural language concepts --- with mappings to example LLM outputs that contain those concepts --- support interpretable exploration of LLM output patterns]]
> - Policies are if-then rules: if these concepts are present, then block, warn (generate as is but warn the user), suppress, or steer toward/away from a direction. A "case" is a user input plus a model output. The idea is to move back and forth between rules and cases, because "the world is messy", rather than state rules without looking at cases. (SP-25 seminar discussion)
> - The implicit claim is that policies made with a tool like this are more robust, because designers can see the landscape of cases and check coverage, rather than only thinking about principles or cherry-picking cases. In the user study, steering was done via prompting rather than by modifying the model. (SP-25 seminar discussion)
> - The map layout uses UMAP; user-defined concepts are added as landmarks, so the layout reflects both the semantics of cases and the concept embeddings. (SP-25 seminar discussion)
>   - Why add concept embeddings (S01 asked whether Sentence Transformer embeddings already capture concepts, and suggested ablations): Joel Chan's read is that sentence embeddings encode the "whole" semantics of a case, so the concept is diluted alongside everything else; the concept embedding *weights* the overall embedding toward the concept.

### Connections to other artifacts and patterns

Claude:
> - Similar to [[ART - DreamSheets]] and [[ART - ChainForge]] in its focus on making sense of your policies/prompts in conversation with cases. Compared with ChainForge's inspector, Policy Projector is less about systematic testing pipelines and more about iterative sensemaking over many cases. (Joel Chan, SP-25 seminar)
> - In theory it targets the open problem seen with [[ART - ConstitutionMaker]] (explicitly cited): no support for reasoning about interactions between principles, cc [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]]
>   - ![[q-sl_43qs5.png]]
> - Looks ahead to [[PTN - Sparse Autoencoders (SAEs)]] and back to [[PTN - Concept Activation Vectors (CAVs)]] from SP-24. (Joel Chan, SP-25 seminar)
> - S05 (🕸️ Connector) linked it to [[ART - Angler]], a system for exploring and creating challenging datasets for machine translation: both help developers explore the unbounded space of model behavior grounded in datasets/cases, and they share co-authors at Apple. Joel Chan pointed to Jeff Bigham as a potential hub for HCAI work at Apple, especially for accessibility.
> - S05 also saw "concepts", "cases", and "if-then" logic as a good scaffold for policy authoring, something missing in [[ART - ChainForge]], where end users lacked a systematic way of thinking (systematic work did appear with experts and with DreamSheets). Using concepts and cases helps users factorize a fuzzy phenomenon into principles or rules based on specific factors.
>   - ![[yTJcyVdgu4.png]]
>   - Joel Chan: reminiscent of cautions from expertise research about over-indexing on principles, and using cases to keep principles/schemas flexible enough for unseen problems: [[THE - Cognitive Flexibility Theory (CFT)]] (https://commoncog.com/learning-ill-structured-domains-series/)
> - Interesting nugget from the same week: [[ART - Spellburst]] ([[@angertSpellburstNodebasedInterface2023]]) bridges large but imprecise exploration in natural language to granular code editing via generated semantic sliders. (SP-25 seminar)
>   - ![[bEZJM6yLDc.png]]

### Evidence of efficacy

Claude:
> User study (section 6), Joel Chan's observations (SP-25 seminar):
> - Recruiting AI policy practitioners is good (not just random people), but the 30-minute sessions are really short (10-minute interview + survey).
> - [[EVD - AI policy practitioners expressed that bridging a map view of concepts and policies w- examples was helpful for reasoning about their LLM policies - @lamAIPolicyProjector2024]]
>   - ![[yIPDvD6PzM.png]]
>   - ![[qeVH6C7Pqi.png]]
> - [[EVD - AI policy practitioners expressed that being able to define and use custom concepts to describe aspects of LLM outputs was helpful for reasoning about flexibliity - coverage of their LLM policie]]
>   - ![[MaF7Fwqt5D.png]]
> - [[EVD - AI policy practitioners who used an initial prototype of ART - AI Policy Projector expressed a desire for more expressivity in definitions of policies, such as OR operators, and additional steer]]: OR operators, more than concepts in the "if" clause, more than WARN/SUPPRESS for steering.
> - [[EVD - AI policy practitioners found if-then statements in ART - AI Policy Projector to support transparent and interpretable LLM policy formulation - @lamAIPolicyProjector2024]], supporting [[CLM - If-then statements support transparent and interpretable LLM policy formulation]]: many participant quotes show the formulation is structured and clear. (S16, ELI5 linter)
>   - ![[ax41K-UA7S.png]]
>   - ![[GihfCoX3_I.png]]
> - ![[OyDFNkG_bo.png]]
>
> Offline evaluation (section 7), Joel Chan's observations: a neat validation of the concept classification components, and then of steering. Take with a grain of salt, since results depend on the model and the key contribution is the interactive framework, which can (at least theoretically) plug and play different models.
> - ![[RiZw2ITBI8.png]]
> - [[CLM - concept-based if-then policy + easy access to more training examples may be a powerful combination for enabling better steering]]
>   - ![[94_sNJ_Swz.png]]
> - Whether LLMs can actually be aligned via prompt engineering remains a live research question: the pipeline "kind of works" for these policies and concepts, but we don't know when it will succeed or fail in general. (SP-25 seminar discussion)

### Critiques

Claude:
> - **UMAP maps.** UMAP 2D projections are quite imperfect: really bad for inference, since *global* spatial separations can't be trusted, but can be ok for exploratory analysis, especially local separations: [[CLM - UMAP 2D projections do not produce meaningful global spatial separation]], but [[CLM - local separations between items in a UMAP 2D projection can be meaningfully interpreted]]. This is not stated in the paper. Joel Chan cited the controversy over a large genome study's race clusters, plus explainers (Science news; Oskolkov's NBIS slides; a Biostars thread; Topos Institute's "Understanding UMAP"). In discussion: all maps distort (cf. the Mercator projection), so it matters to know *what* is lost and how; an isolated point means few similar cases nearby, but global position and axes mean nothing. (Joel Chan as 🚧 Safety Inspection Expert, SP-25 seminar)
> - **Case-to-concept mapping.** Is it 1:1 or 1:many? It seems it must be 1:many, since rules can compose multiple concepts in the "if" clause, but how does this show up on the map? Inference: dots on the map are not 1:1 with actual cases, since cases can be generated to augment the case layer (and perhaps populated near concept landmarks as concepts are enriched). If it is de facto 1:1, the map may be a bad UI for complex case-based reasoning. (Joel Chan)
> - **No interactions between policies.** It still doesn't directly design for, or evaluate, reasoning about complex interactions between policies, e.g. when policies contradict. This was a hoped-for benefit of the map, and remains unsolved, unlike code, where you can test for regressions. (Joel Chan, SP-25 seminar)
> - **Theory.** A missed opportunity to ground the design in more specific theory. Credit for honestly noting experimenter positive bias. (Joel Chan)
>   - ![[Wpb0LBQotx.png]]
> - **Who counts as an expert?** S16 asked who the "AI safety experts" were and what criteria made them experts. S14 noted the participants seem relatively homogeneous and asked how including practitioners from education, healthcare, or public policy would shape tools like this. Joel Chan: the authors share this concern.
>   - ![[WSyAPjxA-_.png]]
>   - ![[JmYfu6pjnk.png]]
> - **What is a "policy gap"?** S16 read the paper's policy gaps as something more specific and previously unknown, rather than categories that modify the initial taxonomy, and questioned calling them "gaps", which implies the same conceptual level as the original safety taxonomy. The paper also doesn't describe the original safety categories given to participants (the "Anthropic red-teaming" reference is indirect). In discussion, one reading was that gaps are clusters of cases where the model's de facto policy diverges from the ideal and no policy is attached; these could be refinements/exceptions or entirely missing classes of harm, at different granularities. (S16, ELI5 linter; SP-25 seminar discussion)
>   - ![[tOVaxa5XCr.png]]
>   - ![[KQAP85O6mS.png]]
> - **Maps for whom?** S16 liked the idea of the map as a [[PTN - boundary object(s)]] but worried about how interactable maps are for different stakeholders, especially in fields where visuals are less common: [[QUE - in what ways might visual sensemaking and exploration paradigms like map-making depend on pre-existing visual sensemaking conventions in the community of users?]]
>   - ![[Fim796jwnk.png]]
> - **LLM-dependence of operations.** S01 (🚧 Safety Inspection Expert) noted many operations rely on prompting an LLM and asked whether the LLM's own policy affects them, e.g. whether it will faithfully summarize harmful cases or refuse, based on an experience of GPT refusing to explain a derogatory emoji usage (and answering when the prompt was reframed as for research). [[QUE - What are the tradeoffs between LLM alignment and performance?]] Joel Chan: there is a large, rapidly growing literature on alignment/performance tradeoffs (arXiv:2401.16332; arXiv:2406.04879).

### Governance and multi-stakeholder policy making

Claude:
> - S14 (🏺 Archaeologist) saw AI governance and human interaction as interdependent, and an emerging area of jobs requiring skills in policy development, constitutional frameworks, and concept mapping: [[QUE - How might visual sensemaking LLM policy tools like ART - AI Policy Projector integrate into broader governance processes?]]
>   - Joel Chan: dangerous to have CS-oriented folks design and execute policy without learning from the mess and wisdom of governance more broadly.
> - S05 noticed how law/governance terms (constitution, policy, case law) are borrowed in AI, and asked what other governance concepts and principles could serve as metaphors or models. Joel Chan pointed to "Interpreting the Rule(s) of Code: Performance, Performativity, and Production" (MIT Computational Law Report), which S05 noted even uses speech act theory to analyze code.
> - In discussion (SP-25): the paper name-checks policy and boundary objects but doesn't cash them out. Policy and governance are a whole field (how policies get legitimized, how flexible they should be, how case law relates to statutes, how to get democratic input). "Concept" and "case" evoke case law, but here cases are used roughly as data examples. Real policy making is rarely single-user, yet the tool and its study are single-user. Students debated tradeoffs: a single editor at the top of a hierarchy vs. collaborative editing (who has approval, whose edits go in; Git-style workflows are very engineering-specific); open participation may over-represent some voices; bureaucracy can be too slow for fast-moving issues; and rulemaking is never one-and-done, so the tool may be best seen as an avenue for iteration. Joel Chan framed these less as critiques than as research questions, e.g. a tool for AI auditors, or whether it could help with the specific ways bureaucracy fails.
> - One student framed the distinction as policymakers informing AI auditors about what to audit, and model makers working toward the auditors' standard, which Joel Chan linked to the idea of inspection. (SP-25 seminar discussion)

### Open questions

Claude:
> - [[QUE - how can we support users to reason about whether they have the right policies when steering LLMs with policy?]]
> - [[QUE - What metrics-framework should be used to evaluate LLM policy effectiveness (technical implementability, interpretability, alignment, etc.)?]] (S16, 🍜 Academic Researcher): what would an empirical framework for the effectiveness of map-based or if-then policies be? Ideas: case studies bridging policies to real-world implementation; comparing how different stakeholder groups apply the same process; policy performance under adversarial attacks.
> - [[QUE - How might visual sensemaking LLM policy tools like ART - AI Policy Projector integrate into broader governance processes?]]
> - [[QUE - in what ways might visual sensemaking and exploration paradigms like map-making depend on pre-existing visual sensemaking conventions in the community of users?]]
> - [[QUE - What are the tradeoffs between LLM alignment and performance?]]
> - [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]]
