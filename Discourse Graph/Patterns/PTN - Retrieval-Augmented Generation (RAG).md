---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e91-c2ec-7594-96a1-f77ac2325eeb
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W13 (2025-04-23)]]"
created: 2026-11-24
---
## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Joel Chan's gloss: "a fancy term for, they use like older techniques to rank, um, parts of documents that might be relevant to a query, and then they feed that into a language model. As the part of the prompt and then the model synthesizes it into a response" (SP-25 W13, [00:26:01]).
> - The model's background knowledge still comes from its (undisclosed, roughly "the internet") training data; the retrieved documents become the basis for responses (SP-25 W13, [00:26:28]-[00:26:50]).

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - AgentBuilder]]: librarians upload documents that ground the agent's answers.
> - [[ART - LangChain]] packages RAG boilerplate for programmers.
> - Joel Chan noted that role prompts plus knowledge upload are now table stakes in commercial systems (SP-25 W13, [00:22:08]).

## Other Notes

Claude:
> - RAG is only as good as what can be extracted from the documents: see [[EVD - library professionals were frustrated that AgentBuilder's knowledge-base upload relied on incomplete documents or ones referencing inaccessible images - @zhengEvaluatingNonAIExperts2025]] and [[CLM - the knowledge domain experts need to steer an LLM agent is often not available as machine-readable documents, because it is in inaccessible formats, unwritten, or hard to verbalize]].

## Suggested relations
Claude:
> - informs → [[CLM - the knowledge domain experts need to steer an LLM agent is often not available as machine-readable documents, because it is in inaccessible formats, unwritten, or hard to verbalize]]: RAG presumes the needed knowledge is in documents
