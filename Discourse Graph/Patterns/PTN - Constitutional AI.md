---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e70-661f-78a8-8302-54a6cd2da175
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/HMHzAvxmY
roamAuthor: "Joel Chan"
created: 2025-03-11
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> - Key source: [[@baiConstitutionalAIHarmlessness2022]] (Anthropic).
> - Constitutional AI tells the AI explicitly what principles it needs to adhere to, and then ensures that future responses adhere to that set. Contrast the standard "baseline" in current interfaces (e.g., ChatGPT) and in RLHF training: the user picks between two responses and the system implicitly figures out why they preferred one. Constitutional AI makes the interpretation of meaning much more explicit, but it requires more work to collect the principles and to interpret how they apply so that outputs comply with all of them (whether conditional or not, how principles interact, and how they scale). (S11, SP-25)
> - Another overview: https://primo.ai/index.php?title=Constitutional_AI (shared by S09, SP-25)

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.
## Other Notes
Claude:
> - Critique from the SP-25 seminar's Distiller thread: the paper under discussion explicitly mentions and contrasts itself with Constitutional AI, claiming that approaches like it focus on enabling LLMs to *execute* policy, assuming we already know what we want (the "forward pass"), rather than helping people figure out what the policy should be. (SP-25 seminar)
> - ![[9QHV90dXH9.png]]
> - ![[QYt8YcUMh6.png]]
