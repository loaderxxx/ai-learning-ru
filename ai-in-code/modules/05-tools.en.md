# 05. Tool calling: the model proposes, the application executes

[Русский](05-tools.md) · [Learning map](../README.en.md)

**Prerequisite:** an adapter and explicit failure behavior. **Outcome:** a bounded tool-calling loop that validates arguments, authority, and results.

## Trace the complete round trip

The application describes available functions. The model proposes a tool name, arguments, and a call identifier. The application validates the proposal, executes a permitted function, and returns its result with the matching identifier. The model may then produce a final answer or request another step. The application sets the step limit.

This differs from `summarize(text)`, an ordinary function that internally calls AI and returns text. In tool calling, the model selects a proposed action from an offered set. In the second case, ordinary code has already chosen the step. A simple task may not need an agent loop at all.

A tool schema constrains format; it does not grant authority. A valid `record_id` may still belong to another user. Tenant identity and permissions come from trusted application context, not model-generated arguments.

## Read

1. [OpenAI function calling](https://developers.openai.com/api/docs/guides/function-calling): tool definitions, call requests, application-side execution, and returning results.
2. [Claude tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview): compare the roles of requests and results. Do not move one SDK's JSON into another without translation.
3. [Gemini function calling](https://ai.google.dev/gemini-api/docs/function-calling): another representation of the same boundary. One provider is sufficient for the exercise.

## Implement the minimum safe loop

1. Allow only `calculate_total` and `lookup_record`. Do not expose arbitrary code, shell commands, SQL, or model-supplied URLs.
2. Define each function's name, purpose, input schema, and result. Reject unexpected fields; validate numeric types and ranges.
3. Use an explicit allowlist in the dispatcher. Avoid `eval`, dynamic imports, or arbitrary function lookup based on a model string.
4. Before `lookup_record`, check record ownership against the trusted tenant. Denial must not expose another tenant's content.
5. Return only the necessary data. Treat tool output as data, not fresh authority to change the system.
6. Bound model invocations and tool steps. Detect reuse of one call ID with different arguments.
7. Record a safe event log: request ID, model, tool name, and status. Exclude keys, full prompts, and private documents.
8. After offline checks, implement one provider round trip: model → tool request → application → tool result → final response. Without that execution, live tool calling remains unverified.

## Required cases

Valid calculation: 250 × 4 → 1000. Invalid type: `quantity=true` → reject. Unknown function `delete_all` → reject before execution. A valid ID belonging to another tenant → deny. Endless lookup proposals → stop at the step limit. A malicious instruction inside a retrieved record → no extension of the allowlist.

Keep the initial tools read-only or pure computations. Writing to a real system requires separate authentication, valid approval, idempotency, and owner authorization. The word “approved” in a model response is not human consent.

## Demonstrate the skill

Show the message sequence and call-ID correspondence, plus a test proving that a prohibited function never executed. A screenshot of an attractive final answer cannot establish that property.

**Independent challenge:** add `get_opening_hours` with two supported day values and rejection for the rest. Make the model request an unsupported day. Explain the difference between invalid arguments and missing knowledge.

**Done:** schemas and model text cannot override authority; final answers are distinct from tool requests; the loop is bounded; negative tests cover the boundaries.

[Previous](04-routing.en.md) · [Next: controlled workflows](06-workflows.en.md)
