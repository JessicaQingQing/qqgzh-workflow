# 排版样式参考

给 AI 排版时参照的组件样式库。以下所有样式都经过微信兼容验证（行内样式、无 flex/grid、无禁用 CSS）。

---

## 一、开头钩子

### 1.1 引导段（lead）

每篇文章开头的一段，叫出读者正在经历的场景，让他们觉得"这说的就是我"。

```html
<p class="lead" style="font-size:17px;color:#6A6A6A;margin-bottom:1.5em;line-height:1.75;">
  你有没有这种感觉——周末花了一小时把下周计划排得满满当当，周三就已经全乱了。不是计划不努力，是计划本身就没给意外留位置。
</p>
```

### 1.2 反常识开头

开头一句话先打破读者的预设，钩住注意力。

```html
<p style="font-size:18px;color:#1A1A1A;font-weight:700;margin-bottom:0.8em;">最好的计划，是不把时间填满的计划。</p>
<p style="font-size:16px;color:#4A4A4A;line-height:1.8;">大多数人做计划的思路是"我有哪些时间可以分配"，但真正有效的思路是"我先守住哪一块不被挤占"。</p>
```

### 1.3 身份亮出式开头

一句话讲清楚"我是谁 + 我跟这个话题什么关系"，建立可信度。

```html
<p style="font-size:16px;color:#3d3d3d;line-height:1.8;">
  我做了八年项目交付。看过的最好的计划，不是最详细的——是一个项目经理在方案第一页只写了三行字：做什么、不做什么、做到什么程度算完。
</p>
```

---

## 二、章节标题

### 2.1 带编号 + 关键词

```html
<h2 style="font-size:20px;font-weight:700;color:#1A1A1A;margin:2em 0 0.6em 0;line-height:1.4;">
  01 先守住一个不被挤占的时段
</h2>
```

### 2.2 提问式标题

```html
<h2 style="font-size:20px;font-weight:700;color:#1A1A1A;margin:2em 0 0.6em 0;line-height:1.4;">
  为什么你列了 10 件事，最后做完了 0 件？
</h2>
```

### 2.3 观点式标题（带「」引号）

```html
<h2 style="font-size:20px;font-weight:700;color:#1A1A1A;margin:2em 0 0.6em 0;line-height:1.4;">
  「完成」比「完美」更能让你下周还想继续
</h2>
```

---

## 三、金句框（takeaway / quote block）

作为章节收尾或文章核心观点的视觉强化。手机宽 375px 下不折行。

### 3.1 暖色金句框

适合个人成长、职场思考类文章。

```html
<section style="background:#faf2d8;border-top:2px solid #d4b040;border-bottom:2px solid #d4b040;padding:18px 16px;margin:1.5em 0;text-align:center;">
  <p style="font-family:Menlo,Consolas,monospace;font-size:9px;color:#b8a060;letter-spacing:3px;margin:0 0 6px 0;">KEY TAKEAWAY</p>
  <p style="font-size:16px;font-weight:800;color:#141414;line-height:1.5;margin:0;">
    先守住一个稳定节奏，<br>再逐步增加复杂度。
  </p>
</section>
```

### 3.2 冷色金句框

适合商业分析、技术、理性向文章。

```html
<section style="background:#EAF4F2;border-left:4px solid #1F6F78;padding:16px 18px;margin:1.5em 0;">
  <p style="font-size:15px;font-weight:600;color:#173B46;line-height:1.6;margin:0;">
    转型不是买一套工具——是把工作流从"人找人"变成"人找 AI、AI 找人"。
  </p>
</section>
```

### 3.3 轻量引用框

适合引用书、文章、别人的话。

```html
<blockquote style="border-left:3px solid #d0d0d0;padding:10px 14px;margin:1.2em 0;background:#fafafa;">
  <p style="font-size:15px;color:#6A6A6A;line-height:1.7;margin:0;">
    "The key is not to prioritize what's on your schedule, but to schedule your priorities." — Stephen Covey
  </p>
</blockquote>
```

---

## 四、卡片（信息块）

适合把一个观点、一个概念、一个步骤"框"出来，在手机屏上形成视觉打断。

### 4.1 实色卡片

```html
<div style="background:#F7F4ED;padding:16px 18px;margin:1.5em 0;border-radius:0;">
  <p style="font-size:16px;font-weight:700;color:#1A1A1A;margin:0 0 8px 0;">一句话总结</p>
  <p style="font-size:15px;color:#3d3d3d;line-height:1.7;margin:0;">
    计划的敌人不是执行不力，是计划本身没给意外留空间。留 30% 的缓冲，比塞满 100% 更可能完成。
  </p>
</div>
```

