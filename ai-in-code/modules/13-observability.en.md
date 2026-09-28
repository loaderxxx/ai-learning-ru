# 13. Observability, cost, and evidence-based optimization

[Русский](13-observability.md) · [Learning map](../README.en.md)

**Prerequisite:** a working CLI or service and an evaluation set. **Outcome:** one request ID reveals the technical path, spending, and evidence for an improvement.

## Questions your telemetry must answer

Which code and prompt versions ran? Which model was actually selected? Did fallback occur? Which tools were requested, and which executed? Where did failure occur? How many attempts were made, and how long did the request take? Answer these without storing every private document in a log.

Logs describe events, metrics aggregate measurements, and traces connect operations within a request. For a small project, start with JSON events and a report instead of buying an observability platform. A trace ID does not grant permission to read its contents.

## Read

1. [OpenTelemetry traces](https://opentelemetry.io/docs/concepts/signals/traces/): spans, context, and parent/child relationships. Start with one request, one model invocation, and one tool.
2. [LiteLLM routing](https://docs.litellm.ai/docs/routing): compare actual attempts with route, timeout, and fallback configuration.
3. [Ollama API introduction](https://docs.ollama.com/api/introduction): an optional local-inference path. A local endpoint alone does not prove that every other component avoids network transfer.

## Practical work

1. Define `request_started`, `model_started`, `model_failed`, `tool_requested`, `tool_completed`, and `request_finished` events. Keep requested actions distinct from completed actions.
2. Add request/trace ID, component version, safe route name, status, and duration. Exclude credentials, authorization tokens, and raw private inputs.
3. Run 20 teaching requests and report successes, abstentions, failures, p50/p95 latency, attempts, tool executions, and unknown usage. Percentiles from such a small sample are unstable; state the sample size.
4. Calculate cost per successful task: all accounted experimental costs, including failed attempts, retrieval, and judging, divided by successful tasks. With zero successes, the ratio is undefined, not zero.
5. Use the selected model's actual tariff on the date of your run. Record the tariff and its source in your report; this course does not prescribe a universal token price.
6. Compare one optimization: shorter context, another route, caching, or fewer steps. Use the same dataset and check quality, latency, and cache isolation.
7. Apply a pre-run budget and post-run accounting. An estimate does not guarantee the provider will charge precisely that amount.
8. Reproduce one failure from the event log and configuration. Do not rely on retaining deleted private material in verbose debug logs.

## Interpret the result

A faster variant that invents prices more often is not automatically better. If the first model routinely fails and invokes a backup, the allegedly cheap first step may increase total cost. Include all attempts, not merely the final successful call.

For a local model, record hardware, model/quantization, memory, latency, and network mode. No API bill does not mean no equipment or operational cost. Buying a new computer is not required for this chapter.

**Independent challenge:** implement sensitive-field redaction and a test that fails if a fictional credential appears in the serialized event log.

**Done:** telemetry explains the execution path, failures, and costs; unknown data is not replaced with zero; optimization is supported by a comparable experiment.

[Previous](12-delivery.en.md) · [Next: choose a specialization](14-specialization.en.md)
