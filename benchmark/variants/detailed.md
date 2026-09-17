# Minimal-change router

Process each request independently.

## Decision procedure

1. Read only the supplied request and repository facts. Do not infer additional facts.
2. Identify the smallest change that would satisfy the request.
3. Check whether a missing fact can change any of these contract surfaces:
   - `behavior`: user-visible results or acceptance behavior;
   - `interface`: a public API, CLI, file format, or compatibility promise;
   - `permission`: authorization, privacy, consent, credentials, or provider choice;
   - `side_effect`: deployment, deletion, sending, charging, or another external effect;
   - `target`: which product, page, repository, environment, file, or destination is affected.
4. If exactly one surface is materially unresolved, choose `ASK`, label that blocker, and ask one question that resolves it. If several are unresolved, label the earliest applicable surface above and combine only the information necessary into one question.
5. Otherwise choose `ACT`. Missing style preferences and reversible internal implementation choices are not blockers; use a reasonable minimum-change default.

Examples of boundaries:

- Exact file plus an exact typo replacement: `ACT`, even if no editing method is specified.
- Rename a public flag without a compatibility requirement: `ASK` with `interface`.
- Refactor a private helper while preserving tested behavior: `ACT`.
- Add analytics without consent or provider facts: `ASK` with `permission`.

## Output check

Return only one JSON array in input order, with no prose or code fence. Every item has exactly:

```json
{"id":"case-id","route":"ACT|ASK","blocker":"none|behavior|interface|permission|side_effect|target","question":null}
```

- `ACT` requires `blocker: "none"` and `question: null`.
- `ASK` requires one non-`none` blocker and exactly one non-empty question string.
