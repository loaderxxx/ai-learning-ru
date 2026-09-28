# 04. Multiple models: quality, adapters, routing, and fallback

[Русский](04-routing.md) · [Learning map](../README.en.md)

**Prerequisite:** stage 03 and [companion 03A — context engineering and first evals](03a-context-and-evals.en.md). Arriving through an old direct link? Complete 03A first. **Outcome:** task-specific quality evidence informs route selection; business logic is independent of SDKs. Testing mock routing does not establish live-model quality.

## What you are building

An adapter translates an application request into a provider format. A router chooses an eligible adapter. Fallback defines behavior after a particular failure. These are distinct responsibilities. Two models from one provider enable comparison but do not establish provider independence.

A shared interface does not make all models interchangeable. Tool/schema support, context limits, streaming, refusals, and data-handling conditions can differ. Check required capabilities and permissions before submission. Never remove a constraint merely to make fallback work.

## Eligibility and quality before economics

Use the matrix from 03A. Define the task category's allowed providers, necessary features, correctness requirements, latency limit, and budget. Select only among candidates meeting mandatory requirements. Then optimize cost/speed or additional quality according to the task's objective.

Calculations remain deterministic code. Choose a FAQ or extraction model from relevant evaluation evidence, not labels such as “simple,” “expensive,” or “smartest.” A general leaderboard or the model's self-confidence does not validate your application.

| Situation | Teaching router policy |
|---|---|
| Data may not be sent to a provider | Exclude it before invocation regardless of quality or price |
| A required format/tool is unsupported | Exclude it or use a separately verified compatible path |
| Quality fails the task-category criterion | Do not select it merely because it is cheaper |
| Several candidates meet requirements | Compare latency and complete cost per successful task; document the trade-off |
| Quality is unknown or no candidate qualifies | Clarify, stop, or escalate to a person; do not call an arbitrary choice a validated policy |

This is a teaching-project policy. Actual thresholds and eligibility belong to each system. A small eval set supports a provisional decision, not a guarantee of future responses.

## Read

1. [LiteLLM introduction](https://docs.litellm.ai/docs/): Python SDK versus proxy. An SDK or two small adapters is sufficient initially.
2. [LiteLLM routing](https://docs.litellm.ai/docs/routing): model groups, retries, fallbacks, and timeouts. Check your installed version's parameters.
3. [Context and first evals](03a-context-and-evals.en.md): capability matrix and admission criteria. [OpenAI Model selection](https://developers.openai.com/api/docs/guides/model-selection), Experiment: evaluate models and settings on your workflow.

## Build it step by step

1. Define `generate(request) -> result`; retain requirements and the actual provider/model used. Record the context-policy version.
2. Create two mock adapters to test rules. Label invented quality profiles as fixtures, not measured model performance.
3. Convert the 03A matrix into task-category eligibility configuration. Record each threshold's rationale, measurement, and date. Use only features available before the answer; the router cannot know future answer correctness.
4. Implement bounded fallback for classified transient failures. Backups must satisfy the same data, feature, and quality requirements. Invalid credentials or denied authority are not reasons to bypass controls.
5. Design post-response quality checks separately from transport fallback. Escalating to another model on a validated signal is a new branch with its own budget, tests, and permissions, not endless retry.
6. Test a cheap candidate below threshold, a capable but prohibited provider, no eligible route, a transient error, and a backup below threshold. Assert which adapters actually run and which must remain uncalled.
7. With authorized access, compare the entire router against a fixed model and the baseline on fresh cases. Include task-classification errors, all attempts, latency, and spending. Good individual models do not establish a good router.
8. Replace an adapter without changing domain rules and rerun contract checks. Mark missing live executions `NOT RUN`.

## Reason about failure

Model A received a request but its response was lost. Retrying generation may be permitted within budget, although the first attempt may already have incurred cost. No response from a write tool does not prove no effect occurred; stage 10 covers reconciliation and idempotency.

Fallback must not circumvent an authorization or policy refusal. If the backup is permitted but fails the required quality standard, a controlled stop/escalation is preferable to silently degrading service.

## Deliver and explain

Save `task_type → eligible_models → quality_evidence → latency/budget → fallback/escalation`, comparison results, and a passport for each verified live connection. Model, prompt, or context updates require rechecking the relevant evidence.

**Independent challenge:** reduce the cheap mock's quality profile for one category only. Other eligible routes should remain; this category must use a qualified alternative or stop.

**Done:** explain not only how to switch models but why the choice is justified by quality. Fallback is bounded, permissions do not expand, and mock/live evidence remains distinct.

[Previous: context and first evals](03a-context-and-evals.en.md) · [Next: tools](05-tools.en.md)
