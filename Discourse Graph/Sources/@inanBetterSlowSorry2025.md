---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-6620-7903-bef9-fa160675017e
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/u1CMImgH3
roamAuthor: "Joel Chan"
created: 2025-03-12
---

- Title: Better Slow than Sorry: Introducing Positive Friction for Reliable Dialogue Systems
- Author(s):: Mert İnan, Anthony Sicilia, Suvodip Dey, Vardhan Dongre, Tejas Srinivasan, Jesse Thomason, Gökhan Tür, Dilek Hakkani-Tür, Malihe Alikhani
- Abstract: While theories of discourse and cognitive science have long recognized the value of unhurried pacing, recent dialogue research tends to minimize friction in conversational systems. Yet, frictionless dialogue risks fostering uncritical reliance on AI outputs, which can obscure implicit assumptions and lead to unintended consequences. To meet this challenge, we propose integrating positive friction into conversational AI, which promotes user reflection on goals, critical thinking on system response, and subsequent re-conditioning of AI systems. We hypothesize systems can improve goal alignment, modeling of user mental states, and task success by deliberately slowing down conversations in strategic moments to ask questions, reveal assumptions, or pause. We present an ontology of positive friction and collect expert human annotations on multi-domain and embodied goal-oriented corpora. Experiments on these corpora, along with simulated interactions using state-of-the-art systems, suggest incorporating friction not only fosters accountable decision-making, but also enhances machine understanding of user beliefs and goals, and increases task success rates.
- Type: Preprint
- Publication: 
- URL : http://arxiv.org/abs/2501.17348
- Date Added: February 28th, 2025
- Zotero links: [Local library](zotero://select/groups/2451508/items/N3SULDB4), [Web library](https://www.zotero.org/groups/2451508/items/N3SULDB4)
- Tags: Computer Science - Computation and Language Computer Science - Human-Computer Interaction
- PDF links : [İnan et al_2025_Better Slow than Sorry.pdf](zotero://open-pdf/groups/2451508/items/C8GRX2ZB)

## Discussion notes
Claude:
> **Where it sat.** Week 14 (April 30th, 2025), the last reading of the SP-25 seminar.
>
> **Key question/problem.** How to align LLM dialogue systems with users' (potentially hidden) conversational expectations, goals, and assumptions, i.e., how to let dialogue systems build [[PTN - common ground]] with the people they talk to. The Distiller thread also asked how much of a problem this is for LLM-based systems, and pointed to sycophancy (https://www.seangoedecke.com/ai-sycophancy/). (Joel Chan, SP-25)

Claude:
> **The proposal: an ontology of positive friction.** The class compared the paper's Table 1 typology to prior typologies.
> ![[-a1_xktn6N.png]]
> ![[PcLTeyun33.png]]
> - S05 (🏺 Archaeologist) pointed to Stolcke et al. (2000), "Dialogue act modeling for automatic tagging and recognition of conversational speech" (https://www.aclweb.org/anthology/J00-3003.pdf), and its Switchboard Dialog Act Corpus (https://convokit.cornell.edu/documentation/switchboard.html), which links to other corpora of human conversation. (S05, SP-25)
> ![[IqGtncpNbL.png]]
> - S05 also pointed to Clark and Wilkes-Gibbs (1986), "Referring as a collaborative process", on how a speaker makes an initial noun phrase and the moves that follow to initiate or complete a conversational repair (see [[THE - conversational repair]]). S05 expected the authors to cite this paper rather than a later, shorter one, and highly recommended it. Its **Tangram matching task**, widely reused in studies of computer-mediated communication, could be adapted to study human-agent conversation. (S05, SP-25)
> ![[M0F1SB8DZE.png]]
> ![[p3yfBdPyBv.png]]
> ![[mGYV3Yhyun.png]]
> - ELI5 framings: S01 linked System 1 (fast, automatic) vs. System 2 (slow, effortful) thinking (https://thedecisionlab.com/reference-guide/philosophy/system-1-and-system-2-thinking). S14 summarized: the researchers thought LLMs were missing human conversation behaviors like pauses, speed, and restating ("positive frictions"), added them, and found the output was better. (S01, S14, SP-25)
> - Datasets used (👾 Hacker thread): [[ART - Multi-Domain Wizard-of-Oz dataset (MultiWOZ)]] (https://github.com/budzianowski/multiwoz), "a fully-labeled collection of human-human written conversations spanning over multiple domains and topics", about 10k dialogues; and [[ART - TEACh dataset]] (https://github.com/alexa/teach), "a dataset of human-human interactive dialogues to complete tasks in a simulated household environment".

Claude:
> **Evidence.**
> - Figure 3 shows positive friction is present in real human-human dialogues. Joel Chan: not news to linguists, but the typology and annotated dataset are still useful for NLP. The key claims are in Section 4.2.
> - How the satisfaction experiment works (Joel Chan's reading, answering S01's and S05's confusion): take a subset of MultiWOZ annotated for user satisfaction by human annotators in [[@sunSimulatingUserSatisfaction2021]] (40 annotators, rating each turn and each dialogue 1-5, Fleiss kappa ~0.574). Train a model to predict these scores. Then measure whether the model aligns better or worse with the human scores depending on whether a randomly sampled turn contains model-classified positive friction. The claim is that model predictions of user satisfaction got worse.
> ![[dczM0R1ZP-.png]]
> ![[-fSzq1526a.png]]
> ![[_RuBI8xO8Q.png]]

Claude:
> **Critiques of the methods.**
> - *NLP or HCI?* S05 (🚧 Safety Inspection Expert) was unsure whether the paper aims at concept testing or an empirical study of friction's effects, and had trouble accepting the "experimental setup" in Section 4.1: how can user satisfaction be measured algorithmically? (S05, SP-25)
> - *Simulated users.* S05 found it ironic that the paper cites linguistic, communication, and cognitive research on how humans achieve grounding, then uses algorithms to simulate "users": "How can conversations involving human be studied in this way??" Joel Chan shared the concern about strength of evidence, and noted that simulating human behavior is a live methods issue in HCI and the social sciences. He pointed to the CHI 2025 panel "Human Subjects Research in the Age of Generative AI" (https://dl.acm.org/doi/full/10.1145/3706599.3716299) and to John Horton's work ("Large language models as economic agents: what can we learn from homo silicus?", https://arxiv.org/abs/2301.07543; "Automated social science: Language models as scientist and subject"), which shows a lineage to agent-based modeling. In his view this is defensible as theorizing only if you are very clear that it differs from empirical observation of the real humans you want to say something about. (S05, Joel Chan, SP-25)
> ![[gkdkG6jt-z.png]]
> - *"Expert" annotators.* Joel Chan objected that the "expert" annotators were engineering students given a short lecture on the linguistics and cognitive science of positive friction, with kappa agreement of only ~0.4.
> ![[wAfFdRPQ9i.png]]
> ![[WglwwCgs53.png]]
> - *Venue.* S11 noted the paper was posted to arXiv before the ACL deadline and has not yet appeared in any *ACL proceedings, and agreed that it began "motivated by cogsci theories", implying a well-motivated human evaluation, then "devolved into a standard NLP paper with hacky evaluation practices." (S11, SP-25)
> - *Ecological validity.* S11 (🕸️ Connector) noted that MultiWOZ and ALFWorld are not natural human-human dialogue: MultiWOZ was built via crowdsourcing with pre-defined templates. Having undergraduates annotate friction in synthetic, rule-based conversations seems poorly motivated, and MultiWOZ being multi-domain doesn't support claims of generalization. (S11, SP-25)

Claude:
> **Connections and open questions.**
> - A related paper from UMD's CLIP lab (https://arxiv.org/pdf/2503.12370) studies Ubuntu chat logs, a more natural setting, and finds friction is more common in failed conversations than successful ones (Table 2). S11: this doesn't mean friction causes failure, but in more ecologically valid settings user needs differ and task difficulty shapes how friction arises. S11 also wondered how friction looks outside query-and-clarify conversations, where "success" is less defined. (S11, SP-25)
> ![[YV0kWx80Ds.png]]
> - Joel Chan connected friction to seamful design, slow search, and, further afield, epistemic action in distributed cognition (e.g., rotating Tetris pieces not to reach the goal directly but to build a mental model).
> - S05 linked this to Clark and Wilkes-Gibbs's "**minimizing collaborative effort**": the trade-off between a speaker crafting a perfect initial phrase and speaker and addressee repairing it together. Seen holistically, "friction" is really the agent *initiating collaborative effort* to coordinate meaning, akin to "other-initiated repair". But people may not see communication with a task-oriented agent as collaborative, so they may calibrate their effort differently than with humans. (S05, SP-25)
> ![[cg8XwzUseM.png]]
> - A participant asked how this differs from Alexa's clarification utterances ("Hmm, can you repeat that?"), noting Alexa supports custom slots in sample utterances. Another got Claude to mimic positive friction when asked. S11 noted that most LLM products already ask follow-up questions, which covers some kinds of friction; e.g., OpenAI's Deep Research asks clarifying questions about scope, much in the spirit of this paper. (SP-25)
> ![[mGizdrZSj-.png]]
> ![[HQeC179zMt.png]]
> ![[kiGJqb_zPW.png]]
