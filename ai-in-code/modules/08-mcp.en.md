# 08. MCP: connect a tool without confusing protocol and trust

[Русский](08-mcp.md) · [Learning map](../README.en.md)

**Prerequisite:** you can execute and constrain ordinary tools. **Outcome:** a small read-only MCP server with verified client interaction, or an explicitly labelled integration design if it has not been run.

## Why a protocol exists

MCP standardizes exchanges between AI applications and capability-providing servers. A host manages the user-facing application, a client maintains a server connection, and a server exposes tools and other resources. The model need not speak MCP directly: the host connects protocol operations to the model SDK.

A tool is an invokable operation, a resource provides context/data, and a prompt provides an interaction template. These are not three permission levels. Advertising a capability does not mean an application must authorize it for a caller or a model.

Use stdio for the local teaching server: a separate process exchanges protocol requests and responses through standard streams. Send diagnostics to stderr so they do not corrupt protocol stdout. For a network server, separately study Streamable HTTP, authentication, and authorization. “It runs on localhost” does not replace assessing the permissions of the process you launch.

## Read

1. [Official MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture): host/client/server, lifecycle, capabilities, and primitives. Record the specification version you actually implement.
2. [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices): trust boundaries, token handling, and client/server restrictions.
3. Optional Russian reference: the repository's [MCP module](../../developers/modules/07-mcp.md). For exact APIs, use the documentation of your selected official SDK.

## Practical exercise

1. Select an SDK through the official MCP documentation and record its version. Do not install an arbitrary similarly named package.
2. Build a server exposing only `lookup_public_note(note_id)`, reading three predefined synthetic records. Do not include file writes, shell execution, or arbitrary filesystem paths.
3. Validate inputs on the server even if the client uses a schema. Return a well-defined result or structured error.
4. Connect a compatible client. Demonstrate initialization, tool discovery, and one invocation. Save a sanitized protocol transcript and both component versions.
5. Try an unknown ID, an invalid type, and an unexpected argument. Ensure rejection does not expose the process environment.
6. Stop the server during a request. The client must stop waiting at its timeout and report technical failure.
7. Connect the tool to your model loop as a separate experiment. An MCP client operating without a model verifies the protocol path, not the entire AI workflow.
8. Document the transport, operations, process privileges, authentication, tests performed, and remaining verification gaps.

## Boundaries that matter

A server with a convincing description can still be untrusted. Its process needs minimum privileges. Do not blindly forward one service's token to another. For HTTP, study audience validation, request origins, address restrictions, and your protocol version's authorization requirements. A working stdio configuration is not a complete network security setup.

A `tools/list` response does not demonstrate successful execution. Show the actual `tools/call` result, server version, and a negative test. An ordinary Python function is not an MCP integration merely because its name includes “tool.”

**Independent challenge:** change the server's result format and detect the incompatibility with a contract test before connecting the new version to a model.

**Done:** provide a repeatable handshake and call, negative cases, timeout behavior, and an integration passport. Without execution, use `DESIGN ONLY`, not “MCP supported.”

[Previous](07-retrieval.en.md) · [Next: evaluations](09-evals.en.md)
