# Looking for AI / LLM engineers

## Don't just use AI. Build systems that put it to work.

**We are looking for developers who can connect ordinary code, models, tools, and data into a controlled product. Already doing this? Show us your work. Still developing some skills? Follow the practical learning path and bring a working example.**

[Русское приглашение](README.md) · [Complete learning pathway](../ai-in-code/README.en.md) · [English repository hub](../README.en.md)

We are interested in an engineer who can explain the entire path: request → application logic → selected model → permitted function/API → validation → result. Prompting and AI-assisted coding are useful, but do not replace understanding the system.

## Core requirements and useful extensions

You do not need every language and framework below. One strong stack and demonstrable skills matter. Python or TypeScript fit the examples well; C#/.NET, Java, Go, and equivalent implementations are welcome too.

| Skill | Evidence that matters | Where to learn |
|---|---|---|
| **Core: programming** | Clear code, Git, HTTP/JSON, errors, tests, and data handling | [00–01: entry and foundations](../ai-in-code/modules/00-start.en.md) |
| **Core: architecture** | A defined problem, contract, constraints, and deterministic calculations outside the model | [02: contracts](../ai-in-code/modules/02-contracts.en.md) |
| **Core: LLM APIs/SDKs** | Model calls, structural and semantic checks, refusal and timeout handling | [03: model adapter](../ai-in-code/modules/03-model-api.en.md) |
| **Core: context engineering and early evals** | Relevant permitted context; task-specific quality measured before choosing a model | [03A: context and evaluation](../ai-in-code/modules/03a-context-and-evals.en.md) |
| **Core: models and routing** | A common interface; eligibility/quality before price optimization; qualified fallback | [04: multiple models](../ai-in-code/modules/04-routing.en.md) |
| **Core: tools and orchestration** | Validated arguments and authority, controlled steps and state | [05: tools](../ai-in-code/modules/05-tools.en.md), [06: workflows](../ai-in-code/modules/06-workflows.en.md) |
| **Core: system quality and security** | Regressions, fresh held-out cases, data boundaries, and safe retries | [09–11: system evals](../ai-in-code/modules/09-evals.en.md) |
| **Core: delivery** | Reproducible startup, safe telemetry, explicit limitations, and cost awareness | [12: delivery](../ai-in-code/modules/12-delivery.en.md), [13: observability](../ai-in-code/modules/13-observability.en.md) |
| **Useful extension: RAG** | Sources, versions, access filtering, retrieval, and factual checks | [07: retrieval](../ai-in-code/modules/07-retrieval.en.md) |
| **Useful extension: MCP** | A real read-only client/server integration and compatibility checks | [08: protocol](../ai-in-code/modules/08-mcp.en.md) |
| **One specialization** | LangGraph/LiteLLM, Agents SDK, AI SDK, Agent Framework, Pydantic AI, or DSPy | [14: choose one stack](../ai-in-code/modules/14-specialization.en.md) |

Operational experience is valuable when supported by a specific example: what failed, how you noticed, how you fixed it, and which test you added. Library names alone are not experience.

## Show a project, not just a list of technologies

A small project is enough: accept a task, assemble context, select a handler using measured quality and constraints, call a model through an adapter, execute one tool safely, validate output, handle failure, and leave a useful event log. Provide startup instructions, negative tests, and an explanation of why the chosen model fits the task rather than merely costing less.

A large commercial product is not required. Demonstrate equivalent existing work or the [Request Desk capstone](../ai-in-code/modules/15-capstone.en.md). Use synthetic data and do not publish someone else's confidential code. Mocks are valid teaching artifacts, but distinguish them honestly from live integrations.

## Missing some skills? Follow the route

**[Open the 16 core stages and companion 03A](../ai-in-code/README.en.md).** Each chapter includes an explanation, official resources, practice, completion criteria, and the next step. Start with the [no-key offline lab](../ai-in-code/lab/README.en.md). Learn to reproduce, change, and explain a result rather than simply copy a tutorial.

You do not have to finish the entire course before asking a question. Experienced developers can start with the capstone and fill specific gaps. New programmers should first follow the language foundations linked from stage 00.

## Introduce yourself

Reply to the person who shared this page. For a public technical introduction, you may [open a GitHub Issue](https://github.com/loaderxxx/ai-learning-ru/issues/new) titled `AI engineer — introduction`.

Briefly include your main stack, what you have built with AI, a project you are authorized to share or an offer of a private demonstration, your own contribution, and skills you are still learning. Do not post phone numbers, identity documents, addresses, API keys, or confidential data in a public issue.

The technical conversation focuses on code, architecture, failures, and working methods. Compensation, engagement format, location, and the specific role are to be discussed separately and have not been announced. A city shown in promotional artwork is not a promise of an office or relocation.

**Learn. Build a working example. Show how it works. Let's connect.**

Version 0.8.1 · 28 September 2026. This is an open invitation to a technical conversation, not guaranteed employment or a requirement to perform unpaid client work. The program is independent of programming schools and tool vendors.
