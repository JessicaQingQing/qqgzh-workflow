# WeChat CSS Baseline

Use a conservative inline-compatible subset:

```css
.article { max-width: 100%; color: #24323D; font-size: 16px; line-height: 1.8; }
.article p { margin: 0 0 1em; }
.article h1 { color: #173B46; font-size: 26px; line-height: 1.35; margin: 0 0 .7em; }
.article h2 { color: #1F6F78; font-size: 20px; line-height: 1.45; margin: 1.5em 0 .65em; }
.article .lead { color: #4B5D67; font-size: 17px; }
.article .takeaway { background: #EAF4F2; border-left: 4px solid #1F6F78; padding: 14px 16px; margin: 1.25em 0; }
.article img { display: block; width: 100%; height: auto; margin: 1.25em 0; }
.article .cta { background: #F7F4ED; padding: 14px 16px; margin: 1.5em 0; }
```

Forbidden: `position: fixed`, `position: sticky`, `@import`, scripts, iframes, form controls, external fonts, and concealed text.
