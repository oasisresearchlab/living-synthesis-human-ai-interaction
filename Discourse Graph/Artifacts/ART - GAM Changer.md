---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e70-661e-7690-bd13-37174bc9465c
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/KmZ9zbTKb
roamAuthor: "Joel Chan"
created: 2025-02-04
---
## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> To empower users, especially domain experts without ML or software engineering expertise, to audit *and edit* [[PTN - Generalized Additive Models (GAMS)]]. It addresses [[QUE - How might we empower users to act on model interpretations when they lack expertise in ML and software engineering?]] (SP-25 Week 2, February 5th, 2025, on Wang et al.).
> - What are GAMs? Very similar to generalized linear models; the main difference is that instead of a weight for each predictor, each predictor has a "shape function" that can be a variety of functions other than simple multiplication. They belong to the class of [[PTN - Glass-box models]].
> ![[YPjU_eux-7.png]]

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> Live demo: https://interpret.ml/gam-changer
> ![[XzgMk4QHXR.png]]

Claude:
> Key design patterns (SP-25 Week 2 discussion):
> - **[[PTN - Shared Representation]]** (not named in the paper): the shape functions are probably far superior to a table. They make it easy to spot misalignments at a granular level, and to edit the model directly.
> - **[[PTN - Direct Manipulation]]**, to help with the basic mechanics of editing the model for users without ML or software engineering expertise: you edit the model by directly editing a shape function, scaffolded by preset "modification types" such as align and interpolate.
> ![[omkpng_BTY.png]]
> - **Continuous feedback**, to help users reason about potential unintended negative consequences of edits: e.g., "link + reorder" to see correlated features.
> ![[JO6PA2aLPZ.png]]
> - **Reversible actions**, inspired by [[ART - git version control]]. The SP-25 Week 9 Group 1 synthesis called out the "nice use of commit logs to enable reverting, auditing by people with relevant knowledge."
> ![[7Rq6xkBINP.png]]
> - The paper suggests GAM Changer instantiates a (new) class of [[PTN - interactive model editing]] tools.
> ![[BHR4HO5cBv.png]]

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

Claude:
> **Sepsis risk prediction**: [[EVD - it was possible for a two physicians to use ART - GAM Changer to edit a GAM model for sepsis risk prediction to account for possible issues with temperature, respiratory rate, and systolic blood]]
> - The model has 7 continuous and 83(!) categorical features; its shape functions are boosted trees, and it is fairly accurate (almost 90% AUC on the test set).
> ![[edOrKqTgI3.png]]
> ![[bHbMMTyQus.png]]
> - A physician made the edits based on a random subset of 5k records (about a quarter of the data).
> - Temperature: edits to reduce potential false negatives; the shape function revealed granular misalignments in the curve. The physician noted how important it is to weed out false positives in high-stakes clinical settings like this.
> ![[gx0Dmlv_-l.png]]
> ![[vwjd7TIXFC.png]]
> - Respiratory rate (difference from age norm): the overall distribution matched clinical knowledge, but there was no physiological explanation for a dip below -21. Rather than smoothing it out, they used a monotonic increase (changing the shape function entirely) to keep a plateau that does have a physiological explanation.
> ![[JPuPLzpQFI.png]]
> - Blood pressure: again with an eye to minimizing the false negative rate.
> ![[-MSe8IQQkp.png]]
> ![[pd5w5aZpYX.png]]

Claude:
> **Pneumonia risk prediction**: [[EVD - it was possible for a physician and ML researcher to use ART - GAM Changer to edit a GAM model for pneumonia risk prediction to account for possible issues with age and asthma predictors - @wang]]
> - 19 continuous and 27 categorical features; again fairly high model performance (AUC on the test set).
> - Edits to the age feature, then checking the consequences for the overall model's fairness by gender:
> ![[yjUpP5AUi7.png]]
> ![[iSmboABr6t.png]]
> - Edits to the asthma feature:
> ![[3WbRvnSxxf.png]]

Claude:
> **Interviews with data scientists** (usability study, semi-structured interviews):
> - [[EVD - data scientists self-reported model editing approaches that align with ART - GAM Changer's options - @wangInterpretabilityThenWhat2022]]
> ![[DpgezkzIIV.png]]
> ![[b01cJqfd4W.png]]
> - [[EVD - data scientists envisioned using ART - GAM Changer to support conversations with diff stakeholders about model behaviors - @wangInterpretabilityThenWhat2022]]
> ![[W9GdtwZEJN.png]]
> - [[EVD - some data scientists cautioned about the need for (stronger) guardrails on model edits when using interactive editing tools like ART - GAM Changer - @wangInterpretabilityThenWhat2022]]
> ![[13NnbAKazh.png]]

## Other Notes
Claude:
> **Who should use it?** [[CLM - ART - GAM Changer or PTN - Direct Manipulation-based approaches to steering models are best used in collaborative teams with domain experts - end users and ML engineers]]. Joel Chan, on the respiratory-rate edit: the difference between the consequences of a monotonic increase vs. linear interpolation "seems super significant, but i wonder if the physician alone would have noticed it: seems **super** important that the discussion was with physician *and* ML research team (from the authors)! probably a requirement for usefulness in real-world settings."

Claude:
> **Hypotheses from the SP-25 Week 2 discussion** (Joel Chan's notes):
> - A benefit of a direct manipulation tool like GAM Changer is to elicit noticing and discussion of fine-grained discrepancies between the model's learned patterns and domain knowledge.
> - Direct manipulation tools like GAM Changer increase user agency.
> - We can increase the trust and usefulness of such tools by providing more direct and granular explanations of model edits that technical experts can understand and edit.
> - Observation: we can actually run GAM Changer ourselves, so we know its functionality is real; this increases confidence in the findings.

Claude:
> **Resources for agency** (S05, SP-25 Week 9 synthesis): GAM Changer affords "**technical resources**" through [[PTN - Shared Representation]] and [[PTN - Direct Manipulation]] to monitor and adjust model behavior directly. Open question: when people without technical expertise get such resources, is their use of them reasonable, and should we limit how much non-experts can access? S05 contrasted this with the "cognitive resources" of [[PTN - LLM Chains]] and [[ART - ChainForge]], and suggested that GAM Changer and LLM chains may also offer "**task resources**" for human task planning and collaboration.

Claude:
> **Other notes.**
> - S09 (🤔 ELI5 linter, SP-25) explained GAM Changer as a tool that helps non-engineers like doctors modify their ML models so the results are accurate, by analogy to retraining a puppy that was trained in a language you don't speak, using hand gestures you both understand.
> - [[ART - ChainForge]] is not as clear an example of [[PTN - Direct Manipulation]] as GAM Changer (Joel Chan, SP-25 Week 4 key insights).
> - The sepsis case study was named in the SP-25 Week 15 synthesis as the kind of in-the-wild deployment the seminar wanted to see more of.
