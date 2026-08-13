# Markdown 报告模板

报告语言跟随 `communication_language` / 当前沟通语言；曲名、艺人、mix/version 和平台名保留官方原文。极速版的中文与英文标题、表头和状态句使用下列精确合同；其它语言按这些槽位本地化。

使用以下结构。简要版是默认交付；用户在第二轮填写“丰富版”时才输出风格、场景、熟悉度与发现感和动态综合四个视角，并最终提供一份综合结果。用户填写“简要版”时只输出一张综合表，但仍保留验证链接和假设。

用户填写“极速版”时，改用以下独立结构，不输出本文件其余报告部分：

中文首批：

```markdown
# 极速版首批（X/N）

| 歌名 | 歌手 | 链接 |
|---|---|---|
| Official Title | Official Artist | [平台](direct-url) |

已完成第一批，正在继续补齐。
```

英文首批：

```markdown
# Fast Mode First Batch (X/N)

| Track | Artist | Link |
|---|---|---|
| Official Title | Official Artist | [Platform](direct-url) |

First batch complete. Continuing to fill the playlist.
```

只有支持中间消息且用户目标大于 20 首时才输出上述首批和继续文字。最终结果使用以下结构；最终必须保留首批全部曲目，但可重新排序：

中文最终：

```markdown
# 极速版（X/N）

| 歌名 | 歌手 | 链接 |
|---|---|---|
| Official Title | Official Artist | [平台](direct-url) |

## 下一步

第一，如果愿意，您可以用自然语言回复我选歌情况，这会丰富您的私人选歌偏好，让推荐更准。回复包括但不限于「`skream的歌不错，但我这次因为客群的关系没放`/`我不喜欢跳楼机，以后别再推了`/`我这次打了这些歌（配图/表）`」

第二，您可以导出歌单，直接回复`导出txt`或者`导出m3u8`即可
```

英文最终：

```markdown
# Fast Mode (X/N)

| Track | Artist | Link |
|---|---|---|
| Official Title | Official Artist | [Platform](direct-url) |

## Next steps

First, if you want, reply in natural language with how the selections worked for you. This helps refine your private selection preferences. For example: “I like Skream, but I did not play it for this crowd” / “I do not like Jumping Machine; do not recommend it again” / “These are the tracks I played (image/list).”

Second, reply `export txt` or `export m3u8` to export the playlist.
```

超过 50 首时，中文最终标题固定为 `# 极速版（X/50；单次上限 50 首）`；英文最终标题固定为 `# Fast Mode (X/50; single-request limit: 50 tracks)`。如果宿主不支持中间消息，中文首批标题固定为 `# 极速版首批（X/50；单次上限 50 首）`，英文首批标题固定为 `# Fast Mode First Batch (X/50; single-request limit: 50 tracks)`；这两者仍是首批，不得写成最终交付。

极速版严格三列，只输出官方歌名、官方艺人和一个逐曲核验后的直接页。它省略需求确认摘要、Digging 摘要、11 列主表、丰富版和“选歌碎碎念”；“下一步”只允许出现在最终结果。若宿主不支持中间消息且目标大于 20 首，仍使用对应语言的首批标题，中文状态句固定为“当前宿主无法自动续跑；如需补齐，请继续此任务。”，英文状态句固定为“Current host cannot continue automatically. Continue this task to fill the remaining tracks.”。超过 50 首的请求按 50 首执行并使用对应的带上限首批或最终标题。

