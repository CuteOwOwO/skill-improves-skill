# A Skill That Improves Your Skill

[English](README.md) · [繁體中文](README.zh-TW.md)

![A teacher seals a retest while three students work from one shared skill book; a validation gate accepts two results and rejects one patch.](assets/skill-generalizer-hero.png)

`skill-generalizer` helps one skill work better across different execution targets: models, versions, reasoning levels, tool sets, or agent contexts. It observes fresh runs, adds one small evidence-backed instruction, and keeps the change only when every target passes a sealed retest without regression.

## The loop

```text
source skill
→ teacher-made scenarios + sealed retest
→ fresh target attempts
→ one repeated gap
→ one small lesson
→ fresh source/candidate retest
→ keep or reject
```

The teacher does not ask target agents what prompt they want. It gives them realistic scenarios and grades their decisions, actions, and outputs against criteria written in advance.

The result is one common `SKILL.md`, not a different prompt for every target.

## Install

```bash
git clone git@github.com:CuteOwOwO/skill-improves-skill.git ~/.codex/skills/skill-generalizer
```

Then ask:

```text
Use $skill-generalizer to improve this skill across these target configurations: [list them].
Keep one common skill and show the evidence for every retained change.
```

## Acceptance rule

A patch ships only when:

- every requested target passes the repaired behavior;
- no previously passing behavior regresses;
- the retest was sealed before the patch was written.

A higher average score cannot hide one failing target.

## Tiny pilot

In a small three-target pilot, one instruction improved the tested behavior from 0/3 passes to 2/3. One target still missed it and regressed elsewhere, so the patch was rejected. This does not establish stable differences between targets; it shows why the retest gate matters.

## Files

```text
SKILL.md                       the complete workflow
agents/openai.yaml             skill metadata
assets/skill-generalizer-hero.png
                               README illustration
```
