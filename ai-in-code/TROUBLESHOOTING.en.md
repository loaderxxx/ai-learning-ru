# Glossary and troubleshooting

[Русский](TROUBLESHOOTING.md) · [Learning map](README.en.md)

## Keep the concepts separate

| Term | Meaning in this course |
|---|---|
| Model / LLM | A component producing responses from context, not the entire product |
| API / SDK | A service interface / client library for using it |
| Adapter | Translation between an internal contract and a specific API |
| Routing | A rule selecting a handler or model |
| Fallback | An eligible backup action after a defined failure |
| Tool calling | A model proposes a call; the application validates and executes it |
| Workflow / orchestration | Control of sequence, state, and transitions |
| Agent | A component using model-selected steps within program constraints |
| MCP | A capability-connection protocol, not authority or a model |
| Retrieval / RAG | Context search / generation using retrieved information |
| Embedding | A numerical representation used for similarity and related operations |
| Eval | AI behavior assessed on tasks against defined criteria |
| Idempotency | Repeating one intent does not create an additional intended effect |
| Trace | Connected events and operations belonging to a request |
| Mock | A substitute for a dependency, not evidence the real dependency works |
| Baseline | The reference implementation used to assess a change |
| Held-out | Cases not used to tune the selected variant |

## Diagnose before rewriting

| Symptom | Check first | Evidence of a fix |
|---|---|---|
| Python command missing | Executable name and installed version | Version output and one test |
| Tests not discovered | Working directory and `-s ai-in-code/lab` | Expected tests run, not “0 tests” |
| API access denied | Account, model permission, and credential configuration | One permitted synthetic live call; no exposed key |
| Repeated timeouts | Network, model, overall deadline, nested retries | Bounded completion time and an attempt log |
| Valid JSON, wrong answer | Labels, source data, and semantic checks | A factual check, not only JSON parsing |
| Tool proposed but never executed | Dispatcher and result/call-ID correlation | A full round trip and `tool_completed` |
| Endless loop | Terminal conditions and counters | An intentionally looping script stops at a limit |
| Fallback transfers prohibited data | Provider eligibility before submission | The prohibited route receives no request |
| Duplicate writes | Transaction, idempotency key, concurrency | One effect after retries and restart |
| RAG cites an old price | Document versions/status, index, cache | The right version or an explicit conflict |
| MCP server does not respond | SDK/protocol, stdout, handshake, timeout | Sanitized discovery/call transcript |
| Savings disappear | All attempts, judges, retrieval, failures | Cost of the complete successful task |
| Sensitive logs | Raw prompts, exceptions, headers, trace exporters | A fictional-secret regression test |
| Works only for its author | Hidden configuration and dependencies | Clean setup by another person |

## Ask a useful question

Include the stage, goal, command, version, minimal synthetic input, expected result, and observed result. Attach a sanitized traceback or event ID. Do not publish credentials, client documents, or entire private chats. First isolate the layer: input, adapter, model, retrieval, tool, workflow, or interface.

A useful AI-tutor request: “Explain this failure with a minimal example. Do not rewrite the whole project. Propose a test that distinguishes two possible causes.” Then explain the fix yourself and run a negative case.

[Workbook](WORKBOOK.en.md) · [First run](lab/README.en.md)
