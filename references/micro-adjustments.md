# Evidence-backed micro-adjustments

A patch changes the smallest instruction span that plausibly controls one observed behavior gap. Instruction density is not a global setting.

## Patch operators

| Observed gap | First local operator |
|---|---|
| Required action omitted | Make one outcome observable with a MUST |
| Boundary decision is wrong | Add or sharpen one if/then boundary |
| Correct actions occur in the wrong order | Add the minimum ordering dependency |
| Output shape drifts | Add a literal schema or deterministic validator |
| Model asks unnecessarily | State what information is non-blocking or add one contrast case |
| Model assumes a material fact | Name the missing fact that must trigger a question |
| Tool is called too early or too late | Add one tool precondition or completion check |
| Instruction causes overfitting or rigidity | Remove, narrow, or replace it with an outcome constraint |
| Mechanical error repeats | Move the invariant into a script or executable check |

Do not automatically add detail. Deleting a distracting instruction, changing its placement, separating two conflated rules, or replacing prose with a validator may be the smaller repair.

Reject a patch whose rationale is a model name or assumed tendency rather than observed cases and contract IDs. A patch must not intentionally alter behavior outside its named contract IDs.

## Patch record

Record each candidate independently:

```json
{
  "patch_id": "P3",
  "contract_ids": ["C4"],
  "targets_with_gap": ["target-b"],
  "evidence_cases": ["cal-07", "cal-11"],
  "instruction_span": "Decision boundaries / paragraph 2",
  "operation": "sharpen-boundary",
  "before": "Ask when important information is missing.",
  "after": "Ask only when the missing fact can change the requested output or authorized side effect.",
  "expected_effect": "Stop asking about reversible implementation choices.",
  "failing_cases_pass": true,
  "contrast_cases_pass": true,
  "cross_target_regression": false,
  "kept_after_removal_test": true
}
```

## Candidate acceptance

Keep a patch only if:

1. the targeted failure is repeatable or affects a critical invariant;
2. the patch fixes the named calibration cases;
3. nearby contrast cases still behave correctly;
4. every previously passing target × contract × case cell remains within its predeclared non-inferiority tolerance;
5. stochastic failures and repairs are evaluated with the same fixed draws or aggregation rule;
6. its effect survives joint and leave-one-patch-out ablation after patches are merged.

If several patches work, prefer the smallest edit with the narrowest behavioral effect, not the shortest total prompt at any cost.

Before emitting a target overlay, retain an incompatibility witness: one common patch repairs target A but regresses target B on the same contract, an alternative reverses the result, and the declared common-patch search budget finds no non-regressing candidate. Otherwise report the gap as unresolved rather than encoding a model stereotype.
