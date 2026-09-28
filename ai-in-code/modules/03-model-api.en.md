# 03. Your first live model call and structured result

[Русский](03-model-api.md) · [Learning map](../README.en.md)

**Prerequisite:** a specification and a mock. **Outcome:** a replaceable model adapter, with live execution recorded separately from offline tests.

**Stage 03 sequence:** first API call on this page → [03A: context engineering and first evals](03a-context-and-evals.en.md) → [04: evidence-based routing](04-routing.en.md). Quality evaluation does not wait until stage 09.

## Understand the call

A remote model is a network service. Your program assembles instructions, input, and permitted context, submits them through an SDK or HTTP, receives a response, and validates it. The SDK is a client library, not the model. A chat-interface subscription is not evidence of API access: check your account's access and spending controls.

Your internal application result should not depend on an SDK's object type. Represent status, useful data, the actual model identity, usage when available, and technical failure. Do not report zero cost when usage is unavailable. Unknown and measured zero are different observations.

Apply three checks in order: the response completed; its structure meets the contract; its content is supported by the inputs. Refusals, interruptions, and output-limit exhaustion are not successful JSON responses. Structured output helps with shape, not the truth of each value.

## Study

1. [OpenAI quickstart](https://developers.openai.com/api/docs/quickstart): credentials, SDK installation, and a first Responses call. Alternatively, follow your available provider's official quickstart.
2. [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs): required fields, the supported JSON Schema subset, refusal, and incomplete output.
3. [Claude tool-use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) and [Gemini function calling](https://ai.google.dev/gemini-api/docs/function-calling): inspect how formats differ. Mastering all providers is not required at this stage.

## Step-by-step implementation

1. Create an isolated environment. Install the SDK from its official source, inspect its version, and record dependencies. Do not trust installation commands copied from an arbitrary chat.
2. Choose a model that your account actually permits. Put its identifier in configuration; an identifier in an article may not match your access.
3. Supply the credential through protected process configuration. Keep it out of Git, browser code, screenshots, logs, and commands stored in shell history.
4. Send one synthetic request such as `"Please explain the club opening hours"`. The allowed classifications are `faq`, `calculation`, `draft`, and `unknown`.
5. Obtain a classification with a brief explanation tied to the input. Validate types and allowed values. Record the prompt and schema versions in your experiment.
6. Inject the adapter into your application. Keep ScriptedModel for tests; make live integration tests an explicit, separate command.
7. Run five previously labelled examples and preserve every outcome, including failures. These are initial development cases for 03A, not an untouched final test set.

This starter fragment is for an isolated experiment. It is **not** a complete adapter, a tool-calling loop, or a live integration verified by this course release:

```python
import os
from openai import OpenAI

client = OpenAI(timeout=20.0, max_retries=0)
response = client.responses.create(
    model=os.environ["OPENAI_MODEL"],
    input="Classify this synthetic request: explain the club opening hours.",
)
print(response.output_text)
```

After the first run, replace the free-text response with a structured format using the provider documentation. The 20-second timeout is an example parameter, not a universal SLA. Set time and token limits deliberately for your task.

## Test failure behavior

Use a fake transport rather than spending money to induce errors: invalid credentials should produce a configuration error without an endless retry; timeout should produce a technical status; an unknown category should fail the contract; valid JSON with the wrong category should fail a quality check. JSON Schema alone cannot detect the last case.

Add streaming only after the non-streaming path works. Never execute a tool from partial argument fragments: wait for the completed message, then validate it. A partially displayed answer must remain labelled incomplete if the stream breaks.

**Ready for 03A:** provide a run command, SDK version, model identifier, five results, and an explicit `LIVE VERIFIED` or `NOT RUN` status. Without API access, complete the contract work and document the missing integration rather than presenting a mock as a live connection.

[Previous](02-contracts.en.md) · [Next: context and first evals](03a-context-and-evals.en.md)
