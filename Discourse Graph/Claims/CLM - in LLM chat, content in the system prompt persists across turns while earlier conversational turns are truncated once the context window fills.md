---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e92-0ede-7ac4-8b33-f6d3498e8db1
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-25 W05 (2025-02-26)]]"
created: 2026-11-24
---
## Grounds

Claude:
> - Joel Chan's model of a request: a system prompt ("you are friendly and helpful", "this stays all the time"), prior conversational turns ("this is what gets truncated"), and the user's actual text. ConstitutionMaker's principles go into the persistent part, so "every prompt will have that". (SP-25 W05 notes; [00:14:03]–[00:15:15]; [00:44:17])
> - Sliding window: "once you hit 16[K], you gotta pick... I want to keep the most recent turn. So I'll drop the one from way long ago", or compress earlier turns. (SP-25 W05, [00:19:06]–[00:19:24])
> - A participant connected this to a news story of a person whose ChatGPT companion forgot their relationship when the conversation hit the token limit. Joel Chan: "what happens is this gets truncated... in the case of like forgetting who you are, that's probably what happened." (SP-25 W05, [00:43:21]–[00:44:17])
> - A participant noted most long-context models do not work as well past about 40K tokens. (SP-25 W05, [00:15:37]–[00:16:01])
> - Through the API, developers can set the system role directly; in consumer web interfaces the system prompt is controlled by the provider. (SP-25 W05, [00:45:17]–[00:46:14])


## Other Notes

Claude:
> - Commercial providers don't release the details, so this is the "simplest" plausible implementation, per Joel Chan ([00:05:23]).

## Suggested relations
Claude:
> - informs → [[ART - ConstitutionMaker]]: explains why its principles persist
> - informs → [[QUE - Which part of a role-based prompt - system, assistant, or user - most effectively carries steering principles?]]
