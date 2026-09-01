# 老炮DJ（dj-crate-digger）

[English](README.en.md)

中文名：老炮DJ；英文名、Skill 名与仓库名：`dj-crate-digger`。

这是一个原生通用 Agent Skill 包，面向 DJ、音乐制作人与电子音乐听众。它把自然语言选歌需求变成经过联网搜索、逐曲页面核验、录音去重、排序和 Set 编排的推荐报告。所有支持标准 Agent Skills 的客户端使用同一份 `SKILL.md` 与 `references/`，不维护宿主专属算法或第二份提示词副本。

## 一、核心能力

### 1.1 自适应问卷与个性化

综合版是所有已触发 DJ 请求的默认输出，与用户说了几句、是否进入问卷无关；只有用户明确指定极速版或丰富版时才切换。用户一次说清场景、声音方向和歌曲数量或 Set 时长，或者用一句话明确表示“其余你判断、直接出结果”时，Skill 跳过问卷并直接按综合版执行。信息不足且没有授权补全时，才进入两轮固定问卷：第一轮收集场景、目标国家/地区、核心声音方向、歌曲数量或 Set 时长、输出版本和其他限制；第二轮收集具体风格、BPM、熟悉度与发现感、时代与经典、情绪、能量走势、平台与链接要求和其他。两轮中没有明确选其他模式，最后仍默认输出综合版。问卷均来自固定语言包，不增加第三轮普通需求收集。

沟通语言和目标市场分开处理。语言决定可见文案，地区只决定当前搜索的文化语境和可用性；明确地区不会改变回复语言，留空地区只使用宽泛的语言市场，也不会写入长期画像。

新会话通过 `/dj` 等斜杠入口时，Skill 会先读取最近会话中的用户语言信号和身份语言偏好，再决定语言；最近会话优先。最近 5 次中有 4 次使用同一语言时，才自动学习为沟通语言偏好。完全没有语言信号时，只显示一次“请选择沟通语言 / Choose your language”，不会默默输出英文模板。该语言偏好与 DJ 品味、目标市场分开保存。

### 1.2 三种输出模式

| 模式 | 适合场景 | 输出 |
|---|---|---|
| 极速版 | 先快速拿到可用曲目 | 独立三列表、单一召回通道、分段首批与续跑规则 |
| 简要版 | 获取一份完整歌单 | 一张严格十二列表格、调性、选择理由和一条创造性接歌建议 |
| 丰富版 | 比较不同选歌方向 | 风格、场景、熟悉度/发现感三个专项视角，加一个动态综合视角 |

简要版和丰富版的表格固定为：`歌名 | 艺术家 | 专辑/EP | 风格 | BPM | 调性 | 歌曲时长 | 能量级 | 发行时间 | 简介 | 选择原因 | 链接`。所有模式都保留完整官方歌名、平台策略、逐曲证据和录音级去重。

### 1.3 搜索、文化语境与排序

官方艺人、厂牌、发行商和授权 DJ 商店用于核验身份、完整歌名、BPM、调性和发行信息。1001Tracklists、Resident Advisor、Pitchfork、Mixmag、DJ Mag、The Quietus 等可用于候选召回、文化语境和 DJ 使用信号，但不能代替最终曲目链接。用户指定的平台只影响允许的搜索与播放链接，不会悄悄回退到其他平台。

调性只接受与同一完整官方歌名对应的可靠证据；未知或冲突时保留歌曲并显示未知。简要版和丰富版收到明确肯定后，才按基础 Camelot 兼容关系进行五度圈重排，并提供最多五组需要 DJ 试听确认的 double drop 候选。没有波形或实际试听证据时，接歌建议只用“可尝试”的创造性表达。

### 1.4 私有反馈记忆

用户可以用自然语言说喜欢、不喜欢、这场会不会用，或粘贴实际播放记录。当前会话反馈立即生效；长期档案只在一轮反馈被整理成简短摘要并获得明确确认后保存。事件日志与可重建画像均保留在本地私有范围内，长期画像在推荐权重中不超过 10%，第一阶段不上传，也不做匿名协同学习。

## 二、快速开始

把完整仓库目录放入客户端支持的 Agent Skills 目录，确保 `SKILL.md`、`references/` 和语言包一起存在，然后直接提出 DJ 选歌需求：

```text
/dj-crate-digger
```

