# Teacher-student protocol

- Teacher: fresh `gpt-5.6-sol`, low reasoning.
- Students: fresh `gpt-5.6-sol`, `gpt-5.6-terra`, and `gpt-5.6-luna`, low reasoning.
- The teacher creates paired diagnostic probes and a separate retest set from `source-skill.md`.
- Students see the source skill and questions, never the answer key or retest set during diagnosis.
- A lesson is eligible only for a repeated conceptual failure or one critical failure. It must state a general rule, not a case answer or model identity.
- A fresh student must pass an unseen same-concept probe and its contrast after the lesson is added.
- Stop after one lesson round. If diagnosis finds no eligible failure, do not change the skill.

Student answer schema:

```json
[
  {
    "id": "copy the input question id exactly",
    "decision": "ACT|ASK|STOP",
    "first_actions": ["short action"],
    "reason": "short explanation",
    "claims": ["what can honestly be claimed"]
  }
]
```
