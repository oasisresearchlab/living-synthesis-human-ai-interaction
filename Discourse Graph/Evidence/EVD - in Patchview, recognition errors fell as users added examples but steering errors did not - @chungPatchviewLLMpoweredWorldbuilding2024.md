---
nodeTypeId: node_E5uZ_O-NU-879JxbpJtcV
nodeInstanceId: 01a20e91-86ea-7fac-b4ad-9b38e5ab4f07
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W11 (2025-04-09)]]"
created: 2026-11-24
---
## Description
> [!Screenshots of key figure/table and/or direct quotes from source that substantiate the evidence statement (e.g., reports of statistical tests, or key quotes from participants), with page numbers.]

Claude:
> Recognition error went down as users added more examples, but steering error showed no real change ("maybeeee slight increasing trend??") (Joel Chan, notes on [[@chungPatchviewLLMpoweredWorldbuilding2024]]).
> ![[Tdi6Jjs8gp.png]]
> Joel Chan in class: steering works by adding the repositioned elements "as an example to their prompt ... which turned out not to be super, super powerful in terms of changing how things worked. But I find this to be a very fascinating ... UI idea" (SP-25 W11, [00:31:31]); the intended model update "turn[ed] out to not really work super well in practice. But I like the idea" (SP-25 W11, [00:23:39]–[00:24:11]).

## Methods Context
> [!info] Add methods details (with associated screenshots/quotes + page numbers) that contextualize how the evidence was produced that help us to understand/evaluate/use it. Specific details vary by methodology, but at a high level we want to know **What** observable measures/data were collected **How** (with what methods, analyses, etc.) from **Who** (which participants, what dataset, what population, etc.)

### What?
> [!info] What **observable measures/data** were collected? Be as specific to the measure (not construct!!) as you can. E.g., __"mean pairwise similarity of alternative uses task responses as judged by two Upwork workers"__

Claude:
> Recognition error (how far the model places elements from where users think they belong) and steering error (how far newly generated elements land from where users asked), as more user-adjusted examples accumulated.

### How?
> [!info] How were the measures/data collected (i.e., with what **procedures/analyses/experimental design**)? Note: this can be easy to blur with the "what", and that's ok. Focus on getting the details capture, not getting the classification just right.

Claude:
> Participants answered sensemaking questions about a generated world with Patchview and with a baseline that had only the list of elements, then used the system to generate and steer worldbuilding while thinking aloud (Joel Chan, notes on [[@chungPatchviewLLMpoweredWorldbuilding2024]]).
> ![[aV2fksnWBZ.png]]

### Who?
> [!info] Who was the data collected from (e.g., which participants in what context, what dataset, etc.)? As a heuristic: what is the population to which this evidence meant to generalize to?

Claude:
> Nine participants with creative-writing experience, one of them an expert screenwriter. Three had no AI experience, including "a hardcore fanfiction writer with no ... usage of AI whatsoever" (SP-25 W11, [00:37:10]–[00:38:23]).

## Other Notes
Claude:
> Separates the interaction idea (spatial steering) from the backend (few-shot examples in the prompt). The weak backend may understate what the interaction could do.

## Suggested relations
Claude:
> - informs → [[PTN - steering generation by pointing to a location in a concept space]]: the interaction outran its implementation
> - informs → [[PTN - prompt engineering]]: few-shot examples were a weak steering channel here
