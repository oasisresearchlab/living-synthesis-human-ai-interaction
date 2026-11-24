---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e70-661e-7ae8-b598-9dc2c04f3d81
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/o7vLz7ant
roamAuthor: "Joel Chan"
created: 2025-03-24
---

## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> Supports AI policy designers in mapping and iterating on policies for LLM behavior: "Our mapmaking approach grants policy designers a global view of policy to understand how a large set of policies and cases interact and provides nuanced control with concepts to iterate and resolve conflicts in policy" (Lam et al., 2024, p. 4; [[@lamAIPolicyProjector2024]]).
> - S01 (SP-25, Group 1) framed it as support for open-ended exploration of a "solution space": like [[ART - DreamSheets]], it visualizes the mapping between inputs and the space of possible outputs to help users understand utility and encourage further exploration. The paper's claim: "map visualization provides a holistic overview of the concepts and policies, which supports users in surveying the terrain of possible model behaviors and iterating on policy designs."
> ![[fQAvl0A9ex.png]]
> ![[0E7K4Wt1yp.png]]

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> The secret sauce is enabling natural-language definitions of "concepts" that can be used to group and steer model outputs (SP-25 Distiller notes, Week 7, March 12th, 2025). The associated claim: [[CLM - LLM-generated and custom-defined natural language concepts --- with mappings to example LLM outputs that contain those concepts --- support interpretable exploration of LLM output patterns]].
> ![[EtjH7jJAwt.png]]
> ![[cQU2qxt_sz.png]]
> - Policies take an if-then form. S16 pointed to participant quotes showing this formulation is structured and clear for formalizing the task: [[EVD - AI policy practitioners found if-then statements in ART - AI Policy Projector to support transparent and interpretable LLM policy formulation - @lamAIPolicyProjector2024]].
> ![[ax41K-UA7S.png]]
> - System screenshots:
> ![[-ThVdAGMsg.png]]
> ![[R3KU6TB0RJ.png]]
> ![[RSyPDE2Lp1.png]]
> ![[Sqb27SIU1n.png]]
> ![[DOS0nsyxuR.png]]
> - Connections (SP-25 seminar notes): look ahead to [[PTN - Sparse Autoencoders (SAEs)]], and back to [[PTN - Concept Activation Vectors (CAVs)]] from the SP-24 seminar.

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

## Other Notes

Claude:
> **Limitations and desired extensions**
> - Joel Chan's observations on Section 6: [[EVD - AI policy practitioners who used an initial prototype of ART - AI Policy Projector expressed a desire for more expressivity in definitions of policies, such as OR operators, and additional steer]]: OR operators, more than concepts for the if clause, and more than WARN / SUPPRESS for steering.
> - S01 (SP-25) raised two challenges for map-style exploration: visualization is limited to at most 3D while natural language lives in high-dimensional embeddings (see [[CLM - UMAP 2D projections do not produce meaningful global spatial separation]]); and if the operators used to explore the space don't produce consistent outputs, the map is less useful because users may want to reproduce outputs they liked.
> - In a later SP-25 session (🕸️ Connector), the steering available here was compared to SAE-based steering, e.g., Linus Lee's UX explorations (https://thesephist.com/posts/prism/#future-work, https://thesephist.com/posts/synth/).
> ![[WE_u50N8hL.png]]
> ![[AS05PfuV7g.png]]
>
> **Governance**
> - S14 (🏺 Archaeologist) highlighted the interdependence of AI governance and human interaction, and suggested graduates may need policy development and concept-mapping skills as tools like this become governance mechanisms: [[QUE - How might visual sensemaking LLM policy tools like ART - AI Policy Projector integrate into broader governance processes?]]
> - Joel Chan: it is dangerous to have CS-oriented folks design and execute policy without learning from the mess and wisdom of governance more broadly. S05 noted that law and governance terms (constitution, policy, case law) are borrowed in AI, and asked what other governance principles could serve as metaphors or models. S14 asked whether the relatively homogeneous group of AI practitioners in the study brought diversity of thought, and how including practitioners from education, healthcare, or public policy might shape tools like this. Joel Chan pointed to [Interpreting the Rule(s) of Code: Performance, Performativity, and Production](https://law.mit.edu/pub/interpretingtherulesofcode/release/4).
>
> **Categorization**
> - S05 grouped it with ConstitutionMaker as tools offering "cognitive (or thinking?) resources" to examine LLM behavior and formulate rules or principles, as distinct from the "technical resources" of [[ART - GAM Changer]] (see [[PTN - LLM Chains]], [[ART - ChainForge]]).