### 4.2 边框卡片

```html
<div style="border:1px solid #e0d8c8;padding:16px 18px;margin:1.5em 0;">
  <p style="font-size:15px;color:#3d3d3d;line-height:1.7;margin:0;">
    <span style="font-weight:700;color:#c9a030;">▸ 试一下：</span>下周先圈出一件事，给它分配一个固定时段。这一周其他可以乱，这一件事不能动。
  </p>
</div>
```

### 4.3 要点列表卡片

```html
<div style="background:#F7F9FA;padding:16px 18px;margin:1.5em 0;">
  <p style="font-size:16px;font-weight:700;color:#1A1A1A;margin:0 0 10px 0;">三个信号说明你的计划有问题</p>
  <p style="font-size:15px;color:#3d3d3d;line-height:1.8;margin:0 0 4px 0;">① 周三还没到就已经全乱了</p>
  <p style="font-size:15px;color:#3d3d3d;line-height:1.8;margin:0 0 4px 0;">② 你不好意思跟别人说你本周只做一件事</p>
  <p style="font-size:15px;color:#3d3d3d;line-height:1.8;margin:0;">③ 复盘时你在解释为什么没做完，而不是做了什么</p>
</div>
```

---

## 五、数据/事实高亮

适合在段落中强调关键数字或结论，让扫读的人一眼看到。

### 5.1 段落内金色强调

```html
<p style="font-size:15px;color:#3d3d3d;line-height:1.75;text-indent:1em;margin:0 0 1em 0;">
  调查了 200 个中层管理者之后发现，<span style="color:#c9a030;font-weight:700;">其中 73% 的人每周花在"对齐信息"上的时间超过 6 小时</span>——不是做决策，是让不同的人知道同一个信息。
</p>
```

### 5.2 大数字 + 说明（视觉锤）

```html
<div style="text-align:center;padding:24px 0;margin:1.5em 0;">
  <p style="font-size:48px;font-weight:900;color:#1F6F78;line-height:1;margin:0;">73%</p>
  <p style="font-size:14px;color:#8B9DAF;margin:6px 0 0 0;">的中层管理者每周"对齐信息"超过 6 小时</p>
</div>
```

---

## 六、对比展示

### 6.1 左右对比（双列 inline-block）

适合展示"传统 vs AI"、"改前 vs 改后"、"误区 vs 正解"。

```html
<div style="margin:1.5em 0;font-size:0;">
  <div style="display:inline-block;vertical-align:top;width:48%;font-size:15px;margin-right:4%;">
    <p style="font-size:14px;font-weight:700;color:#999;margin:0 0 6px 0;letter-spacing:2px;">❌ 误区</p>
    <p style="font-size:15px;color:#3d3d3d;line-height:1.7;margin:0;">计划越详细越好，把每小时的安排都写清楚</p>
  </div>
  <div style="display:inline-block;vertical-align:top;width:48%;font-size:15px;">
    <p style="font-size:14px;font-weight:700;color:#1F6F78;margin:0 0 6px 0;letter-spacing:2px;">✅ 正解</p>
    <p style="font-size:15px;color:#3d3d3d;line-height:1.7;margin:0;">只锁死最重要的 1-2 件事的时间，其余保持弹性</p>
  </div>
</div>
```

### 6.2 三步/三点横向要点

```html
<div style="margin:1.5em 0;">
  <p style="font-size:15px;color:#3d3d3d;line-height:1.8;margin:0 0 6px 0;">
    <span style="display:inline-block;min-width:22px;height:22px;line-height:22px;text-align:center;background:#1F6F78;color:#fff;font-size:13px;font-weight:700;margin-right:8px;">1</span> 圈出一件最重要的事
  </p>
  <p style="font-size:15px;color:#3d3d3d;line-height:1.8;margin:0 0 6px 0;">
    <span style="display:inline-block;min-width:22px;height:22px;line-height:22px;text-align:center;background:#1F6F78;color:#fff;font-size:13px;font-weight:700;margin-right:8px;">2</span> 给它分配一个不受打扰的固定时段
  </p>
  <p style="font-size:15px;color:#3d3d3d;line-height:1.8;margin:0;">
    <span style="display:inline-block;min-width:22px;height:22px;line-height:22px;text-align:center;background:#1F6F78;color:#fff;font-size:13px;font-weight:700;margin-right:8px;">3</span> 周五花 5 分钟问自己：这件事推进了多少？
  </p>
</div>
```

