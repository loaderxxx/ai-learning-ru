# 06. Orchestration: from functions to a stateful workflow

[Русский](06-workflows.md) · [Learning map](../README.en.md)

**Prerequisite:** a safe tool loop. **Outcome:** a process with explicit states, transitions, and stopping rules, followed by a comparable implementation in one framework.

## Start without a framework

Request Desk needs a small sequence: validate input → classify → retrieve permitted information or calculate → validate the result → prepare a response. The `not_found` branch ends without guessing. A technical failure ends with an explicit status. Writing or sending is not added automatically.

A workflow predetermines permitted transitions. An agent may choose its next step dynamically, but remains subject to program constraints. Additional complexity is justified only by a useful capability that simple functions do not provide as conveniently.

State means execution data: `request_id`, trusted identity, status, source IDs, tool results, counters, and errors. Do not put credentials or an unbounded chat into a shared object. Distinguish one run's state, long-term user memory, and a document collection.

## Read

1. [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview): state, nodes, and edges. LangGraph can be used independently of LangChain.
2. [Workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents): chaining, routing, and dynamic control. Choose one pattern for one problem.
3. [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence): checkpoints, threads, and recovery. Persisted state does not automatically make repeated external actions safe.

## Build two comparable versions

1. Draw a transition table: current state, condition, action, next state. Every path needs a terminal outcome.
2. Implement it in ordinary Python. Classification can use a mock or the stage-03 adapter. Retain this version as the baseline.
3. Add a step cap, an overall deadline, and an explicit `needs_approval` state for a proposed write that is not yet executed.
4. Prohibit direct transitions from untrusted text to a write tool. Bind approval to the exact action and arguments, not the entire conversation.
5. Install one framework in an isolated environment and record its version. Implement the same process using LangGraph or your stack's equivalent.
6. Run identical cases against both implementations. Outcomes and constraints must agree even if the internal machinery differs.
7. Add a checkpoint before a permitted stopping point. Terminate and resume the process. Identify which steps repeat and which must not.
8. Record what the framework added: clearer transitions, controlled interruption, persistence, or another concrete benefit. Concluding that it overcomplicated a simple scenario is a valid engineering result.

## Worked reasoning

For a question without evidence, `retrieve → not_found → finish` is better aligned with the specification than `retrieve → model guesses → answered`. An exhausted-budget path must terminate rather than re-enter retry.

After recovery, you cannot assume an email was not sent merely because the following checkpoint was not saved. Workflow memory and external side effects are separate systems. Stage 10 addresses that boundary.

## Explain and test

Explain what code determines, what a model selects, where state is stored, how the loop is bounded, and why chat history is not an authorization system. Demonstrate an error path and a paused path, not just success.

**Independent challenge:** add human review of a draft. Changing the draft must invalidate approval of the earlier version. Actual sending remains outside this exercise.

**Done:** terminal states are explicit, the baseline remains available, failure and recovery behavior are tested, and adopting a framework does not expand permissions.

[Previous](05-tools.en.md) · [Next: data and RAG](07-retrieval.en.md)
