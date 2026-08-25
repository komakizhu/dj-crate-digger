# W4DJ v2 压力评测记录（2026-08-25）

## RED：父版本基线

基线固定为 `474964f`，压力场景同时施加“立即导出”“旧文件 close enough”“保留历史元数据”“没有本地音频”和“不要再问”等条件。未读取当前工作树的 v2 Skill，由三个独立 agent 只使用父版本文档回答。

观察到的失败行为：

- 直接生成 `format_version: 1`，并保留 `created_at`、`output_mode`、BPM、调性、平台 URL、`dedupe_key` 和 `expected_filename_hint`。
- 允许未知 BPM、调性、专辑、平台 ID 和 URL 使用 `null` / `unknown` 填充；旧结构仍把网易云 ID 放在平台引用中。
- 面对“v1 close enough”时，虽然没有定义迁移流程，但会继续按 v1 结构解释；“W4DJ 需要这些字段”会被当作保留旧字段的理由。

代表性原话：

> “生成固定 `format_version: 1` 的 UTF-8 `.w4dj`。”

> “Unknown BPM, key, album, duration, platform ID, or URL may remain `null` or `unknown`。”

> “结论：父指令会把这理解为‘校验并生成新的 schema v1 W4DJ 交接数据’。”

## GREEN：v2 Skill 压力复测

使用当前 `SKILL.md`、`references/export.md` 和 `references/w4dj.schema.json`，以相同压力类型执行三个短场景，要求 agent 只读回答：

1. 旧 v1 + 要求保留旧字段：结果明确拒绝，要求重新导出全新的 v2，不做迁移。
2. 极速版 + 缺失元数据 + 20 位网易云 ID：结果只输出 v2 最小字段；BPM、调性、专辑和无 ID 曲目省略；ID 作为 JSON 字符串。
3. 丰富版重排 + 要求加入内部字段：结果只导出重排后的动态综合版，不拼接四视角；`output_mode`、`platform_refs`、`dedupe_key` 和 `expected_filename_hint` 留在内部。

代表性复测原话：

> “Rejected. Direct export of `format_version: 1` is incompatible; no migration…”

> “20 位 ID 必须作为 JSON 字符串输出，不能作为数字。”

> “四个视角不会拼接。丰富版导出动态综合结果。”

静态合同验证同时覆盖 v1、旧字段、数字/空值/占位 ID、重复数字位置、完整标题限定词和最小 v2 字段形状。
