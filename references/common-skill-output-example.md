# Common skill output example

The public result is one ordinary skill. It should not expose the optimization machinery that produced it.

The following is an illustrative shape, not a validated result from the pilot:

```markdown
---
name: evidence-first-bug-fixing
description: Diagnose and fix repository bugs while preserving unrelated work, grounding claims in executed checks, and reporting verification limits.
---

# Evidence-first bug fixing

When handling a repository bug:

1. Inspect the relevant implementation, tests, repository guidance, and worktree before editing.
2. Attempt the smallest runnable reproduction before changing code. If reproduction is unavailable, state the exact limitation and do not claim it succeeded.
3. Ask only when a missing decision would materially change public behavior, permissions, external effects, or the requested target. Otherwise use a reversible implementation default.
4. Make the smallest scoped fix and preserve unrelated user changes.
5. Run focused verification and proportionate broader checks. Distinguish new failures from failures demonstrated to predate the change.

## Completion report

Return these fields:

- `Diagnosis`
- `Changed files`
- `Reproduction evidence`
- `Verification`
- `Remaining risks`
```

The accompanying evidence bundle remains outside the public skill:

```text
evaluation/
├── packet.json          diagnostic, contrast, retest, and keys
├── lesson.json          failure evidence and proposed rule
├── answers/             source and candidate student runs
├── grading.json         item-level verdicts
└── summary.md           target-by-condition table and limitations
```

If the candidate fails any target or regresses elsewhere, publish the unchanged source `SKILL.md` and retain the edited version only as `candidate-SKILL.md` in the evidence bundle.
