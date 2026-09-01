# W4DJ v2 兼容备忘录

## 目的

这份备忘录只记录老炮 DJ Skill 与 W4DJ RKB 之间的 `.w4dj` 机器兼容约定。它不是给用户选版本的界面，也不是一份新的用户流程。

## 基线与证据

- 基于用户指定的 aKb4 基线。
- 对照的联动任务：[`codex://threads/01a0580a-4e81-7710-89c9-90611dcaa692`](codex://threads/01a0580a-4e81-7710-89c9-90611dcaa692)。
- 当前 RKB 工作树：[`/Users/mac2/.codex/worktrees/a1fe/W4DJ RKB/src/dj_playlist.rs`](/Users/mac2/.codex/worktrees/a1fe/W4DJ%20RKB/src/dj_playlist.rs)。
- 对应分支：`codex/w4dj-pro-4.0.0-beta.1`。
- RKB 解析器将 `format_version` 作为必填整数字段，只接受值 `2`，并拒绝未知字段。这是本工作区补齐该字段的直接原因。

## 现行决定

1. Skill 生成的 `.w4dj` 根对象固定写入 `"format_version": 2`。
2. 用户只需说“导出到 w4dj”，不需要知道、选择或手动填写版本。
3. 无版本、非 `2`、未知根字段和未知曲目字段均不自动迁移；这类文件应重新导出。
4. 本次只改老炮 DJ Skill 的导出边界，不改 RKB 解析器、不复制 RKB 代码，也不接入 RKB 内部数据库。

## 固定线上形状

```json
{
  "format": "w4dj",
  "format_version": 2,
  "export_id": "unique-export-id",
  "playlist": {"name": "Playlist Name"},
  "tracks": [
    {
      "position": 1,
      "title": "Complete Official Title (Extended Mix)",
      "artist_display": "Official Artist",
      "netease_track_id": "123456"
    }
  ]
}
```

`playlist` 只能有 `name`。每首曲目只能有 `position`、`title`、`artist_display` 和可选的字符串 `netease_track_id`。不写 BPM、调性、本地路径、音频、下载任务或 RKB 内部字段。

## 不在本次范围内

- 不维护 RKB 的采集、转换、库存或 UI 逻辑。
- 不为旧文件增加自动迁移、多版本回退或两套导出模式。
- 不把这个机器字段暴露成用户的选项。

## 什么时候才能移除

只有在 RKB 解析器和 Skill 同时设计并验证了新协议，并且双边的实际导入测试都通过后，才能考虑移除这个固定字段。到那时必须同时更新：

- `references/w4dj.schema.json`
- `references/export.md` 和两份 README
- `evals/w4dj-fixtures.json` 及其验证脚本
- RKB 对应解析、序列化和实际导入测试
- 本备忘录和工作区边界说明