---

## 七、分割与过渡

### 7.1 小节之间空白分隔

最简单也最干净的过渡——靠留白。

```html
<p style="margin:2.5em 0;">&nbsp;</p>
```

### 7.2 细线分隔

```html
<div style="width:32px;height:3px;background:#d0c040;margin:2em 0;"></div>
```

### 7.3 三点分隔

```html
<p style="text-align:center;color:#ccc;font-size:18px;letter-spacing:6px;margin:2em 0;">···</p>
```

### 7.4 窄线分隔

```html
<div style="width:100%;height:1px;background:#e8e8e8;margin:2em 0;"></div>
```

---

## 八、结尾区域

### 8.1 END 标记

信号：文章正文到这里结束了。

```html
<p style="text-align:center;color:#b8a060;font-size:14px;letter-spacing:4px;margin:2em 0;">— END —</p>
```

### 8.2 带走一句话（每篇固定）

```html
<section style="background:#F0F7F4;padding:14px 16px;margin:2em 0;border-left:3px solid #1F6F78;">
  <p style="font-size:15px;font-weight:600;color:#173B46;line-height:1.6;margin:0;">
    <strong>带走一句话：</strong>最好的计划不是把时间塞满，是先守住一件最重要的事不被挤走。
  </p>
</section>
```

### 8.3 软广落点（选配）

```html
<section style="background:#FFF7EB;padding:16px 18px;margin:1.5em 0;text-align:center;">
  <p style="font-size:15px;font-weight:700;color:#1A1A1A;margin:0 0 8px 0;">Harborfield Field Guide</p>
  <p style="font-size:14px;color:#4A4A4A;line-height:1.7;margin:0 0 10px 0;">12 周的练习册，每周一个可打印的反思模板。不承诺改变人生，只陪你走 12 周。</p>
  <p style="font-size:14px;color:#1F6F78;font-weight:600;margin:0;">了解更多 → 私信「节奏」</p>
</section>
```

### 8.4 关注连接区（每篇固定）

```html
<section style="background:#F7F4ED;padding:14px 16px;margin:1.5em 0;text-align:center;">
  <p style="font-size:16px;color:#24323D;line-height:1.6;margin:0;">
    对独立工作者的可持续节奏感兴趣？<br>关注公众号「Harborfield Notes」后私信「节奏」，一起聊聊。
  </p>
</section>
```

### 8.5 作者签名

```html
<p style="font-size:14px;color:#8B9DAF;text-align:center;margin:1em 0;">
  Alex Chen — Harborfield Notes 创始人，专注独立工作者的可持续工作节奏。
</p>
```

---

## 九、配色速查

用 Profile 里的 `accent_color` 替换下面示例中的 `#1F6F78`（冷色系）或 `#c9a030`（暖色系）。

| 用途 | 建议色值（冷色） | 建议色值（暖色） | 说明 |
|------|----------------|----------------|------|
| 强调色/主色 | `#1F6F78` | `#c9a030` | 金句框左边框、编号圆圈、链接色 |
| 正文 | `#3d3d3d` | `#3d3d3d` | 统一用这个，不要纯黑 `#000` |
| 标题 | `#1A1A1A` | `#141414` | 比正文重一点 |
| 引导段/辅助文字 | `#6A6A6A` | `#6A6A6A` | lead、说明、引用 |
| 浅底 | `#EAF4F2` | `#faf2d8` | 金句框/卡片底色 |
| 更浅底 | `#F7F9FA` | `#F7F4ED` | 关注区/CAT 底色 |
| 浅边框 | `#e0d8c8` | `#d4b040` | 卡片边框、金线 |
| 淡文字 | `#8B9DAF` | `#b8a060` | 签名、说明、角标 |

---

## 十、常见页面结构（三段式）

```
[开头钩子] → lead 段落，亮身份或反常识
[章节1] → h2 → 正文 → 金句框
[章节2] → h2 → 正文 → 卡片/对比 → 金句框
[章节3] → h2 → 正文 → 步骤列表 → 金句框
[带走一句话] → takeaway section
[软广落点] → 可选 cta section
[— END —]
[关注连接] → connect section
[作者签名]
```

---

> **使用方式：** AI 排版时从上面选合适的组件拼装。不是每篇文章把所有组件都用一遍——挑 2-3 种最适合文章节奏的。一段纯文字超过四屏还没视觉打断，加一个卡片或金句框。
