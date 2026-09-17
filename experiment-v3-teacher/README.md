# Teacher–student pilot

A fresh Sol teacher wrote paired diagnostic and retest questions for one source skill. Fresh Sol, Terra, and Luna students answered at low reasoning. The teacher graded against frozen keys, and separate graders audited both grading rounds.

The only audited repeated gap was that Terra and Luna implied which files changed instead of explicitly listing them. The candidate added one general rule: final reports need a distinct changed-files list.

| Model | Diagnostic source | Retest source | Retest candidate | Target item r5 |
|---|---:|---:|---:|---|
| Sol | 6/6 | 5/6 | 6/6 | fail → pass |
| Terra | 5/6 | 5/6 | 6/6 | fail → pass |
| Luna | 5/6 | 5/6 | 4/6 | fail → fail |
| **Total** | **16/18** | **15/18** | **16/18** | **0/3 → 2/3** |

The candidate is **not accepted as cross-model fitted**. Luna still omitted the required changed-files list and also regressed on r2. The experiment supports the teacher–student discovery loop and the need for a retest gate; it does not show stable model differences or a universally effective patch. There was one answer per model and item, one task family, and no repeated draws.

Key artifacts:

- `source-skill.md` and `candidate-skill.md`: the only prompt difference;
- `diagnostic-questions.json` and `diagnostic-key.json`: teacher-authored diagnosis;
- `grading.json` and `grading-audit.json`: corrected diagnostic scoring;
- `retest-questions.json` and `retest-key.json`: unseen paired retest;
- `results/`: all student answers;
- `retest-grading.json` and `retest-grading-audit.json`: confirmed final scores.
