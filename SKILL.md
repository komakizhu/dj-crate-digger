---
name: dj-crate-digger
description: 当用户明确要求为 DJ 演出、打碟歌单、暖场/开场/压场/收场 set，或特定场景、流派、艺人、曲目参考进行挖歌、digging、发现、策划、排序、编排或导出时使用；响应 /dj-crate-digger、旧版 /crate-digger、/迪歌、迪歌、挖歌、找歌、排set、排 set、排歌、排歌单、setlist、编排 set、安排 DJ set、crate digger、crate digging，以及带 DJ、演出、set、场景、流派、艺人或参考曲目的 playlist/歌单请求。不要仅因“做歌单”“找一套”“playlist”或“/DJ”触发，也不要把识别歌曲请求当成挖歌。 Use when a user asks to dig, discover, curate, rank, sequence, arrange, or export music for a DJ set or playlist with clear music-curation context, including /dj-crate-digger, the legacy /crate-digger alias, /迪歌, “迪歌”, “挖歌”, “找歌”, “排set”, “排 set”, “排歌”, “排歌单”, “setlist”, “编排 set”, “安排 DJ set”, “crate digger”, “crate digging”, and equivalent Chinese or English requests.
---

# DJ挖歌助手（DJ Crate Digger）

## 目标

像 DJ Assistant 一样完成一次真实的 Digging Workflow，而不是凭记忆随口推荐歌曲。

把用户的一句话转成经过联网搜索、来源验证、去重、排序和播放顺序设计的歌单。默认输出 Markdown；只有环境具备官方授权能力且用户确认后，才执行平台导出。

## 核心原则

- 先理解用户要完成的场景，再找歌。曲目数量不是质量。
- 联网验证每首曲目。模型记忆只能提供搜索线索，不能作为存在性证据。
- 曲名和艺人名保留官方原文。报告语言跟随用户输入语言。
- 不确定的 BPM、流派、发行时间或流行度标为“未知”，不要补造。
- 让用户看见关键推断和选择理由，但默认不用虚假的精确分数包装主观判断。
- 没有平台约束时，最终链接展示顺序默认为 SoundCloud → Apple Music → Spotify；跨平台发现采用均衡轮询或并行抽样，而不是按默认平台顺序偏置候选池。用户给出的平台顺序、允许列表或禁用列表覆盖默认值，但平台优先级只决定发现覆盖与链接呈现，不改变风格、场景和流行度的内容排序。

## 资源路由

开始搜索前读取 [search-verification.md](references/search-verification.md)。

开始排序前读取 [ranking.md](references/ranking.md)。

组织最终答案前读取 [report-template.md](references/report-template.md)。

仅当用户要求创建、导入或导出平台歌单时，读取 [export.md](references/export.md)。

## 触发边界

以下表达可以直接触发：`/dj-crate-digger`、`/crate-digger`、`/迪歌`、`迪歌`、`挖歌`、`crate digger`、`crate digging`。明确的 DJ 编排表达也可以直接触发：`排set`、`排 set`、`排一套 set`、`setlist`、`编排 set`、`安排 DJ set`、`sequence a DJ set`。`digger`、`digging` 需要同时有音乐语境，例如 track、music、house、techno、DJ 或 set。

`找歌`、`找歌单`、`排歌`、`排歌单`、`歌单`、`playlist`、`做个 playlist`、`找一套`、`find tracks` 和 `build a set` 需要同时出现 DJ、打碟、演出、set、club、暖场、开场、压场、推峰、收场、舞池、场地、流派、艺人、参考曲目、BPM、情绪或明确音乐场景等策划语境。`打碟歌单`、`暖场歌单`、`DJ playlist`、`DJ setlist` 等自身已经包含足够语境。

不要仅因 `/DJ`、`做歌单`、`找一套`、`playlist` 或 `歌单` 单独出现而触发；“这是什么歌”“帮我识别歌名”等识别已有曲目的请求也不属于本 skill。

## 工作流

### 0. 互动需求收集（严格两轮）

