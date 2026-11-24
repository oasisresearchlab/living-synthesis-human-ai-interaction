---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-661f-703d-86cc-267763bbcf8b
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/AzNAUqTQP
roamAuthor: "Joel Chan"
created: 2025-02-04
---

## Discussion notes

### Reading context
Claude:
> Read in Week 2 of the SP-25 HCAI Reading Seminar (February 5, 2025): Wang, Z. J., Kale, A., Nori, H., Stella, P., Nunnally, M. E., Chau, D. H., Vorvoreanu, M., Wortman Vaughan, J., & Caruana, R. (2022). Interpretability, Then What? Editing Machine Learning Models to Reflect Human Knowledge and Values. *Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining*, 4132–4142. https://doi.org/10.1145/3534678.3539074
> - Live demo (shared by the 👾 Hacker role): https://interpret.ml/gam-changer. The tool is open source and can run as a Jupyter notebook extension; a user's own model can be loaded as a JSON specification exported from Python. Joel Chan praised this as "next level" compared with the usual blurry demo video: "you don't have to take their word for it."

### Problem and question
Claude:
> The paper goes beyond showing people what a model does, to letting them *act* on what they see: [[QUE - How might we empower users to act on model interpretations when they lack expertise in ML and software engineering?]] (Distiller notes, SP-25). Two sub-challenges were pulled out:
> - the basic mechanics of actually editing the model
> ![[lQ4LXYFRSE.png]]
> - reasoning about potential unintended negative consequences of modifications
> ![[x1tAMGdXMQ.png]]

### The artifact: GAM Changer
Claude:
> The paper proposes [[ART - GAM Changer]] as a way to let users audit and *edit* [[PTN - Generalized Additive Models (GAMS)]]. "GAM Changer is a tool that helps non-engineers modify GAM models" (Joel Chan, SP-25 seminar).
> - What are GAMs? Very similar to generalized linear models, but instead of a weight for each predictor, each feature has a "shape function" that can be a variety of (nonlinear) functions rather than simple multiplication. The features are additive, without higher-order interactions, and are specified up front rather than learned in hidden layers. GAMs belong to the class of [[PTN - Glass-box models]]: all features and shape functions are visible. (Distiller notes and seminar discussion, SP-25)
> ![[YPjU_eux-7.png]]
> - In discussion, the shape functions were framed as a trade-off on the model side: less predictive power in theory than a large neural network, but much nicer properties for reasoning about each feature on its own. S14 offered an intuition: each component is a mathematical function, and the final output is a curve that approximates that shape. A clarification later in the session: the edited functions are continuous piecewise functions; categorical features are shown as bars, one per bin. (SP-25 seminar)
> - A norm Joel Chan proposed for the semester: don't say "AI", name the specific model. This is not an interactive model editing tool for "AI"; it is one for GAMs. It may extend to other glass-box models or regressions, but says nothing about editing large language models.
> - S09 (🤔 ELI5 linter) offered an analogy: a new puppy was trained in a language you don't speak, so instead of learning the language you find hand gestures it responds to. The shape-function interface is the "hand gesture" that lets non-engineers retrain the model.

### Key design patterns
Claude:
> - [[PTN - Shared Representation]]: not named in the paper, but the shape functions are a medium that both the user and the model can reason about, probably far better than a table. You can spot misalignments at a granular level (e.g., "it's weird that this group of patients gets no sepsis prediction") and fix them by editing that same representation instead of writing instructions or code. Joel Chan called this "a common design pattern ... that's very, very powerful" in human-centered AI design. (Joel Chan, SP-25 seminar)
> - [[PTN - Direct Manipulation]] to address the mechanics challenge: edit the model by directly editing its shape function, with scaffolds in the form of preset "modification types" (align, interpolate, monotonize, etc.).
> ![[omkpng_BTY.png]]
> - Joel Chan noted it is not the purest example of direct manipulation (the purest would be dragging the curve itself; here you still select boxes and click icons), but the constraint matters because interpolating vs. flattening vs. smoothing vs. making a segment linear are quite different edits. It is still far better than writing code.
> - Continuous feedback and reversible actions address the consequences challenge:
>   - continuous feedback, e.g., link + reorder to see correlated features
> ![[JO6PA2aLPZ.png]]
>   - reversible actions, inspired by [[ART - git version control]]
> ![[7Rq6xkBINP.png]]
> - The paper suggests GAM Changer instantiates a new class of [[PTN - interactive model editing]] tools.
> ![[BHR4HO5cBv.png]]

