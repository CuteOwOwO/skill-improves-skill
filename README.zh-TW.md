# 一個幫你的 Skill 變得更好的 Skill

[English](README.md) · [繁體中文](README.zh-TW.md)

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

## 小型 pilot

在一次三個 target 的小型測試中，一條新指令讓受測行為從 0/3 提升到 2/3，但其中一個 target 仍然漏掉它，並在另一題退步，因此補丁被退回。這不能證明 targets 之間存在穩定差異；它只說明為什麼需要重測閘門。

## 檔案

```text
SKILL.md                       完整流程
agents/openai.yaml             skill metadata
assets/skill-generalizer-hero.png
                               README 插圖
```
