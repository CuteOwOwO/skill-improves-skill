# A Skill That Improves Your Skill — 插畫交接 Brief

[English](ILLUSTRATION-BRIEF.en.md) · [繁體中文](ILLUSTRATION-BRIEF.md)

## 一句話介紹

這是一個用「老師出題、不同模型實作、失敗後只做最小修正、再用未見題驗收」的方式，讓同一份 AI skill 更適合多個模型使用的開源專案。

GitHub README 的重點不是宣稱「一鍵讓所有模型變完美」，而是：我們有一套可觀察、可驗證、失敗時也不會硬說成功的調整流程。

## 希望插畫傳達的故事

可以把整個系統想成一間可愛的小教室或工坊：

1. 老師先準備診斷題、對照題，以及一封封好的重測題。
2. 三位不同個性的學生閱讀同一本 skill 手冊並解題。
3. 老師從實際答案找出共同遺漏，而不是問學生「你想要什麼提示」。
4. 老師只在手冊上貼一張小補丁，不整本重寫。
5. 全新的學生打開封存題重測。
6. 只有所有學生都通過且沒有其他退步時，才把同一份 common skill 交給大家。

這個流程可以簡寫為：

```text
source skill
→ teacher-made scenarios
→ Sol / Terra / Luna students
→ one small lesson
→ sealed retest
→ one common skill, or reject the patch
```

## 角色設定

### 老師

- 溫和、認真、像研究員兼老師。
- 拿著題目卡、放大鏡或評分板。
- 不是權威裁判，更像協助大家找出指令哪裡不夠清楚的教練。

### 三位學生

- 三個平等、可愛、輪廓明顯不同的小角色。
- 可以用太陽、土地、月亮作為非常輕微的視覺聯想，對應 Sol、Terra、Luna。
- 不要使用任何公司的正式 logo，也不要畫成官方模型吉祥物。
- 不要把其中一位畫得比較笨；差異應是注意到的細節不同，而不是智力排名。
- 若要加識別，可使用小小的 `S`、`T`、`L` 名牌，不必在主視覺放完整模型名稱。

### Skill

- 可以是一份大家共用的小手冊、卷軸或 recipe book。
- 微調可以畫成便利貼、小補丁或新增的一張 checklist。
- 最終永遠是一份 common skill，不是三本模型專用手冊。

### Sealed retest

- 用封蠟信封、鎖住的小題目箱或蓋布遮住的考題表示。
- 必須讓人感覺它在修改 skill 之前就已經準備好，而且修改者看不到內容。

## 必要主圖：README Hero

建議畫面是一張橫幅式「可愛研究工坊」：

- 中央是一本打開的 common skill 手冊。
- 左側老師正在準備幾張情境卡，其中一疊放進封好的 retest 信封。
- 右側三位學生各自在做不同表面情境的任務。
- 手冊旁只有一張小補丁，暗示 minimal adjustment。
- 遠處有一道驗收閘門；三位都通過時，共同手冊才會被送到 GitHub／大家手上。
- 可以有一個小小的黃色警示標誌，表示「總分提高但仍有一位失敗時，不能發布候選版」。

希望第一眼感覺：可愛、容易理解、帶一點實驗室感，但不是嚴肅論文圖。

## 選配第二張：流程小圖

如果時間允許，希望有一張簡單的六格或單線流程圖：

1. `Freeze expectations`
2. `Teacher creates scenarios`
3. `Students attempt`
4. `Find repeated gap`
5. `Patch one rule`
6. `Fresh retest → keep or reject`

請讓第六格有兩條清楚結果：

- 全部通過、無回歸 → 發布 common skill
- 任一模型失敗或其他行為退步 → 保留 source skill

這張可以比主圖更圖示化，但仍沿用相同角色與色彩。

## 本次實驗可以藏入的彩蛋

實驗中，三位學生都容易忘記在完成報告中明確列出 `Changed files`。加入一句提示後，Sol 和 Terra 通過，但 Luna 仍然漏掉，並且另一題退步，所以候選 skill 沒有被接受。

可以用很小的彩蛋表達：

- 報告 checklist 上有 `Changed files` 欄位。
- 兩位學生已打勾，一位還拿著漏掉一格的表單。
- 老師因此把候選補丁放回「needs another round」托盤，而不是頒發成功獎章。

請不要把這個彩蛋畫成羞辱 Luna，也不要讓主圖看起來像整個方法失敗。它代表的是驗收機制有成功擋住不可靠的修改。

## 視覺方向

- 氣氛：溫暖、聰明、親切、帶手作感。
- 風格：簡潔可愛的 editorial illustration、繪本感或柔和扁平插畫皆可。
- 形狀：圓潤、輪廓清楚，小尺寸仍可辨識。
- 配色：奶油白底，搭配柔和黃、土綠、月光藍；避免高飽和霓虹科技藍。
- 可以加入紙張、便利貼、鉛筆、印章、封蠟信封、放大鏡等元素。
- GitHub 同時有亮色與暗色介面；主體不要依賴純白細線或過低對比。

## 文字使用

主圖盡量少字，避免縮小後無法閱讀，也方便不同語言的 README 使用。

若需要文字，優先只使用：

- `Source skill`
- `Teacher`
- `Sealed retest`
- `Common skill`
- `Keep` / `Reject`

不要把實驗分數或長句畫進圖裡；分數會留在 README 表格。

## 請避免

- 不要呈現成「強模型教訓弱模型」或模型能力排行榜。
- 不要暗示所有候選修改都一定成功。
- 不要畫成三個模型各拿一本不同的最終 skill。
- 不要使用 OpenAI 或其他公司的商標、正式 logo、產品 UI 截圖。
- 不要用厚重的論文流程圖、密集小字或企業簡報風格。
- 不要把 evolve 畫成無限制自我改寫；這個方法每輪只接受一個有證據的小調整。

## 交付項目

### 必要

- README hero：建議比例 `16:9` 或約 `1600 × 900 px`。
- PNG：2x 尺寸，適合 GitHub README。
- 可編輯原始檔：SVG、AI、Figma 或 PSD 皆可。
- 如果背景不是透明，請另附透明背景版本。

### 選配

- 流程小圖：約 `1600 × 600 px`，適合放在 README 方法段落。
- 三位學生與老師的獨立透明 PNG／SVG，可供未來文件重複使用。
- 方形社群預覽裁切版本：`1200 × 1200 px`。

請在輸出時保留安全邊界，避免 GitHub 或社群卡片裁切到角色與關鍵物件。

## 建議檔名

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

## 建議替代文字

主圖 alt text：

> A teacher prepares diagnostic cards and a sealed retest while three distinct students use one shared skill book; a small patch must pass a common validation gate before publication.

流程圖 alt text：

> A teacher-generated evaluation loop: freeze expectations, create scenarios, observe student behavior, patch one repeated gap, run a sealed retest, then keep or reject the common skill.

## 專案參考

若需要理解專案而不閱讀所有實驗資料，依序看：

1. `README.md`：專案定位與結果表格。
2. `SKILL.md`：實際 teacher-student workflow。
3. `references/scenario-design.md`：情境題與 sealed retest 的規則。
4. `references/common-skill-output-example.md`：最後交給使用者的 common skill 長相。

有創作上的取捨時，優先保留這三個概念：**同一本 skill、先封存重測、失敗就不發布補丁**。