### Evidence of efficacy
Claude:
> **Case studies**
> - [[EVD - it was possible for a two physicians to use ART - GAM Changer to edit a GAM model for sepsis risk prediction to account for possible issues with temperature, respiratory rate, and systolic blood]]
>   - 7 continuous and 83 categorical features; shape functions are boosted trees; the model is fairly accurate overall (almost 90% AUC on the test set). The physician made the edits on a random subset of about 5k records (about 1/4 of the data).
> ![[edOrKqTgI3.png]]
> ![[bHbMMTyQus.png]]
>   - Temperature: edits to reduce potential false negatives; the shape function reveals these granular misalignments.
> ![[gx0Dmlv_-l.png]]
> ![[vwjd7TIXFC.png]]
>   - Respiratory rate (difference from age norm): the overall shape matched clinical knowledge, but there was no physiological explanation for a dip below -21, so it was smoothed with a monotonic increase (rather than linear interpolation) to keep a plateau that *does* have a physiological explanation.
> ![[JPuPLzpQFI.png]]
>   - Blood pressure: again, minimizing false negatives.
> ![[-MSe8IQQkp.png]]
> ![[pd5w5aZpYX.png]]
> - [[EVD - it was possible for a physician and ML researcher to use ART - GAM Changer to edit a GAM model for pneumonia risk prediction to account for possible issues with age and asthma predictors - @wang]]
>   - 19 continuous and 27 categorical features, again with high test-set AUC. The age feature was edited and the consequences for fairness by gender checked; the asthma feature was also edited.
> ![[yjUpP5AUi7.png]]
> ![[iSmboABr6t.png]]
> ![[3WbRvnSxxf.png]]
> - Joel Chan: "these are pretty neat examples: i actually have a hard time imagining how an ML engineer would accomplish the same results by editing the code for the models!"
>
> **Usability study** (7 data scientists; 8-minute tutorial, think-aloud use, then a semi-structured interview and usability survey, all within about an hour)
> ![[C5fRZjHLLX.png]]
> ![[t0IHIwWA2U.png]]
> - Usability survey: "The results suggest that the tool is easy to use (average 6.14), easy to understand (average 5.86), and especially enjoyable to use (average 7.00—all participants gave the highest rating). Most participants would like to use GAM Changer in their work to edit models" (p. 7).
> ![[nwFjxuOEnX.png]]
> - Semi-structured interview:
>   - [[EVD - data scientists self-reported model editing approaches that align with ART - GAM Changer's options - @wangInterpretabilityThenWhat2022]]
> ![[DpgezkzIIV.png]]
> ![[b01cJqfd4W.png]]
>   - [[EVD - data scientists envisioned using ART - GAM Changer to support conversations with diff stakeholders about model behaviors - @wangInterpretabilityThenWhat2022]]
> ![[W9GdtwZEJN.png]]
>   - [[EVD - some data scientists cautioned about the need for (stronger) guardrails on model edits when using interactive editing tools like ART - GAM Changer - @wangInterpretabilityThenWhat2022]]
> ![[13NnbAKazh.png]]
>
> **How much weight to put on this evidence** (Joel Chan, SP-25 seminar)
> - The case studies show only that it is *possible*: if a misalignment exists and the relevant domain experts are present and can recognize it, they can make the changes. They give no support for claims that the tool improves decisions or speeds them up.
> - The semi-structured interviews were the more useful part: data scientists already make these kinds of edits, in code, so the edits are reasonable things to do to a model.
> - Joel Chan said he largely ignored the usability survey scores: 7 people, about 30 minutes on Zoom, the researcher present, no comparison condition, not a real task, and high demand characteristics. He would prefer triangulation with more "objective" measures (time to completion, pupil dilation as an index of cognitive load) or log data and more examples of what people actually did with the tool.
> - Relevant baselines for a controlled comparison: (1) not editing the model at all, and (2) engineers editing it manually in code while going back and forth with clinicians or legal staff.

### Critiques and boundary conditions
Claude:
> - **Teams, not solo users.** In both case studies the physician and the ML research team were together on the call. Joel Chan noted that the difference between a monotonic increase and linear interpolation for respiratory rate seemed significant, and wondered whether the physician alone would have noticed it: "seems **super** important that the discussion was with physician *and* ML research team ... probably a requirement for usefulness in real-world settings." The study never tested a user with no engineering expertise working alone, and the seminar worried about the tool being sold as "any user can now edit your models." See [[CLM - ART - GAM Changer or PTN - Direct Manipulation-based approaches to steering models are best used in collaborative teams with domain experts - end users and ML engineers]].
> - **Which tasks does this fit?** S05 (🚧 Safety Inspection Expert) asked whether the system requires a supervised, prediction-based task with "well-understood features" that domain experts can align with their knowledge, and whether it could work for unsupervised models or language generation. S11: yes, it depends on [[PTN - Glass-box models]] like GLMs/GAMs. S15 doubted practicality: real-world models have high dimensionality, so can humans browse them to find the features that matter? Joel Chan: perhaps another tool, process, or person is needed to *identify* problematic (clusters of) features; this tool assumes you already have one.
> - **Higher-order consequences of edits.** Joel Chan wanted to see more about how overall model performance changed after edits, and raised [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]]. Checking fairness by gender after editing age is a start, but it is unclear how often such issues can be detected or fixed. The authors partly agree, claiming [[CLM - local edits to shape function of single features have minimal global impacts on generalized additive model performance]], which (if true) is another boundary condition on the approach.
> ![[E2HR8OiLex.png]]
> - **Harmful or biased edits.** S11 quoted the Discussion (section 6): continuous feedback and reversible edits "do not guarantee to prevent users from overfitting the model, injecting harmful bias, or maliciously manipulating model predictions," and asked how to minimize risk from well-intentioned but overconfident domain experts. S14 asked how we know clinicians' own "training data" (education, experience) is free of bias, and noted the extra time to edit, test, comment, and review creates pressure to skip these "responsibility" steps; S14 would have liked a study in real work settings. In discussion, the general theme was that the onus falls on the user, and the tool shows *interpretable* shape functions but gives no explanation or guidance on what is "correct". Joel Chan's view: guarding against bias probably needs social or process measures, not only technical ones, and "I would rather have a tool that makes us ask that question than a tool that feels objective that hides these things." Decisions such as accepting lower accuracy to avoid harming more untreated patients should not be made by the engineer alone or the domain expert alone.
> - **Retrain or edit?** S01 echoed participant P2 ("it was more 'objective' to retrain the model until it learned expected patterns rather than manually modifying the model") and asked how to balance data-driven insight from the pure GAM against expert judgment. In discussion, Joel Chan separated noticing a discrepancy between prior knowledge and the training data (which the tool supports) from deciding what to do about it (retrain, collect more data, or edit), which is arguably out of the tool's scope. Also noted: GAM contributions are correlational, not causal.
> - **Interpretability of the edits themselves.** S01: "GAM CHANGER strives to act on the interpretability and my concern is how about the interpretability on the actions performed?" What happens to the underlying function when you align or monotonize a segment? In discussion, people suggested hover help to build first-time trust, and showing technical experts *why* the model changed. Joel Chan linked this to a general trade-off with direct manipulation interfaces: experts move between intuitive drag-and-drop and fine-grained control (e.g., moving from a drag-and-drop figure to ggplot), so lowering the barrier should still leave a path to fine control.
> - **Disagreement among experts.** One participant suggested keeping a portfolio of models rather than one consensus model, so a dissenting expert's version could be tested against the consensus. Joel Chan: the tool isn't designed for that (one could imagine branching or forking models, git-style), but it might give a dissenter "more ammunition": showing the model's consequences instead of only talking.
> - **Design space.** S01 (Other/misc) asked how the authors decided the boundaries of the edit types, and when to stop adding edit types in research-through-design.
> - **Novelty.** Joel Chan found the claim to be the first interactive model editing tool dubious: [[PTN - interactive topic modeling]] has existed since at least 2015 (e.g., https://ceur-ws.org/Vol-2327/IUI19WS-ExSS2019-2.pdf), and so has interactive machine learning with [[PTN - cooperative contextual bandits]] in [[@kochMayAIDesign2019]].

### Connections and open questions
Claude:
> - Joel Chan (🍜 Academic Researcher): how could a tool like this change the quality of conversations between domain experts and ML experts by acting as a (better?) [[PTN - boundary object(s)]]? Reminds him of [[@caiOnboardingMaterialsCrossfunctional2021]].
> - S11 (🕸️ Connector) linked research on human–AI complementarity (https://www.nature.com/articles/s41562-024-02024-1) and asked how editing strategies or guidelines should change if the AI or the human is a complete novice. Joel Chan: the models here are already good (~90% AUC), so if they beat humans one might predict human–AI collaboration would do worse than the model alone with, say, medical students. He is skeptical of such general trends in isolation, expecting large heterogeneity by model type and interface, and pointed to a counterexample: [[EVD - human teams found 0.7 more major errors per team than ChatGPT-assisted teams and 1.1 more major errors than ChatGPT-led teams when reproducing results from behavioral science papers - @brodeurCo]].
> - S14 (🏺 Archaeologist) followed the paper to the idea of inductive bias and found "How Interpretable and Trustworthy are GAMs?" (Chang et al., 2021; https://dl.acm.org/doi/pdf/10.1145/3447548.3467453) helpful for seeing why this work is needed.
> - S01 connected the paper to [[PTN - Actionable explainability]] with direct manipulation: if explainability is extended to let users customize models, responsible and accountable change should be supported. Reversible edits undo damage, but some monitoring mechanism to detect harmful edits is also needed, e.g., an LLM judge with a constitution to safeguard model integrity.
> - Joel Chan later cited the sepsis case study as a step toward more in-the-wild deployments, when thinking about how different components might work together in larger compositions.
