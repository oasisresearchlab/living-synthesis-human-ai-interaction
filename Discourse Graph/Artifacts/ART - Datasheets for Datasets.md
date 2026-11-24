---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e94-7e17-7139-bd69-6eb37dc6df7f
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W13-16 Evaluation and accountability]]"
created: 2026-11-24
---
## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> Documentation of a dataset: where it's from, how it was collected, and its operating characteristics, to clarify what a model was trained on, given many precedents of inappropriate training data use. (S05 Distiller and S11 Archaeologist, SP-24 W14)

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> A standard set of questions answered by dataset creators. Cited by Raji et al. (section 4.4.2) as necessary for internal audits. (S11, SP-24 W14)

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

Claude:
> - Standard on Hugging Face as data cards (Joel Chan, SP-24 W14). How well they're filled out: [[EVD - an analysis of over 7,000 Hugging Face data cards found that many recommended sections were ignored, focusing on data description over considerations for use - James Zou group ICLR 2024]].
> - Adapted to healthcare by Lauren Wilcox et al. (a co-author of [[@beede2020humancentered]]) as Healthsheet: https://arxiv.org/pdf/2202.13028.pdf (Joel Chan, SP-24 W14).

## Other Notes

Claude:
> Source: Gebru et al. (2018), Datasheets for Datasets, https://arxiv.org/abs/1803.09010 (no source note in the vault).

## Suggested relations
Claude:
> - instantiates → [[PTN - algorithmic transparency]]
> - informs → [[ART - SMACTR internal algorithmic audit framework]]
