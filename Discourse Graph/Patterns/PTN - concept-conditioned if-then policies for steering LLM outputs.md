---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e91-2333-7a90-85d8-3db51ad04330
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W07 (2025-03-12)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> - Users define natural-language "concepts" (e.g., "property crime and vandalism") backed by classifiers that tag whether a case (user input plus model output) contains them. Policies are if-then rules: if these concepts are present, then apply an action. (Joel Chan, SP-25 W07, [00:29:35]–[00:30:30], [00:32:08])
> - Preset action primitives: **block**; **warn** (output as-is but warn the user); **suppress** (steer away from a direction); **add** (steer toward a direction). (Joel Chan, SP-25 W07, [00:30:30]–[00:30:55])
> - Policies can be supplemented with examples of the desired behavior. (SP-25 W07, [00:49:04])
> - Key source: [[@lamAIPolicyProjector2024]].

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - AI Policy Projector]]: concepts and policies are layered over a map of cases.
> - Related principle-based steering: [[ART - ConstitutionMaker]] and [[PTN - Constitutional AI]], which use free-form principles rather than concept-conditioned rules.
## Other Notes
Claude:
> Limits from participants: requests for OR operators, more than concepts in the if clause, and more actions than WARN / SUPPRESS ([[EVD - AI policy practitioners who used an initial prototype of ART - AI Policy Projector expressed a desire for more expressivity in definitions of policies, such as OR operators, and additional steer]]).

## Suggested relations
Claude:
> - [[ART - AI Policy Projector]] — instantiates → this node
> - [[EVD - AI policy practitioners found if-then statements in ART - AI Policy Projector to support transparent and interpretable LLM policy formulation - @lamAIPolicyProjector2024]] — supports → this node
> - consistent with → [[CLM - If-then statements support transparent and interpretable LLM policy formulation]]
> - consistent with → [[CLM - concept-based if-then policy + easy access to more training examples may be a powerful combination for enabling better steering]]
