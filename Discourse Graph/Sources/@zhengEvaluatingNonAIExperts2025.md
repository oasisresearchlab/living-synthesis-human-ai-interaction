---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-6620-7139-a6e7-736bb23c99d4
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/zecDNX-iV
roamAuthor: "Joel Chan"
created: 2025-04-09
---

- Title: Evaluating Non-AI Experts' Interaction with AI: A Case Study In Library Context
- Author(s):: Qingxiao Zheng
- Abstract: Public libraries in the U.S. are increasingly facing labor shortages, tight budgets, and overworked staf, creating a pressing need for conversational agents to assist patrons. The democratization of generative AI has empowered public service professionals to develop AI agents by leveraging large language models. To understand the needs of non-AI library professionals in creating their own conversational agents, we conducted semi-structured interviews with library professionals (n=11) across the U.S. Insights from these interviews informed the design of AgentBuilder, a prototype tool that enables non-AI experts to create conversational agents without coding skills. We then conducted think-aloud sessions and followup interviews to evaluate the prototype experience and identify the key evaluation criteria emphasized by library professionals (n=12) when developing conversational agents. Our fndings highlight how these professionals perceive the prototype experience and reveal fve essential evaluation criteria: interpreting user intent, faithful paraphrasing, proper alignment with authoritative sources, tailoring the tone of voice, and handling unknown answers efectively. These insights provide valuable guidance for designing AI-supported "end-user creation tools" in public service domains beyond libraries.
- Type: Conference paper
- Date Added: April 8th, 2025
- Zotero links: [Local library](zotero://select/groups/2451508/items/D2ZI9DB5), [Web library](https://www.zotero.org/groups/2451508/items/D2ZI9DB5)
- PDF links : [Zheng - 2025 - Evaluating Non-AI Experts' Interaction with AI A .pdf](zotero://open-pdf/groups/2451508/items/SEGYFF7B)

## Discussion notes
Claude:
> Read in Week 13 of the SP-25 seminar (April 23rd, 2025), published in the Proceedings of CHI 2025.
>
> **Key question and setting**
> - Key question: [[QUE - How to enable non-AI experts to design and customize conversational agents for their own use in their own communities (without coding)?]] Subgoal: what are the unique requirements of this setting? Section 2.1 abstracts criteria for the library deployment setting; Section 2.2 describes the needs chatbots might respond to (SP-25 Distiller notes).
> - S05 liked the framing in Section 2.1 about "democratizing AI" for low-stakes, non-AI experts: people with technical or task expertise know how to leverage AI resources to their advantage, while non-experts may keep being disadvantaged, "so the gap between experts and non-experts can be widening if the AI or human-AI interaction design do not consider the specific contexts of non experts." The seminar tied this to [[PTN - Matthew Effects]] (rich get richer, poor get poorer).
> - Reframing (SP-25 seminar notes): "maybe not non-AI experts, but people with different expertise", connecting to the idea of vernacular software development: "A vernacular software developer ... creates software in a specific context, has principal responsibility in that context, and has professional training, if any, in that context rather than in software development; the software is a means to an end, not an end in itself." S05 likewise saw the librarians as non-AI experts but still domain experts, and wondered how things would differ for people who are experts in neither.
>
> **What we know about how well it works**
> - Evaluation findings are in Section 5.2. S05 found the challenges with Knowledge Base Upload interesting: what is a good way for domain experts to share their knowledge with the conversational agent?
> ![[0qiQJrmwSh.png]]
> - Participant pool caveat (SP-25 seminar, unattributed): how would outcomes differ for a pool without LLM backgrounds, given the tool targets people with minimal technical skills? "Participants had extensive experience serving in public libraries ... with an average of over 5 years of service. Most participants (10, 83.3%) had used LLM-based applications prior" (Zheng, 2025, p. 10).
> ![[sHVQrOwaeC.png]]
>
> **Critiques (🚧 Safety Inspection Expert)**
> - S05 was at first concerned about using generated personas to simulate conversations, but Figure 3 showed descriptions with specific behavioral characteristics rather than just a user "category".
> ![[Ab5FMlWGI-.png]]
> - S16 questioned the formative method: interviews used ChatGPT to demonstrate Q&A and prompted needs with questions synthesized from other studies, which might steer participants toward building a chatbot ("AI" loosely describes the end goal). Joel Chan: the semi-structured interview maybe not, but getting participants to actually design seemed effective. It elicited expertise in recursive querying and knowledge that wasn't (accessible) in the documents they uploaded, which they doubted could have been elicited just by talking: "points in favor of design methods!"
>
> **Connections**
> - S05 (🕸️ Connector): the "Source Transparency" feature could use chain-of-thought to show the agent's reasoning; ChatGPT showing its code for data-analysis tasks is another way to show transparency.
> - 🏺 Archaeologist: the paper cites Michelle Lam's doctoral consortium paper (https://dl.acm.org/doi/pdf/10.1145/3672539.3686714), part of a collection of work (e.g., LLooM) the commenter really liked.
> - Related work shared in the same session, a related study of machine-translation-mediated conversation (shared in the seminar) on agency for non-native speakers using machine translation: three interaction designs (labeling vs. regular post-editing vs. augmented post-editing). Evidence: post-editing increased perceived sense of agency vs. simply upvoting/downvoting translations, but reduced conversational fluency (total exchanges, average elaborations per information turn) and conversational alignment vs. labeling. Joel Chan noted it as a "neat use of theory": [[THE - Bandura's theory of agency]], agency as resource involvement; the study contextualized "resource" in non-native speakers' language resource composition, which led to the three conditions.
> ![[SBJ-4YH9pf.png]]
> ![[JYiwbwzj0V.png]]
> ![[Uur1wJTDdN.png]]
> ![[dx1804v9fU.png]]
> ![[2sUP63P6SV.png]]
> ![[LPGDNHUz86.png]]
