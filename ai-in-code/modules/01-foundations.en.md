# 01. Code, HTTP, JSON, concurrency, and tests

[Русский](01-foundations.md) · [Learning map](../README.en.md)

**Prerequisite:** stage 00. **Outcome:** a small, testable program with boundaries that can later accept a model adapter.

## Understand the mechanism

An AI application is still software. Input handling, validation, a network client, business logic, storage, and presentation sit between the user's request and the result. Mixing everything into one function makes provider replacement and failure testing unnecessarily difficult.

Start with four responsibilities: `domain` defines valid data and rules; `model_adapter` translates your internal request into a provider API; `tools` perform permitted operations; `application` controls the sequence. The lab is deliberately compact for reading. Split these responsibilities into modules when your project becomes hard to inspect; do not invent dozens of abstractions before you need them.

JSON is an exchange format, not a guarantee of valid meaning. The string `"4"`, number `4`, `null`, an empty list, and an absent field are different inputs. A Python or TypeScript annotation does not itself validate an untrusted network response at runtime.

Concurrency is useful while waiting for I/O. It does not remove the need for deadlines, cancellation, or bounded parallelism. Do not launch hundreds of model calls just because `gather` is available. First bound the queue and the number of active operations.

## Read, then implement

1. [Python Tutorial](https://docs.python.org/3/tutorial/): Data Structures, Modules, Input and Output, Errors and Exceptions, Virtual Environments. Implement the relevant exercise immediately after reading each section.
2. [MDN HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview): requests/responses, methods, headers, and status codes. Draw one POST request and one failure response.
3. [asyncio coroutines, cancellation, and timeouts](https://docs.python.org/3/library/asyncio-task.html): understand a sequential call before running two independent waits concurrently and cancelling them.
4. Alternative stack: [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html), particularly narrowing and handling unknown input.

## Guided exercise

1. Define a `Request` containing `request_id`, `tenant_id`, and `text`. Use synthetic data only.
2. Implement `validate_request`: reject empty text, non-string identifiers, and excessive input length. Choose and document the length limit as a teaching-project constraint, not a universal standard.
3. Add `calculate_total(unit_cents, quantity)`. Use integer minor currency units. Define bounds and reject Boolean values, negative values, and unexpected fields.
4. Define a model-client interface. The test implementation returns a scripted message or raises a specific exception. No network is needed yet.
5. Separate configuration from code. Put variable names and safe empty values in `.env.example`; exclude the real `.env` from Git.
6. Write positive and negative tests. Check result serialization and preservation of `request_id` separately.
7. Make a small change on your branch, inspect the diff, and save an informative commit.

## Worked check

For `unit_cents=199` and `quantity=3`, the result must be `597`. For `quantity="3"`, explicitly choose strict rejection or a documented conversion **before** the domain function. This course uses strict rejection to avoid hiding integration mistakes.

An empty response from an external service is not automatically a successful empty answer. Success, invalid input, and technical failure must be distinguishable by calling code without parsing a human-readable error sentence.

## Demonstrate understanding

Show a clean setup/run, the diff of one change, a failure test, and the place where a model adapter can be replaced. Explain how an exception, an HTTP status, and a business status differ.

**Independent challenge:** introduce a fake delay and an overall deadline. Demonstrate that a cancelled operation does not continue mutating state unnoticed. Do not use a paid live API to test this behavior.

**Done:** inputs are validated, deterministic calculations stay outside the LLM, the network client is replaceable, and failures can be reproduced by tests.

[Previous](00-start.en.md) · [Next: problem and contracts](02-contracts.en.md)
