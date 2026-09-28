# Официальные материалы / Official learning resources

[Русский маршрут](README.md) · [English pathway](README.en.md)

**Дата сверки / Review date: 2026-09-28.** Ниже первичные источники: документация авторов инструментов и учебные материалы их создателей. Мы прочитали относящиеся к маршруту разделы, а не все сайты целиком. Объяснения, упражнения, порядок, рубрика и учебные ограничения в этом репозитории — собственный учебный синтез; это не официальный курс перечисленных компаний.

**Review scope:** selected relevant official sections, not exhaustive website audits. Explanations, exercises, sequencing, rubrics, and teaching constraints here are our educational synthesis, not vendor certification. Read the section named in each chapter; do not attempt to finish every linked site before coding.

| ID | Primary source / первичный источник | Focus / что читать | Stages |
|---|---|---|---|
| S01 | [Harvard CS50P](https://cs50.harvard.edu/python/) | Functions, types, exceptions, tests, files / основы языка | 00 |
| S02 | [Python Tutorial](https://docs.python.org/3/tutorial/) | Data structures, modules, I/O, exceptions, environments | 00–01 |
| S03 | [Pro Git](https://git-scm.com/book/en/v2) | Git Basics, branching / изменения и ветки | 00–01 |
| S04 | [MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) | Requests, responses, headers, status codes | 01 |
| S05 | [Python asyncio](https://docs.python.org/3/library/asyncio-task.html) | Tasks, timeouts, cancellation / отмена и ожидание | 01, 10 |
| S06 | [Python unittest](https://docs.python.org/3/library/unittest.html) | Assertions, fixtures, discovery / запуск проверок | 01, 09 |
| S07 | [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) | Types, narrowing, unknown input | 01, 14 |
| S08 | [OpenAI quickstart](https://developers.openai.com/api/docs/quickstart) | SDK setup and a first request | 03 |
| S09 | [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs) | Schema support, refusal, incomplete results | 02–03 |
| S10 | [OpenAI function calling](https://developers.openai.com/api/docs/guides/function-calling) | Definitions and complete tool round trip | 05 |
| S11 | [OpenAI evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | Datasets, criteria, comparisons / оценка качества | 07, 09 |
| S12 | [Claude tool-use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) | Tool requests and results / другой формат API | 03, 05 |
| S13 | [Gemini function calling](https://ai.google.dev/gemini-api/docs/function-calling) | Function declarations and responses | 03, 05 |
| S14 | [LiteLLM introduction](https://docs.litellm.ai/docs/) | Python SDK versus proxy | 04, 14 |
| S15 | [LiteLLM routing](https://docs.litellm.ai/docs/routing) | Eligible routes, retries, fallback, timeouts | 04, 13 |
| S16 | [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) | State, nodes, edges / устройство графа | 06, 14 |
| S17 | [LangGraph workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents) | Chaining, routing, dynamic selection | 02, 06 |
| S18 | [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence) | Checkpoints and recovery / сохранение прогресса | 06, 10 |
| S19 | [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture) | Host/client/server, lifecycle, capabilities | 08 |
| S20 | [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices) | Trust boundaries and tokens / границы доверия | 08, 11 |
| S21 | [OWASP GenAI Top 10](https://genai.owasp.org/llm-top-10/) | Injection, data disclosure, excessive agency | 07, 11 |
| S22 | [AWS Builders' Library: idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) | Intent, request IDs, consistent mutation | 10 |
| S23 | [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) | Models, dependencies, errors, testing | 12 |
| S24 | [Docker getting started](https://docs.docker.com/get-started/) | Images, containers, configuration | 12 |
| S25 | [GitHub Actions Python](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) | Build/test workflow / автоматическая проверка | 12 |
| S26 | [OpenTelemetry traces](https://opentelemetry.io/docs/concepts/signals/traces/) | Spans and context propagation | 13 |
| S27 | [pgvector official repository](https://github.com/pgvector/pgvector) | Exact/approximate search and filtering | 07 |
| S28 | [Ollama API](https://docs.ollama.com/api/introduction) | Local inference interface / локальный запуск | 13 |
| S29 | [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) | Tools, handoffs, guardrails, tracing | 14 |
| S30 | [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/) | Current .NET/Python agent framework overview | 14 |
| S31 | [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/) | Existing-project architecture and SDK scope | 14 |
| S32 | [Pydantic AI](https://pydantic.dev/docs/ai/overview/) | Typed agents / типизированные границы | 14 |
| S33 | [DSPy](https://dspy.ai/) | Signatures, modules, metrics, optimization | 14 |
| S34 | [AI SDK: generating text](https://ai-sdk.dev/docs/ai-sdk-core/generating-text) | generateText and streamText | 14 |
| S35 | [AI SDK: tools](https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling) | Tool definitions, execution, loop controls | 14 |

## Границы проверки / Verification limits

S34–S35 reviewed through official indexed page excerpts: the direct AI SDK documentation root could not be fully fetched in this research environment. Their code was not installed or executed here. / Для S34–S35 прочитаны индексированные фрагменты официальных страниц; прямое чтение корня документации в среде исследования было недоступно. SDK здесь не запускался.

MCP documentation redirected to the 2026-07-28 documentation version during review. Stable documentation links are retained above; record your actual protocol/SDK version when implementing. / Во время сверки MCP направлял на версию документации 2026-07-28. Фиксируйте реально используемую версию.

Other links were opened for the relevant material; this does not establish that every example runs on every platform, that a package is vulnerability-free, or that pricing/access remains unchanged. Check the model, SDK, provider terms, and price at your own execution date. / Чтение источника не подтверждает запуск всех примеров, безопасность пакета или неизменность тарифов.

We do not copy complete third-party courses. Follow their licenses and academic rules. Primary documentation supports technical facts; the proposed exercises and assessment thresholds remain course design choices. / Полные чужие курсы не копируются; условия использования и правила выполнения заданий сохраняются.
