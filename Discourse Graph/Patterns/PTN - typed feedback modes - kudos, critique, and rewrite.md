---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e92-045d-76bc-aeae-291eed2e4544
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W05 (2025-02-26)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Give users a small set of feedback types as scaffolding for thinking about what to change: **kudos** ("do more of this"), **critique** ("don't do this"), and **rewrite** (edit the output directly). Each type becomes a principle. (Joel Chan, SP-25 W05, [00:30:36]–[00:31:00]: "These are kinds of critique. Kudos. Do more of this. Critique. Don't do this... I want to change what you wrote... this is the scaffolding they're providing. Like how do I think about what I want to change?")
> - Positive feedback matters: S05 noted that in [[@petridisConstitutionMakerInteractivelyCritiquing2024]] (Section 7.1) the baseline mainly let people steer the chatbot away from negative responses, while kudos also let them record positive behavior to continue. (S05, SP-25 W05 notes)


## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - ConstitutionMaker]] ([[@petridisConstitutionMakerInteractivelyCritiquing2024]])
> - Thumbs-up/down vs. post-editing interfaces in a related study of machine-translation-mediated conversation (shared in the seminar), a parallel contrast between evaluative and editing feedback (SP-25 W05 notes)

## Other Notes

Claude:
> - S11 placed this against the standard "baseline" in current AI interfaces such as ChatGPT, where users pick between two responses and the system implicitly infers why, the basis of RLHF. [[PTN - Constitutional AI]] is more explicit but needs more work to collect and apply. (S11, SP-25 W05 notes)

## Suggested relations
Claude:
> - instantiates → [[PTN - interactive natural language critique]]: these are the concrete forms the critique takes in ConstitutionMaker
> - enables → [[CLM - supporting positive feedback lets users reinforce desired AI behaviors rather than only steering away from bad ones]]
