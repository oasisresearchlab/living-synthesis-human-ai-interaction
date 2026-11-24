---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-661f-718b-9b66-1f5843ce7bb7
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/0c2uCr0M0
roamAuthor: "Joel Chan"
created: 2025-01-15
---

- Title: Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences
- Author(s):: Shreya Shankar, J.D. Zamfirescu-Pereira, Bjoern Hartmann, Aditya Parameswaran, Ian Arawjo
- Abstract: Due to the cumbersome nature of human evaluation and limitations of code-based evaluation, Large Language Models (LLMs) are increasingly being used to assist humans in evaluating LLM outputs. Yet LLM-generated evaluators simply inherit all the problems of the LLMs they evaluate, requiring further human validation. We present a mixed-initiative approach to “validate the validators”—aligning LLM-generated evaluation functions (be it prompts or code) with human requirements. Our interface, EvalGen, provides automated assistance to users in generating evaluation criteria and implementing assertions. While generating candidate implementations (Python functions, LLM grader prompts), EvalGen asks humans to grade a subset of LLM outputs; this feedback is used to select implementations that better align with user grades. A qualitative study finds overall support for EvalGen but underscores the subjectivity and iterative nature of alignment. In particular, we identify a phenomenon we dub criteria drift: users need criteria to grade outputs, but grading outputs helps users define criteria. What is more, some criteria appear dependent on the specific LLM outputs observed (rather than independent and definable a priori), raising serious questions for approaches that assume the independence of evaluation from observation of model outputs. We present our interface and implementation details, a comparison of our algorithm with a baseline approach, and implications for the design of future LLM evaluation assistants.
- Type: Conference paper
- Publication: 
- URL : https://dl.acm.org/doi/10.1145/3654777.3676450
- Date Added: October 14th, 2024
- Zotero links: [Local library](zotero://select/groups/2451508/items/LQ7DI28F), [Web library](https://www.zotero.org/groups/2451508/items/LQ7DI28F)
- PDF links : [Shankar et al_2024_Who Validates the Validators.pdf](zotero://open-pdf/groups/2451508/items/4558S6MU)

## Discussion notes
Claude:
> **What it proposes.** [[ART - EvalGen]], a system that helps users generate, implement, and validate evaluation criteria for LLM outputs. Listed on the reading list under "Design examples" (published at UIST 2024).

Claude:
> **Key finding: criteria drift.** A qualitative study with 9 practitioners found that users need criteria to grade outputs, but grading outputs helps users define criteria. So evaluations may depend on the LLM outputs observed, rather than being definable a priori.
> - In SP-25 this finding was cited as motivation for [[QUE - how can we support users to reason about whether they have the right policies when steering LLMs with policy?]] (the "backward pass" left open by that week's reading), under the key claim that users need cases, lots of them, examined systematically and in conversation with concepts and principles.
> - A seminar comment noted that the result "is kinda obvious a priori from [[THE - Sensemaking Theory]], but good to have domain-specific validation."
