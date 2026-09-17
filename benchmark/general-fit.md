# Minimal-change router

For each request and its repository facts, choose `ACT` when an authorized, scoped minimum change can proceed with reasonable implementation defaults. Choose `ASK` only when missing information would materially change user-visible behavior, a public interface, permission or consent, an external side effect, or the target location. Do not invent facts.

Classify the blocker by the missing decision:

- `behavior`: user-visible result;
- `interface`: public API, CLI, configuration, file-format, or external-consumer compatibility;
- `permission`: authorization, privacy, consent, credentials, or provider choice;
- `side_effect`: an external operational effect when no public contract is changing;
- `target`: destination or affected location.

Public-consumer compatibility is `interface`, even though changing it would also have external effects.

Return only a JSON array in input order. Every item must be:

```json
{"id":"case-id","route":"ACT|ASK","blocker":"none|behavior|interface|permission|side_effect|target","question":null}
```

`ACT` uses `none` and `null`. `ASK` uses the relevant blocker and exactly one non-empty question.
