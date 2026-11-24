---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e93-3e53-7639-9957-85081844bb37
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W08-12 Collaboration and grounding]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Instead of AI producing codes for researchers, AI works with them: it takes the texts a researcher has already coded and suggests where the same codes apply, or proposes additional codes from them. S16 (Distiller, SP-24 W10) drew this from [[@feustonPuttingToolsTheir2021]]: "Thinking of ways AI can extend human capabilities by having AI code with, rather than for, researchers."
> A related ML technique, linted by Joel Chan (ELI5 linter, SP-24 W10): **active learning**, where "AI can tailor results to work a human has performed" (p. 20).
## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - PaTAT]] learns interpretable patterns from user-annotated codes in real time (S13, Archaeologist, SP-24 W10).
> - [[ART - CollabCoder]] offers on-demand code suggestions during independent open coding (S13, Archaeologist, SP-24 W10).
> - Scholastic ([[@hongScholasticGraphicalHumanAI2022]]) is the system design that followed from the Feuston and Brubaker work, per Joel Chan's notes on the source.
## Other Notes
Claude:
> - Risk: [[EVD - a qualitative scholar worried that AI trained on their earlier coding would make past decisions assert themselves over present discovery - @feustonPuttingToolsTheir2021]].
> - Possibly related: [[PTN - interactive topic modeling]].

## Suggested relations
Claude:
> - informs → [[QUE - How might we design AI-infused systems that augment — rather than replace — human intelligence and work?]]
> - consistent with → [[CLM - whether qualitative researchers accept AI assistance depends on the stage of analysis - early coding is where researchers come to know their data, so AI help there threatens the analysis]]: it waits until the human has coded
> - consistent with → [[CLM - LLM-generated qualitative codes are more useful as an adjustable starting point, like a colleague's open codes, than as a finished analysis]]
