---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e91-0d22-7300-b7e3-a4a2da80c570
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W12 (2025-04-16)]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> In the [[ART - DynaVis]] study, participants in the NLI-only baseline issued roughly 8.4 natural language commands per task, versus about 2 with DynaVis, so dynamic widgets cut the number of prompts by roughly a factor of four (section 5.3.1 as read in the seminar).
> - Distiller notes: "more natural language prompts in baseline (about 4x more: 8ish vs. 2ish)" (Joel Chan, SP-25 W12 notes).
> - "they do more 8.4 natural language commands per task, so they roughly like reduced it by a factor of four ... you don't need as many like turns with the model to like complete the task" (SP-25 W12, [00:39:32]).
> - A participant-behavior reading from the seminar: in both conditions people kept up their effort, but with widgets they put it into repeated tweaks and trying out values rather than prompts (SP-25 W12, [00:39:00]).

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> Count of natural language commands issued per task.

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> Within-subjects comparison of DynaVis against a baseline that was DynaVis with dynamic widget synthesis removed: the baseline kept natural language editing and pre-populated UI widgets for basic chart manipulation (SP-25 W12, [00:38:14]).

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> "We recruited 24 participants (13 female, 10 male, 1 chose not to disclose) through the mailing lists of two research universities." Most worked with visualizations at least monthly (2 daily, 4 weekly, 14 at least monthly, 4 less often). (p. 8, quoted in SP-25 W12 notes)

## Other Notes

## Suggested relations
Claude:
> - supports → [[CLM - natural language interfaces can get users most of the way to a visualization but make fine-grained iterative tweaks hard to discover and control]]: fewer prompts are needed once fine-grained control moves into widgets (Distiller notes)
> - supports → [[CLM - synthesizing persistent GUI widgets from natural language edits removes the LLM round trip from later tweaks, which cuts the latency of iterative editing]]: each prompt avoided is a model round trip avoided (SP-25 W12, [00:28:50])
> - informs → [[QUE - How would the advantage of dynamically synthesized widgets over natural language editing change with stronger models and better prompting practices?]]: the gap may shrink if stronger models need fewer turns (SP-25 W12, [00:43:07])
