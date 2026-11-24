---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e92-4493-75a7-a9d7-44baf72f84ad
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-25 other weeks and synthesis]]"
created: 2026-11-24
---
## Grounds

Claude:
> - [[@wangInterpretabilityThenWhat2022]], quoted by S01: "... continuous feedback ... as well as transparent and reversible edits ... (h)owever ... do not guarantee to prevent users from overfitting the model, injecting harmful bias, or maliciously manipulating model predictions. This potential vulnerability warrants further study on how to audit and regulate model editing." (S01, SP-25 W09 synthesis)
> - S01: "Reversible edits are measures to cancel damage dealt. However, there should be sort of monitoring mechanism to detect harmful edit." S01 proposed an LLM judge with a constitution as one option. (S01, SP-25 W09 synthesis)
> - Group 1 proposed a human role: "an auditor/moderator to track and revert user-initiated commits." (SP-25 W09 synthesis, Group 1)

## Other Notes

Claude:
> - Reversibility helps only if someone notices an edit is harmful. Detection, by a person or a model, is the missing piece.

## Suggested relations

Claude:
> - supports → [[QUE - How should user-initiated edits to AI models be governed, and who should audit, track, and revert them?]]
> - consistent with → [[EVD - some data scientists cautioned about the need for (stronger) guardrails on model edits when using interactive editing tools like ART - GAM Changer - @wangInterpretabilityThenWhat2022]]: participants in the same study asked for guardrails (@wangInterpretabilityThenWhat2022)
> - informs → [[PTN - Actionable explainability]]: a boundary condition on letting explanations drive edits (S01, SP-25 W09 synthesis)
> - informs → [[PTN - interactive model editing]]
> - informs → [[PTN - edit history with authorship and comments for accountable model editing]]: commit logs give reversibility but not detection
