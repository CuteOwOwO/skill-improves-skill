# A Skill That Improves Your Skill

[English](README.md) · [繁體中文](README.zh-TW.md)

**A meta-skill that tests and improves your other skills across models and agent setups.**

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

## Related research

- **[A Psychometric Framework for Evaluating and Shaping Personality Traits in Large Language Models](https://doi.org/10.1038/s42256-025-01115-6)** — Serapio-García et al., *Nature Machine Intelligence*, 2025. Across 18 LLMs and varied prompting conditions, the reliability and validity of measured output traits depended on properties such as scale and instruction tuning; the traits could also be deliberately shaped through prompting. This supports measuring behavior for each target configuration instead of assuming one instruction behaves identically everywhere.

- **[Large Language Models as Optimizers](https://arxiv.org/abs/2309.03409)** — Yang et al., *ICLR*, 2024. OPRO uses an LLM to propose new solutions from previously evaluated candidates and their scores, including optimizing natural-language instructions for task accuracy. This skill follows the same broad generate–evaluate–improve idea, with an added sealed retest and reject-on-regression gate.

- **[You Don’t Need a Personality Test to Know These Models Are Unreliable](https://aclanthology.org/2024.naacl-long.295/)** — Shu et al., *NAACL*, 2024. Testing 17 LLMs, the authors found that minor prompt changes—including response-option order and negation—could substantially reduce consistency. This motivates frozen test conditions, contrast cases, and fresh regression checks before accepting an instruction change.

## Files

```text
SKILL.md                       the complete workflow
agents/openai.yaml             skill metadata
assets/skill-generalizer-hero.png
                               README illustration
```
