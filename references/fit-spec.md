# Behavioral fit specification

Freeze this manifest before adapting a skill. YAML is illustrative; use any equivalent format the harness can execute.

```yaml
skill: path/to/SKILL.md

targets:
  - id: target-a
    model_snapshot: exact-model-version
    reasoning: low
    decoding: {temperature: fixed-or-unsupported, top_p: fixed-or-unsupported}
    observed_at: ISO-8601-timestamp
  - id: target-b
    model_snapshot: exact-model-version
    reasoning: low
    decoding: {temperature: fixed-or-unsupported, top_p: fixed-or-unsupported}
    observed_at: ISO-8601-timestamp

environment:
  system_context: contexts/system.txt
  developer_context: contexts/developer.txt
  skill_activation: explicit
  tools: [shell, apply_patch]
  state_reset: fresh_agent_per_run
  harness_version: commit-or-version
  tool_versions: {shell: version, apply_patch: version}
  evaluation_bundle_revision: commit-or-content-hash
  artifact_hashes:
    skill: sha256
    contexts: sha256
    cases_oracles_graders: sha256

contract:
  - id: C1
    behavior: Produces the required output schema
    critical: true
    threshold:
      rule: zero_observed_failures
  - id: C2
    behavior: Asks only when a missing fact changes the result
    critical: false
    threshold:
      rule: pass_rate_at_least
      value: 0.9

cases:
  - id: cal-01
    split: calibration
    contract_ids: [C1, C2]
    input: cases/cal-01.json
    expected: oracles/cal-01.json
    grader: graders/router.py
  - id: ctr-01
    split: contrast
    contract_ids: [C2]
    input: cases/ctr-01.json
    expected: oracles/ctr-01.json
    grader: graders/router.py
  - id: hid-01
    split: hidden
    contract_ids: [C1, C2]
    input: cases/hid-01.json
    expected: oracles/hid-01.json
    grader: graders/router.py

execution:
  independent_draws_per_case: 2
  scoring_unit: case_draw

grader_output:
  required_fields: [case_id, draw_id, verdicts]
  verdict_fields: [contract_id, status, evidence]
  statuses: [pass, fail]
  one_verdict_per_linked_contract: true
  undeclared_na: error
  infrastructure_error: "rerun the invalid draw once; if unresolved, block the claim"

aggregation:
  aggregate_by: [split, target, contract_id]
  case_verdict:
    critical: all_draws_pass
    noncritical: draw_pass_rate
  contract_verdict: applicable_case_pass_rate_against_contract_threshold
  numerator: passed_applicable_cases
  denominator: all_applicable_cases
  pool_splits: false

phase_gates:
  calibration: all_contract_thresholds_pass_before_patch_selection
  contrast: all_contract_thresholds_pass_before_candidate_freeze
  hidden: all_contract_thresholds_pass_for_final_claim

non_inferiority:
  comparison_unit: target_contract_case
  compare: candidate_draw_pass_rate_minus_baseline_draw_pass_rate
  allowed_margin: 0.0
  critical_regressions_allowed: 0

holdout:
  isolated_from_patch_generation: true
  run_only_after_candidate_freeze: true
  retire_after_feedback_is_viewed: true

claim_scope:
  require_all_targets: true
  wording: "Met the declared contract on this evaluation batch and configuration."
```

For every contract item, define its applicable cases, expected outcome, scoring unit, repeat aggregation, denominator, and exact acceptance rule. A numeric threshold without those semantics is not executable.

Report per-contract results. A single aggregate score can hide a critical failure and is insufficient for declaring fit. For critical items, say "zero observed failures in N trials" rather than implying universal reliability.
