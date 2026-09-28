# Lab: code → scripted model → permitted function

[Русский](README.md) · [Start learning](../modules/00-start.en.md) · [Learning map](../README.en.md)

**This lab needs no API key, third-party package, or network call. It is a mock demonstration, not a connected neural model.** Source: [core.py](core.py), [test_core.py](test_core.py).

## Start from a clean directory

You need Git and Python 3.11+. This release was tested on Python 3.13.5; other Python versions were not independently run. On Windows the command may be `py`; on macOS/Linux it may be `python3`. Check the actual version before substituting a command.

```bash
git clone --branch work/chatgpt/20260928-ai-in-code --single-branch https://github.com/loaderxxx/ai-learning-ru.git
cd ai-learning-ru
python --version
python -m unittest discover -s ai-in-code/lab -p 'test_*.py' -v
python ai-in-code/lab/core.py
```

Do not overwrite an existing working copy. Check `git status`, preserve your work, and obtain this branch in a separate directory/worktree. While this release remains on a work branch, downloading `main` does not include it.

## Expected behavior

The primary mock raises a transient failure. Code switches to the permitted backup mock. It proposes `calculate_total(250, 4)`, receives the real calculated result `1000`, and returns a predefined final sentence. Output includes `mode: mock`, `status: answered`, `model: mock-backup`, `attempts: 3`, and one `tool_completed` event.

Attempts are the failed primary, the successful backup proposal, and the backup's final reply. The reply text is scripted, not generated. Changing user text alone does not change the script; change the expected scripted scenario when constructing another exercise.

## Read the implementation

`Model` defines a minimal interface. `ScriptedModel` substitutes for a provider. `dispatch` constrains functions and arguments. `run` connects steps, fallback, tool results, and safe events. `seen` reuses results for an identical call ID within one run; it is not durable idempotency.

The two tools perform an exact calculation in cents and retrieve a fictional record with a tenant check. Tenant identity is supplied by a trusted application; the lab does not implement authentication. Size and numeric limits are teaching choices.

## Try these changes

1. Change quantity from four to five and update the expected final sentence. Obtain 1250.
2. Supply `True` or a string instead of a quantity. Observe contract rejection.
3. Request `beta-hours` as `alpha`. Confirm the content is not returned.
4. Repeat a call ID with identical and then changed arguments. Compare behavior.
5. Create an apparently endless script and reduce `max_steps`; locate the stop.
6. Replace TransientError with AccessError. Confirm the backup is never called.

## What is not implemented

There is no live LLM, HTTP service, MCP, embeddings/RAG, database, provider SDK, network deadline, streaming, persisted state, external write tool, or approval system. Final text is validated only structurally, not factually. A synchronous step cap cannot interrupt a hung external call; implement actual timeout/cancellation during stage 10. Events exclude raw prompts, but a real model's final answer would still require privacy checks.

**All 30 automated tests passed in the release-preparation environment.** They test this teaching code, not real-model quality. See [VALIDATION](../VALIDATION.md) for the exact scope.
