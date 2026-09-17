# Minimal-change router

For each request and its repository facts, choose `ACT` when an authorized, scoped minimum change can proceed with reasonable implementation defaults. Choose `ASK` only when missing information would materially change user-visible behavior, a public interface, permission or consent, an external side effect, or the target location. Do not invent facts.

Return only a JSON array in input order. Every item must be:

```json
{"id":"case-id","route":"ACT|ASK","blocker":"none|behavior|interface|permission|side_effect|target","question":null}
```

`ACT` uses `none` and `null`. `ASK` uses the relevant blocker and exactly one non-empty question.
