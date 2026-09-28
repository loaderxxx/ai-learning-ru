# 14. Choose a stack and specialization, not every framework

[Русский](14-specialization.md) · [Learning map](../README.en.md)

**Prerequisite:** the common engineering route. **Outcome:** one chosen specialization, an implemented migration or extension, and an explanation of trade-offs.

## Transferable skills come first

We are interested in the ability to build a verifiable system. You do not need simultaneous mastery of Python, TypeScript, C#, Java, LangGraph, every SDK, and several databases. Choose one main stack and demonstrate contracts, tools, state, security, evaluation, and delivery.

First solve a problem with an ordinary SDK. Add an abstraction when it reduces a specific difficulty. Neither framework count nor agent count is a measure of engineering ability by itself.

## Choose one route

| Direction | Study | Demonstrate |
|---|---|---|
| Python, controlled workflows | [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview), optionally [LiteLLM](https://docs.litellm.ai/docs/) | Explicit workflow states and a replaceable model |
| Python, agent runtime | [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) | Tools, constraints, result handling, safe tracing |
| TypeScript, AI applications | [AI SDK text generation](https://ai-sdk.dev/docs/ai-sdk-core/generating-text), [tools](https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling) | A backend with tools and correct streaming/cancellation |
| C# / .NET | [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/) | Typed boundaries, tools, state, and tests |
| Existing C#/Python/Java systems | [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/) | Understanding the installed SDK and a justified compatibility plan |
| Python, typed agents | [Pydantic AI](https://pydantic.dev/docs/ai/overview/) | Validated inputs/outputs, dependency injection, contract tests |
| Python, programmable AI functions | [DSPy](https://dspy.ai/) | Signatures/modules, a metric, and before/after optimization evidence |

At the review date, Microsoft's documentation describes Agent Framework as a successor to Semantic Kernel and AutoGen. Study the current route for a new .NET project; do not describe an existing project's migration as complete without checking its implementation. Do not automatically transfer Semantic Kernel's language-support list to another framework.

DSPy is particularly relevant to “an ordinary program containing an AI-powered function”: define inputs/outputs and compose modules, then potentially optimize the program against a metric. This is an additional specialization, not a replacement for tests, permissions, or understanding provider APIs.

## One elective exercise

1. Keep the Request Desk specification and evaluation dataset fixed.
2. Select one tool from the table and name the problem it should solve.
3. Read its official quickstart and the relevant operation guides. Record SDK and model versions.
4. Port one component rather than rewriting everything. Preserve the baseline.
5. Run the same tests and evals. Compare clarity, code volume, repeatability, latency, and cost.
6. Record a decision: adopt, defer, or reject, with a condition for reconsideration.

## Not required for the first conversation

For multi-agent work, compare one executor with two roles on identical tasks, including coordination cost. RAG and fine-tuning address different problems: supplying context is not changing weights. Fine-tuning, training custom models, GPU clusters, Kubernetes, and A2A are possible later directions, not prerequisites for this program.

**Independent challenge:** replace the framework with ordinary code for one scenario. Explain which capability you lost and which part became simpler.

**Done:** demonstrate one working stack, understand alternatives, and distinguish reading a tutorial from operating a system.

[Previous](13-observability.en.md) · [Next: capstone](15-capstone.en.md)
