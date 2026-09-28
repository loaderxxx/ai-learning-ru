# Engineering workbook: knowledge supported by evidence

[Русский](WORKBOOK.md) · [Learning map](README.en.md)

Keep your workbook in your own repository or notes. You do not need to upload personal information, entire chats, or other people's work to this public teaching repository. Short records that support reproduction and explanation are enough.

## 1. One stage record

```text
Stage / date:
Skill being practised:
What I could already do:
Reading completed (specific section/link):
My own implementation:
Where AI helped and how I checked its output:
Code version / commit:
Environment and dependencies:
Run command:
Positive case / observed result:
Negative case / observed result:
New condition tested:
What remains broken or unverified:
My explanation of the mechanism in 3–5 sentences:
Next step:
```

Do not fill missing evidence with assumptions. “API not run” is accurate; “API works because an adapter exists” is not.

## 2. Integration passport

| Field | Record |
|---|---|
| Components | Client, server/provider, SDK, and versions |
| Model | Exact configured and returned identifiers; distinguish claims from observations |
| Transport | HTTP/stdio/local process; endpoint with no credentials |
| Mode | MOCK / CONTRACT TEST / LIVE VERIFIED / DESIGN ONLY / NOT RUN |
| Capabilities | Structured output, tools, streaming, or MCP actually exercised |
| Data | Synthetic or explicitly authorized inputs, tenant boundary, permitted transfer |
| Limits | Timeout, overall deadline, maximum calls/steps, eligible fallback |
| Evidence | Command, date, sanitized transcript/result, code version |
| Failure | One reproduced failure and the application's response |
| Cost | Measured usage/spending or UNKNOWN; do not substitute zero |

Do not include API keys, tokens, or complete authorization headers. Reviewers do not need access to your provider account.

## 3. Architecture decision card

```text
Problem:
Option A (simplest solution):
Option B:
Criteria: quality / cost / complexity / security / compatibility
What sources establish:
Our hypothesis:
Small test performed:
Result and limitations:
Selected option and rationale:
Condition for reconsideration:
```

Example: “Do five fixed steps need LangGraph?” Either conclusion is acceptable when supported by a comparison. Do not choose complexity merely to add a technology to a résumé.

## 4. Experiment table

Fix the question, corpus, and scoring rule before execution. Keep one row per case, including failures.

| case_id | split | expected | actual | sources permitted? | facts correct? | prohibited action? | attempts | latency | usage | failure |
|---|---|---|---|---|---|---|---|---|---|---|
| demo-01 | dev | answered | fill after execution | — | — | — | — | — | — | — |

The row is a template, not an observed result. Do not change expected behavior after seeing an output just to make it match. If a label is genuinely wrong, document the correction and rerun both compared variants.

## 5. Small threat model

| Asset | Untrusted input | Potential harm | Enforced control | Negative test | Residual risk |
|---|---|---|---|---|---|
| Tenant records | Model-proposed ID | Another tenant's data disclosed | Server-side authorization before model context | Request another tenant's ID | Record separately |

This is a teaching example. A table does not prove that its control exists: attach a test or mark it `NOT IMPLEMENTED`.

## 6. Skill levels and review

| Level | Observable behavior |
|---|---|
| L0 — exposed | Recognizes the term; no practice yet |
| L1 — assisted | Explains or performs with substantial help |
| L2 — reproduces | Runs a supplied example and describes it |
| L3 — applies | Solves a similar task independently and tests failures |
| L4 — adapts | Handles a new condition and explains trade-offs and limits |
| L5 — teaches/systematizes | Helps another person reproduce the skill and improves a tested method |

This is an internal teaching rubric, not official certification. Assess **individual skills**, not the entire course at once. Distinguish self-assessment from another person's review. An honest L2/L3 demonstration in selected topics can support an initial technical conversation; collaboration is not decided by an automatic total score.

## 7. Demonstration packet

Provide startup instructions, a short architecture description, chosen stack, one working scenario, three negative cases, eval results, a live/mock passport, known limitations, and a small adaptation to a new condition. An equivalent existing project is welcome; repeating the full teaching project is not mandatory.

[Capstone](modules/15-capstone.en.md) · [Invitation](../engineers/README.en.md)
