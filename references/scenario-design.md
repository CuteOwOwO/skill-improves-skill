# Scenario design

## What a scenario is

A scenario is a small realistic task that forces a target model to exercise one behavior from the source skill. It is not a question asking the model to repeat or explain the rule.

Include only the state needed to make the decision observable:

- the user's request;
- available files, evidence, tools, or prior results;
- relevant missing information;
- permissions, costs, destructive effects, or other decision boundaries;
- the decision, action plan, tool call, or output the student must produce.

Do not quote the tested rule, announce the expected decision, or copy a prior failure into the prompt.

## Build the packet

Derive behavior IDs from the source skill before writing cases. For each selected behavior, create:

1. a diagnostic scenario where the behavior should apply;
2. a nearby contrast where one important fact changes the expected behavior;
3. an unseen retest pair that preserves the concept but changes the domain, actors, artifacts, and wording;
4. an answer key naming the expected decision, required observable concepts, forbidden behavior, and criticality.

A retest is not a paraphrase. For example, a diagnostic about a serializer and a pre-existing lint failure may retest the same attribution behavior with an image parser and an unavailable proprietary dataset.

Generate the complete packet before any student run. Record it immutably for that round. The patch author may see diagnostic failures and keys but not the sealed retest. Students see only the active skill and their assigned questions. Graders receive anonymized answers when practical.

## Fixed versus generated cases

Use both:

- **Fixed regression cases** remain stable across skill versions and reveal regressions over time.
- **Generated sealed cases** are newly written for a round and reduce memorization and case-specific tuning.

Teacher-generated does not mean dynamically changed during grading. Once generated, both the questions and their keys are fixed for that round. If the retest is exposed or its results influence a patch, retire it and generate a new sealed set before evaluating another candidate.

## Minimum evidence

One fresh answer per model and case is enough for an exploratory pilot, not a reliability claim. Treat a noncritical lesson as eligible only when the same conceptual failure occurs in at least two independent model-case cells. A single failure may qualify only when the key marked it critical before execution.
