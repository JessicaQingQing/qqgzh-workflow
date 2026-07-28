---
name: 排版
description: 把文章草稿 + 软广方案 → 微信兼容 HTML。只用微信不会吞的 CSS，手机优先。
---

# 微信排版

把文章变成微信后台能直接粘贴的 HTML，手机上看着干净舒服。

## 吃进去什么

- 文章草稿（纯文本或 Markdown）
- 软广方案（`软广判断` 出来的，可能是"这篇不推"）
- 用户 Profile ——品牌语气、强调色、连接 CTA、软广话术
- `references/wechat-css.md` ——微信 CSS 白名单
- `references/article-structure.md` ——文章结构规范
- `references/typography-guide.md` ——排版样式参考：各种金句框、卡片、对比表、开头钩子、结尾组件怎么拼。**排版时从里面选 2-3 种最适合本篇节奏的组件。**
- `references/anti-ai-voice.md` ——去 AI 味写作指南：文章读起来像人写的，不是机器写的。写稿时对照自查。

> 纯文字超过四屏还没一个视觉打断的话，加一个卡片或金句框。样式从 `typography-guide.md` 里挑。
> 写完之后读一遍。如果这段话你对朋友不会这么说，改掉。具体规则见 `anti-ai-voice.md`。
- `templates/article.html` —— HTML 骨架

## 吐出来什么

一个自包含的 `.html` 文件，结构固定，**按顺序**：

1. `<h1>` 大标题
2. `<p class="lead">` 开头钩子段落
3. 封面图（可选——没图就直接跳过）
4. 正文，含 `<h2>` 章节标题和段落
5. **`.takeaway` 金句区** ——读者看完能带走的一句话（**必须**）
6. 软广落点（可选——没选方向就去掉 `.cta` 区块）
7. `— END —` 结束标记
8. **`.connect` 连接区** ——Profile 里的固定关注引导（**必须**）
9. 作者简介一行

## CSS 铁律

- 所有样式**行内写**。不要 `<style>` 块，不要外部样式表。
- 不要 `@import`，不要外链字体。
- 不要 `position: fixed` 和 `sticky`。
- 不要 `<script>`、`<iframe>`、`<form>`、`<input>`、`<button>`。
- 不要 `display: flex` 和 `grid`。
- 正文字号不小于 15px；行高舒服（1.6–1.8）。
- 图片只从 Profile `visual.approved_image_hosts` 里的白名单域名加载（默认只有 `https://mmbiz.qpic.cn/`）。

## 颜色怎么用

Profile 里的 `accent_color` 只用在：
- `.takeaway` 金句区的左边框
- 可选：章节标题小点缀、关键词轻强调

别到处用。一章一处就够了。

## 脑子里装着手机

微信文章 90% 在手机上读。写每一行 HTML 之前先想：375px 宽的屏幕上这好看吗？段短、标题紧凑、留白慷慨但不浪费。
