---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e94-7a86-7e3d-9cee-64889c49e7c9
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-24 W13-16 Evaluation and accountability]]"
created: 2026-11-24
---
## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> An end-to-end framework for internal algorithmic auditing, meant to close the "AI accountability gap" by building audits into an organization's development process. From [[@rajiClosingAIAccountability2020]]. (S05, Distiller, SP-24 W14)
> ![[v1ipfwnNHs.png]]

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> Five stages, each with documents (S05, Distiller, SP-24 W14):
> - **Scoping**: clarify the audit's objective and principles; risk analysis for harms; ethical review of the use case; social impact assessment.
> - **Mapping**: review what has been done; stakeholder map; ethnographic field study of the development process and how errors are prioritized.
> - **Artifact collection**: design checklist of expected documentation; datasheets and model cards.
> - **Testing**: adversarial testing; ethical risk analysis chart.
> - **Reflection**: compare test results to the values from scoping; use-related risk analysis and FMEA; remediation and risk mitigation plan; audit summary report.
> Governance guidance: "anticipation, reflexivity, inclusion, and responsiveness".

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

Claude:
> Illustrated with a fictional Company X auditing a high-stakes child abuse screening tool and a low-stakes smile detection algorithm. Example audit materials for the smile detection case were shared as a Google Drive folder. (S05 and Joel Chan, SP-24 W14)

## Other Notes

Claude:
> Joel Chan (SP-24 W14) on genre: "interdisciplinary synthesis of perspectives from XYZ domains tailored to T target domain". S05 compared it to a paper adapting historical union tactics to platform-mediated labor. Joel also noted the paper doesn't show the framework "works".

## Suggested relations
Claude:
> - instantiates → [[PTN - internal algorithmic auditing]]
> - uses → [[PTN - Failure Modes and Effects Analysis (FMEA)]]
> - uses → [[ART - Model Cards]]
> - uses → [[ART - Datasheets for Datasets]]
> - informs → [[ART - CheckList]]: S11 (Archaeologist, SP-24 W14) proposed CheckList for the testing stage (section 4.5)
> - informs → [[QUE - How can we tell whether an internal AI audit framework actually works, at what cost, and whether its recommendations change practice?]]
> - derived from → [[@rajiClosingAIAccountability2020]]
