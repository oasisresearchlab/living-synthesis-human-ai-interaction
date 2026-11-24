---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e91-cd9e-75be-9afa-8837e04cd455
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W13 (2025-04-23)]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> "Participants expressed 'frustration' (n=3) with the system's reliance on provided documents, which were often 'incomplete' (U1) or 'referenced inaccessible elements, such as images' (U4), which can lead to 'inaccuracies and omissions' (U11)." Example: P4 uploaded a PDF of monthly programming with many graphical elements; the agent struggled with references to inaccessible features (e.g., annotations marking registered-only sessions) or details not fully described (e.g., location). ([[@zhengEvaluatingNonAIExperts2025]], Section 5.2, screenshot from S05's notes)
> ![[0qiQJrmwSh.png]]

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> Think-aloud sessions and follow-up interviews with the AgentBuilder prototype (from the paper's abstract).

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> 12 U.S. library professionals in the evaluation study, run in summer 2023 with GPT-3.5-turbo; most (10, 83.3%) had prior LLM-app experience.

## Other Notes

Claude:
> - Joel Chan: this is a PDF-parsing problem, likely smaller with newer multimodal models (SP-25 W13, [00:32:35]-[00:34:45]).

## Suggested relations
Claude:
> - supports → [[CLM - the knowledge domain experts need to steer an LLM agent is often not available as machine-readable documents, because it is in inaccessible formats, unwritten, or hard to verbalize]]
> - informs → [[QUE - How well do current LLM pipelines extract knowledge from human-oriented documents like heavily formatted PDFs and flyers, and do existing benchmarks capture this?]]
