---
nodeTypeId: node_Gp7JMdrzm9DUuPfBzUptc
nodeInstanceId: 01a20e92-2370-7af5-a7b7-e46f7addfc8a
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W02 (2025-02-05)]]"
created: 2026-11-24
---
## Context
Claude:
> In discussion, a participant asked about keeping "a portfolio" of models instead of "one model that everybody agrees to": if one expert disagrees with the consensus about a feature (e.g., how much age should matter), keep their version and test whether it predicts better. "Otherwise you're kind of forcing conformity of people who are subject matter experts that disagree, but you don't ... get to test that." The participant added that "in medicine, it's mostly judgment, and a lot of times people kind of fall into the consensus." (SP-25 W02, [00:31:24]–[00:33:00])
>
> Joel Chan suggested that, from a git point of view, you could branch or fork models, but said [[ART - GAM Changer]] is "not really ... considering that", "which I don't knock them for" (SP-25 W02, [00:32:38]).

## Other Notes
Claude:
> - [[ART - GAM Changer]] already borrows reversible, commit-style edits from [[ART - git version control]], so branching is a natural extension.
> - A softer version: the tool as "ammunition" for a dissenting expert; see [[CLM - model editing tools can let a dissenting expert show the consequences of a feature's learned behavior rather than only argue verbally]].

## Suggested relations
Claude:
> - informs → [[CLM - model editing tools can let a dissenting expert show the consequences of a feature's learned behavior rather than only argue verbally]]
> - uses → [[ART - git version control]]: branching or forking as the proposed mechanism (SP-25 W02, [00:32:38])
> - informs → [[PTN - edit history with authorship and comments for accountable model editing]]
