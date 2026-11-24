---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-661f-72c1-8580-6e828644a4f2
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/5kMrOZWoA
roamAuthor: "Joel Chan"
created: 2025-01-23
---

- Citation: Durmus, E., Tamkin, A., Clark, J., Wei, J., Marcus, J., Batson, J., Handa, K., Lovitt, L., Tong, M., McCain, M., Rausch, O., Huang, S., Bowman, S., Ritchie, S., Henighan, T., & Ganguli, D. (2024, October 25). __Evaluating feature steering: A case study in mitigating social biases__.
- URL: https://anthropic.com/research/evaluating-feature-steering

## Discussion notes
Claude:
> **Where it sat.** Week 10 (April 2nd, 2025) of the SP-25 seminar.
>
> **Key question/problem.**
> ![[VGwBBzjxsu.png]]
> ![[6m0KDitPMk.png]]

Claude:
> **Artifact and secret sauce.**
> - [[PTN - Sparse Autoencoders (SAEs)]]: train a separate model that "compresses" the original giant network in the LLM, such that individual "neurons" in the new model are "monosemantic" and correspond to human-interpretable features (which still need labels). (Joel Chan, SP-25)
> - [[PTN - feature steering]]: "First, we use a technique called dictionary learning, which identifies a large number of interpretable directions – the features – in the residual stream of a model. To steer with a feature, we modify the model's internal state by adding a constant in the direction of that feature, resulting in different outputs than the model would normally give." It works like a "dial".
> ![[jDny9FvRC9.png]]
> - Technically, steering decomposes the residual stream activity into the SAE reconstruction plus a reconstruction error, clamps one SAE feature to a specific value, and runs the forward pass with the modified activity for every input and token position (from Anthropic's "Scaling Monosemanticity" appendix: https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html#appendix-methods-steering). S01 (🤔 ELI5 linter) pointed to this and to "Towards Monosemanticity" (https://transformer-circuits.pub/2023/monosemantic-features) as explainers.
> ![[7GIiuKSEbF.png]]
> ![[yVyPEdl1gO.png]]

Claude:
> **Evidence from the social bias evaluation.**
> ![[f7NQPZ1Wf-.png]]
> - *On-target effects:* steering a feature expected to increase or reduce a target successfully moved that target, in proportion to the steering factor.
> ![[Ja5Pz73HHr.png]]
> ![[sUF1K4bUqk.png]]
> ![[c-fwAiq1rz.png]]
> - *Off-target effects:* steering a gender-bias feature also steered age bias.
> ![[ZZtfjI83-c.png]]
> ![[hLLDv2qDDj.png]]
> - *Multifaceted effects:* some features (e.g., neutrality) reduced a variety of undesirable biases at once.
> ![[QMoNf5_Qf-.png]]
> - *Steering/performance tradeoff:* steering too much degrades model performance. See [[QUE - What are the tradeoffs between LLM alignment and performance?]]
> ![[eDxhwvhSaO.png]]

Claude:
> **Critiques and open questions.**
> - *Higher-order interactions.* The off-target results suggest we need more than individual feature steering: there are complex higher-order interactions, even between monosemantic features. See [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]] (Joel Chan, SP-25)
> ![[pUrxUAIxba.png]]
> - *Circuits.* S11 (🍜 Academic Researcher) highlighted the paper's limitation that "individual features do not operate in isolation" and that effective steering may need understanding of circuits. S11 noted that real-world concepts are entangled too: text with gender bias likely carries other biases, so clamping one feature will inevitably shift others. S11 wondered how circuits would be modeled, since the number of feature interactions could be computationally prohibitive. (S11, SP-25)
> - *Who gets to steer?* S01 asked whether feature steering will be opened to general users, and how much control can be given without breaching safety safeguards; letting users steer features could invite attacks that tamper with feature clamping requests. (S01, SP-25)
> - *Compared with prompting and other UIs.* It's worth comparing this steering to what [[ART - AI Policy Projector]] offered, and to [[PTN - prompt engineering]]: changing prompts may be easier for end users, but its reliability is unclear, and the effects may be comparable.
> ![[WE_u50N8hL.png]]
> - *Outside data.* A 🚧 Safety Inspection Expert asked whether search history from other platforms could affect Claude's output, as with Google or Facebook. Joel Chan: it shouldn't unless it gets into the prompt/context; long contexts are expensive, so providers are unlikely to do this for everyone in the background, though people do pay for tools that put more of their info in context (e.g., Cursor for code).
> - *Industry vs. academic research* was raised as a meta point.

Claude:
> **Connections.**
> - S11 (🏺 Archaeologist) noted that steering remains "preparadigmatic", and that NLP has proposed many other interventions besides SAE dictionary learning (see [[PTN - Sparse Autoencoders (SAEs)]] for the links).
> - [[@obrienSteeringLanguageModel2024]] (Steering Language Model Refusal with Sparse Autoencoders) as related work. (🕸️ Connector, SP-25)
> - Linus Lee's UX experiments with SAEs: https://thesephist.com/posts/prism/#future-work and https://thesephist.com/posts/synth/
> ![[AS05PfuV7g.png]]
> - Anthropic's announcement thread as an entry point into public discussion: https://x.com/AnthropicAI/status/1849840131412296039
