---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-661f-7b78-9ee0-a078e26f5b75
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/yEu0iylFm
roamAuthor: "Joel Chan"
created: 2025-01-23
---

- Title: ConstitutionMaker: Interactively Critiquing Large Language Models by Converting Feedback into Principles
- Author(s):: Savvas Petridis, Benjamin D Wedin, James Wexler, Mahima Pushkarna, Aaron Donsbach, Nitesh Goyal, Carrie J Cai, Michael Terry
- Abstract: Large language model (LLM) prompting is a promising new approach for users to create and customize their own chatbots. However, current methods for steering a chatbot’s outputs, such as prompt engineering and fine-tuning, do not support users in converting their natural feedback on the model’s outputs to changes in the prompt or model. In this work, we explore how to enable users to interactively refine model outputs through their feedback, by helping them convert their feedback into a set of principles (i.e. a constitution) that dictate the model’s behavior. From a formative study, we (1) found that users needed support converting their feedback into principles for the chatbot and (2) classified the different principle types desired by users. Inspired by these findings, we developed ConstitutionMaker, an interactive tool for converting user feedback into principles, to steer LLM-based chatbots. With ConstitutionMaker, users can provide either positive or negative feedback in natural language, select auto-generated feedback, or rewrite the chatbot’s response; each mode of feedback automatically generates a principle that is inserted into the chatbot’s prompt. In a user study with 14 participants, we compare ConstitutionMaker to an ablated version, where users write their own principles. With ConstitutionMaker, participants felt that their principles could better guide the chatbot, that they could more easily convert their feedback into principles, and that they could write principles more efficiently, with less mental demand. ConstitutionMaker helped users identify ways to improve the chatbot, formulate their intuitive responses to the model into feedback, and convert this feedback into specific and clear principles. Together, these findings inform future tools that support the interactive critiquing of LLM outputs.
- Type: Conference paper
- Publication: 
- URL : https://dl.acm.org/doi/10.1145/3640543.3645144
- Date Added: January 23rd, 2025
- Zotero links: [Local library](zotero://select/groups/2451508/items/WPQSVGXK), [Web library](https://www.zotero.org/groups/2451508/items/WPQSVGXK)
- PDF links : [Petridis et al_2024_ConstitutionMaker.pdf](zotero://open-pdf/groups/2451508/items/V88CTMF6)

## Discussion notes

### Key question and design pattern
Claude:
> Read in Week 5 of the SP-25 seminar (February 26th, 2025; published in Proceedings of the 29th International Conference on Intelligent User Interfaces, 853–868). The key question the Distiller thread framed was [[QUE - How can we empower users to customize LLMs via natural language critique?]], answered with the design pattern [[PTN - interactive natural language critique]]: specifically, "compile" critiques so they persist as **principles**, as in a constitution.
> ![[Boxohj93Uo.png]]
> ![[GVIighJwRn.png]]
>
> Joel Chan's framing at the start of the session: if we want to control how a model behaves and get feedback from users, how can they actually do it? Users tell the model in natural language "don't do this, do this differently", and the system compiles those critiques into principles that are stuffed into the prompt. He placed it alongside other prompt-steering systems the seminar read, such as [[ART - ChainForge]], where users control model behavior by changing what goes into the prompt.

### What the system is and how it works
Claude:
> [[ART - ConstitutionMaker]] supports an LLM-powered "suggest → compile" flow that turns critiques into principles.
> ![[CM-Onc0iD7.png]]
> ![[tjDCpzCnrS.png]]
> ![[JWlSOseMSf.png]]
> - "Constitution Maker, users can provide either positive or negative feedback in natural language, select auto-generated feedback, or rewrite the chatbot’s response; each mode of feedback automatically generates a principle that is inserted into the chatbot’s prompt." (Petridis et al., 2024, p. 854; quoted by S09, SP-25)
> - The user never writes the principle directly. The scaffolding is three kinds of feedback: kudos ("do more of this"), critiques ("don't do this"), and rewrites. Because people don't always know what they want, an LLM generates candidate rationales for each kind; the user picks one or writes their own, and a second LLM call converts it into a principle that is added to the prompt. The principle-generation step is plain few-shot prompting, not a fine-tuned model; the prompts are in the paper's appendix. The constitution appears to be an editable text box. (SP-25 seminar discussion)
> - Mental model of where principles go (Joel Chan, SP-25): `{system prompt: "you are friendly and helpful"}` (stays all the time) + `{prior conversational turns}` (what gets truncated when the context window fills) + `{the user's actual text}`. Principles are appended to the persistent system-prompt part, so every response is conditioned on them. This is why principles "persist" across turns even though the model's weights never change.
>
> **Prompting vs. training.** Much of the session clarified that ConstitutionMaker is an inference-time technique: it changes the prompt, not the model. S11 contrasted this with [[PTN - Constitutional AI]] as a training scheme: preference-based training (RLHF) asks which of two responses a human prefers and implicitly learns why, whereas Constitutional AI makes the rules explicit and trains responses to adhere to them. In the ConstitutionMaker paper, by contrast, the "constitution" only lives in the prompt (S11 and Joel Chan, SP-25). Joel described prompting LLMs as an "improv game": the prompt sets the scene and the model predicts what text is likely to follow. Asking a model "do you remember X?" does not trigger a memory check; it just starts an improv scene about remembering.
>
> **Interpretable vs. opaque models.** Joel Chan connected this to the semester arc: the first model the seminar looked at ([[ART - GAM Changer]]) was a glass-box model whose shape functions users could directly edit. An LLM's network is too large to modify that way, so tools like this one use the lever that is available, which is in-context prompting.

### Formative study and principle types
Claude:
> - Formative study with 8 industry professionals: 25 minutes writing principles, then a conversation about the experience, yielding 79 principles.
> ![[pP4Wyx7HdE.png]]
> ![[huZ557XEg6.png]]
> - Principle classification: conditional vs. unconditional; scope of the conditional context (e.g., entire history, last response, next action); scope of the conditional action (e.g., a single turn vs. multiple turns).
> ![[Ad_WGItDjx.png]]
> ![[2Qczduztoe.png]]
> ![[LjoYkNQiVc.png]]
> ![[-pxA0pqWsT.png]]
> - Needs identified: support users to (1) identify things to critique, (2) translate feedback into principles, and (3) test principles.
> ![[m9rTOPKOHK.png]]
> ![[fAdqshRJrJ.png]]
> ![[qK0Jbpl9TN.png]]
> - Joel Chan's annotations: identifying things to critique "feels similar to the comparison stuff in chain forge"; the translation step "is happening under the hood" and he has "mixed feelings about how effective it is"; testing principles is "not well-supported relative to [[ART - ChainForge]] or [[PTN - LLM Chains]]".

### Evidence of efficacy
Claude:
> - User study: 14 participants (industry professionals, "probably at Google!"), within-subjects comparison against an ablated version where users write their own principles. Tasks: a foodbot and a vacationbot. Survey measures drawn from NASA-TLX.
> ![[aMCE8L91dY.png]]
> ![[WJqdEkFlIZ.png]]
> ![[6tFUzZ5Vru.png]]
> ![[9TPsu--FeE.png]]
> ![[U9iv1ZLhIU.png]]
> - Joel Chan's read: "we have clear confidence that they can generate principles", and participants reported they could guide the chatbot more easily and efficiently, but "whether it's actually effectively steering it to what they want is a different story." The study did not measure whether the bot actually behaved better. A stronger design would compare steering vs. no steering on a task with a performance measure, or have other users interact with bots designed with vs. without principles and rate their satisfaction. The self-report items were single questions ("did you find it easy"), so their reliability and construct validity are unknown, unlike the full, validated NASA-TLX.
> - The most interesting finding for Joel was that participants wrote principles that **conflicted with each other**, even within a single user. This echoes the earlier question of how we know user modifications to a model are effective.
> - Why NASA-TLX? S01 asked how HCI researchers pick measures. S05 answered that NASA-TLX is close to a standard workload measure for intervention studies, and that measures generally follow from the RQs and the core variables in prior literature (SP-25).

### Critiques
Claude:
> - **No scaffolding for good principles.** "big gap IMO: no scaffolding for what counts as a 'good/effective' principle" → [[QUE - How to support users to design effective principles for steering LLMs?]]. There is also no support for reasoning about interactions between principles → [[QUE - How can users reason about and account for higher-order consequences of their (proposed) edits to a high-dimensional model?]] (Joel Chan, 🚧 Safety Inspection Expert, SP-25)
> - **Hard-coded specificity.** "i'm kinda aghast that it's hard coded to be specific and conditional: no wonder they later find that things conflict!" and "I'm also really... really.... really wondering how good the translations are." (Joel Chan, SP-25)
> - **Missed connection to related UIs.** A "missed opportunity to really reflect on this in relation to other UIs like [[ART - ChainForge]] and [[PTN - LLM Chains]]". The paper cites [[@wuAIChainsTransparent2022]], but only in passing in related work. (Joel Chan, SP-25)
> - **Instruction following is assumed.** The system assumes that prompt engineering reliably steers the model. Joel noted some evidence that you can nudge a model one way or the other, but the conditions under which this works are an active research question → [[QUE - How good are LLMs at following instructions in prompts?]]. S11 shared benchmarks for "format-following capabilities" in LLMs (https://arxiv.org/abs/2402.18667) and a paper showing that emotional stimuli, even threats, can change LLM performance (https://arxiv.org/pdf/2307.11760) (SP-25 chat).
> - **Who is the user?** S05 found it unclear whether the tool is for individual users customizing their own chatbot or for designers incorporating feedback from groups of users. The study asked participants "to pretend to be a chatbot **designer**... so that it performs better for **users**", while the discussion raises conflicts between principles from multiple users. Section 8.2 (multiple principle writers) is future work; each participant in the study wrote principles alone. In the session, this connected to agency: whether a user is trying to get an answer or designing a bot for others changes their goals and how much they will invest in giving feedback. (S05 and seminar discussion, SP-25)
> - **Persistence.** One participant asked whether a constitution persists across sessions. Joel's answer was that the intent is yes: principles live in the system prompt, while earlier conversational turns are what get truncated when the context window fills (SP-25 discussion).

### Design alternatives raised
Claude:
> - **Conversation-level granularity** (S11, SP-25). The authors did not design for conflicting principles, though P2 raised it and P8 suggested a workflow change.
> ![[4GEZBl1cbw.png]]
> Rather than writing rules on the fly per response, the participant could review a whole conversation and then decide how to rate each response. Pro: more context goes into deriving general principles, which reduces conflicting and compounding principles. Con: risk of "unaligned" future responses that make the whole conversation useless. Section 7.4 (limits of principles) also suggests other ways to author principles, e.g., visualizing conversation arcs (P14) or structured UI elements instead of natural language (P13).
> - **LLM-based conflict check.** S14 highlighted the authors' suggestion to "leverage an LLM to conduct a pairwise comparison of principles to assess if any two are at odds, and then suggest a solution."
> - **Where principles go in an API call.** S01 asked whether principles should go in the system, assistant, or user role when the API allows role-based input, and which would steer most effectively. In the session it was noted that the system role is where general principles usually go, and that this control is available through the API but not in consumer chat interfaces.
> - **Positive feedback.** S05 noted (Section 7.1) that the baseline mostly let people steer away from bad responses, while kudos let them reinforce good ones. In a related study of machine-translation-mediated conversation (shared in the seminar), thumbs up/down vs. post-editing interfaces had different values, and a lack of edits is hard to interpret (satisfied, or didn't care / didn't know how?). S11 replied that both kinds of steering are standard (e.g., ChatGPT's pick-one-of-two, the basis of RLHF), and that [[PTN - Constitutional AI]] is more explicit but costs more work to collect and to apply across principles that interact and scale.

### Connections and open questions
Claude:
> - Looking back (S16, 🏺 Archaeologist, SP-25): Bubeck et al. (2023), "Sparks of artificial general intelligence: Early experiments with GPT-4" (https://arxiv.org/pdf/2303.12712), which S16 saw as steering attention toward interactive critique of LLM outputs. It evaluated GPT-4 through the researchers' own interactions with the model rather than standard benchmarks.
> - Looking forward (S16): Shankar et al. (2024), "Who validates the validators?" (UIST), which proposes [[ART - EvalGen]]. EvalGen has an LLM suggest evaluation criteria, users pick which to implement and grade outputs, and the system selects the assertions that best align with the user's grades. Its qualitative study with 9 practitioners found "criteria drift": users need criteria to grade outputs, but grading outputs helps them define the criteria.
> - S01 (🕸️ Connector) asked [[QUE - What is the effectiveness of LLM-generated critiques?]] and pointed to work on LLM-as-judge showing that "strong LLM judges ... match both controlled and crowdsourced human preferences well, achieving over 80% agreement, the same level of agreement between humans" (https://arxiv.org/pdf/2306.05685).
> - S05 read the interactive critique as [[THE - conversational repair]] and asked: [[QUE - how-should the way a human repair with a chatbot differ from how they would repair with a person?]], [[QUE - how-should chatbot be designed to converse in a way that resembles how humans coordinate meaning or just be designed as a bot that follows rule]], and [[QUE - How might designing chatbots to align or not with human patterns of repair and meaning coordination in conversations impact how humans communicate with each other?]]
> - S01 (🤔 ELI5 linter) defined **formative usability evaluation**: evaluation done to find and fix problems with an existing product to make it more usable.
