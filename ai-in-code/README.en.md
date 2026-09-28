# AI Inside Software — the AI / LLM engineering pathway

**From an ordinary function to a verifiable AI service: 16 stages with explanations, sources, exercises, and completion criteria.**

[Русская версия](README.md) · [Who we are looking for](../engineers/README.en.md) · [English program hub](../README.en.md)

> Go beyond receiving code from AI. Build software that calls models, uses permitted tools, checks results, and behaves predictably when something fails.

## Start here

**Your first action: [stage 00 — diagnostic and first run](modules/00-start.en.md).** Open the [lab guide](lab/README.en.md), run the example without an API key, and trace one request. Then follow the “Next” link at the bottom of each chapter.

Already building these systems? Read the [capstone brief](modules/15-capstone.en.md), demonstrate an equivalent existing project, and study only identified gaps. Completing every chapter is not required to start a technical conversation.

## Audience and prerequisites

For developers, programming-school students, and graduates who want to integrate LLMs into applications. You need functions, basic types, exceptions, file handling, and the ability to run a test. Stage 00 links to programming foundations when those skills are missing. The repository's introductory conversational-AI course is not a programming course.

The teaching example uses Python; one language is enough. [Specialization routes](modules/14-specialization.en.md) cover TypeScript, C#/.NET, and Java alternatives. A computer is needed for code; reading can be done on a phone. Without paid API access, complete offline exercises and explicitly record the unverified live integration. You do not need every tool subscription or new hardware.

## Use the same learning loop

**Understand the mechanism → read the selected sections → reproduce an example → build your version → introduce a controlled failure → verify → explain → move on.**

Each stage includes an outcome, resources, implementation steps, failure cases, and an independent change of condition. Use the [workbook](WORKBOOK.en.md) to record code version, command, result, limitation, and explanation. “Read,” “reproduced,” and “can apply independently” are different levels of evidence.

## The complete sequence

| Stage | Topic and reading | Evidence to produce |
|---|---|---|
| 00 | [Diagnostic and first run](modules/00-start.en.md) | A mock-lab run and an explanation of valid and invalid input |
| 01 | [Code, HTTP, JSON, concurrency, and Git](modules/01-foundations.en.md) | Validated functions, tests, and a reviewable diff |
| 02 | [Problem, architecture, and contracts](modules/02-contracts.en.md) | A specification, labelled cases, and a non-AI baseline |
| 03 | [Model API and structured output](modules/03-model-api.en.md) | A replaceable adapter and separately verified live call |
| 04 | [Multiple models, routing, and fallback](modules/04-routing.en.md) | A common interface and safe route-selection rules |
| 05 | [Tool / function calling](modules/05-tools.en.md) | A complete round trip, call IDs, allowlist, argument checks |
| 06 | [Workflow, state, and orchestration](modules/06-workflows.en.md) | Explicit states, stops, interruption, and a baseline comparison |
| 07 | [Retrieval, documents, and RAG](modules/07-retrieval.en.md) | Sources, versions, ACL filtering, and abstention |
| 08 | [MCP and external tools](modules/08-mcp.en.md) | A read-only server, handshake, call, compatibility passport |
| 09 | [Evals and regressions](modules/09-evals.en.md) | Development/held-out cases and a comparative error report |
| 10 | [Reliability and idempotency](modules/10-reliability.en.md) | Bounded retries and a local write surviving repeated requests |
| 11 | [Security and privacy](modules/11-security.en.md) | A threat model and execution/data-boundary tests |
| 12 | [Service API, CI, and delivery](modules/12-delivery.en.md) | Clean setup, tests, configuration, and local rollback |
| 13 | [Observability, cost, and optimization](modules/13-observability.en.md) | Request traces and quality/latency/cost comparisons |
| 14 | [Stack and specialization](modules/14-specialization.en.md) | One justified framework choice or component migration |
| 15 | [Request Desk capstone and review](modules/15-capstone.en.md) | A repository, evidence, demonstration, and adaptation to a new condition |

Numbers describe dependencies, not calendar dates. Progress by outcomes, not an invented deadline. For a first small project, concentrate on 00–06 plus basic testing and security; add MCP, advanced retrieval, and specialization after the core works. The complete route supports a broader engineering portfolio, not a promise of qualification within a fixed number of days.

## What you build

**Request Desk** is a fictional club's enquiry service. It chooses a permitted handler, retrieves reference information, calculates with ordinary code, and prepares an evidence-backed response. Unknowns remain unknown. Another tenant's data stays out of context. Limits stop cycles. Writing and sending require separate authority mechanisms.

The included lab implements **only an offline core**: ScriptedModel, two mock routes, a calculation, tenant-checked lookup, structural validation, limits, and events. You implement HTTP, live SDKs, MCP, RAG, and durable idempotency through the exercises. See the [verification record](VALIDATION.md).

## Supporting resources

[Workbook and review rubric](WORKBOOK.en.md) · [Glossary and troubleshooting](TROUBLESHOOTING.en.md) · [Official sources](SOURCES.md) · [Lab commands](lab/README.en.md) · [RU/EN maintenance policy](MAINTENANCE.md)

Older materials elsewhere in the repository remain primarily Russian: [developer track](../developers/README.md), [advanced AI-assisted coding](../advanced/README.md), [practical missions](../practical/README.md), and [local models/team comparisons](../next/README.md). They are optional extensions, not untranslated prerequisites hidden inside this English route. They have not been replaced or presented as fully translated.

## Completion means evidence

Show working code, negative tests, an evaluation report, and your own explanation of decisions. One successful answer is not proof of production readiness. Completion is not certification, guaranteed employment, or authorization to access private systems.

**Ready to show your work? [Read the engineering invitation](../engineers/README.en.md).**

Version 0.8 · 28 September 2026. RU/EN cover the same 16 stages. Materials are prepared; learner outcomes and live integrations have not been validated by this release.
