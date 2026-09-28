# 15. Request Desk capstone and engineering conversation

[Русский](15-capstone.md) · [Learning map](../README.en.md)

**Outcome:** a small AI service another engineer can run, test, and discuss. This is a synthetic educational project, not unpaid client work.

## The assignment

Request Desk receives an enquiry for a fictional club. It identifies the task, retrieves permitted information, performs exact calculations with ordinary code, and prepares an evidence-backed answer. It abstains when information is missing and denies access to another tenant's data. The demonstration does not send emails, pay invoices, or modify real accounts.

Choose your main language. A Python [mock starter lab](../lab/README.en.md) is provided, but it is **not a completed capstone**. Retrieval, live providers, MCP, a database, an HTTP service, and persisted approvals are separate student implementations covered by earlier stages.

## Build through checkpoints

### A. Contract and baseline

Specify the user, inputs, outputs, constraints, and permissions. Prepare synthetic documents and labelled cases. Demonstrate a non-model baseline. Outcomes include `answered`, `not_found`, `needs_approval`, `invalid_input`, and `technical_error`; denial of another tenant's content must not disclose it.

### B. Models and tools

Add a common interface with two routes, at least one live provider when access permits, validated output, and read-only tools. Demonstrate a complete call-ID round trip. Two stubs are not two connected models; a second mock is acceptable only as an explicit remaining gap.

### C. Data and control

Add retrieval with ACL filtering before model context, citations, version rules, and abstention. Demonstrate a step cap, one permitted bounded fallback, a timeout, and negative tests. MCP is an extension with its own integration passport; a function name must not disguise an absent protocol implementation.

### D. Verification and handover

Run 20 labelled cases as described in stage 09, separating 12 development and eight held-out cases. Report failures, not just a success percentage. Provide clean-environment setup, safe logs, cost information, and rollback instructions. Another person should reproduce at least the local path.

## Acceptance scenarios

| Scenario | Observable expected behavior |
|---|---|
| Four sessions at 250 cents | The tool returns 1000; the answer cites the current price |
| No answer exists in the corpus | `not_found`, with no invented source |
| Two active documents disagree | Surface the conflict or apply a previously documented precedence rule |
| Another tenant's source | Its data never enters the caller's model context, output, or cache |
| `quantity=true` or an unknown tool | Reject before execution |
| Transient model failure | Bounded eligible fallback or a technical status |
| Data is prohibited from an external provider | No leakage through a backup route |
| Endless tool proposals | Stop at the configured limit with a clear reason |
| A document asks for wider permissions | The allowlist and trusted identity remain unchanged |
| A repeated local write in the extension exercise | One effect with key/argument checks, including after restart |

These are a testable educational minimum, not a complete security audit. A schema or valid source identifier verifies structure; supporting meaning still needs review.

## Bring to the conversation

Your repository or a private demonstration; startup README; a short architecture description; SDK/model/corpus versions; test and eval results; one successful and one failed request; disclosure of AI assistance during development; and known limitations. Do not publish someone else's private code or client documents.

The [workbook](../WORKBOOK.en.md) contains templates. For each skill, distinguish reading, reproduction, application, and explanation under a new condition. An honest boundary is more useful than a long list of library names.

## Demonstrate understanding

Without prompts, explain why a model is needed, what happens when it refuses, who executes tools, how authority is established, what tests do not cover, how a provider can be replaced, why valid JSON can be wrong, how to repeat a write safely, and which work should remain deterministic.

The reviewer changes one condition: another record format, an unsupported tool, or a new ambiguity. Localize the change and add a check rather than rewriting the application blindly.

**Ready for discussion:** a reproducible project with explainable limits. Completion is not a job guarantee, a diploma, or automatic access to real infrastructure. Experienced candidates may demonstrate an equivalent existing project instead of completing every chapter.

[Engineering invitation](../../engineers/README.en.md) · [Previous](14-specialization.en.md) · [Learning map](../README.en.md)
