---
nodeTypeId: node_LyyTDCfZHGTvQWfvU0h8m
nodeInstanceId: 01a20e70-661e-76c0-a265-3b133b34be4e
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/dd6ppvvtt
roamAuthor: "Joel Chan"
created: 2024-02-14
---
## Purpose
> [!info **Why** might someone use this thing? What is it for, or what function or purpose does it serve? Note: it's ok to just note whatever purpose(s) you're focus on at the moment, and ignore any other purpose(s) that the thing might be for: we can add them later.]

Claude:
> Data wrangling: transforming and cleaning data tables.

## Mechanism
> [!info] **How** does this thing fulfill its purpose? Focus on describing the "secret sauce" or key mechanisms of action. Ideally we'd map them to one or more underlying conceptual or design patterns that explain how it works.

Claude:
> Wrangle is a high-level [[PTN - Domain-Specific Language (DSL)]] for data transformation. Interfaces built on it (e.g., [[ART - Wrangler]]) use [[PTN - Predictive Interaction]]: the user selects data, the system suggests transforms expressed in the DSL, and visual previews show their effect.
> ![[4FcnCc4Z7_.png]]

## Example(s) of usage
> [!info] Describe at least one concrete example of this artifact in use. At minimum, we want an example of it in *intended* use, but we can later add and link to some variations if we like.

Claude:
> - The user selects the text "Alabama" in the first row. The system responds with automatic transform suggestions, such as extracting or cutting text from table cells.
> - The selected transform extracts text after the span "in." Visual previews in the table grid show the effect of applying the transform.
> - Reported outcomes: increased productivity and user discovery of useful transformations.

## Other Notes
Claude:
> - Came up in the SP-24 seminar summary of [[@heerAgencyAutomationDesigning2019]], which presents three use cases of interactive agents from the authors' prior work; data wrangling is one of them.
> - Related systems: [[ART - Wrangler]] ([[@kandelWranglerInteractiveVisual2011]]) and Proactive Wrangling ([[@guoProactiveWranglingMixedinitiative2011]]).
> - Listed as an example of [[PTN - Domain-Specific Language (DSL)]].
