---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e91-87c7-79e1-811c-94d07b19d719
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W11 (2025-04-09)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Instead of writing a prompt that describes what to generate, the user points to a place in a space defined by concepts, and the model generates something that belongs there. Joel Chan: "instead of writing a natural language prompt to say, make a new element that is blah, blah, blah. You say, make a new element here ... the model interprets that as, I want to make something that's in between these three concepts" (SP-25 W11, [00:22:49]–[00:23:14]). His examples: between "chaotic good and lawful evil", or a policy "in the middle" between Republican and Democrat (SP-25 W11, [00:23:14]).
> Revision works the same way: "this is not really here. It should be somewhere here", and the move is fed back as an example for the model (SP-25 W11, [00:23:39]–[00:24:00]). Key source: [[@chungPatchviewLLMpoweredWorldbuilding2024]].
> ![[8d0mwINZWp.png]]
> Joel compared it to [[ART - GAM Changer]]'s direct manipulation ("make it more flat"), but noted "this is not example based, this is like concept based" (SP-25 W11, [00:31:55]–[00:32:19]).

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - Patchview]], via [[PTN - Generative Dust and Magnet Visualization]].

## Other Notes
Claude:
> - Evidence: [[EVD - worldbuilders found steering by repositioning elements in Patchview easy and natural, but felt natural-language prompts were better for specific requests - @chungPatchviewLLMpoweredWorldbuilding2024]] (felt easy and natural); [[EVD - in Patchview, recognition errors fell as users added examples but steering errors did not - @chungPatchviewLLMpoweredWorldbuilding2024]] (the backend steering was weak).
> - Boundary: [[CLM - direct manipulation suits rough, exploratory steering of generative models, while code or natural language is preferred when users need precise, specific control]].

## Suggested relations
Claude:
> - instantiates ← [[ART - Patchview]]: Patchview instantiates this pattern
> - derived from → [[PTN - Generative Dust and Magnet Visualization]]
> - instantiates → [[PTN - Direct Manipulation]]: a DM form of steering
> - informs → [[QUE - How might we let people steer generative models with intentions they cannot easily put into words?]]