也可以使用旧别名：

```text
/迪歌
```

自然语言同样可以触发，例如：

```text
帮我为广州的地下俱乐部排一套 60 分钟 UK Bass set，参考 Skream 和 Nikita, the Wicked。
```

完整流程是：发起需求 → 信息足够或已授权补全时直接搜索，否则完成两轮问卷 → 逐曲核验 → 返回综合版或用户明确选择的模式 → 可选反馈、文字歌单、W4DJ 或五度圈重排。

## 三、导出与交接

报告完成后的“下一步”才会显示两个导出动作：

- `输出文字版歌单`：只在聊天中返回按当前最终顺序排列的可复制文本，不创建文本文件，也不声称一键写入 DJ 软件。
- `导出到w4dj`：在当前 Agent 确实有文件写入能力且用户明确触发后，创建 UTF-8 `.w4dj` 文件。它只交接歌单名、顺序、完整官方歌名、艺人和可选字符串 `netease_track_id`；不包含本地音频、路径、下载任务或内部元数据。

`.w4dj` 使用当前唯一合同：根字段为 `format`、`format_version`、`export_id`、`playlist`、`tracks`，其中 `format_version` 固定写为整数 `2`，只用于兼容 W4DJ，不是用户需要选择的版本；`playlist` 只有 `name`；每首曲目只有 `position`、`title`、`artist_display` 和可选的 `netease_track_id`。完整操作请查看[《一键导入 Set 教程》](https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.md)。本 Skill 不下载音乐、不生成本地音频，不负责后续本地导入动作。

兼容的基线、原因和未来移除条件记录在[《W4DJ v2 兼容备忘录》](docs/w4dj-v2-compatibility-memo.md)。

## 四、通用 Agent 兼容性

本仓库只提供一个标准 Skill 包。支持完整 Agent Skills 导入的客户端可以按自身目录规则加载同一份文件；搜索、打开网页、写文件和发送中间消息等能力由客户端映射，Skill 不要求固定工具名、SDK、命令或模型。

当前兼容状态采用三级标记：正式支持、原生兼容待实测、待确认。由于本项目还没有为每个组合完成完整冷启动回放，以下客户端暂标为“原生兼容，待实测”，不把文档兼容性写成实机验收：

| 客户端 | 状态 |
|---|---|
| Codex | 原生兼容，待实测 |
| Claude Code、Gemini CLI | 原生兼容，待实测 |
| VS Code / GitHub Copilot、Cursor、Windsurf、OpenCode | 原生兼容，待实测 |
| WorkBuddy / CodeBuddy、Qoder / QoderWork、Trae / TraeWork | 原生兼容，待实测 |
| 豆包工作（Doubao Work） | 待确认 |
| 其他声称支持“技能”的客户端 | 待确认 |

支持 26 个固定语言包，清单见 [`references/locales/manifest.json`](references/locales/manifest.json)。运行时按阶段只加载当前语言包的触发、问卷、检索上下文、报告或后续动作资源；问卷、报告、状态、动作和平台表达均不临场翻译整套模板。不支持的语言才回退英语。多语言正式声明还需要母语审校与计划中的 312 次模型冷启动回放。

目录发现规则以各客户端公开的 Agent Skills 文档为准，例如 [Claude Code](https://code.claude.com/docs/en/skills)、[Gemini CLI](https://geminicli.com/docs/cli/using-agent-skills/)、[VS Code Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)、[Cursor](https://prod.cursor.com/docs/skills)、[Windsurf](https://docs.windsurf.com/windsurf/cascade/skills)、[OpenCode](https://opencode.ai/docs/skills/)、[WorkBuddy/CodeBuddy](https://www.workbuddy.cn/docs/cli/skills)、[Qoder/QoderWork](https://docs.qoder.com/qoder/skills) 和 [Trae](https://docs.trae.cn/ide_skills)。这些链接只说明标准导入边界，不替代本项目的实机回放验收。

## 五、能力不足时的边界

缺少网页搜索或打开具体页面的能力时，不输出伪验证歌单；缺少文件写入能力时，不声称已经生成 `.w4dj`。平台缺曲、版本不匹配、调性冲突或候选不足时减少数量并说明原因，不用错误链接、错误歌名、未核验曲目或重复录音凑数。

本项目采用 Apache License 2.0，详见 [LICENSE](LICENSE)。