触发 skill 后先进入 collect_requirements，不能在第二轮答复完成前搜索、建立候选池或推荐曲目。两轮提问的唯一展示形式固定为可复制的 fenced Markdown 代码块：第一轮一个代码块，第二轮一个代码块。两轮答复后直接生成只读摘要并进入搜索，不追加普通澄清问题。

填写规则只在第一轮代码块的开头出现一次；后续字段不重复解释 AI、空白或自定义语义。需要补充的艺人、曲目、地区或限制直接写在对应字段后。

第一轮只确认选歌主题和两个副主题，三个问题使用同一组五个主题选项：

```markdown
【第一轮：选歌主题】
填写说明：可填写“AI判断”；空白代表“无 / 不需要”。
选歌主题：风格 / 场景 / BPM / 情绪 / 能量
选歌副主题 1（最多 2 个）：风格 / 场景 / BPM / 情绪 / 能量
选歌副主题 2（最多 2 个）：风格 / 场景 / BPM / 情绪 / 能量
```

第二轮一次完成主题细化、地区、数量、版本、平台和其他限制；不再重复第一轮的填写说明。第二轮固定使用以下选项，按第一轮填写说明处理空白字段：

```markdown
【第二轮：主题细化与全部需求】
风格：House / Deep House / Organic House / Disco House / Tech House / Progressive House / Garage / Techno / Left-field
场景：酒吧 / 俱乐部 / 婚礼
BPM：100–115 慢拍松弛 / 118–126 中速律动 / 128 四四抖腿 / 132–136 推进 / 140 操栏杆必备
情绪：温暖 / 迷幻 / 紧张
能量级与走势：平稳 / 逐渐升高 / 先熟后怪 / ……
熟悉度与流行度：热门 / 平衡 / 冷门发现
参考艺人 / 参考曲目：
Set 用途：暖场 / 推峰 / 收场
地区：
歌曲数量：10 首（约 20–40 分钟） / 20 首（约 40–80 分钟） / 30 首（约 60–120 分钟） / 自定义
输出版本：综合版（1 张表） / 四个版本（风格、场景、流行度、动态综合）
主平台：Spotify / Apple Music / 网易云音乐 / Bandcamp / SoundCloud / AI 自动选择
备用平台：Spotify / Apple Music / 网易云音乐 / Bandcamp / SoundCloud / AI 自动选择
其他：可直接填写 Explicit、Clean、Original、Remix、Dub、Edit、Live、Radio Edit、Extended Mix、商业度或其他限制
```

主平台和备用平台只决定链接优先级：主平台链接优先，备用平台作为第二顺位；不再询问链接策略。用户在自然语言中明确说“只接受 / 仅要”某个平台时，仍将 platform_policy 设为 exclusive。空白备用平台表示不设置备用链接，不自动改变用户明确的 exclusive 规则。

第二轮答复后立即写入需求卡并设置 intake_status: ready。第一轮和第二轮都必须保留为 Markdown 代码块，不得改成普通文本、散落项目符号或只显示 UI 控件；两轮之外不再要求用户重新填写需求。

### 1. 解析需求

从原始提示词提取：

- 风格、子流派、参考艺人、参考歌曲
- 场景、地点、时间、活动、听众
- 情绪、能量、BPM、年代、新鲜度
- 对热门、冷门、熟悉度或发现感的要求
- 搜索平台偏好、导出目标平台、曲目数量、歌单用途
- 各信号在原始提示词中首次出现的顺序

先把中文 DJ 口语按语义角色归一化，再开始搜索，不要只按字面翻译：

- “暖场 / 开场 / 收场 / 压场 / 推峰 / 左场 / 地下 / 凌晨”主要描述场景、能量或播放段落。
- “大家熟 / 有反应 / 土 / 俗 / 不烂大街 / 商业 / 冷门”描述熟悉度与发现感的取舍，不等于音乐质量，也不自动排除或奖励某首歌。
- “像某艺人 / 某曲的声音”“把某人当采样语汇”是参考关系；除非用户明确要求专题，不要把参考对象扩写成整套只含该艺人的歌。
- “以 X 为主 / X 优先 / 先……再……”是显式排序信号；它可以覆盖同类信号的首次出现顺序。

平台也要单独解析，不能和内容优先级混在一起：