```markdown
# [Playlist Theme]

## 需求确认摘要

- 沟通语言：...
- 场景：...
- 目标国家 / 地区：...
- 地区来源：用户填写 / 根据语言临时推断 / 未确认 / unknown
- 核心声音方向：...
- 歌曲数量或 Set 时长：... 首 / ... 分钟
- 具体风格：...
- 速度 / BPM：... / 未验证
- 熟悉度与发现感：...
- 时代与经典：...
- 输出版本：极速版 / 简要版 / 丰富版
- 情绪：...
- SET 能量级或能量走势：...
- 平台与链接要求：...
- 平台策略：允许 ...；禁用 ...；exclusive / preferred / cross-platform
- 导出意图：未请求 / 仅解释 / 准备 / 已确认执行
- 导出目标：未指定 / [用户指定平台]
- 数量口径：目标 ... 首；候选不足时实际 ... 首
- 其他：...
- 关键假设：...

## Digging 摘要

[2–4 句说明搜索方向、候选池规模、去重后数量和明显限制。]

## 综合版（实际数量 / 目标数量）

| 歌名 | 艺术家 | 专辑/EP | 风格 | BPM | 歌曲时长 | 能量级 | 发行时间 | 简介 | 选择原因 | 链接 |
|---|---|---|---|---:|---:|---|---|---|---|---|
| Official Title | Official Artist | Official Release | Deep House | 未知 | 未知 | 中高 | YYYY-MM-DD / 未知 | ... | ... | [主平台](direct-url) |

综合版按推荐顺序排列。需要展示能量弧线时，可以将同一结构的表格分为以下小节，不增加额外表格列：

### Warm Up

[同样表格]

### Groove

[同样表格]

### Peak

[同样表格]

### Closing

[同样表格]

## 丰富版（仅用户填写“丰富版”时输出）

### 风格优先版（实际数量 / 目标数量）

| 歌名 | 艺术家 | 专辑/EP | 风格 | BPM | 歌曲时长 | 能量级 | 发行时间 | 简介 | 选择原因 | 链接 |
|---|---|---|---|---:|---:|---|---|---|---|---|
| Official Title | Official Artist | Official Release | ... | 未知 | 未知 | ... | YYYY-MM-DD / 未知 | ... | ... | [主平台](direct-url) |

### 场景优先版（实际数量 / 目标数量）

| 歌名 | 艺术家 | 专辑/EP | 风格 | BPM | 歌曲时长 | 能量级 | 发行时间 | 简介 | 选择原因 | 链接 |
|---|---|---|---|---:|---:|---|---|---|---|---|
| Official Title | Official Artist | Official Release | ... | 未知 | 未知 | ... | YYYY-MM-DD / 未知 | ... | ... | [主平台](direct-url) |

### 熟悉度与发现感优先版（实际数量 / 目标数量）

| 歌名 | 艺术家 | 专辑/EP | 风格 | BPM | 歌曲时长 | 能量级 | 发行时间 | 简介 | 选择原因 | 链接 |
|---|---|---|---|---:|---:|---|---|---|---|---|
| Official Title | Official Artist | Official Release | ... | 未知 | 未知 | ... | YYYY-MM-DD / 未知 | ... | ... | [主平台](direct-url) |

### 动态综合版（实际数量 / 目标数量）

按 Warm Up → Groove → Peak → Closing 顺序使用同样的 11 列曲目表。

## 选歌碎碎念

- Track — Artist：说明关键选择判断；若它是整份丰富版唯一重复出现的高质量曲目，明确解释为什么值得跨两个视角保留。

## 下一步

第一，如果愿意，您可以用自然语言回复我选歌情况，这会丰富您的私人选歌偏好，让推荐更准。回复包括但不限于「`skream的歌不错，但我这次因为客群的关系没放`/`我不喜欢跳楼机，以后别再推了`/`我这次打了这些歌（配图/表）`」

第二，您可以导出歌单，直接回复`导出txt`或者`导出m3u8`即可
```

“缺失与不确定信息”、核验来源、记忆状态和本轮反馈仍须写入内部记录，但默认不作为报告栏目展示；用户明确追问时，从对应内部记录回答，不主动提示这些记录。

## 曲目链接规则

- 极速版的“链接 / Link”单元格只能包含一条符合平台策略、逐曲核验的直接页；不得并列备用链接。
- 链接文字使用允许的平台名，指向具体曲目页；preferred 模式按用户平台顺序排列。
- 同一曲目有多个允许的平台链接时，`composite` / `four_views` 可以并列显示，但只占一个曲目位置；这条多链接规则不适用于极速版。
- exclusive 模式只显示目标平台直接链接；其他平台只能在内部验证，不放进用户报告。
- 不使用搜索结果页、首页或无法确认内容的短链接。
- 核验来源保存在内部来源记录中，默认不展示独立来源栏目；用户明确追问时，再从该记录回答对应事实。

## 长度控制

默认简要版只输出一张 11 列曲目表。丰富版下保持每首理由在一句以内，专项版不重复写完整元数据；跨视角共性放到“选歌碎碎念”统一解释。不要向主表添加序号、Mix、段落或验证状态列。

丰富版默认整份报告零重复；确有充分质量证据时，最多允许一首录音出现两次，任何录音不得出现三次，参考艺人和参考曲目也不豁免。如果候选少于目标数量，在标题中显示实际数量，不复制曲目凑数。
