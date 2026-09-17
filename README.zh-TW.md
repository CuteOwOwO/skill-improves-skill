# 一個幫你的 Skill 變得更好的 Skill

[English](README.md) · [繁體中文](README.zh-TW.md)

**每個模型都有自己的個性——你的 skill 有為它們調整過嗎？**

![老師封存重測題，三位學生共用同一本 skill 手冊；驗收閘門接受兩個結果，並退回一個未通過的補丁。](assets/skill-generalizer-hero.png)

`skill-generalizer` 幫助同一份 skill 更適合不同執行目標，包括模型、版本、reasoning level、工具組合或 agent context。它先觀察全新執行的實際行為，再加入一條有證據的最小修改；只有當每個目標都通過封存重測，而且沒有其他行為退步時，修改才會保留。

## 核心流程

```text
source skill
→ 老師產生情境題並封存重測
→ 全新目標實作
→ 找出一個重複缺口
→ 加入一條小 lesson
→ 用全新執行重測 source / candidate
→ 採用或退回
```

老師不會問目標 agent「你想要什麼 prompt」，而是提供接近真實工作的情境，並依事先寫好的標準評分它的決定、行動與輸出。

最後產出的是一份 common `SKILL.md`，不是每個目標各自一套提示詞。

## 安裝

```bash
git clone git@github.com:CuteOwOwO/skill-improves-skill.git ~/.codex/skills/skill-generalizer
```

接著可以說：

```text
Use $skill-generalizer to improve this skill across these target configurations: [list them].
Keep one common skill and show the evidence for every retained change.
```

## 驗收規則

修改只有在以下條件全部成立時才能發布：

- 每個指定目標都通過要修復的行為；
- 原本通過的行為沒有退步；
- 重測題在修改產生前就已封存。

平均分數變高，不能掩蓋某個目標仍然失敗。

## 相關研究

- **[A Psychometric Framework for Evaluating and Shaping Personality Traits in Large Language Models](https://doi.org/10.1038/s42256-025-01115-6)** — Serapio-García et al., *Nature Machine Intelligence*, 2025。研究涵蓋 18 個 LLM 與多種 prompting conditions；輸出特質測量的可靠性與效度會受到模型規模、instruction tuning 等因素影響，而且這些特質也能透過 prompting 有方向地調整。這支持我們針對每個 target configuration 實測，而不是假設同一條指令在所有環境都會產生相同行為。

- **[Large Language Models as Optimizers](https://arxiv.org/abs/2309.03409)** — Yang et al., *ICLR*, 2024。OPRO 讓 LLM 根據先前候選解法與評分提出新解法，也示範了如何針對任務正確率優化自然語言指令。本 skill 採用相近的「產生、評估、改善」概念，並另外加入封存重測與 regression 即退回的驗收閘門。

- **[You Don’t Need a Personality Test to Know These Models Are Unreliable](https://aclanthology.org/2024.naacl-long.295/)** — Shu et al., *NAACL*, 2024。作者測試 17 個 LLM，發現包含回答選項順序與否定句在內的小幅 prompt 變動，都可能明顯降低回答一致性。這支持我們固定測試條件、加入 contrast cases，並在接受指令修改前使用全新執行做 regression check。

## 檔案

```text
SKILL.md                       完整流程
agents/openai.yaml             skill metadata
assets/skill-generalizer-hero.png
                               README 插圖
```
