# 07. Retrieval and RAG: answers grounded in permitted data

[Русский](07-retrieval.md) · [Learning map](../README.en.md)

**Prerequisite:** an answer contract and a workflow. **Outcome:** retrieval with sources, access checks, and abstention, plus a comparison between a simple and an enhanced search implementation.

## Understand the mechanism

Retrieval selects relevant fragments from a collection. RAG supplies those fragments to generation. This does not train model weights or guarantee truthful answers. If retrieval selects the wrong document, a generator may confidently explain the wrong information.

Separate the questions: did search find the right source; is it permitted for this caller; is it current; does it support the particular claim; did generation add unsupported details? A single “good answer” score is not enough to diagnose failures.

Each fragment needs its `document_id`, version, provenance, section boundaries, and permissions. Arbitrary character splitting may separate a price from its conditions. Chunk size is an experimental parameter, not a magic number. A cache must also account for tenant, corpus version, and settings; correct retrieval cannot prevent leakage through an incorrectly shared cached answer.

## Study

1. [pgvector](https://github.com/pgvector/pgvector): vector search in PostgreSQL. Read about distances, exact/approximate search, and filtering. Installing a vector database is not required for the first baseline.
2. [OpenAI evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices): separating retrieval quality from response quality.
3. [OWASP GenAI risks](https://genai.owasp.org/llm-top-10/): prompt injection and sensitive information. Retrieved documents remain untrusted inputs.
4. Optional Russian extension: the repository's [RAG module](../../developers/modules/04-rag.md). This English lesson does not depend on reading it.

## Work with a small corpus

1. Create six fictional documents: opening hours, prices, cancellation rules, archived prices, a conflicting clarification, and another tenant's record. Mark versions and status.
2. Write eight questions, including an unanswerable question and a request for another tenant's data. Identify allowed source IDs before running the system.
3. Implement simple keyword retrieval over authorized documents. Filter access before constructing model context. Never send another tenant's document to the model and rely on a prompt to prevent disclosure.
4. Display retrieved fragments separately from the generated response. Inspect the results manually.
5. Add embeddings or hybrid search as a separate experiment. Compare paraphrased questions, not only exact word matches.
6. Verify source identifiers, supporting passages, and numeric claims. A link to an existing document does not prove that it supports the answer.
7. Delete or update a document. Check the index, cache, and a repeated answer. Distinguish historical experiment evidence from information still permitted as current context.
8. Place a malicious instruction in a synthetic document. It must not change the tool allowlist, tenant identity, or disclosure policy.

## Worked check

The current document prices a session at 250 cents; an archived document says 200. A question about the current price must follow an explicit version rule, not take the first similar fragment. If two active sources conflict and precedence is unknown, report the conflict.

`not_found` is a useful correct result. Do not keep lowering a search threshold until the system inevitably retrieves something. Asking for clarification is preferable to attaching an irrelevant citation.

**Independent challenge:** two tenants submit the same question. Demonstrate isolation in model context, cache entries, and outputs. Use synthetic content throughout the report.

**Done:** provide a baseline, a retrieval comparison, verifiable citations, an unanswerable-case test, and a cross-tenant denial test. The starting lab's tiny lookup mechanism is not a complete RAG implementation.

[Previous](06-workflows.en.md) · [Next: MCP](08-mcp.en.md)
