# 老炮DJ Skill 工作区边界

本工作区以 `dj-crate-digger` Skill 包为唯一主体。`SKILL.md`、`references/`、`evals/`、`scripts/`、`agents/`、`docs/w4dj/` 和 `LICENSE` 均从本机已安装的老炮 DJ Skill 原样分离而来；后续对选歌流程、语言包、验证脚本和 `.w4dj` 导出行为的修改，默认只在本工作区进行。

## 与 W4DJ RKB 的最小联动面

老炮 DJ 只负责生成推荐报告和用户明确请求的 UTF-8 `.w4dj` 交接文件；它不下载音频、不读取 W4DJ 数据库、不处理本地音频，也不负责导出 Rekordbox 播放列表。跨项目联动只经过 `.w4dj` 文件：歌单名、曲目顺序、完整官方歌名、艺人，以及可选的字符串 `netease_track_id`。

需要了解联动时，按以下顺序读取，不要扫描整个 RKB：

1. 本工作区的 [`references/export.md`](../references/export.md)、[`references/w4dj.schema.json`](../references/w4dj.schema.json) 和 [`docs/w4dj/README.md`](w4dj/README.md)。
2. 当前对照基线 RKB 工作树的 [`src/dj_playlist.rs`](</Users/mac2/.codex/worktrees/a1fe/W4DJ RKB/src/dj_playlist.rs>)：`.w4dj` 解析、字段拒绝和版本要求。
3. RKB 的 [`src/dj_playlist_match.rs`](</Users/mac2/.codex/worktrees/a1fe/W4DJ RKB/src/dj_playlist_match.rs>)：ID 精确匹配、标题+艺人唯一回退和歧义处理。
4. RKB 的 [`src/w4dj_library.rs`](</Users/mac2/.codex/worktrees/a1fe/W4DJ RKB/src/w4dj_library.rs>)：实际输出路径与网易云身份的本地索引关系。
5. RKB 的 [`tests/dj_playlist.rs`](</Users/mac2/.codex/worktrees/a1fe/W4DJ RKB/tests/dj_playlist.rs>)、[`tests/dj_playlist_match.rs`](</Users/mac2/.codex/worktrees/a1fe/W4DJ RKB/tests/dj_playlist_match.rs>) 和 [`tests/w4dj_library.rs`](</Users/mac2/.codex/worktrees/a1fe/W4DJ RKB/tests/w4dj_library.rs>)：只在需要核对行为时读取对应测试。

RKB 的其他模块、分析模型、转换链路、数据库迁移、UI 和历史计划不属于本工作区的默认上下文。除非任务明确涉及这些内容，否则不读取、不复制、不在这里维护镜像。详细决策和移除条件见 [W4DJ v2 兼容备忘录](w4dj-v2-compatibility-memo.md)。

## 当前协议同步状态

当前已按 aKb4 / W4DJ Pro 4 基线对齐：Skill 的 `.w4dj` 导出固定包含 `format_version: 2`，它是兼容用的机器字段，不是用户需要选择的版本。归档的证据、非目标和可能的移除条件见 [W4DJ v2 兼容备忘录](w4dj-v2-compatibility-memo.md)。

## 初始化来源

本目录的初始内容来源于：`/Users/mac2/.codex/skills/dj-crate-digger`。源 Skill 与本工作区现在是两份独立文件；在本工作区完成修改后，不自动同步回本机 Skill 安装目录，也不自动提交或发布。
