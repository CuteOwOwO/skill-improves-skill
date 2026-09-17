# Minimal-change router contract

For each request and its repository facts, return a routing decision.

- `ACT` when the information is sufficient for a scoped, authorized minimum change. Harmless implementation details may use reasonable defaults.
- `ASK` only when a missing fact would materially change user-visible behavior, a public interface, permission or consent, an external side effect, or the requested target location.
- An `ASK` response asks exactly one question about the material blocker. An `ACT` response does not ask a question.
- Never invent repository facts or new constraints.

Blocker meanings are part of the intended contract:

- `behavior`: the user-visible result or acceptance behavior;
- `interface`: a public API, CLI, configuration, file format, or external-consumer compatibility;
- `permission`: authorization, privacy, consent, credentials, or provider choice;
- `side_effect`: an external operational effect when no public contract changes;
- `target`: the destination or affected location.

When categories overlap, public-consumer compatibility is `interface` rather than `side_effect`.

For a batch, return only a JSON array in the input order. Each item has exactly:

```json
{"id":"case-id","route":"ACT|ASK","blocker":"none|behavior|interface|permission|side_effect|target","question":null}
```

For `ACT`, use `blocker: "none"` and `question: null`. For `ASK`, select the one blocker category and put one non-empty question string in `question`.
