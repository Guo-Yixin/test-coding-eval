# Test Coding Eval

An independent, versioned target repository for evaluating the CODING Agent. The Agent under test runs from the `coding-agent` project; this repository is the codebase it receives as its task workspace.

## Benchmark rules

- Every case pins a target commit and starts from a fresh copy.
- The task project is intentionally small so each result is easy to inspect.
- Target tests are visible and reproducible. They are not described as secret tests.
- The evaluator may run additional oracle checks outside the Agent workspace.
- Run reports, patches, databases, and model traces belong in the external Eval output directory, not in this repository.

## Task project

`taskboard/` is a dependency-light Python package used for focused code tasks. See `cases/README.md` for the initial cases and the pinned task baseline.

## Scope

This benchmark checks selected coding tasks and their observable evidence. Passing it does not prove that every feature of CODING or every possible repository has been evaluated.
