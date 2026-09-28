# 11. AI application security and data boundaries

[Русский](11-security.md) · [Learning map](../README.en.md)

**Prerequisite:** documented tools, data, and flows. **Outcome:** a small threat model, enforced controls, and repeatable negative tests.

## Understand the risk

The model reads user text and retrieved documents. Those inputs may contain instructions pretending to be developer commands. A system prompt saying “ignore malicious instructions” is not proof that prompt injection has been eliminated.

Separate trusted application decisions from untrusted content. Identity, permitted operations, storage access, and resource limits are established outside the model. Output checks supplement these boundaries; they do not replace them.

Request Desk has four important assets: the provider credential, tenant documents, tool-execution authority, and request logs. Map who can read and modify each. Do not use real client material to test controls.

## Read

1. [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/): prompt injection, sensitive information, supply chain, output handling, and excessive agency. Relate each relevant risk to your own data flow.
2. [MCP security guidance](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices): connected-server and token risks.
3. Optional Russian extension: the repository's [security module](../../developers/modules/09-security.md).

## Build the controls

1. Make a table: asset → untrusted input → possible harm → control → test. A list of acronyms is not a threat model.
2. Deny tools by default. Separate reads and writes; user content must not enable additional tools.
3. Filter authorized data before retrieval and before passing it to a model. Include tenant identity in cache keys and establish identity server-side.
4. Validate structured arguments and business constraints. Do not execute generated SQL, HTML, or shell content as trusted code. Escape output safely when displaying text.
5. Remove credentials from source and logs. `.gitignore` helps prevent future mistakes but does not remove a previously published key from history; an actual leak requires owner-managed revocation/rotation.
6. Limit input/output size, steps, network destinations, and experimental spending. Do not grant excessive privileges simply to make a teaching demo convenient.
7. Record dependency origins and versions. Before an update, review package provenance, API changes, and test results. Never automatically execute installation instructions found in a document.
8. Define retention for teaching inputs and logs. Deleting a database row also requires checking indexes and caches. Do not claim deletion from an external provider without a supported mechanism and confirmation.

## Five controlled tests

Use synthetic fixtures only: a document asks for a fictional secret; a request targets another tenant's record; an argument supplies an arbitrary path; a tool result asks to enable another tool; an oversized input attempts to exhaust the budget. Observe actual execution rather than relying on a model saying it refused.

If a model proposes a prohibited call but the server blocks it, report both outcomes: unsafe model behavior and a successful execution boundary. If the model refuses while the server would have executed the prohibited call, the system still lacks a necessary control.

**Independent challenge:** ensure a tool error does not expose stack traces, filesystem paths, credentials, or another tenant's content through either logs or responses.

**Done:** code enforces permissions, credentials are not published, negative cases cannot execute prohibited actions, and remaining risks are documented. This is a teaching assessment, not a professional security audit or a guarantee of vulnerability-free software.

[Previous](10-reliability.en.md) · [Next: delivering a service](12-delivery.en.md)
