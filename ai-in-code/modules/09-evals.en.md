# 09. Evals: demonstrate improvement rather than assume it

[Русский](09-evals.md) · [Learning map](../README.en.md)

**Prerequisite:** a baseline and several scenarios. **Outcome:** a repeatable evaluation set, an error report, and evidence supporting one change.

## Separate the layers

A unit test checks a function. A contract test checks compatibility. An integration test exercises an actual connection. An eval measures AI-system behavior on tasks against quality criteria. None replaces the others.

Begin with the decision the experiment supports: for example, whether to adopt new retrieval or whether a lower-cost model damages calculation accuracy. Do not generate hundreds of requests without a question merely to obtain an impressive percentage.

Case counts and thresholds in this course are teaching choices, not industry standards or proof of production reliability. A small set finds known failure patterns; it cannot precisely estimate rare risks.

## Read

1. [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices): define a task, dataset, criteria, comparison, and continuing evaluation.
2. [Python unittest](https://docs.python.org/3/library/unittest.html): fixtures, assertions, and discovery. Use an equivalent runner when working in another language.
3. Optional Russian extension: the repository's [evals module](../../developers/modules/05-evals.md).

## Build a small evaluation set

1. Write 20 synthetic cases: eight ordinary, four unanswerable/ambiguous, four access-control or prompt-injection cases, and four format/transport failures. This is a starting teaching composition.
2. Record an ID, input, permitted sources, expected status, required facts, and prohibited actions for each case. Do not require one exact wording for every free-text answer.
3. Split the set into 12 development cases and eight held-out cases. Keep close paraphrases of one scenario together so near-duplicate examples do not leak across the split.
4. Tune code and prompts using development cases. Run held-out cases after selecting a variant; repeatedly tuning against them makes them another development set.
5. Run the baseline and then one changed variant. Record model, prompt/corpus/code versions, parameters, seed where supported, elapsed time, and cost or usage.
6. Measure status correctness, supported facts, access boundaries, prohibited actions, completion, and latency separately. A high average usefulness score must not hide a data leak.
7. For nondeterministic cases, repeat under the same protocol and report variation rather than only the best response.
8. Categorize errors as retrieval, generation, contract, tool, authorization, or transport. Fix the cause instead of reflexively lengthening the prompt.

## Human review and model judges

Start by manually reviewing several outputs against a rubric. A model judge can help scale evaluation but is not ground truth by definition. Check it against human-agreed examples, including persuasive but incorrect answers. Account for judge cost and possible sensitivity to length or style.

For example, a correct `source_id` combined with an incorrect price must fail the content check. `not_found` on a genuinely unanswerable question should pass even though it appears less helpful.

## Deliver evidence

Report: experimental question → baseline → change → all results → failures → limitations → keep or revert. State the denominator: “seven of eight held-out cases,” not simply “87.5% quality.”

**Independent challenge:** add a new enquiry category not present during tuning. Explain why success on the old dataset does not establish quality in the new domain.

**Done:** another person can reproduce the comparison, failures have not been replaced with selected successes, and critical violations are reported separately. Live-model evaluation and offline mock evaluation have distinct labels.

[Previous](08-mcp.en.md) · [Next: reliability](10-reliability.en.md)
