# Behavior-fit experiment v2

This experiment tests one adaptation method: behavioral contracts plus counterexample-guided micro-patching. It does not compare prompt lengths.

The intended contract, development cases, contrast cases, hidden cases, and answer keys were written and hashed before any execution. Sol, Terra, and Luna received the same source skill. Executors could not read keys, other runs, or hidden data during development.

## Observed gap and patch

The baseline produced one failure: Luna classified removal of a public webhook with unknown external-client compatibility as `side_effect` rather than `interface` (`cal-03`). Sol and Terra passed every development case.

Three independent patch proposers converged on the same C2 precedence rule. The accepted patch added one sentence:

> When public-interface compatibility and an external operational side effect both apply, classify the blocker as `interface`.

No model name, case answer, or whole-skill rewrite was added.

## Results

| Model | Development baseline | Development patched | Hidden baseline | Hidden patched |
|---|---:|---:|---:|---:|
| Sol | 18/18 | 18/18 | 12/12 | 12/12 |
| Terra | 18/18 | 18/18 | 12/12 | 12/12 |
| Luna | 17/18 | 18/18 | 12/12 | 12/12 |

All six development contrast cases stayed correct, and every run had zero output-shape violations. Removing P1 reproduces the recorded Luna development failure, providing the ablation evidence for retaining it.

The supported conclusion is narrow: P1 repaired the observed cross-model counterexample without an observed regression. Hidden runs establish non-regression, not uplift, because all three baseline hidden runs already passed. With one draw per case, this does not establish repeated-run reliability.

## Artifacts

- `source-skill.md`: unchanged baseline
- `candidate-skill.md`: baseline plus P1
- `intended-contract.md`: frozen C1–C3 behavior
- `fit-spec.yaml`: declared targets and acceptance rule
- `frozen-bundle.json`: pre-execution input hashes
- `candidate-freeze.json`: candidate and hidden hashes recorded before hidden execution
- `patch-ledger.json`: evidence and retention decision
- `results/`: raw blind executions
