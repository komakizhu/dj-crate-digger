# DJ Crate Digger `.w4dj` v2 最小交接格式

## 目标

让 DJ Crate Digger 输出一个只承担“歌单顺序与显示身份”职责的 `.w4dj` 交接文件。后续 W4DJ 应用负责本地歌曲匹配、占位音频、M3U8 和 Rekordbox 工作；Skill 不把推荐元数据和本地实现细节泄漏到交接格式。

## 固定格式

```json
{
  "format": "w4dj",
  "format_version": 2,
  "export_id": "playlist-001",
  "playlist": { "name": "UK Bass" },
  "tracks": [
    {
      "position": 1,
      "title": "Midnight Request Line (Extended Mix)",
      "artist_display": "Skream",
      "netease_track_id": "123456789012345678"
    }
  ]
}
```

根层只允许 `format`、`format_version`、`export_id`、`playlist` 和 `tracks`；`playlist` 只允许 `name`。每首曲目只允许 `position`、完整官方 `title`、`artist_display` 和可选的 `netease_track_id`。网易云 ID 必须是 JSON 字符串；没有 ID 时省略字段，不写占位值。

完整官方曲名中的 Remix、Edit、Live、Dub、Instrumental、Radio Edit、Extended Mix 等限定必须保留在 `title` 内，不设独立 `version` 字段。BPM、调性、专辑、URL、平台状态、`record_id`、`artists`、`duration`、`musical_key`、`platform_refs`、`dedupe_key`、`expected_filename_hint` 和本地路径均不属于 v2 文件。

## 兼容策略

v1 明确拒绝，不接受旧字段、不自动归一化、不迁移。用户需要从 DJ Crate Digger 重新导出 v2。未知字段同样拒绝，以免 W4DJ 在未设计协议的情况下误读推荐元数据。

## 验证与交付边界

- `references/w4dj.schema.json` 是 v2 的机器可读结构。
- `evals/w4dj-fixtures.json` 覆盖最小有效文件、无网易云 ID、超大字符串 ID、同一歌曲在多个不同 `position` 的重复播放位置、重复数字位置、v1、数字/占位 ID、本地路径和旧元数据字段拒绝。
- `scripts/validate_w4dj_contract.py` 同时检查 Schema、夹具、模板术语和 v2 最小字段形状。
- Skill 仍可在内部记录平台链接、调性、BPM、去重键和验证证据，但这些不进入 `.w4dj`。
- 宿主没有文件写入能力时，只返回等价 JSON manifest，不声称已经创建文件。

格式校验只能保证官方限定词与完整 `title` 使用同一个字段，不能凭 JSON 自身判断曲名是否漏写了 Remix 或 Edit。完整官方歌名仍由 Skill 的逐曲平台验证负责；夹具使用带 `(Remix)` 的合法标题，并拒绝独立 `version` 字段。
