---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e70-661e-7155-a090-9e7f69a28198
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/V_jy7V9xf
roamAuthor: "Joel Chan"
created: 2025-02-18
---
## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> - To systematically explore and evaluate hypotheses about LLM behavior (SP-25 discussion).
> - In S05's terms (SP-25 Week 9 synthesis), ChainForge and [[PTN - LLM Chains]] offer **cognitive (or thinking) resources** rather than direct technical control of a glass-box model, as in [[ART - GAM Changer]]: they let people examine LLM behavior against multiple changing prompt parameters and formulate rules or principles for model behavior. S05 put ConstitutionMaker and [[ART - AI Policy Projector]] in the same category.
> - Claim: [[CLM - tools like ART - ChainForge can impact users of LLMs by empowering developers to design better LLM-powered systems]]

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> Project site: https://www.chainforge.ai/
> ![[ghPztSpO8Q.png]]

Claude:
> Points from Joel Chan's key insights for synthesis (SP-25 Week 4, Arawjo et al.):
> - ChainForge is not a clear example of [[PTN - Direct Manipulation]], compared to [[ART - GAM Changer]].
> - ChainForge cannot really help edit the underlying data.

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

Claude:
> - [[EVD - data scientists successfully used ART - ChainForge to do systematic testing of their LLM pipelines - @arawjoChainForgeVisualToolkit2024]]; named again in the SP-25 Week 15 synthesis as the kind of in-the-wild deployment the seminar wanted to see more of.
> - But: [[EVD - users --- including those with prior proramming experience --- infrequently transitioned to systematic testing with ART - ChainForge - @arawjoChainForgeVisualToolkit2024]]

## Other Notes
Claude:
> **Who can benefit?** The SP-25 discussion floated a claim (not yet a node): maybe scientific literacy is necessary for people to benefit from tools like ChainForge to systematically explore and evaluate hypotheses about LLMs. Grounds offered:
> - [[EVD - phd student reading ChainForge paper found it difficult to formalize intuitive sense on different dimensions when comparing into metrics that can be studied systematically]]
> - [[EVD - users --- including those with prior proramming experience --- infrequently transitioned to systematic testing with ART - ChainForge - @arawjoChainForgeVisualToolkit2024]]
>
> This led to [[QUE - how do we enable people with less scientific literacy to benefit from systematic tools like ART - ChainForge?]], which came back in the Week 15 synthesis as part of wanting tools that work for "the rest of us" (people without a technical or programming background, and not used to thinking like a scientist). Related: [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]]

Claude:
> **Used as a benchmark for later readings (SP-25).**
> - A later system's support for testing principles was judged "not well-supported relative to" ChainForge or [[PTN - LLM Chains]]. Joel Chan saw a missed opportunity to reflect on such UIs, which that paper cites ([[@wuAIChainsTransparent2022]]) only in passing in related work.
> - A comparison-based system motivated by [[THE - Sensemaking Theory]] was described as "like ChainForge, but turned up to 100000 on the comparison/sensemaking dimension."
> - The system behind [[QUE - how can we support users to reason about whether they have the right policies when steering LLMs with policy?]] "feels similar to [[ART - DreamSheets]] and ChainForge in its focus on making sense of your policies/prompts and in convo with cases."
> - [[ART - Patchview]] ([[@chungPatchviewLLMpoweredWorldbuilding2024]]) differs subtly from DreamSheets and ChainForge: its target of sensemaking is the generated world, not necessarily the model.
