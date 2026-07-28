# Profile 配置指南

你的全部品牌信息在一个 JSON 文件里。改它就是换品牌。

---

## 结构

```json
{
  "schema_version": 1,
  "brand":        { ... },   // 品牌身份
  "audience":     { ... },   // 目标读者
  "visual":       { ... },   // 视觉（配色 + 配图风格 + 图床白名单）
  "connection":   { ... },   // 读者连接（每篇固定的底部邀请）
  "monetization": { ... },   // 商业转化（产品/服务，可空）
  "publishing":   { ... }    // 发布控制
}
```

---

## `brand` — 品牌身份

```json
"brand": {
  "name": "你的公众号名称",
  "tagline": "一句话说清楚你的号是干嘛的",
  "voice": ["说人话", "给方法", "不灌水"],
  "avoid": ["标题党", "贩卖焦虑"],
  "style_notes": "仿写过程中沉淀的偏好。喜欢开头直接抛出问题，句子短，一段不超过三句话..."
}
```

| 字段 | 说明 |
|------|------|
| `name` | 公众号名称，出现于页眉和 connection CTA |
| `tagline` | 一句话定位 |
| `voice` | 2-4 个文风关键词，AI 参考 |
| `avoid` | 你不想要的写法 |
| `style_notes` | **仿写过程中自动积累**——你喜欢什么开头方式、句子长短、段落节奏。AI 每次仿写后更新 |

---

## `audience` — 目标读者

```json
"audience": {
  "primary": "想用 AI 提效但不知道从哪开始的职场人",
  "needs": ["能落地的实操指南", "避坑经验", "选型推荐"]
}
```

| 字段 | 说明 |
|------|------|
| `primary` | 核心读者一句话画像 |
| `needs` | 读者最需要的东西（2-4 个） |

---

## `connection` — 读者连接（每篇固定）

文章底部永远出现，用来引导读者关注公众号并私信你。

```json
"connection": {
  "primary_channel": "公众号私信",
  "account_name": "你的公众号名",
  "invitation": "对XX感兴趣？关注公众号「XX」后私信「暗号」，一起聊聊。",
  "wechat_id": ""
}
```

| 字段 | 说明 |
|------|------|
| `primary_channel` | 通常是 `"公众号私信"` |
| `account_name` | 跟 `brand.name` 一样 |
| `invitation` | 邀请语——暗号+路径清晰 |
| `wechat_id` | 可留空 |

**invitation 要点：** 暗号给一个具体词（如"聊聊""节奏""AI转型"），温和，像邀请聊天不象引流。

**跟 monetization offer 的区别：**
- connection：关注 → 建立关系，**每篇都有**，在 `— END —` 之后
- offer：了解产品 → 购买，**选了才有**，在正文中段

---

## `visual` — 视觉规范

```json
"visual": {
  "accent_color": "#1F6F78",
  "image_style": "clean geometric flat illustration",
  "approved_image_hosts": ["https://mmbiz.qpic.cn"]
}
```

| 字段 | 说明 |
|------|------|
| `accent_color` | 品牌强调色，十六进制 `#` + 6 位 |
| `image_style` | 配图风格描述，**AI 生图时参考，不生图可不管** |
| `approved_image_hosts` | 图片域名白名单，**默认只允许微信官方图床** |

> **配图是可选的。** 你不生图可以跳过——审查不会因为缺图而拦截。只要出现的图片 URL 在白名单里就行。

---

## `monetization` — 商业转化

```json
"monetization": {
  "offers": [
    {
      "name": "一对一职业诊断",
      "fit": "想换方向但不确定往哪走的职场人",
      "cta": "感兴趣可以私信聊聊你的情况。"
    }
  ],
  "claims_policy": "只使用私有知识库中可核实的事实，不夸大。"
}
```

| 字段 | 说明 |
|------|------|
| `offers` | 产品/服务列表，**可为空数组 `[]`** |
| `name` | 产品或服务名 |
| `fit` | 适合谁 / 什么场景 |
| `cta` | 低压力邀请语——不催促、不制造紧迫感 |
| `claims_policy` | 证据使用原则 |

**不卖东西** → `"offers": []`。工作流自动跳过转化步骤。底部连接 CTA 依然在。

内置规则（你不需要手动管）：
- 一篇文章最多 1 个 offer，不强塞
- 商业内容 ≤~20%
- 观点先行，身份后置
- offer 只出现一次，不反复刷
- 不虚构稀缺感、紧迫感、保证

---

## `publishing` — 发布控制

```json
"publishing": {
  "mode": "manual_draft_only",
  "requires_explicit_confirmation": true
}
```

| 字段 | 说明 |
|------|------|
| `mode` | 固定 `"manual_draft_only"` |
| `requires_explicit_confirmation` | **必须 `true`，不能改** |

---

## 完整示例

→ `profiles/example/profile.json`

---

## 验证 Profile

```bash
python scripts/validate_profile.py 你的Profile路径.json
```

它会检查：必填字段有值、颜色格式正确、确认开关是 true、没不小心写进本地路径或 API Key。

---

## 私密信息怎么存

真实姓名、公司名、案例细节、客户数据、生图 API Key、发布凭据 → 放 `private/` 下。

`private/` 在 `.gitignore` 里，不进 Git 也不进发布包。
