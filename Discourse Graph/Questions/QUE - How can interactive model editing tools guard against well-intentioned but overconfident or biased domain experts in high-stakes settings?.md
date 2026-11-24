---
nodeTypeId: node_Gp7JMdrzm9DUuPfBzUptc
nodeInstanceId: 01a20e92-22a5-7d4d-a5d2-0041a1318f27
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W02 (2025-02-05)]]"
created: 2026-11-24
---
## Context
Claude:
> S11 (🚧 Safety Inspection Expert, SP-25 W02 notes) quoted the paper's Discussion (section 6): "Guarding against harmful edits is our top priority ... However, they do not guarantee to prevent users from overfitting the model, injecting harmful bias, or maliciously manipulating model predictions." Because this kind of editing is evaluated in high-stakes settings, S11 asked: "how do we minimize risk from well-intentioned but overconfident domain experts?"
>
> S14 (same thread) raised bias (conformity, implicit): if editing is left to clinical expertise, "how do we know that their training data (education, experience, etc.) is without bias", and will they recognize and self-correct it? S14 also worried that the extra time to edit, test, comment, and review would lead people to bypass these "responsibility" steps.
>
> In discussion: "what happens if ... the user is like, not really an expert, or like ... just too overconfident" (SP-25 W02, [00:27:30]).

## Other Notes
Claude:
> - One answer from the discussion: the tool does not correct for human biases, and that is acceptable if social or process mechanisms do; see [[CLM - interactive model editing tools do not correct for editors' own biases, so safeguards against biased edits must come from social and process mechanisms]].
> - Related: [[EVD - some data scientists cautioned about the need for (stronger) guardrails on model edits when using interactive editing tools like ART - GAM Changer - @wangInterpretabilityThenWhat2022]] and [[PTN - Actionable explainability]] (S01's note on harmful edits).

## Suggested relations
Claude:
> - derived from → [[EVD - some data scientists cautioned about the need for (stronger) guardrails on model edits when using interactive editing tools like ART - GAM Changer - @wangInterpretabilityThenWhat2022]]: participants in the study raised the same concern
> - informs → [[CLM - interactive model editing tools do not correct for editors' own biases, so safeguards against biased edits must come from social and process mechanisms]]
> - informs → [[PTN - edit history with authorship and comments for accountable model editing]]: authorship and comments as a partial safeguard (SP-25 W02, [00:19:00])
