# 12. Turn a prototype into a reproducible service

[Русский](12-delivery.md) · [Learning map](../README.en.md)

**Prerequisite:** contracts, tests, and a threat model. **Outcome:** another person can start the service in a clean environment, verify a change, and understand how to roll it back.

## Beyond an IDE demonstration

A successful IDE run does not establish service readiness. Configuration, dependencies, incoming requests, concurrent users, interface failures, and upgrades become part of the system. Do not introduce Kubernetes merely to run a teaching endpoint. Start with the simplest reproducible setup.

An HTTP API accepts data but must not treat a submitted `tenant_id` as proof of identity. A clearly labelled teaching identity is acceptable for a demo; real use requires server-side authentication. Model credentials remain on the server, not in browser JavaScript.

With streaming, distinguish “text arriving,” “response complete,” and “action executed.” A displayed fragment is not a completed result and must not trigger a tool. Long operations may benefit from job IDs and status tracking, but entering a queue is not evidence of completion either.

## Read

1. [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/): request bodies, response models, dependencies, errors, and testing. This is one Python route, not a mandatory framework for every language.
2. [Docker getting started](https://docs.docker.com/get-started/): images, containers, builds, volumes, and configuration. Containerization alone does not prove security.
3. [GitHub Actions: build and test Python](https://docs.github.com/en/actions/tutorials/build-and-test-code/python): test changes automatically. Check action versions and permissions before publishing a workflow.

## Implementation sequence

1. Add `/health` without exposing configuration and `/requests` with explicit input/output contracts. Do not return raw exception contents to callers.
2. Inject the model adapter through configuration. The teaching service defaults to a clearly labelled mock mode.
3. Write a README covering environment requirements, installation, tests, startup, an example request, expected response, shutdown, and limitations.
4. Record dependencies. Supply `.env.example` with safe empty values. Check the archive/repository for credentials.
5. Test the HTTP contract: valid request, malformed JSON, excessive input, technical failure, and invalid identity. The default test command must not call providers.
6. Add minimal CI: installation, static checks, unit/contract tests. Live tests need a separate explicit run, approved data, and a budget. Do not expose credentials to untrusted pull requests.
7. If useful, build a local container running without unnecessary privileges. Bind the teaching service to loopback rather than exposing it to the internet.
8. Ask a reviewer to run the project, or repeat setup in a clean directory. Record and fix deviations from the instructions.
9. Document rollback: a known commit, configuration version, shutdown sequence, data recovery, and post-rollback checks. Execute the teaching rollback locally.

## Acceptance

A reviewer should receive the expected response, observe a controlled error, run tests, and understand how a real provider is enabled. A public deployment is not required. Publishing an endpoint can incur cost or expose information and therefore needs a separate decision.

**Independent challenge:** support cancellation from an interface. Check what happens to server-side work; closing a browser tab does not prove the backend stopped.

**Done:** clean setup is reproducible, mock mode is explicit, tests do not spend money, secrets are separated from configuration, and rollback has been documented and locally tested. Writing CI YAML is not equivalent to observing a successful remote CI run.

[Previous](11-security.en.md) · [Next: observability and economics](13-observability.en.md)
