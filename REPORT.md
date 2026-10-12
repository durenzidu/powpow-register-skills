# powpow-register 多语言 v2.1.0 对齐 + 发布 — 完成报告

## 结论
全部 **38 个**语言变体已对齐到 **v2.1.0**（PayPal 订阅改为 agent 代管），其中第三批 12 个语言（am bho ha jv ln pcm sw tl yo my or pnb）于本批次完成翻译、补丁、校验并**发布上线**，且逐字节回环校验通过。

## 增量内容（v2.0.1 → v2.1.0，严格只改用户可见交互文案）
- 脚本 `scripts/powpow-register.mjs` 新增 `--provider alipay|paypal`；PayPal `ACTIVE`/`PENDING` 轮询、新 PayPal API 端点。
- `SKILL.md`：描述/简介加入 PayPal；版本号 2.0.1→2.1.0；流程第 6 步改为「让用户选支付渠道」；支付边界文案加 /PayPal。
- `references/payment-and-activation.md`：新增 `## PayPal 订阅通道` 章节 + 3 条排错行。
- `references/agent-flow.md`：命令表、API 表、时序、排错表加入 PayPal。
- `README.md`:功能/安全/支付说明同步 PayPal。

## 第三批 12 个语言发布校验
| 语言 | 本地 verify3 | 发布 | 回环 verify_upload |
|---|---|---|---|
| am 阿姆哈拉 | OK | 200 ok | OK |
| bho 博杰普尔 | OK | 200 ok | OK |
| ha 豪萨 | OK | 200 ok | OK |
| jv 爪哇 | OK | 200 ok | OK |
| ln 林加拉 | OK | 200 ok | OK |
| pcm 尼日利亚皮钦 | OK | 200 ok | OK |
| sw 斯瓦希里 | OK | 200 ok | OK |
| tl 他加禄 | OK | 200 ok | OK |
| yo 约鲁巴 | OK | 200 ok | OK |
| my 缅甸 | OK | 200 ok | OK |
| or 奥里亚 | OK | 200 ok | OK |
| pnb 西旁遮普 | OK | 200 ok | OK |

- 26 个较早语言（批次 1、2）此前已上线 2.1.0，本次复核确认在线状态均为 2.1.0。
- 每个语言固定 7 个文件发生变化：README.md、SKILL.md、_meta.json、references/agent-flow.md、references/payment-and-activation.md、scripts/powpow-register.mjs、skill-card.md。

## 备注 / 待办（非本批范围）
- `de` 商店简介仍停留在 v1 旧文案：ClawHub API 无商店简介写入通道，需联系 ClawHub 官方处理。
- 发布状态 `publicationStatus` 创建后为 `pending`，约 1–3 分钟内自动转为正式发布；本次已确认 12 个全部翻转为 `2.1.0` 在线。
