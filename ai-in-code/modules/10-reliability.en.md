# 10. Reliability: deadlines, retries, idempotency, and recovery

[Русский](10-reliability.md) · [Learning map](../README.en.md)

**Prerequisite:** explicit states and failure tests. **Outcome:** bounded failure handling without endless loops or duplicated side effects.

## Distinguish two problems

Repeating generation may increase latency and cost. Repeating a write may create duplicate tickets, notifications, or payments. Applying one generic retry wrapper to both is dangerous.

Define an overall request deadline, then bound attempts, individual-call time, and remaining budget within it. Nested retries multiply: three SDK attempts inside three application attempts can produce nine calls. Choose which layer controls retries and disable or explicitly account for the others.

Invalid credentials and missing permissions are not fixed by waiting. A transient overload may justify a bounded delay and retry, respecting server guidance. Do not retry every exception indefinitely.

## Read

1. [AWS Builders' Library: retries and idempotency](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/): identifying intent, repeated requests, and consistent writes.
2. [asyncio tasks and cancellation](https://docs.python.org/3/library/asyncio-task.html): cancellation, timeouts, and cleanup.
3. [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence): persisted progress must be combined with safe external-effect handling.

## Exercise — local storage only

1. Replace the transport with controlled outcomes: transient failure, permission denial, timeout, and success. Specify the expected number of attempts for each.
2. Add capped backoff and jitter to the network implementation. Inject a clock/sleeper in tests instead of introducing long real delays.
3. Create a SQLite table for fictional tickets. Writes stay local and contain no personal information.
4. Introduce an idempotency key tied to tenant and specific intent. Store normalized arguments or a stable hash. Reusing the key with different arguments must cause a conflict rather than returning an unrelated earlier success.
5. Record the mutation and deduplication data in one transaction, backed by a unique constraint. Checking “key not present” before a separate write is vulnerable to races.
6. Simulate losing the acknowledgement after commit. Repeating the same key returns the completed intent's result rather than creating another row.
7. For an external API with an unknown outcome, design reconciliation. Do not promise exactly-once execution based on a local dictionary; consider a transactional outbox and the receiving system's guarantees.
8. Bind human approval to exact arguments, identity, and expiry. A changed action invalidates earlier approval.

## Required scenarios

Two identical sequential requests; two concurrent requests; an old key with a changed amount; failure before commit; a crash after commit but before response; expired approval; and an exhausted overall deadline. For each, report the number of actual writes and the final status.

The starter lab only deduplicates read-only/computational tool calls within one process. That demonstrates a mechanism, but does not survive restart and does not implement this SQLite exercise.

**Independent challenge:** restart the process after a completed write and repeat the request. Demonstrate that correctness does not depend on the old Python process's memory.

**Done:** attempts are bounded; authorization failures do not trigger retries; one repeated intent does not duplicate a local effect; an unknown external outcome remains unknown until reconciled. Describe the scope of the guarantee instead of promising that failures cannot happen.

[Previous](09-evals.en.md) · [Next: security](11-security.en.md)
