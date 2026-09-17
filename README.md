# A Skill That Improves Your Skill

[English](README.md) · [繁體中文](README.zh-TW.md)

![A teacher seals a retest while three students work from one shared skill book; a validation gate accepts two results and rejects one patch.](assets/skill-generalizer-hero.png)

`skill-generalizer` helps one skill work better across multiple models. It observes fresh model behavior, adds one small evidence-backed instruction, and keeps the change only when every target passes a sealed retest without regression.

## The loop

```text
source skill
→ teacher-made scenarios + sealed retest
→ fresh target-model attempts
→ one repeated gap
→ one small lesson
→ fresh source/candidate retest
→ keep or reject
```

The teacher does not ask models what prompt they want. It gives them realistic scenarios and grades their decisions, actions, and outputs against criteria written in advance.

The result is one common `SKILL.md`, not a different prompt for every model.

## Install

```bash
git clone git@github.com:CuteOwOwO/skill-improves-skill.git ~/.codex/skills/skill-generalizer
```

Then ask:

```text
Use $skill-generalizer to improve this skill across Sol, Terra, and Luna.
Keep one common skill and show the evidence for every retained change.
```

## Acceptance rule

A patch ships only when:

- every requested target passes the repaired behavior;
- no previously passing behavior regresses;
- the retest was sealed before the patch was written.

A higher average score cannot hide one failing target.

## Tiny pilot

In a small Sol/Terra/Luna pilot, one instruction improved the target behavior from 0/3 passes to 2/3. Luna still missed it and regressed elsewhere, so the patch was rejected. This is not evidence of stable model differences; it shows why the retest gate matters.

## Files

```text
SKILL.md                       the complete workflow
agents/openai.yaml             skill metadata
assets/skill-generalizer-hero.png
                               README illustration
```
