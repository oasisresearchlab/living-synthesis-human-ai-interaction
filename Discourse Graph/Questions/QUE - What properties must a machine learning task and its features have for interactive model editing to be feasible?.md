---
nodeTypeId: node_Gp7JMdrzm9DUuPfBzUptc
nodeInstanceId: 01a20e92-2403-75f6-91bf-3ae46259c8db
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W02 (2025-02-05)]]"
created: 2026-11-24
---
## Context
Claude:
> S05 (🚧 Safety Inspection Expert, SP-25 W02 notes): "Does the system require a ML task that is supervised and prediction-based and have 'well-understood features' that domain experts can use to align their knowledge and model behavior? Can this system work with other tasks that are more open-ended or ambiguous such as unsupervised models and language generation ...? Essentially, what are the constraint/requirement of an ML task that are suitable for this system?"
>
> S11 answered yes: the work is for editing structured, well-understood features, because it depends on [[PTN - Glass-box models]] like GLMs and GAMs.
>
> Joel Chan opened the discussion on the same point: "this is a very specific type of model", and features are specified by developers rather than learned as in a neural network (SP-25 W02, [00:03:03], [00:06:18]).

## Other Notes
Claude:
> - Candidate requirements raised in the session: supervised prediction; additive structure; named, well-understood features; a domain expert who holds prior knowledge about each feature's relationship to the outcome.
> - See [[CLM - claims about a human-AI interaction design should be scoped to the model class it was built and tested with, not to AI in general]] and [[CLM - local edits to shape function of single features have minimal global impacts on generalized additive model performance]] (another boundary condition).

## Suggested relations
Claude:
> - informs → [[CLM - claims about a human-AI interaction design should be scoped to the model class it was built and tested with, not to AI in general]]
> - informs → [[PTN - Glass-box models]]
> - informs → [[PTN - interactive model editing]]