- “优先 / 最好有”表示首选平台，允许在用户允许的次级平台备用，并标明实际来源。
- “只要 / 仅接受”表示目标平台是 exclusive；该平台没有曲目时列入缺失，不用其他平台或相似曲目暗中替代。
- “不要 X / 不提供 X”表示 forbidden；不要搜索、引用或在来源汇总中出现该平台。
- “导出到 X”只设置 `export_platform`，不自动把 X 变成唯一搜索平台。

将理解结果保留为内部需求卡：

```yaml
genre: []
artist_references: []
track_references: []
scene: []
mood: []
energy: unknown
energy_level: unknown
energy_curve: unknown
bpm: unknown
popularity_intent: balanced
freshness_intent: balanced
search_platform: cross-platform
platform_policy:
  mode: cross-platform  # cross-platform | preferred | exclusive
  priority: []           # 兼容字段；主平台与备用平台的链接展示顺序
  allowed: []            # 允许的链接/来源平台；空表示按 mode 处理
  forbidden: []          # 禁止搜索、引用和链接的平台
discovery_strategy: balanced_round_robin  # balanced_round_robin | ordered | exclusive
discovery_order: []      # 发现覆盖顺序；空表示按允许平台均衡轮询
link_priority: []        # 主链接和备用链接顺序；空表示默认顺序
export_intent: none  # none | explain | prepare | execute
export_platform: none
track_count: 30
priority_order: []       # style | scene | bpm | mood | energy | popularity | familiarity；不含平台顺序
intake_mode: markdown_fallback  # 两轮提问固定使用可复制 Markdown；保留 interactive 仅作兼容标记
intake_status: collecting # collecting | ready | blocked
selection_priority:
  primary: ai             # style | scene | bpm | mood | energy | popularity | familiarity | freshness | ai
  secondary: []
output_mode: composite    # composite | four_views
set_duration_minutes: derived_from_track_count  # 按每首 2–4 分钟从歌曲数量估算
scene_context:
  venue: []
  region: unknown
  set_role: unknown
explicit_policy: unknown
assumptions: []
```

用户明确指定数量时，默认把它解释为综合版目标数；只有用户在互动需求收集中选择“四个版本”时，三个专项版才各取 10 首，综合版使用用户指定数量。未指定数量时，综合版默认 30 首。任何版本候选不足都显示实际数量，不复制凑数。

### 2. 决定是否澄清

默认不再根据“信息是否足够”直接行动，而是先完成两轮互动需求收集。第二轮答复后，将 `selection_priority.primary` 和 `selection_priority.secondary` 映射为 `priority_order`；该显式选择覆盖原始提示词中的首次出现顺序。

用户选择“AI 判断”“不限”或未提供低影响字段时，可以合理假设并在报告中披露。例如未填写 BPM 时，仍可依据可验证的风格、氛围和场景信息编排，但 BPM 写为未知。

不得因为普通风格、BPM、情绪、场景、平台或自定义字段缺失而追加第三轮问题；这些情况统一按用户选择的“不限 / AI 判断”处理，并在需求摘要中标明假设。只有平台策略出现实际冲突、exclusive 目标无法解释，或用户明确要求导出且外部写入需要安全确认时，才允许在两轮之后单独请求修正或确认。

### 3. 建立候选池

按 [search-verification.md](references/search-verification.md) 生成多组搜索查询。先解析 `platform_policy`：`cross-platform` 和 `preferred` 模式默认采用 `balanced_round_robin`，让每个允许平台至少完成一轮发现；`exclusive` 模式只为目标平台建立可交付候选；`forbidden` 平台不得搜索、引用或输出。用户给出的平台顺序优先用于 `link_priority` 和备用链接，不自动成为候选发现的唯一顺序。Digging 摘要应如实说明实际覆盖的平台和停止原因。用户只指定导出平台时，仍可跨平台发现，但候选必须优先验证能否映射到导出平台。不要把“导出到 SoundCloud”误读成“只在 SoundCloud 搜索”。

