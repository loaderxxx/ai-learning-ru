# 02. From a problem to contracts: where AI belongs

[Русский](02-contracts.md) · [Learning map](../README.en.md)

**Prerequisite:** stages 00–01. **Outcome:** a one-page specification, a data-flow description, and a non-model baseline.

## Three different directions of control

`classify_request(text)` may be an ordinary application function that calls an LLM internally: **code calls a model**. With tool calling, the model returns a proposal such as `lookup_record(id)`: **the model requests an action**, and the application executes it. Orchestration connects both directions into a process. MCP describes interaction with tools; it does not replace business logic. Calling all of these things an “agent” hides important boundaries.

Our teaching project, **Request Desk**, handles synthetic enquiries for a fictional club. It retrieves permitted reference material, calculates totals with ordinary code, and prepares a draft. It does not send messages, make payments, or modify real accounts. The name and all scenarios are fictional teaching material.

Break down “Explain the price of four sessions and prepare a reply.” Finding the price is data access. Multiplication belongs in code. Drafting a readable explanation may benefit from a model. Sending it would be a separate action requiring separate authority; this teaching project does not include sending.

## Study the relevant concepts

1. [LangGraph workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents): distinguish a predefined process from dynamic step selection. Focus on chaining and routing, not copying an entire framework.
2. [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs): understand the format contract and the semantic checks that remain your responsibility.
3. Optional additional reading in Russian: the repository's [specification module](../../developers/modules/02-specification.md). This English chapter is self-contained; reading that module is not required.

## Write the specification

1. Name one user and one job: “receive an evidence-backed answer from teaching materials.” Avoid “a universal assistant for everything.”
2. Define accepted input, size, language, `tenant_id`, and the source of identity. The application establishes a tenant after authentication; the model must not infer authority from request text.
3. Define explicit outcomes: `answered`, `not_found`, `needs_approval`, `invalid_input`, and `technical_error`. Specify which fields belong to each outcome.
4. Enumerate permitted tools and prohibited actions. A sentence inside a retrieved document does not grant permission.
5. Write ten synthetic enquiries: direct question, paraphrase, unknown answer, conflicting documents, another tenant's data, calculation, malformed input, timeout, repeated action, and a malicious instruction embedded in a source.
6. Solve them manually and record expected behavior **before** tuning a model.
7. Build a baseline using simple lookup and template responses. Measure what AI improves compared with that implementation, rather than comparing it with having no program.

## Worked contract

```json
{"request_id":"demo-01","status":"answered","answer":"Four sessions cost 1000 cents.","source_ids":["price-v1"]}
```

This illustrates a format, not a verified answer. A reviewer must establish that `price-v1` exists, is permitted for this caller, and actually contains the price `250` per session. The same JSON with `900` in the answer could be structurally valid and factually wrong.

For `not_found`, do not invent a price. When two active documents disagree, do not silently pick the convenient one: surface the conflict or request clarification. Define rules for authority, validity dates, and version precedence before implementing retrieval.

## Demonstrate and extend

Show three cases where deterministic code is sufficient and one where you intend to test an LLM's contribution. Explain the difference between a prompt, a data contract, an access right, and a test.

**Independent challenge:** some documents now belong to another club. Identify every boundary that must preserve isolation: retrieval, cache, model context, output, and logs.

**Done:** another developer can explain what to build, which actions are prohibited, and which examples determine success. Record the decision in the [workbook](../WORKBOOK.en.md).

[Previous](01-foundations.en.md) · [Next: the model API](03-model-api.en.md)
