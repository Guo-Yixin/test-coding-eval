# Initial cases

The first suite uses the `taskboard/` project at the baseline commit recorded in each JSON case.

| Case | Skill focus | Acceptance |
| --- | --- | --- |
| `taskboard-status-filter` | Requirement reading, focused edit, regression safety | Case-insensitive status matching and no input mutation |
| `taskboard-title-search` | Retrieval and implementation across existing code/tests | Case-insensitive title search, stable order, missing-title safety |
| `taskboard-priority-aliases` | Multi-condition change and test behavior | Priority aliases, stable ordering, explicit tests for edge cases |

Each run gets a fresh copy. `target_tests` are visible in this repository. The Agent is asked to extend the corresponding test file; the evaluator also runs an independent oracle stored with the evaluator, outside the candidate workspace. Since this repository is public, no claim is made that its visible tests are secret.