候选池目标按综合版目标数动态计算：`pool_goal = min(max(2 × final_target, final_target + 8), 120)`。候选池阶段允许保留 `partial` 或 `unknown` 记录；只有进入任一最终版本的曲目才必须深度核验。达到候选池目标、连续两轮查询只产生重复或低相关结果，或平台限制无法继续时停止。达到预算上限仍不足时透明报告实际数量，不降低验证门槛；同一录音出现在多个版本时只做一次深度核验。

### 4. 验证与标准化

每个候选至少需要以下字段；进入最终任一版本前都要重新检查这些字段，而不是只验证候选池摘要：

- 官方曲名
- 官方艺人名
- 至少一个直接可访问的平台或权威来源链接
- 来源平台
- `version_label`：页面上的完整官方版本名
- `playback_urls`：符合平台策略的播放/发行链接
- `verification_sources`：实际查看过的曲目、发行或元数据来源
- `availability`：可用、地区受限、需登录、失效或未知
- `dedupe_key`：ISRC 或规范化录音键

能验证时再记录 mix/version、发行时间、BPM、genre、mood、popularity proxy。保留证据强度：`verified`、`partial` 或 `unknown`。`partial` 只能表示元数据或证据字段不完整，不能替代直接可访问的曲目/发行链接；在 exclusive 目标平台下没有该平台页面的候选放入“目标平台缺失”，不进入可交付曲目表。播放链接和核验来源分开记录，最终每行曲目必须有自己的可追溯来源。

按 ISRC 去重；没有 ISRC 时按标准化后的艺人 + 曲名 + mix/version 去重。Original、Remix、Edit、Live 等不同版本不要误合并。

### 5. 生成输出视角

`output_mode: composite` 是默认交付，输出一张综合版；只有用户在互动需求收集中选择“四个版本”时，才输出风格、场景、流行度和动态综合四个视角。报告过长时压缩每首理由，不要静默改变用户选择。选择四版本时，所有版本共享同一个已验证、已去重候选池，分别排序：

1. 风格优先版：默认 10 首
2. 场景优先版：默认 10 首
3. 流行度优先版：默认 10 首
4. 动态综合版：默认 30 首

版本内部不得重复。综合版四个段落合计也不得重复同一录音；跨平台链接只合并为一条曲目记录。版本之间可以重复；重复入选时，在综合说明中指出它跨视角成立的原因。

综合版只根据互动需求卡中的 `priority_order` 和 `selection_priority` 动态分配内容权重；平台顺序不能进入这组权重。只有 Markdown fallback 且用户没有显式优先级时，才使用原始提示词中的明确核心信号顺序。不要擅自把固定“风格第一”覆盖用户选择。

### 6. 设计播放顺序

专项版也要形成简短能量弧线。综合版按以下四段组织，并在编号和去重时把四段视为同一条连续播放顺序：

- Warm Up
- Groove
- Peak
- Closing

V1 只做逻辑编排，不声称完成 BPM beatmatching、调性匹配或谐波混音。缺少可靠 BPM 时，根据可验证的风格、氛围、密度与场景信息排序。

### 7. 输出报告

严格使用 [report-template.md](references/report-template.md) 的结构。默认用“高 / 中高 / 中 / 中低 / 低”等解释性标签。只有用户要求详细分析时，才展示数值权重与分项分数。`composite` 模式核对综合版表格；`four_views` 模式再逐项核对四个版本标题和表格。候选不足只减少曲目数量，不静默改变用户选择。

报告的标题、段落标题、表头、状态标签和解释文字跟随用户输入语言；不要因为模板示例是中文，就在英文请求中保留“需求理解”“来源”等中文固定标题。曲名、艺人名、mix/version、平台名以及 `Warm Up / Groove / Peak / Closing` 等约定段落名保留官方或约定写法。

主表严格使用以下栏目，不增加序号、Mix、段落或验证状态列：`歌名 | 艺术家 | 专辑/EP | 风格 | BPM | 歌曲时长 | 能量级 | 发行时间 | 简介 | 选择原因 | 链接`。歌名保留官方版本名；同一录音的主平台和备用平台链接合并在“链接”单元格中。综合版的行顺序就是推荐播放顺序，必要时用 `Warm Up / Groove / Peak / Closing` 作为表格前的小标题。无法验证的 BPM、时长、专辑、能量级或发行时间写“未知”。不要用搜索结果页代替曲目链接；禁用平台也不要出现在来源汇总中。

