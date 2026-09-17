---
name: skill-generalizer
description: Adapt an existing skill for multiple target models by having a teacher probe observable behavior, turn confirmed failures into minimal model-neutral lessons, and accept changes only after fresh cross-model retesting. Use when porting, calibrating, or regression-testing a skill across models; do not use for untested prompt rewriting.
---

# Skill Generalizer

Use a teacher to discover behavioral gaps. Do not infer what a model needs from its name, apparent intelligence, or self-report.

## Teacher-student loop

1. Freeze the source skill, target models, reasoning settings, tools, and expected behaviors. Give each behavior a stable ID and mark any behavior whose single failure is critical.
2. Before seeing any student answer, have a capable teacher generate and freeze the whole evaluation packet:
   - diagnostic scenarios that require the model to apply each behavior;
   - nearby contrasts that test the behavior's decision boundary;
   - answer keys with observable pass criteria and forbidden behavior;
   - unseen retest scenarios that exercise the same behavior through materially different surface details.
   Read [scenario design](references/scenario-design.md) when generating or reviewing this packet.
3. Give the unchanged skill and diagnostic questions to fresh instances of every target model. Do not show them keys, lessons, or retest questions. Judge what they do, not whether they say they understand.
4. Have the teacher grade all answers against the frozen key. Audit borderline failures with a second fresh grader before learning from them. Exclude harness errors and ambiguous questions.
5. A lesson is eligible only when the same conceptual failure appears in at least two independent model-case cells, or when one predeclared critical behavior fails.
6. Turn one eligible gap into one minimal lesson. State the observable action, boundary, or output explicitly. Do not mention model names, diagnostic scenarios, or answer-key solutions. Do not rewrite unrelated parts of the skill.
7. Freeze the candidate. On the unseen retest, run fresh source-skill and candidate-skill students for every target under the same conditions. Grade them blind to condition when possible.
8. Keep the lesson only if every target passes the repaired behavior and no previously passing behavior regresses. Otherwise return the candidate as unvalidated and keep the source skill.

The teacher may generate new scenarios for every run, but a scenario becomes immutable once the evaluation packet is frozen. Keep a small fixed regression set for comparison across versions and a newly generated sealed retest for resistance to memorization.

Stop after one lesson round. A second attempt requires a newly written, still-hidden retest; never tune on an exposed retest. If a teacher creates a question after reading student failures, treat it as a development case rather than a valid retest.

## Lesson shape

Record each proposed lesson as:

```json
{
  "target_behavior": "stable behavior ID",
  "evidence": ["model/case failure IDs"],
  "rule": "one model-neutral imperative",
  "expected_observation": "what a passing answer or action must contain"
}
```

Prefer an explicit output slot or decision rule when vague prose was ignored. For example, require a distinct `Changed files` field instead of saying only that changed files should be discussed.

## Publishable result

Publish one concise common skill, not one version per model. Preserve the source intent and include only lessons that passed retesting. Do not include model names, scores, test scenarios, grading commentary, or failed candidate rules in the published skill; keep those in the evaluation artifacts.

If no candidate passes, return the unchanged source skill plus an explicitly unvalidated candidate. Never silently publish a partially successful patch. See [common skill output example](references/common-skill-output-example.md) for the intended separation between the public skill and its evidence bundle.

## Acceptance and claims

- One exploratory draw can find candidate gaps, but it does not establish stable model behavior. Use repeated fresh draws for reliability claims.
- Do not average away a target failure. A common skill fits only when every requested target meets the declared behavior contract.
- A higher total score does not excuse a regression elsewhere.
- The teacher proposes and grades; fresh target executions provide the evidence.
- If the candidate fails its retest, report what improved and what did not. Do not call it fitted.

## Required output

Return:

- `SKILL.md`: the accepted common skill, or the unchanged source when no candidate passes;
- `candidate-SKILL.md`: only when a proposed patch remains unvalidated;
- an evidence bundle containing the frozen packet, lesson ledger, compact target-by-condition table, raw answers, grading, and limitations.
