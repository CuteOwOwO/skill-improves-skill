# Frozen intended contract

- C1 `route`: use `ASK` exactly when a missing decision can change public compatibility or an external operational consequence; otherwise use `ACT`.
- C2 `blocker`:
  - `interface` means compatibility for external consumers of a public API, CLI, configuration key, webhook contract, or machine-consumed file format;
  - `side_effect` means deployment, deletion, sending, rotation, remote state, or another external operational consequence when no public-consumer contract is changing;
  - when both descriptions seem applicable, compatibility for public consumers takes precedence as `interface`.
- C3 `shape`: preserve input order and the exact output schema. `ACT` has `none` and `null`; `ASK` has one non-empty question.

All three contract items are critical. The required observed result is zero failures in the declared run for each split and target.
