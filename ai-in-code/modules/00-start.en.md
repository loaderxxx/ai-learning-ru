# 00. Entry diagnostic and first run

[Русский](00-start.md) · [Learning map](../README.en.md)

**Outcome:** identify your starting point, run the teaching program, and explain exactly which components are still mocks. No API key or paid subscription is needed.

## Find your starting point

This route develops an AI application engineer, not a researcher training a foundation model from scratch. You will connect ordinary code, a model, data, and permitted actions. You still need to understand functions, types, exceptions, and tests.

Demonstrate rather than self-rate your prerequisites: can you read JSON from a file, write a function that validates its input, handle an error, run a test, and explain a Git diff? If not, study the relevant programming fundamentals first. The conversational AI lessons elsewhere in this repository **are not a replacement** for learning a programming language.

Choose one main language. The supplied lab uses Python and its standard library. An experienced developer may implement the same contracts in TypeScript, C#, Java, or Go. Learning five languages simultaneously is not required.

## Study in this order

1. New to programming: [CS50P](https://cs50.harvard.edu/python/), especially Functions/Variables, Conditionals, Loops, Exceptions, Unit Tests, and File I/O. Follow that course's academic rules. Our exercises are independent practice, not answers to its assessments.
2. Already a programmer, new to Python: [the official tutorial](https://docs.python.org/3/tutorial/), chapters 4–8 and 12. This tutorial assumes basic programming knowledge.
3. [Pro Git](https://git-scm.com/book/en/v2): Getting Started, Git Basics, and Basic Branching. Start with clone, status, diff, add, commit, and a branch you own.

## Complete a first pass

1. Open the [lab guide](../lab/README.en.md). Download the branch it specifies: these materials may not yet exist on `main`.
2. Run `python --version` and `git --version`. The teaching code needs Python 3.11+. Record your actual environment, not the version mentioned in a screenshot.
3. From the repository root, run `python -m unittest discover -s ai-in-code/lab -p 'test_*.py' -v`.
4. Run `python ai-in-code/lab/core.py`. Locate the `mock` label, calculation result, and step log.
5. Read `Model`, `ScriptedModel`, `run`, and `dispatch`. Follow how a model proposal turns into a call to an ordinary function.
6. Change the calculation inputs. Predict the result **before** running the code. Then supply an incorrect type and explain the rejection.

Your first deliverable is small: the command, environment version, one successful case, one rejected case, and a description of the data path. Use the [evidence workbook](../WORKBOOK.en.md).

## Work through an example

A teaching tool receives `{"unit_cents":250,"quantity":4}`. The expected result is `1000` cents. A model invocation may be probabilistic, but the multiplication belongs in deterministic code. The input `{"unit_cents":250,"quantity":true}` must be rejected: a Boolean is not an acceptable quantity even if your language allows that conversion.

ScriptedModel returns predefined messages. A successful run demonstrates program behavior on those scenarios. It does **not** demonstrate LLM quality, an OpenAI connection, or two live providers. Keep that distinction in your portfolio.

## Explain and verify

Without consulting a chat, explain who calls the model, who executes a tool, where arguments are checked, what is mocked, and what leaves the machine. In this starting example, nothing leaves the machine: it makes no network requests.

**Done:** you reproduced the run, changed a condition, obtained the expected result, and demonstrated rejection of bad input. If tests fail to start, check your working directory, Python version, and filename before asking AI to rewrite the project.

**Independent challenge:** add a negative-quantity test. Explain why removing validation merely to make a test green would defeat the purpose.

[Next: engineering foundations](01-foundations.en.md)
