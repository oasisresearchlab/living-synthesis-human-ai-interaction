---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-661f-7893-9ba2-de382722ef7b
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/ezIXBDrMR
roamAuthor: "Joel Chan"
created: 2024-01-24
---

Claude:
> - Citation: Lipton, Z. C. (2017). The Mythos of Model Interpretability (arXiv:1606.03490). arXiv. http://arxiv.org/abs/1606.03490

## Discussion notes
Claude:
> **Framing.** Read in Week 6 of SP-24 (February 28th, 2024). Joel Chan was struck by the framing of the question as "what is (x)?", a view from nowhere. He agreed with S13 that Lipton takes a realist or Platonic view of concepts, and preferred a constructivist or pragmatic framing: "how can we conceptualize (x)?", "how do (who) conceptualize (x) in (context) for (what purpose)?", "what do we gain by framing (x) as y?" (Joel Chan and S13, SP-24)
> > "Many papers propose interpretability as a means to engender trust (Kim, 2015; Ridgeway et al., 1998). But what is trust? Does it refer to faith in a model’s performance (Ribeiro et al., 2016), robustness, or to some other property of the decisions it makes? Does interpretability simply mean a low-level mechanistic understanding of our models? If so does it apply to the features, parameters, models, or training algorithms?" (p. 2)
> - The paper is motivated by "the oft-made claim that linear models are preferable to deep neural networks on account of their interpretability (Lou et al., 2012)" (p. 1), and argues against [[CLM - linear models are inherently more interpretable than deep neural network models]]. This focus on linear models complements S11's worries about the linear assumptions in the [[PTN - Concept Activation Vectors (CAVs)]] implementation in [[@caiHumanCenteredToolsCoping2019]]. (Joel Chan, notes)

Claude:
> **Desiderata** (dimensions of interpretability: what researchers actually want when they say they want interpretability). (Joel Chan, notes)
> > "the very desire for an interpretation suggests that in some scenarios, predictions alone and metrics calculated on these predictions do not suffice to characterize the model (Figure 1). We should then ask, what are these other desiderata and under what circumstances are they sought?" (p. 2)
> > "interpretations serve those objectives that we deem important but struggle to model formally." (p. 2)
> - **Trust**: supporting appropriate estimates of trust in the model. "What is trust? Is it simply confidence that a model will perform well? ... Trust might also be defined subjectively ... Alternatively, when the training and deployment objectives diverge, trust might denote confidence that the model will perform well with respect to the real objectives and scenarios." (p. 3)
> - **Causality**: enabling justified inferences, since researchers often use supervised models "in the hope of inferring properties or generating hypotheses about the natural world."
> - **Transferability**: enabling accurate predictions about generalization, which needs to be more informative than the training-test performance gap (edge cases, adversarial situations, etc.). "humans exhibit a far richer capacity to generalize, transferring learned skills to unfamiliar situations." (p. 3)
> - **Informativeness**: "the supervised model is used instead to provide information to human decision makers ... While the machine learning objective might be to reduce error, the real-world purpose is to provide useful information." (p. 4) Joel Chan reads this as a more general version of the informativeness built into the other desiderata (information relevant to judging trust, inferring causality, predicting transferability).
> - **Fair and ethical decision-making**: enabling assessment or contestation of violations of standards. The EU's proposed "right to explanation" means explanations "must (i) present clear reasoning based on falsifiable propositions and (ii) offer some natural way of contesting these propositions and modifying the decisions appropriately if they are falsified." (p. 4)

Claude:
> **Properties of interpretability** (aka interpretability design patterns). (Joel Chan, notes)
> - Transparency: [[PTN - simulatability]] (one can contemplate the entire model), [[PTN - decomposability]] (one can understand how individual components work), [[PTN - algorithmic transparency]].
> - [[PTN - post-hoc interpretability]]: [[PTN - text explanations]], [[PTN - visualization]], [[PTN - local explanations]], [[PTN - explanation by example]], and contrastive explanations.
> - Systems seen so far, to analyze with this taxonomy: [[ART - ImageSense]], [[ART - SMILY]], [[ART - Graphologue]], [[ART - Wrangler]], [[ART - Predictive Translation Memory (PTM)]]. For example, what desiderata are targeted by the CAVs in SMILY, or by the slider in ImageSense? Is anything missing? (Joel Chan, 🕸️ Connector, SP-24)

Claude:
> **Connections in later sessions.** (SP-24 seminar)
> - [[PTN - Automated Rationale Generation]] is an instance of post-hoc interpretability. (Joel Chan, 🕸️ Connector)
> - Algorithmic transparency and opacity in a later reading connect back to Lipton's [[PTN - algorithmic transparency]]. (S05, 🕸️ Connector)
> - A later reading's point linked back to the properties of interpretability: "Selbst and Barocas argue that 'one must seek explanations of the process behind a model's development, not just explanations of the model itself'" (p. 5 of that reading). (Joel Chan, responding to S13)
