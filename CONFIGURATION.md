# Profile 配置指南

你的全部信息在一个 JSON 文件里。改它就是换一个人——你的经历、你的资产、你想写什么、写给谁。

---

## 结构

```json
{
  "schema_version": 2,
  "identity":     { ... },   // 你是谁——经历、能力、风格
  "content":      { ... },   // 你想写什么——方向、选题库
  "brand":        { ... },   // 公众号信息（可选）
  "channels":     { ... },   // 发布渠道（可选）
  "connection":   { ... },   // 读者连接（可选，默认关）
  "publishing":   { ... }    // 发布控制
}
```

---

## `identity` — 你是谁（核心必填）

```json
"identity": {
  "name": "陈则远",
  "professional_background": "12年供应链管理，从采购专员做到供应链总监",
  "key_experiences": [
    {
      "event": "供应商突然断供，72小时找到替代并完成交付",
      "capability": "危机中的供应链快速重组",
      "evidence": "被写进了公司风险管理手册，老板年会专门提了",
      "status": "confirmed"
    }
  ],
  "voice": ["具体", "接地气", "有判断"],
  "avoid": ["空洞术语", "贩卖焦虑"]
}
```

| 字段 | 说明 |
|------|------|
| `name` | 你的名字或笔名 |
| `professional_background` | 一句话说清你干什么、干了多久 |
| `key_experiences` | 3-8 件你做过的事——每件包含具体事件、体现的能力、外部证据、状态 |
| `voice` | 你说话的风格（2-4 个关键词） |
| `avoid` | 你不想用的写法 |

经历状态：`confirmed`（已确认）/ `hypothesis`（还在验证）

---

## `content` — 你想写什么（核心必填）

```json
"content": {
  "directions": [
    {
      "label": "供应链人的实战笔记",
      "target_readers": "做了几年供应链但感觉在做执行的人",
      "sample_topics": ["供应商说断就断——你的B计划不该只是备选名单"],
      "status": "active"
    }
  ],
  "topic_bank": [
    {
      "topic": "供应商突然断供，我72小时做了什么",
      "category": "经验案例",
      "source_event": "2023年供应商断供危机",
      "status": "drafted"
    }
  ]
}
```

方向状态：`active`（在写）/ `testing`（试试看）/ `parked`（暂时搁置）
选题状态：`seed`（想法）/ `outlined`（有提纲）/ `drafted`（有初稿）
选题类别：`经验案例` / `判断框架` / `反常识观察` / `失败复盘` / `关系洞察`

---

## `brand` — 公众号信息（可选）

```json
"brand": {
  "name": "则远的供应链手记",
  "tagline": "一个供应链人的实战复盘",
  "style_notes": "喜欢开门见山，不喜欢铺垫"
}
```

如果你还没有公众号，这部分可以空着。以后有了再填。

---

## `channels` — 发布渠道（可选）

```json
"channels": {
  "wechat": {
    "enabled": true,
    "account_name": "则远的供应链手记",
    "publishing_mode": "manual_draft_only"
  }
}
```

目前只支持微信公众号。按需启用。

---

## `connection` — 读者连接（可选）

```json
"connection": {
  "enabled": true,
  "invitation": "对供应链实战话题感兴趣？关注「则远的供应链手记」后私信「供应链」。",
  "offers": []
}
```

| 字段 | 说明 |
|------|------|
| `enabled` | `true` 或 `false`——是否在文章底部加读者连接入口 |
| `invitation` | 关注引导文案（仅 `enabled: true` 时生效） |
| `offers` | 你的产品或服务——暂时没有就空数组 `[]` |

**很多人在探索阶段不需要连接入口——关掉就好，文章照样发。** 审查不会因为缺连接入口而拦截。跟旧版不一样：旧版每篇强制有连接 CTA，新版由你控制。

---

## `publishing` — 发布控制

```json
"publishing": {
  "requires_explicit_confirmation": true
}
```

`requires_explicit_confirmation` **必须为 `true`**——每次发布前都要你亲口确认。

---

## 完整示例

→ `profiles/example/profile.json`（虚构人物"陈则远"，12年供应链管理）

---

## 验证 Profile

```bash
python scripts/validate_profile.py 你的Profile路径.json
```

检查：必填字段有值、格式正确、确认开关是 true、没写进本地路径或 API Key。

---

## Profile v1 迁移到 v2

如果你有旧版 Profile（v1，`schema_version: 1`），结构从"品牌优先"变成了"人和经历优先"。让 AI 帮你迁移——把旧 Profile 贴给 AI，说"帮我升级到 v2 格式"。

主要变化：
- 新增 `identity`（必填）：你的专业背景和关键经历
- 新增 `content`（必填）：内容方向和选题库
- `brand` / `channels` / `connection` 变为可选
- `connection` 新增 `enabled` 开关，默认关
- `audience` 合并入 `content.directions[].target_readers`
- `visual` 简化入 `brand`
- `monetization` 合并入 `connection`

---

## 私密信息

真实姓名、公司名、案例细节、客户数据、生图 API Key、发布凭据 → 放 `private/` 下。

`private/` 在 `.gitignore` 里，不进 Git 也不进发布包。
