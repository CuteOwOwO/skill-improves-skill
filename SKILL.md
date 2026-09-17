---
name: skill-generalizer
description: Improve an existing skill across target configurations by testing observable behavior, adding one evidence-backed instruction, and keeping it only when fresh retests pass without regression. Use when adapting or validating a skill across models, versions, reasoning settings, tool environments, or agent contexts.
---

# Skill Generalizer

Improve one common skill from observed behavior—not assumptions about a model, version, or configuration.

A target is any frozen execution configuration: model and version, reasoning setting, system context, available tools, and runtime environment.

## Workflow

1. Read the source skill and list the few behaviors that define success. Mark any behavior whose single failure is critical.
2. Before testing, have a teacher create and freeze:
   - diagnostic scenarios and nearby contrasts;
   - observable answer criteria;
   - a sealed retest that checks the same behaviors through different scenarios.
3. Give the unchanged skill and diagnostic scenarios to fresh runs of every target configuration. Do not show them the keys or retest.
4. Grade what the runs actually decide, do, and produce. A lesson is eligible only when the same noncritical gap appears at least twice, or one predeclared critical behavior fails.
5. Patch one gap with one small, target-neutral rule. Name the required action, boundary, or output explicitly; do not mention target identities or copy a test answer into the skill.
6. Give the source and candidate skills to fresh target instances on the sealed retest. Keep the patch only if every target passes the repaired behavior and no previously passing behavior regresses.
7. If the candidate fails, keep the source skill and label the candidate unvalidated. Any new attempt needs a new sealed retest.

The teacher may generate new scenarios for each run, but questions and keys become fixed before student answers exist. Prefer a concrete output field or decision rule when vague prose is ignored.

## Return

Return:

- one accepted common `SKILL.md`, or the unchanged source skill;
- the proposed lesson and the failures that justified it;
- a compact source-versus-candidate table for every target;
- limitations such as single draws, unavailable target runs, or unvalidated candidates.

Never claim general fit when one requested target still fails, even if the average score improves.
