---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e92-1e6e-7a85-aeeb-9cc6d039bb03
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W06 (2025-03-05)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Use an LLM to generate candidate values along a dimension of variation (e.g., kinds of cats: Persian, Siamese, ...) or prompt modifiers, which then become rows or columns for exploring a second generative model's output space. The LLM is not the model being steered; it helps users expand the exploration space.
> - Joel Chan: in [[ART - DreamSheets]] "there's actually two models in here and they're only evaluating control of one"; the target is the text-to-image model (Stability), while GPT is used "to help you expand out, like types of cats... points on the dimension space." (SP-25 W06, [00:15:02]–[00:15:30])
> - Not everyone used it: some participants explored manually, and only some (E2, E3, per Joel's recollection) used generative semantic exploration. (SP-25 W06, [00:15:59]–[00:16:26]); see [[EVD - some participants used ART - DreamSheets to power exclusively -manual- variations in prompts and parameters - @almedaPromptingDiscoveryFlexible2024]]
> - When it worked, it surfaced modifiers the user had not thought of: [[EVD - an expert artist used LLM-generated variations in DreamSheets to discover prompt modifiers like monochromatic, watercolor, and pixel art - @almedaPromptingDiscoveryFlexible2024]]

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - DreamSheets]] (GPT-generated variations for Stable Diffusion prompts)
> - Related: [[ART - ConstitutionMaker]] surfaces candidate rules for users in a similar way (Joel Chan, SP-25 W06 notes, Distiller thread)

## Other Notes

## Suggested relations
Claude:
> - [[ART - DreamSheets]] — instantiates → this pattern
> - consistent with → [[ART - ConstitutionMaker]]: both use an LLM to propose options the user then selects among (Joel Chan, SP-25 W06 notes)
