# 04. Multiple models: adapters, routing, and fallback

[Русский](04-routing.md) · [Learning map](../README.en.md)

**Prerequisite:** stage 03 or its offline contract work. **Outcome:** business logic is independent of a particular SDK, and selection/fallback rules are testable without a network.

## What you are building

An adapter translates your application's request into a provider format. A router chooses an eligible adapter. A fallback policy defines what happens after a particular failure. These are three distinct responsibilities. Two models from one provider enable comparison; they do not establish provider independence.

A common interface does not make every model interchangeable. Tool support, schemas, context limits, streaming, refusal formats, and data-handling conditions may differ. Your contract must either use shared capabilities or explicitly check required capabilities. Never remove a security constraint to make fallback succeed.

Begin with a simple rule: calculations go to deterministic code; short classifications to available model A; more involved drafting to model B. This is a teaching hypothesis, not a claim that a particular model is cheaper or better. Test the rule on the same inputs.

## Read

1. [LiteLLM introduction](https://docs.litellm.ai/docs/): distinguish the Python SDK from a separately deployed proxy. Start with the SDK or two small adapters of your own.
2. [LiteLLM routing](https://docs.litellm.ai/docs/routing): model groups, retries, fallbacks, and timeouts. Check parameters against your installed version rather than copying an old configuration blindly.
3. Revisit the [model API contract](03-model-api.en.md): structure, refusals, usage, and failures must have consistent meaning to calling code.

## Build it step by step

1. Define `generate(request) -> result`. Include format and permitted-route requirements; retain the provider/model actually used in the result.
2. Create two mock adapters. One can raise a transient error; the other returns a valid response. Test routing without credentials.
3. Configure each route's capabilities and permitted data categories. User-supplied text must not alter those permissions.
4. Implement one bounded fallback for explicitly classified transient failures. Invalid credentials, prohibited data transfer, and contract violations must not silently send the request to another party.
5. Integrate one live provider and test it separately. Connect a second only when access and data-transfer conditions permit it.
6. Compare ten identical synthetic tasks: outcome, latency, attempts, usage, and failures. Do not select a model solely from its most attractive answer.
7. Replace one adapter without changing a domain function. Show the diff and rerun the contract suite.

## Reason about a failure

Model A received the request, but the connection failed before a response arrived. Retrying pure generation may be acceptable within a budget, although the first attempt may already have incurred cost. For a state-changing tool, a missing response does not prove that the action did not occur. Stage 10 covers reconciliation after this situation.

Fallback must not circumvent an explicit refusal based on permissions or policy. Its purpose is resilience of an authorized process, not finding a provider willing to perform a prohibited action.

## Deliver and explain

Save the route table, two failure scenarios, and an integration passport for every live connection. Label a stub `MOCK` and an unexecuted adapter `NOT RUN`. Describe two models behind one API accurately as “two models from one provider.”

**Independent challenge:** add a requirement that a particular category of data must not leave the permitted environment. If no eligible route is available, stop rather than using a prohibited backup.

**Done:** model selection is explainable, fallback is bounded, live calls are distinguished from mocks, and changing an SDK does not change business rules.

[Previous](03-model-api.en.md) · [Next: tools](05-tools.en.md)
