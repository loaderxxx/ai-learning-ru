# 03A. Context engineering and first evals — before routing

[Русский](03a-context-and-evals.md) · [Learning map](../README.en.md)

**Position:** a required companion within stage 03, after the first API call and before stage 04. The 16 core-stage numbers and their existing URLs are preserved.

**Outcome:** reproducible context assembly, a small evaluation set, and evidence for selecting models by quality rather than price alone. A complete framework, MCP, and a vector database are not prerequisites.

## A. First decide what the model will see

Context engineering concerns more than prompt wording: select the information for each call, including instructions, the task, examples, relevant documents and history, tool descriptions, and earlier results. Read [Anthropic — Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), particularly the distinction from prompting and the anatomy of context.

Distinguish the context sent to a model from application state used to assemble it. Omitting a message from one request does not delete it from storage. Read [LangChain — Context engineering](https://docs.langchain.com/oss/python/langchain/context-engineering), especially Model Context, Data sources, and Transient/Persistent context. Implementing its middleware API is not required here.

### Design a context builder

Add `build_context(request, trusted_identity, records, history)` to Request Desk. This is a student implementation exercise, not an already implemented starter-lab function.

1. **Task and constraints.** Include the original question, output contract, and behavior when evidence is missing. Never put the evaluation set's expected answer into the prompt.
2. **Permissions and sources.** Filter records by trusted identity before model submission. Select relevant authorized records and retain IDs, versions, and validity status. Do not serialize API credentials or internal authority objects into model context.
3. **History.** Preserve current clarifications and unresolved questions rather than automatically sending everything. Label summaries as derived and retain source references for important conditions.
4. **Tools and results.** For now, identify which data will be needed. After stage 05, include only permitted tools and results relevant to the current step. A tool description does not authorize execution.
5. **Budget.** Allocate context space with room for output and an explicit reduction policy. Remove irrelevant material and duplicates first. Never silently drop the only supporting source or a task constraint. Clarify, split, or stop when required information cannot fit.
6. **Reproducibility.** Record the assembly-policy version, ordered source selection, and a safe configuration identifier. Retain assembled synthetic examples; do not turn private production text into a permanent debug archive.

### Worked teaching scenario

The current record `price-v2` says a session costs 250 cents. Archived `price-v1` says 200. There is an unrelated coffee note and another club's record. The question is: “What do four sessions cost now?”

Supply the permitted current price and question. Exclude the other club's record and irrelevant note. Do not present archived pricing as current. The grading reference is 1000 cents; the application performs multiplication in ordinary code. Remove the only current source and the correct outcome becomes missing verified pricing, not a confident guess. All data is fictional.

Prepare baseline and improved context policies. Compare them first **on one model with unchanged settings**. Changing model, prompt, and document selection simultaneously prevents attribution of an improvement. Do not deliberately violate access boundaries to create a bad baseline: both variants must enforce them.

### Negative cases

A missing source; conflicting active versions; a clarification lost during compaction; an instruction embedded in a document; and insufficient room for required evidence. Inspect both the outgoing packet and the answer. XML/Markdown boundaries help organize text but do not themselves enforce security.

**Deliver:** selection rules, two synthetic packets, results on identical tasks, and a case where shortening the context damages the outcome. The objective is sufficient relevant information, not the smallest possible string.

## B. Then measure candidate quality

Evaluation begins here, not after the entire system exists. Read [OpenAI — Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices), specifically Evals tips and Design your eval process: objective, data, criteria, and comparison. We use the methodology, not a requirement to adopt a particular hosted evaluation product.

### A small first evaluation

1. Extend stage 02's cases into 8–12 **development** examples: a direct question, paraphrase, ambiguity, absent evidence, conflict, structured extraction, and a prohibited request. This is a teaching size, not evidence of statistical reliability.
2. Before running, specify expected status, required facts, permitted source IDs, and critical violations. Wording may vary; fabrication and incorrect values remain checkable.
3. Assess schema/types, semantic correctness, source support, completeness, and appropriate abstention separately. Test access controls in application code: the model saying it refused does not establish server-side authorization.
4. Evaluate a non-model baseline first. Compare available models on identical tasks using the same context policy and comparable settings. Record prompt versions, model parameters, adapter formats, and unavoidable differences.
5. Report quality **by task category**, not only one overall average. A model may classify well but struggle with conflicting records. Use a short predefined rubric and human review for free text; the model's confidence statement is not a reliability measurement.
6. Keep all attempts, including timeouts, refusals, and wrong answers. Repeat ambiguous cases when budget permits. Do not retrospectively keep only the best response.
7. Freeze the proposed selection rule, then check it on a small fresh **validation** set that was not used for tuning. Once inspected, those examples are no longer an untouched test. Stage 09 requires fresh held-out cases for the complete system.

A minimal record:

```text
case_id | task_type | model/config | context_version | expected | actual
schema_ok | facts_ok | source_ok | critical_violation | attempts | latency | usage/cost
```

Record unavailable usage as `UNKNOWN`, not zero cost. Mocks test scoring and failure handling, not real-model quality. With one available API, compare context variants and leave the comparison between two live models unverified.

### What you need before routing

Produce a **task-category capability matrix**: where each model reaches the chosen standard, where it violates a mandatory criterion, and where evidence is insufficient. Include data-handling, feature, latency, and budget constraints. Set and justify thresholds before comparison; there is no universal passing percentage.

Illustration: A handles short FAQs adequately but fails the requirement for extraction from conflicting documents. B meets both requirements but is slower. A possible policy is FAQ → A and extraction → B. This is a **fictional example**, not a ranking of actual models. If neither qualifies, improve the context/task, request clarification, or escalate to a person rather than choose the cheapest inadequate option.

Read [OpenAI — Model selection](https://developers.openai.com/api/docs/guides/model-selection), especially Experiment: evaluate models and settings on your workflow. Our course policy is eligibility and required capabilities → sufficient measured quality → cost/latency optimization within task constraints.

## Independent check and progression

Explain which fact was missing from a failed request, how context improvements were isolated from model changes, and why a proposed route is eligible for a particular task type. A future router cannot use an unknown correct answer as an input feature.

**Done:** provide a context policy, labelled cases, results or explicit `NOT RUN`, model-admission criteria, and a justified draft route table. With mocks only, the proposed routes remain teaching hypotheses.

Later, [stage 09](09-evals.en.md) extends this foundation to regressions, tools/retrieval, complete-system evaluation, and fresh held-out cases. It remains in the curriculum rather than being duplicated or removed.

[Previous: first API call](03-model-api.en.md) · [Next: routing by quality and constraints](04-routing.en.md)

Companion version 0.8.1 · 28 September 2026. Sources support concepts; Request Desk, exercises, rubrics, and admission policies are original teaching design, not provider experiment results.
