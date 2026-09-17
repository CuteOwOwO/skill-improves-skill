# 一個幫你的 Skill 變得更好的 Skill

[English](README.md) · [繁體中文](README.zh-TW.md)

![老師封存重測題，三位學生共用同一本 skill 手冊；驗收閘門接受兩個結果，並退回一個未通過的補丁。](assets/skill-generalizer-hero.png)

`skill-generalizer` 是一個用來改善其他 skill 的 meta-skill。老師模型先設計行為情境，觀察全新的目標模型實際怎麼做，再提出一個有證據的最小修改；只有當所有目標模型都通過封存重測，而且沒有其他行為退步時，修改才會發布。

它不預設「較弱的模型只需要更長的指令」，而是先測行為。

## 運作方式

```text
固定預期行為並封存重測題
→ 讓全新模型使用未修改的 skill
→ 評分可觀察行為，而不是模型的自我描述
→ 把一個重複失敗轉成一條小 lesson
→ 用全新重測比較 source 與 candidate
→ 發布一份 common skill，否則退回補丁
```

![封存重測題、共用同一份 skill，並把未通過補丁退回的短動畫。](assets/teacher-student-loop.gif)

[觀看畫質較高的 10 秒 MP4](assets/teacher-student-loop.mp4)。

老師必須在任何學生作答前，一次寫完診斷題、對照題與重測題。少量固定 regression cases 用來比較不同版本；每輪新產生並封存的題目則降低針對題庫調參的風險。詳見[情境設計規則](references/scenario-design.md)。

## 最後發布什麼

產物是一份精簡的 common `SKILL.md`，而不是 Sol、Terra、Luna 各自一套提示詞。公開版保留原 skill 的意圖，而且只加入在所有目標上都通過驗收的最小 lesson。

模型名稱、題目、分數、失敗候選版與批改資料會留在獨立 evidence bundle。只要候選版在任一模型失敗，或讓其他行為退步，公開版就維持原始 skill。可參考 [common skill 產出範例](references/common-skill-output-example.md)。

## 目前的 pilot

[Teacher–student pilot](experiment-v3-teacher/README.md) 使用全新的 Sol、Terra、Luna agent，全部採 low reasoning。診斷中出現一個重複缺口：完成報告沒有明確列出 changed files，因此我們加入了一條小規則。

| 模型 | 診斷原版 | 重測原版 | 重測候選版 | 目標行為 |
|---|---:|---:|---:|---|
| Sol | 6/6 | 5/6 | 6/6 | fail → pass |
| Terra | 5/6 | 5/6 | 6/6 | fail → pass |
| Luna | 5/6 | 5/6 | 4/6 | fail → fail |
| **總計** | **16/18** | **15/18** | **16/18** | **0/3 → 2/3** |

候選版改善了目標行為，但 Luna 仍然漏掉它，並在另一題退步。因此候選版被標記為 **unvalidated**，不能稱為 fitted。這個負面結果很重要：重測閘門成功阻止了一個直覺合理、實際上卻不可靠的補丁發布。

這次 pilot 每個模型與題目只有一份回答，只有一種任務類型，也沒有重複抽樣。它證明的是流程與拒絕機制可以運作，而不是模型家族之間存在穩定差異，更不是任何 skill 都一定會改善。

## 試用這個 skill

把 repository clone 到 Codex skills 目錄：

```bash
git clone git@github.com:CuteOwOwO/skill-improves-skill.git ~/.codex/skills/skill-generalizer
```

接著可以對 Codex 說：

```text
Use $skill-generalizer to test this skill across Sol, Terra, and Luna.
Keep one common skill and show me the evidence for every retained change.
```

若要宣稱 skill 已經 fitted，流程必須能執行全新的目標模型測試。如果做不到，仍可準備題目、評分規則與候選 lesson，但結果必須標記為 pending 或 unvalidated。

## 驗收規則

候選版只有在以下條件全部成立時才能採用：

- 每個指定目標都通過要修復的行為；
- 原本通過的行為沒有退步；
- 重測題在補丁產生前就已封存；
- 評分依據是執行前定義好的可觀察標準。

平均分數變高，不能掩蓋某個目標仍然失敗。

## Repository 結構

```text
SKILL.md                           teacher–student generalization workflow
references/scenario-design.md     自動生成與固定題目的規則
references/common-skill-output-example.md
                                   可發布 common skill 的範例
experiment-v3-teacher/            最新 pilot 與原始證據
experiment-v2/                    較早的 behavior-fit 實驗
benchmark/                        保留的 density pilot
results/                          早期原始結果與 audit trail
assets/                           README 圖片與視覺產製紀錄
```

[Fit specification](references/fit-spec.md) 與 [micro-adjustment rules](references/micro-adjustments.md) 保留了較完整、較重型的實驗協議。

## 驗證

驗證 skill package：

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py .
```

使用保留的 benchmark 評分：

```bash
python3 benchmark/grade.py path/to/answers.json benchmark/calibration-key.json
```

## 視覺文件

插畫交接文件提供 [English](ILLUSTRATION-BRIEF.en.md) 與[繁體中文](ILLUSTRATION-BRIEF.md)兩版；生成方式與動態處理紀錄在 [assets/VISUAL-LINEAGE.md](assets/VISUAL-LINEAGE.md)。
