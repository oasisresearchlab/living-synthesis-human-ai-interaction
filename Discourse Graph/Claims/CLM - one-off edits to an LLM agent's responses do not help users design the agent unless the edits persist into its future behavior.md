---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e91-c62a-709b-8354-39718d088d61
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-25 W13 (2025-04-23)]]"
created: 2026-11-24
---
## Grounds

Claude:
> - Joel Chan's reading of [[ART - AgentBuilder]]: "my understanding is that this is a one-off fix. That if they see a response they didn't like, they edit it. Does it actually change the overall behavior of the model?" (SP-25 W13, [00:24:04]-[00:24:30]).
> - A participant: "if it's not learning, then how is this useful for making like customizable... conversation agents if it's not remembering?" (SP-25 W13, [00:27:00]).
> - Joel Chan: "this seems like something that could be useful if like you're deploying this with a human co-pilot... But in terms of... the design process... it's not useful for the design process if the edits don't go anywhere" (SP-25 W13, [00:27:16]-[00:27:39]).

## Other Notes

Claude:
> - Boundary condition: one-off edits still help at run time when a human supervises live responses.
> - Uncertain: AgentBuilder's Figure 3 shows a "[Rule]" button beside Show and Edit, so the paper may support some persistence; the discussion didn't resolve this.

## Suggested relations
Claude:
> - informs → [[PTN - generalizing one-off output edits into persistent rules or examples]]: motivates generalizing edits
> - consistent with → [[ART - ConstitutionMaker]]: ConstitutionMaker persists critiques as principles
