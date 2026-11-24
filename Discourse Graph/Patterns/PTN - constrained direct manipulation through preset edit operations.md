---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e92-2a28-709d-912f-94eb951d5994
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W02 (2025-02-05)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Instead of letting users freely redraw a model component, the interface offers a small menu of named operations (e.g., align, interpolate, monotonize, smooth, remove effects) applied to a selected region. This keeps much of the immediacy of [[PTN - Direct Manipulation]] while making each edit's meaning explicit.
>
> Joel Chan: "the most direct manipulation way would be to actually like move the curve. This one, they constrain it a little bit, right? So you have to select ... one of these predetermined ... ways to edit ... which I think is actually pretty important ... because ... if you interpolate it versus, like, flatten it versus smooth it versus make it linear, those are all pretty different" (SP-25 W02, [00:12:14]–[00:12:52]). He called it "not the best example of direct manipulation ... But this is pretty close ... way better than like writing code."

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - GAM Changer]]'s modification types:
> ![[omkpng_BTY.png]]
> - The respiratory-rate edit in the sepsis case: choosing monotonic increase vs. linear interpolation changed the result substantially ([[EVD - it was possible for a two physicians to use ART - GAM Changer to edit a GAM model for sepsis risk prediction to account for possible issues with temperature, respiratory rate, and systolic blood]]).

## Other Notes
Claude:
> - The choice of operations is itself a design-space question: [[QUE - How should designers of interactive model editing tools decide which edit operations to support?]].
> - Joel Chan (notes) doubted the physician alone would have noticed the difference between monotonic and interpolation edits; see [[CLM - ART - GAM Changer or PTN - Direct Manipulation-based approaches to steering models are best used in collaborative teams with domain experts - end users and ML engineers]].

## Suggested relations
Claude:
> - (reverse) [[ART - GAM Changer]] instantiates this pattern
> - derived from → [[PTN - Direct Manipulation]]
> - informs → [[QUE - How should designers of interactive model editing tools decide which edit operations to support?]]
