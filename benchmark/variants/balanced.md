# Minimal-change router

For each request and its repository facts, decide whether work can proceed.

1. Choose `ACT` if the request authorizes a scoped minimum change and every missing detail is only a reversible implementation choice. Use reasonable defaults for those details.
2. Choose `ASK` only if a missing fact would change user-visible behavior, a public interface or compatibility promise, permission or consent, an external side effect, or the requested target location.
3. Do not treat preferences, harmless implementation details, or information already supplied as blockers. Do not invent repository facts or constraints.

Return only a JSON array in input order. Every item must have exactly these fields:

```json
{"id":"case-id","route":"ACT|ASK","blocker":"none|behavior|interface|permission|side_effect|target","question":null}
```

For `ACT`, set `blocker` to `none` and `question` to `null`. For `ASK`, select the single material blocker and ask exactly one non-empty question that resolves it.