### 8. 条件导出

`export_intent` 用四态区分用户意图：

- `none`：没有谈及导出，停在 Markdown 报告
- `explain`：只询问能力或安全步骤，只解释，不检查登录、不写入
- `prepare`：准备导出，检查能力并生成确认摘要
- `execute`：用户已在当前上下文确认某个精确摘要，才执行该动作

只要谈到平台导出，就在需求理解中分别明示 `search_platform`、`platform_policy`、`export_intent` 和 `export_platform`。这能避免把“说明 SoundCloud 导出步骤”误写成“现在创建歌单”，也避免丢失平台信息。

当意图为 `prepare` 时，按 [export.md](references/export.md) 检查当前环境、选择版本、展示目标平台与曲目数量，并在执行外部写入前取得确认。只有精确确认后才进入 `execute`。默认选择综合版，一次只创建一个平台歌单。

## 降级行为

- 无联网工具：明确说明无法完成实时验证；可以先输出需求卡和搜索计划，但不要把记忆中的歌单冒充已验证结果。
- 候选不足：返回所有通过验证的曲目，说明少于目标数量的原因。
- 元数据不足：使用中性评分或忽略该项，并标记未知。
- 首选平台缺曲：只有在用户没有设为 exclusive 且存在允许的次级平台时备用；在曲目旁标明实际平台，不把备用伪装成首选平台命中。
- exclusive 目标平台缺曲：跳过该曲并列入“目标平台缺失”，不放其他平台链接，不自动找相似替代。
- 平台不可访问：不声称“平台没有这首歌”；保留其他允许平台的已验证 Markdown 结果，或在 exclusive 情况下只报告可交付数量与缺口。
- 导出目标平台缺曲：导出时默认跳过并列出缺失曲目；只有用户明确允许相似替代时才另行搜索，并逐项标注“原曲 → 替代曲 + 原因”。

## 不要做

- 不开发独立应用、前端、数据库、用户系统或后台任务。
- 不下载音乐文件，不提供盗版来源，不绕过登录墙、付费墙或机器人验证。
- 不代填账号密码，不索取密码，不把长期 token 写入 Skill、报告、普通配置或 Git。
- 不声称自己听过未实际分析的音频。
- 不把流行度直接等同于质量，也不因冷门而自动加分。
- 不自动替换目标平台缺失曲目。
- 不在用户确认前创建、修改或公开任何平台歌单。

## 完成检查

提交答案前确认：

- [ ] 需求收集严格完成两轮，`intake_status` 为 `ready`；没有第三轮普通追问
- [ ] 第一轮的主主题、副主题 1、副主题 2 都展示完整且相同的主题选项集
- [ ] 第二轮对风格、场景、BPM、情绪、能量级、能量走势和熟悉度/流行度分别给出选项
- [ ] 每一个可见问题都有非空选项；没有“字段名：”式空白问题
- [ ] 主导向、次导向、数量、版本和平台来自用户的互动选择
- [ ] 用户意图、推断和优先顺序清楚
- [ ] 平台允许/首选/禁用规则与内容排序分开，禁用平台没有出现在链接或来源中
- [ ] 每个允许平台至少完成一轮发现，发现覆盖顺序与链接优先级没有混淆
- [ ] 候选池按目标数使用自适应预算，最终曲目与候选记录均有可追溯证据
- [ ] `composite` 只输出综合版；`four_views` 才输出四种版本并来自同一候选池
- [ ] 主表严格使用 11 个指定栏目，不增加额外列
- [ ] 每个最终曲目都逐条真实可验证并有符合约束的直接链接
- [ ] 版本内部无重复，综合版跨四段无重复，mix/version 未误合并
- [ ] 综合版权重反映提示词顺序
- [ ] 数量不足时显示实际数量，不复制凑数
- [ ] 播放顺序不冒充专业混音分析
- [ ] 不确定字段明确标记
- [ ] 导出操作满足授权、确认和凭证安全要求
