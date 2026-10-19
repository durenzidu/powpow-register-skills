# powpow-register 多语言 v2.2.0 对齐 + 发布 — 完成报告

## 结论
全部 **38 个**语言包 + 中文主包（`powpow-register`）已对齐到 **v2.2.0**（适配平台免费测试期），并于 2026-10-19 全部发布上线；注册表逐个 slug 核对确认 39/39 均为 `2.2.0`。本仓库同步更新：38 个语言包 + `work/zh` 主包 + `base210` 英文基线 + v2.2.0 翻译管线（`data2_*` / `apply2.py` / `changelog2.py` / `verify2.py`）。

## 增量内容（v2.1.0 → v2.2.0，严格只改用户可见交互文案）
- 脚本 `scripts/powpow-register.mjs` **零改动**（457 行含 PayPal 全部保留）；仅中性化 3 处提示文案。
- `SKILL.md`：frontmatter description / intro / banner / 触发行改写；流程表第 6/7 行重写；Step 6+7 章节整体替换；Step 8 更新；硬规则区第 4 条 bullet 换成免费期边界。
- 核心行为变化：注册成功后 `login-link --target home` **直接进首页**（免费测试期，无需付费即可使用全部功能）；**自适应回退**——用户落地订阅页 = 测试期已结束，流程自动转支付路径（pending 链接 → create-order → query → refresh-login → home 链接）。该设计使付费墙恢复后无需再改 skill。
- `references/agent-flow.md`：login-link 表行、Dual-Link + Full Sequence 段、错误表 403 行 + 新增订阅落地行、fallback 行。
- `references/payment-and-activation.md`：首个 `## ` 标题后插入免费期提示 blockquote。
- `references/registration-flow.md`：状态流转段整体替换 + 403 行 + 落地行。
- `README.md`：版本段扩展；功能项 3（`me?token=` 行）替换。
- `_meta.json` / `skill-card.md` / `clawhub-listing.json`：版本号 2.1.0→2.2.0，listing notes 更新。

## 翻译与校验
- 23 个翻译 key × 38 语言，`data2_en.py` 为英文模板，`data2_1.py`–`data2_29.py` 分文件承载，`data2_all.py` 聚合。
- 每个语言三重校验全部通过：① Python 语法编译；② 异源文字杂质扫描（CJK/假名/西里尔/阿拉伯文/其他印度系文字混入，豁免有意的平台错误文案「请完成订阅以激活账户」与印度系共用 danda）；③ 23 key 完整性 + 语言无关锚点（`pending_payment`、`me?token=`、`powpow_token`、`powpow-simple`、`¥6.99/¥19.99/¥69.99`、URL、命令、版本号等）。
- 期间修复的杂质：JA/KO 中文污染（重建）、DE 德语引号语法错误、BN 韩文混入、FA「WeChat」音译、ML 泰米尔/卡纳达/孟加拉字符混入、MR 拉丁混排、GU/PA/BHO/OR/PNB 等多处字符级错误、PNB 9 处 CJK 杂质。
- `apply2.py` 需处理本地化数字：bn 用孟加拉数字（U+09E6–EF）、fa/ur 用波斯数字（U+06F0–F9），已内置多数字系统归一化匹配；曾因波斯数字基址写错（0x06F6）导致 fa 匹配失败，已修正为 0x06F0。

## 发布校验（2026-10-19）
| 批次 | 语言 | 结果 |
|---|---|---|
| 主包 | zh（powpow-register） | 2.2.0（2026-10-18 发布） |
| 批次 1 | en ja ko es fr de pt it ru pl tr vi id ar hi th | 16/16 在线 2.2.0 |
| 批次 2 | bn ur fa ta te ml kn mr gu pa am bho ha jv ln pcm sw tl yo my or pnb | 22/22 在线 2.2.0 |

- 注册表按版本号去重：若某包已存在 2.2.0，重复发布会直接返回 `400 Version 2.2.0 already exists`——本次全部返回 200 新建，证明 38 个语言包此前从未发布过 2.2.0（昨天只更新了中文主包）。
- `publicationStatus` 创建后为 `pending`，约 1–3 分钟自动翻正式发布；最终 `check_registry.py` 对 39 个 slug 全部确认 `version: 2.2.0`。

## 文件构成
- 每包固定 16 个文件（zh 主包 17：多 `skill-card.md`；与发布源差异的 `_meta.json`/`skill-card.md` 从 git 历史恢复后单独改版本号）。
- `base210/` 为英文基线（= work/en），供 `apply.py` 复制脚本与 skill-card 到各包。
