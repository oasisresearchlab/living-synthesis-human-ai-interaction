---
nodeTypeId: node_Gp7JMdrzm9DUuPfBzUptc
nodeInstanceId: 01a20e70-661c-7362-9311-bd2ffa3d4a05
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/EFaPe2yM5
roamAuthor: "Joel Chan"
created: 2025-03-24
---

## Context
Claude:
> - Left open by an SP-25 reading on steering LLMs with policies: how do we know we have the right policies? This is tricky, and is sometimes called the "backward pass". (SP-25 seminar, 👩🏽‍🔬 Distiller thread on the key question/problem)
> ![[aXEqzqg2um.png]]
> - Key claim from the discussion: users need cases, lots of them, explored systematically and in conversation with concepts and principles. (SP-25 seminar)
> - Motivation comes from a prior finding in [[@shankarWhoValidatesValidators2024]], which proposes [[ART - EvalGen]], a system that helps users generate, implement, and validate evaluation criteria. A qualitative study with 9 practitioners revealed "criteria drift": users need criteria to grade outputs, but grading outputs helps users define criteria. So evals depend on seeing LLM output, rather than being definable a priori. (seminar participant note, SP-25)
>   - Joel Chan: this result is "kinda obvious a priori" from [[THE - Sensemaking Theory]], but good to have domain-specific validation. (Joel Chan, SP-25 seminar)
> - Feels similar to [[ART - DreamSheets]] and [[ART - ChainForge]] in its focus on making sense of your policies/prompts in conversation with cases. (SP-25 seminar)
> - In theory it also targets an open problem we saw with [[ART - ConstitutionMaker]] (explicitly cited in the reading): no support for reasoning about interactions between principles. See also [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]]. (SP-25 seminar)
> ![[q-sl_43qs5.png]]

## Other Notes
Claude:
> - Related: [[QUE - What metrics-framework should be used to evaluate LLM policy effectiveness (technical implementability, interpretability, alignment, etc.)?]], raised by S16 in the same session. (SP-25 seminar)
