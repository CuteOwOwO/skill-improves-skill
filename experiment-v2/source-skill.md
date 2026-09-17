# Change router

For each requested repository change, decide whether to act or ask one blocking question.

- Choose `ACT` when the request and repository facts are sufficient for an authorized, scoped minimum change.
- Choose `ASK` only when a missing fact could materially change a public interface or an external operational side effect.
- Do not invent facts or ask about reversible internal implementation preferences.

Return only a JSON array in input order. Every item has exactly:

```json
{"id":"case-id","route":"ACT|ASK","blocker":"none|interface|side_effect","question":null}
```

For `ACT`, use `blocker: "none"` and `question: null`. For `ASK`, choose the relevant blocker and provide one non-empty question string.
