# A Skill That Improves Your Skill — Illustration Brief

[English](ILLUSTRATION-BRIEF.en.md) · [繁體中文](ILLUSTRATION-BRIEF.md)

## One-line summary

This open-source project helps one AI skill work better across multiple models: a teacher creates scenarios, different models try the skill, one small evidence-backed correction is proposed, and an unseen retest decides whether it ships.

The README should not promise a magical universal prompt. The project is about an observable, testable improvement loop that can reject its own patch when the evidence is not good enough.

## Story to communicate

Imagine the system as a warm little classroom or workshop:

1. The teacher prepares diagnostic cards, contrast cards, and a sealed retest.
2. Three distinct students solve tasks using the same skill handbook.
3. The teacher finds omissions in their actual work instead of asking what prompt they would like.
4. The teacher adds one small note to the handbook rather than rewriting it.
5. Fresh students open the sealed retest.
6. The same common skill reaches users only if every student passes without regression.

The loop in shorthand:

```text
source skill
→ teacher-made scenarios
→ Sol / Terra / Luna students
→ one small lesson
→ sealed retest
→ one common skill, or reject the patch
```

## Characters

### Teacher

- Warm, attentive, and part researcher, part coach.
- May hold question cards, a magnifying glass, or a grading board.
- Should feel like someone helping the group discover unclear instructions, not an unquestionable authority.

### Three students

- Three equally capable, cute characters with clearly different silhouettes.
- Subtle sun, earth, and moon motifs may suggest Sol, Terra, and Luna.
- Do not use company logos or depict official model mascots.
- Do not frame one student as less intelligent. Their difference is which detail they notice, not a ranking of ability.
- Tiny `S`, `T`, and `L` name tags are optional; full model names are unnecessary in the hero.

### The skill

- A single shared handbook, scroll, or recipe book.
- A micro-adjustment can appear as one sticky note, patch, or checklist card.
- The final result is always one common skill, never three model-specific books.

### Sealed retest

- Represent it with a wax-sealed envelope, locked question capsule, or covered test box.
- It should feel clearly prepared before the skill is edited and hidden from the patch author.

## Required image: README hero

A wide “cute research workshop” composition:

- One open common-skill handbook sits in the center.
- On the left, the teacher prepares scenario cards and locks one set away as the retest.
- On the right, three students work on tasks with different surface details.
- Only one small patch sits near the handbook, suggesting a minimal adjustment.
- A validation gate in the background releases the common handbook only when all three pass.
- A small amber warning may show that a higher total score is not enough when one student still fails.

The first impression should be cute, legible, and lightly experimental—not an academic paper figure.

## Optional second image: process strip

A simple six-panel or single-line sequence:

1. `Freeze expectations`
2. `Teacher creates scenarios`
3. `Students attempt`
4. `Find repeated gap`
5. `Patch one rule`
6. `Fresh retest → keep or reject`

The sixth panel needs two unmistakable outcomes:

- everyone passes with no regression → publish the common skill;
- any target fails or another behavior regresses → keep the source skill.

This can be more diagrammatic than the hero while retaining the same characters and palette.

## A small pilot easter egg

In the pilot, students often failed to list `Changed files` explicitly in their completion reports. After one instruction was added, Sol and Terra passed, but Luna still omitted the field and regressed on another question. The candidate was therefore rejected.

Possible subtle details:

- a report checklist with a `Changed files` row;
- two students with that row checked and one holding a form with the row still blank;
- the teacher placing the candidate patch in a “needs another round” tray instead of awarding a success badge.

Do not use this detail to embarrass Luna or make the whole method look unsuccessful. It shows that the validation gate correctly stopped an unreliable change.

## Visual direction

- Mood: warm, smart, welcoming, and handmade.
- Style: cute editorial illustration, picture-book art, or soft flat illustration.
- Shapes: rounded, distinctive, and readable at small sizes.
- Palette: cream background with soft yellow, earthy green, and moonlight blue; avoid generic neon tech blue.
- Useful props: paper cards, sticky notes, pencils, stamps, wax seals, envelopes, and magnifying glasses.
- GitHub has both light and dark interfaces; avoid essential details made only from faint white lines or very low contrast.

## Text in the artwork

Keep the hero nearly text-free so it remains legible at small sizes and works across language versions.

If labels are necessary, prefer only:

- `Source skill`
- `Teacher`
- `Sealed retest`
- `Common skill`
- `Keep` / `Reject`

Do not place experiment scores or long explanations in the image; those belong in the README table.

## Avoid

- A “strong model teaches weak model” hierarchy or intelligence leaderboard.
- Implying that every candidate improvement succeeds.
- Giving each model a different final skill.
- Company trademarks, official logos, or product screenshots.
- Dense paper diagrams, tiny labels, or corporate slide aesthetics.
- Depicting evolve as uncontrolled self-rewriting; the method tests one evidenced change per round.

## Deliverables

### Required

- README hero: `16:9`, ideally about `1600 × 900 px`.
- A 2x PNG suitable for GitHub README display.
- Editable source: SVG, AI, Figma, or PSD.
- If the main export has a background, include a transparent-background version as well.

### Optional

- Process strip around `1600 × 600 px`.
- Separate transparent PNG or SVG assets for the teacher and three students.
- Square social preview crop at `1200 × 1200 px`.

Leave safe margins around characters and key props for GitHub and social-card crops.

## Suggested filenames

```text
assets/
├── skill-generalizer-hero.png
├── skill-generalizer-hero.svg
├── teacher-student-loop.png
├── teacher-student-loop.svg
└── characters/
    ├── teacher.png
    ├── sol.png
    ├── terra.png
    └── luna.png
```

## Suggested alt text

Hero:

> A teacher prepares diagnostic cards and a sealed retest while three distinct students use one shared skill book; a small patch must pass a common validation gate before publication.

Process strip:

> A teacher-generated evaluation loop: freeze expectations, create scenarios, observe student behavior, patch one repeated gap, run a sealed retest, then keep or reject the common skill.

## Project references

To understand the project without reading every experiment artifact, review:

1. `README.md` for the public framing and result table.
2. `SKILL.md` for the teacher–student workflow.
3. `references/scenario-design.md` for scenario and sealed-retest rules.
4. `references/common-skill-output-example.md` for the final common-skill shape.

When visual tradeoffs are necessary, preserve these three ideas: **one shared skill, seal the retest first, and reject a patch that fails**.
