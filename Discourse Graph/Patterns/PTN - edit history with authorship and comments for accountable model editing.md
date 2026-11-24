---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e92-2ab9-7f9d-8d71-e76a4c33583b
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W02 (2025-02-05)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Each edit to a model is recorded with who made it and a comment on why, in a reversible history, so that edits can be reviewed, audited, and undone by people with relevant knowledge. Borrowed from [[ART - git version control]].
>
> A participant in discussion (matching S14's written Safety Inspection comment): while reading, "I had all these questions like, okay ... if everything is put on ... the person who's interacting and having the power to edit these things ... there should be some comments ... Oh, wow, they do have comments ... is there a way for you to know who the user is, who made the edits ... look at that, there's a little code that says so and so did what." So the tool supports "the intentions of people to be documented", but "it's still on the person". (SP-25 W02, [00:19:00]–[00:20:04])

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - GAM Changer]]'s edit history:
> ![[7Rq6xkBINP.png]]

## Other Notes
Claude:
> - S14 worried that the time needed for these "responsibility" steps (edit, test, comment, review) could lead users to skip them (S14, notes; SP-25 W02, [00:20:04]).
> - Branching this history would support [[QUE - How might model editing tools preserve and test dissenting expert views instead of forcing consensus on a single model?]].

## Suggested relations
Claude:
> - (reverse) [[ART - GAM Changer]] instantiates this pattern
> - derived from → [[ART - git version control]]
> - informs → [[QUE - How can interactive model editing tools guard against well-intentioned but overconfident or biased domain experts in high-stakes settings?]]
> - informs → [[CLM - interactive model editing tools do not correct for editors' own biases, so safeguards against biased edits must come from social and process mechanisms]]
