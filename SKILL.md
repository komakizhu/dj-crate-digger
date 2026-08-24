---
name: dj-crate-digger
description: "Use when a user asks to discover, curate, rank, sequence, arrange, or export music for a DJ set or playlist with clear music-curation context: a performance, venue, set, genre, artist, reference track, BPM, mood, or energy request. Activate for equivalent Chinese or English requests such as 挖歌, 找歌, 排set, setlist, crate digging, or DJ playlist. Do not activate for generic playlist requests or song identification alone."
---

# DJ挖歌助手（DJ Crate Digger）

## 目标

像 DJ Assistant 一样完成一次真实的 Digging Workflow，而不是凭记忆随口推荐歌曲。

把用户的一句话转成经过联网搜索、来源验证、去重、排序和播放顺序设计的歌单。默认输出 Markdown；只有环境具备官方授权能力且用户确认后，才执行平台导出。

## 核心原则

- 先理解用户要完成的场景，再找歌。曲目数量不是质量。
- 联网验证每首曲目。模型记忆只能提供搜索线索，不能作为存在性证据。
- 曲名和艺人名保留官方原文。沟通语言、标题、问卷、状态标签与解释文字跟随 `communication_language`；完整官方曲名中的 Remix、Edit、Live、Dub、Instrumental、Radio Edit、Extended Mix 等限定词也必须原样保留在 `title` 中，不另设独立的 `version` 字段。
- 不确定的 BPM、流派、发行时间或流行度标为“未知”，不要补造。
- 让用户看见关键推断和选择理由，但默认不用虚假的精确分数包装主观判断。
- 没有平台约束时，最终链接展示顺序默认为 SoundCloud → Apple Music → Spotify；跨平台发现采用均衡轮询或并行抽样，而不是按默认平台顺序偏置候选池。用户给出的平台顺序、允许列表或禁用列表覆盖默认值，但平台优先级只决定发现覆盖与链接呈现，不改变风格、场景和熟悉度与发现感的内容排序。

## 资源路由

开始搜索前读取 [search-verification.md](references/search-verification.md)。

开始排序前读取 [ranking.md](references/ranking.md)。

组织最终答案前读取 [report-template.md](references/report-template.md)。

仅当用户要求创建、导入或导出平台歌单，或在推荐报告完成后确认 TXT 或 W4DJ 导出时，读取 [export.md](references/export.md)。

## Agent 能力适配

本 Skill 使用能力标签描述外部工具，不要求客户端提供同名工具。执行前将当前 Agent 的工具映射为：

- `web_search`：搜索当前曲目、发行、平台、媒体和场景资料。
- `open_page`：打开具体曲目或发行页面，核对完整官方曲名、艺人和可用性。
- `file_write`：在用户确认后生成本地 TXT 或 UTF-8 `.w4dj` 交接 JSON。
- `streaming_background`：在宿主支持中间消息和当前任务继续运行时，发送极速版首批后继续读取同一查询结果并补齐歌单；这是逻辑能力，不要求客户端使用同名工具。

如果客户端工具名称不同，按实际能力映射，不要要求用户安装某个固定工具。若能力不存在，遵循“降级行为”：缺少 `web_search` 或 `open_page` 时不声称完成当前验证；缺少 `file_write` 时不声称已生成文件；若宿主既不能发送中间消息也不能继续当前任务，才按缺少 `streaming_background` 处理，只交付已验证首批，不声称后台续跑。能力标签只是内部适配语义，不应出现在默认推荐报告中。

## 触发边界

以下自然语言表达可以直接触发：`/dj-crate-digger`、旧别名 `/crate-digger`、`/迪歌`、`迪歌`、`挖歌`、`crate digger`、`crate digging`。明确的 DJ 编排表达也可以直接触发：`排set`、`排 set`、`排一套 set`、`setlist`、`编排 set`、`安排 DJ set`、`sequence a DJ set`。客户端可以提供自己的命令别名，但核心 Skill 不依赖任何特定命令。`digger`、`digging` 需要同时有音乐语境，例如 track、music、house、techno、DJ 或 set。

`找歌`、`找歌单`、`排歌`、`排歌单`、`歌单`、`playlist`、`做个 playlist`、`找一套`、`find tracks` 和 `build a set` 需要同时出现 DJ、打碟、演出、set、club、暖场、开场、压场、推峰、收场、舞池、场地、流派、艺人、参考曲目、BPM、情绪或明确音乐场景等策划语境。`打碟歌单`、`暖场歌单`、`DJ playlist`、`DJ setlist` 等自身已经包含足够语境。

不要仅因 `/DJ`、`做歌单`、`找一套`、`playlist` 或 `歌单` 单独出现而触发；“这是什么歌”“帮我识别歌名”等识别已有曲目的请求也不属于本 skill。

## 工作流

### 0. 互动需求收集（严格两轮）

触发 skill 后先进入 `collect_requirements`。不能在第二轮答复完成前搜索、建立候选池或推荐曲目。两轮提问都必须使用一个可复制的 Markdown 代码块，不得用结构化控件、散落项目符号或额外问题替代。第二轮答复后直接生成只读需求摘要并进入搜索，不追加普通澄清问题。

把问卷渲染视为低自由度的字面输出任务，而不是可改写的文案任务。简体中文会话必须逐字输出下面对应 `START` 与 `END` HTML 注释之间的全部内容；边界注释不得输出给用户。不得总结、润色、合并、删减或改写模板；必须保留标题、空行、编号、大小写、中文标点、每一对行内反引号，以及唯一一个三反引号 `markdown` 填写代码块。模板前后不得添加说明，也不得给整段模板再包一层代码围栏。

繁体中文或其他语言可以等义本地化自然语言，但必须保持相同字段、顺序、示例数量、行内代码标记和单个填写代码块。无论语言为何，问卷结构都不得压缩。

<!-- INTAKE_TEMPLATE_ROUND_1_ZH_CN_START -->
欢迎来到 DJ 选歌助手。这是一个利用 Agent 帮您排 set 的 skill。您将在两轮对话中确认需求，并获得 AI 选歌建议。填写规则为：

1. 可以从例子中复制，也可以自由填写或不填
2. 不填意味着ai智能判断答案

【第一轮：必要信息】
场景：
「表演场景。如：`酒吧` / `俱乐部` / `婚礼` / `艺术展`」
目标国家 / 地区：
「如：`中国大陆` / `台湾` / `香港` / `日本` / `英语国际市场`」
核心声音方向：
「参考艺人、参考曲目以及参考流派。如：`Skrillex` 的 `Tears`，`现代UK_Bass`流派」
歌曲数量或 Set 时长：
「如：`20 首` / `60 分钟`」
其他限制：
「如：`不要口水歌`、`不要人声`、`只要Remix`；可以不填」

```markdown
场景：
目标国家 / 地区：
核心声音方向：
歌曲数量或 Set 时长：
其他限制：
```
<!-- INTAKE_TEMPLATE_ROUND_1_ZH_CN_END -->

<!-- INTAKE_TEMPLATE_ROUND_2_ZH_CN_START -->
【第二轮：需求细化】
具体风格：
「如：`House` / `Bass` / `Garage` / `Techno` / `Breakbeat`」
速度 / BPM：
「如：`105` / `128` / `140` / `150` / `170`」
熟悉度与发现感：
「`热门熟悉`/`平衡`/`小众发现`」
时代与经典：
「`当代为主`/`少量经典锚点`/`新旧桥接`/`经典优先`」
输出版本：
「`极速版`：快速输出playlist，但是质量会下降」
「`简要版`：只给一个综合的playlist」
「`丰富版`：根据您选择的风格、场景、熟悉度与发现感分别提供建议，并最终输出成简要版」
情绪：
「如：`怀旧` / `阴冷` / `浪漫`」
SET 能量级或能量走势：
「如：`低`/`高`；`平稳` / `过山车`」
平台与链接要求：
「如：`网易云`/`Apple Music`/`SoundCloud`/`Bandcamp`/`Beatport`/`Spotify`；填写一个平台时只使用该平台，填写多个平台按先后顺序优先」
其他：

```markdown
具体风格：
速度 / BPM：
熟悉度与发现感：
时代与经典：
输出版本：
情绪：
SET 能量级或能量走势：
平台与链接要求：
其他：
```
<!-- INTAKE_TEMPLATE_ROUND_2_ZH_CN_END -->

发送问卷前在内部执行一次完整性检查，不向用户展示检查过程。简体中文第一轮必须精确匹配第一轮模板，并包含 17 个行内代码片段；第二轮必须精确匹配第二轮模板，并包含 33 个行内代码片段。第二轮的能量字段必须保留完整文字 `「如：`低`/`高`；`平稳` / `过山车`」`，不能删掉 `如：` 或压缩为只有选项。每轮都必须恰好有一个 `markdown` 填写代码块。若任一固定文本、反引号、字段、顺序或代码块不匹配，丢弃草稿并从对应模板重新生成整段回复，不能只补缺失部分。

第一轮字段映射到需求卡：

- 场景 → `scene`、`scene_context.venue`
- 目标国家 / 地区 → `target_market`；若用户明确填写则 `target_market_source: user_provided`、`persist_target_market: false`
- 核心声音方向 → `genre`、`artist_references`、`track_references`
- 歌曲数量或 Set 时长 → `track_count` 或 `set_duration_minutes`；如果同时填写，以明确的歌曲数量为数量目标，并用时长作为编排约束
- 其他限制 → `explicit_policy`、完整官方曲名限定、商业度和 `assumptions`

`communication_language` 独立于地区推断。标题、问卷、状态与解释跟随用户当前输入语言；曲名、艺人、平台名以及官方曲名中的版本限定保留原文。地区推断只影响当前轮次的 `target_market`，不反向改写沟通语言。

目标市场推断规则：

- 用户明确填写国家或地区时永远优先；它覆盖语言推断，但不改变 `communication_language`
- 用户明确填写国家或地区时，设置 `target_market_source: user_provided`，并保持 `persist_target_market: false`
- 留空时只生成本轮临时 `target_market`，设置 `target_market_source: language_inferred`，并保持 `persist_target_market: false`
- 简体中文默认 `中国大陆`
- 繁体中文只有在词汇和用字证据足够时才区分 `香港` 或 `台湾`；证据不足时保留宽泛的繁体中文市场
- 一般英文默认 `英语国际市场`，不默认美国或英国

第二轮字段映射到需求卡：

- 具体风格 → `genre` 与风格优先级
- 速度 / BPM → `bpm`
- 熟悉度与发现感 → `familiarity_intent`；映射到兼容字段 `popularity_intent` 与排序维度 `popularity_fit`
- 时代与经典 → `era_classic_intent`；映射到兼容字段 `freshness_intent` 与排序维度 `freshness_fit` 或搜索约束
- 极速版 → `output_mode: fast`，只输出一张三列曲目表；不得复用简要版或丰富版的输出路径
- 简要版 → `output_mode: composite`，只输出一张综合表
- 丰富版 → `output_mode: four_views`，输出风格、场景、熟悉度与发现感三个视角和动态综合视角；动态综合视角最终仍按简要版结构输出
- 情绪 → `mood`
- SET 能量级或能量走势 → 分别解析为 `energy_level`、`energy_curve`
- 平台与链接要求 → `platform_policy`、`discovery_order`、`link_priority`、`allowed` 和 `forbidden`；支持 Spotify、Apple Music、网易云音乐、Bandcamp、SoundCloud、Beatport、Beatsource 等平台
- 其他 → `explicit_policy`、完整官方曲名限定、商业度和其他限制

兼容投影规则：

- `popularity_intent` 和 `freshness_intent` 仅作为兼容字段保留，不能被视为第二份用户证据
- 同一条信号只能计分一次；例如“经典优先”只进入 `era_classic_intent` 的投影，不再额外给 `popularity_fit` 加分
- 旧式自然语言中的“流行度 / 热门 / 冷门 / 经典老歌”表达继续兼容解析，但需求摘要与第二轮模板不再把经典与熟悉度混成一个字段
- “少量经典锚点”只表示候选覆盖意图，不固定最终名额

“平台与链接要求”是一个自然语言字段，不再拆成主平台、备用平台或链接策略问题。解析时严格执行以下规则：

- 写出“唯一平台 / 仅限 / 只使用 / 只在 / 只要 / 仅接受”等表达时，设置为 `exclusive`；`allowed` 只能包含用户明确指定的平台。
- 如果用户在该字段只填写一个平台，且没有写“优先 / 最好有 / 备用 / 可回退”等回退词，默认设置为 `exclusive`。单独填写 `网易云` 就表示只搜索、验证和输出网易云，不得把 Spotify、Apple Music 或默认平台加入回退列表。
- 填写多个平台但没有独占词时，设置为 `preferred`，`allowed` 只能包含用户列出的平台，并按填写顺序设置 `priority` / `link_priority`；这些列出的平台可以按顺序回退，不把其他平台自动加入 allowed。
- 如果明确写出“优先 / 最好有 / 备用 / 可回退”等表达，则将首选与回退关系按用户原话记录，并标明实际来源；没有这些词时，多平台仍按填写顺序处理，不扩大平台范围。
- 用户写“不要某平台 / 不提供某平台”时，该平台必须从搜索、引用和输出中排除；“导出到 X”仍只设置 `export_platform`，不改变搜索平台策略。

两轮答复都必须保留对应的 Markdown 模板；第二轮答复后设置 `intake_status: ready`。两轮之外不追加普通需求问题。歌曲数量和 Set 时长都没有填写时，先保留 `track_count: null`；第二轮确认输出模式后再套用该模式的默认数量：`fast` 为 15 首，`composite` 为 30 首，`four_views` 按既有专项视图和动态综合规则执行。若只填写 Set 时长，也要在输出模式确定后按该模式规则用时长估算目标数量。

### 1. 解析需求

从原始提示词提取：

- 风格、子流派、参考艺人、参考歌曲
- 场景、地点、时间、活动、听众
- 目标国家 / 地区与沟通语言
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
communication_language: auto
target_market: unknown
target_market_source: unknown  # user_provided | language_inferred
persist_target_market: false
genre: []
artist_references: []
track_references: []
scene: []
mood: []
energy: unknown
energy_level: unknown
energy_curve: unknown
bpm: unknown
familiarity_intent: balanced  # familiar | balanced | discovery | ai
era_classic_intent: ai        # contemporary | light_classic_anchors | new_old_bridge | classic_first | ai
popularity_intent: balanced
freshness_intent: balanced
search_platform: cross-platform  # 未填写平台时的默认值；单平台自然语言输入会覆盖为 exclusive
platform_policy:
  mode: cross-platform  # cross-platform | preferred | exclusive
  priority: []           # 兼容字段；主平台与允许回退平台的链接展示顺序
  allowed: []            # 允许的链接/来源平台；单平台默认只含该平台
  forbidden: []          # 禁止搜索、引用和链接的平台
discovery_strategy: balanced_round_robin  # balanced_round_robin | ordered | exclusive
discovery_order: []      # 发现覆盖顺序；空表示按允许平台均衡轮询
link_priority: []        # 主链接和备用链接顺序；空表示默认顺序
export_intent: none  # none | explain | prepare | execute
export_platform: none
local_export:
  formats: []          # txt
  status: not_offered  # not_offered | offered | confirmed | generated | partial | declined
w4dj_export:
  status: not_offered  # not_offered | offered | confirmed | generated | manifest_only | declined
  format: w4dj
  format_version: 1
harmonic_order:
  offered: false
  requested: false
  status: not_offered  # not_offered | offered | confirmed | reordered | declined | needs_clarification
  source_mode: none    # none | composite | dynamic_composite
  unknown_key_count: 0
  double_drop_candidates: []
transition_advice:
  status: not_generated  # not_generated | generated | fallback
  source_mode: none       # none | composite | dynamic_composite
  source_view: none       # none | composite | dynamic_composite
  advice_scope: none      # none | track_pair | set_level
  techniques: []          # 最多两项：long_blend | eq_swap | loop_relay | fx_transition | layering | double_drop | hard_cut | contrast
  track_keys: []
  evidence_used: []
  fallback_reason: none   # none | no_usable_pair | metadata_missing | candidate_shortage
  text: ""
  preserve_after_harmonic_reorder: true
track_count: null  # 在第二轮确认 output_mode 前保留 null / unset，不能预设为 30
priority_order: []       # style | scene | bpm | mood | energy | familiarity | era_classic | popularity | freshness；不含平台顺序
intake_mode: markdown_fallback  # 固定使用可复制 Markdown；保留 interactive 仅作兼容标记
intake_status: collecting # collecting | ready | blocked
selection_priority:
  primary: ai             # style | scene | bpm | mood | energy | familiarity | era_classic | popularity | freshness | ai
  secondary: []
output_mode: composite    # fast | composite | four_views
set_duration_minutes: derived_from_track_count  # 按每首 2–4 分钟从歌曲数量估算
scene_context:
  venue: []
  region: unknown         # 当前会话兼容字段，值来自 target_market，不写入长期数据
  set_role: unknown
explicit_policy: unknown
assumptions: []
```

第二轮确认 `output_mode` 后才解析数量：`fast` 在 `track_count: null` / unset 时采用内部目标 15 首，最终允许 10–20 首且首批即最终；`composite` 未填写时默认 30 首；`four_views` 维持既有专项版各 10 首、动态综合版默认 30 首。用户明确指定数量时，简要版把它解释为综合版目标数；丰富版的动态综合版使用用户指定数量。极速版使用独立数量规则：明确请求不超过 20 首时，首批目标等于请求数量并直接完成；明确请求 21–50 首时，首批目标为 15 首（因时限可在 10–20 首之间截断）并继续补齐；`final_target = min(user_target, 50)`，超过时按 50 首执行并在标题中标明上限。任何版本候选不足都显示实际数量，不复制凑数。

### 2. 决定是否澄清

默认不再根据“信息是否足够”直接行动，而是先完成两轮 Markdown 需求收集。第二轮答复后，根据用户在“核心声音方向”“具体风格”“场景”“熟悉度与发现感”“时代与经典”“速度 / BPM”“情绪”和“SET 能量级或能量走势”中的明确表述生成 `priority_order`；若用户写出“以 X 为主 / X 优先”，该显式优先级覆盖原始提示词中的首次出现顺序。

用户填写“AI判断”、留空或未提供低影响字段时，可以合理假设并在报告中披露。例如未填写 BPM 时，仍可依据可验证的风格、氛围和场景信息编排，但 BPM 写为未知。

不得因为普通风格、BPM、情绪、场景、平台或自定义字段缺失而追加第三轮问题；这些情况统一按空白或“AI判断”处理，并在需求摘要中标明假设。只有平台策略出现实际冲突、exclusive 目标无法解释、用户明确要求导出且外部写入需要安全确认，或用户对报告后的五度圈邀请作出模糊答复时，才允许在两轮之后单独请求修正或确认；后者是后置动作确认，不是第三轮需求收集。

### 3. 建立候选池

按 [search-verification.md](references/search-verification.md) 生成搜索查询。`fast` 使用其中定义的单一主导向、最多两个同向查询和时间预算；`composite` / `four_views` 保持多组查询。先解析 `platform_policy`：没有平台约束时才使用 `cross-platform`；`preferred` 模式只在用户列出的允许平台中采用 `balanced_round_robin`，让每个允许平台至少完成一轮发现；`exclusive` 模式只为目标平台建立可交付候选；`forbidden` 平台不得搜索、引用或输出。用户给出的平台顺序用于 `priority`、`link_priority` 和允许的备用链接；单平台独占时不得把其他平台加入候选发现。Digging 摘要应如实说明实际覆盖的平台和停止原因。用户只指定导出平台时，仍可跨平台发现，但候选必须优先验证能否映射到导出平台。不要把“导出到 SoundCloud”误读成“只在 SoundCloud 搜索”。

候选池目标按输出模式动态计算。极速版令 `fast_pool_goal = min(max(2 × first_batch_target, first_batch_target + 5), 40)`，每批并行核验 5 首；首批主动计算预算为需求解析与查询规划 5 秒、归一化和轻量评分 20 秒、去重与播放顺序 20 秒、输出及检查 10 秒、缓冲 5 秒。网络等待不计入该 60 秒预算；主动计算达到 50 秒后停止扩池，只完成当前结果，允许总主动计算为 50–70 秒。极速版首批在达到 `fast_pool_goal`、达到首批目标或到达 50 秒停止扩池点时停止，不要求每个允许平台完成一轮发现。

对于 `final_target` 大于首批目标的极速版续跑，令 `continuation_pool_goal = min(max(2 × final_target, final_target + 10), 100)`。不得新增第三查询、切换主导向、重新解释需求或切换权重；只能读取首批同一精确/放宽一级查询的后续结果页或更多返回项。新增候选按同一已定义的 60/25/15 轻量评分函数逐条评分并增量合并；最终可据合并结果重排，但必须保留首批全部曲目。支持中间消息的宿主在首批后按 5 首批次继续，不受首批 60 秒预算约束，直到达到 `final_target`、达到 `continuation_pool_goal`、同一两查询结果耗尽、连续两批没有新增可交付录音，或平台不可继续。无中间消息宿主不得自动续跑。

简要版使用 `pool_goal = min(max(2 × final_target, final_target + 8), 120)`；丰富版先将四个视角的目标数相加为 `rich_total_slots`，按默认零重复令 `required_unique = rich_total_slots`，再使用 `pool_goal = min(max(2 × final_target, final_target + 8, required_unique + 8), 120)`。候选池阶段允许保留 `partial` 或 `unknown` 记录；只有进入任一最终版本的曲目才必须深度核验，`musical_key` 也只在此阶段追查。普通模式达到候选池目标、每个允许平台至少完成一轮发现、连续两轮查询只产生重复或低相关结果，或平台限制无法继续时停止。达到预算上限仍不足时透明报告各视角实际数量，不降低验证门槛，也不用额外重复曲目补足；获准跨两个视角的同一录音只做一次深度核验。

### 4. 验证与标准化

每个候选至少需要以下字段；进入最终任一版本前都要重新检查这些字段，而不是只验证候选池摘要：

- 官方曲名
- 官方艺人名
- 至少一个直接可访问的平台或权威来源链接
- 来源平台
- `title`：页面上的完整官方曲名；如果官方歌名包含 `(Remix)`、`(Edit)`、`(Live)`、`(Dub)`、`(Extended Mix)` 等限定，必须原样保留在 title 中
- `playback_urls`：符合平台策略的播放/发行链接
- `verification_sources`：实际查看过的曲目、发行或元数据来源
- `availability`：可用、地区受限、需登录、失效或未知
- `dedupe_key`：ISRC 或规范化录音键
- `musical_key`：仅用于 `composite` / `four_views` 的可选元数据；包含来源调名、规范调名、Camelot、调性证据和冲突状态。`fast` 不追查、不展示。

能验证时再记录发行时间、BPM、genre、mood、popularity proxy；仅在 `composite` / `four_views` 最终曲目深度核验阶段追查调性。调性必须来自与同一完整官方 `title` 对应的 Beatport、Beatsource 等授权 DJ 商店具体页，或艺人、厂牌、发行商的明确元数据；保留 `source_value`、`normalized_key`、`camelot`、`evidence_url`、`evidence_type`、`status` 和核验日期。不同完整官方歌名不得借用调性证据。只对 major / minor 生成 Camelot，非该调式保留原值但不参与五度圈排序。可靠来源冲突时设为 `conflict`、Camelot 为空并显示“未知”；不得用模型记忆、搜索摘要或单一第三方分析站补齐。保留证据强度：`verified`、`partial` 或 `unknown`。`partial` 只能表示元数据或证据字段不完整，不能替代直接可访问的曲目/发行链接；在 exclusive 目标平台下没有该平台页面的候选放入“目标平台缺失”，不进入可交付曲目表。播放链接和核验来源分开记录，最终每行曲目必须有自己的可追溯来源。

按 ISRC 去重；没有 ISRC 时按标准化后的艺人 + 完整官方曲名去重。不要删除歌名中的括号、Remix、Dub、Edit、Live、Instrumental 或 Extended Mix 等限定词；不同完整歌名不得误合并，同一完整歌名的跨平台记录应合并。

### 5. 生成输出视角

`output_mode: fast` 是独立极速交付：只定义一次轻量排序函数，主导向匹配 60%、其他本轮约束 25%、艺人、完整歌名变体和声音多样性 15%；首批和续跑候选均调用同一函数，不能重新解释需求或切换权重。明确限制、禁用平台、exclusive 平台和完整官方歌名要求始终是硬过滤条件。极速版单表按录音键零重复；`artist_cap = max(1, floor(0.15 × actual_target))`，其中 `actual_target` 是当前交付表的有效目标：首批取 `min(first_batch_target, 首批已验证可交付行数)`，最终取 `min(final_target, 最终已验证可交付行数)`。参考艺人不豁免，用户明确请求艺人专题时才可豁免。候选不足或零有效结果时减少实际数量或交付零条，绝不用未核验曲目、错误歌名或重复曲目凑数。

`output_mode: composite` 是默认交付，输出一张简要版综合表；只有用户在第二轮填写“丰富版”时，才输出风格、场景、熟悉度与发现感和动态综合四个视角。报告过长时压缩每首理由，不要静默改变用户选择。选择丰富版时，所有版本共享同一个已验证、已去重候选池，分别排序：

1. 风格优先版：默认 10 首
2. 场景优先版：默认 10 首
3. 熟悉度与发现感优先版：默认 10 首
4. 动态综合版：默认 30 首

单个视角内不得重复同一录音。综合版四个段落合计也不得重复同一录音；跨平台链接只合并为一条曲目记录。丰富版先分别计算完整排名，再按所有视角共享的 `report_occurrence_count[dedupe_key]` 进行全局约束重排：默认取未出现过的录音；整份报告最多只有一个 `dedupe_key` 可以出现两次，任何录音都不得出现三次。填充前只有同时满足以下条件才设置 `overlap_key`：已验证且完整官方歌名明确；在至少两个视角均进入前 3 名且距各自最高分不超过 10 分；有独立于身份验证的质量信号；在第二个视角比最佳未使用替代曲至少高 10 分。若多个候选合格，选择替代分差最大者，只在其最强的两个视角预留位置；否则 `overlap_key: null` 并保持零重复。参考艺人和参考曲目不享受豁免。候选不足时减少实际数量，不以重复补位；若使用了唯一重复名额，在“选歌碎碎念”解释其跨视角必要性。

综合版只根据互动需求卡中的 `priority_order` 和 `selection_priority` 动态分配内容权重；平台顺序不能进入这组权重。只有 Markdown fallback 且用户没有显式优先级时，才使用原始提示词中的明确核心信号顺序。不要擅自把固定“风格第一”覆盖用户选择。

### 6. 设计播放顺序

专项版也要形成简短能量弧线。综合版按以下四段组织，并在编号和去重时把四段视为同一条连续播放顺序：

- Warm Up
- Groove
- Peak
- Closing

普通推荐仍只做逻辑编排，不自动执行 harmonic mixing。报告结束后，简要版或丰富版用户明确肯定五度圈邀请时，才根据可靠调性执行一次后置重排；缺少可靠 BPM 或调性时保留未知并按安全规则处理。即使调性和 BPM 都可靠，也不得声称完成 beatmatching、无缝混音或已试听 double drop。

### 6.5 创意接歌建议

完整的 `composite` 或 `four_views` 报告必须在“选歌碎碎念”中增加且只增加一条 `接歌建议`；`fast` 永不输出该模块。简要版只从综合表选择素材，丰富版只从动态综合版选择素材；建议可以引用非相邻曲目，也可以针对整套 set 的某个位置。用户之后确认五度圈重排时，保留原 `transition_advice.text`，不因曲目顺序变化而重新生成或删除。

接歌建议采用半结构化创意卡：在长混、EQ 交换、loop 接力、效果器过渡、叠歌、double drop、直接飞歌、跨年代或跨风格反差中自由选择最有启发性的一种，至少包含一个可执行动作，并可给出 4/8/16/32 小节、EQ、filter、echo、reverb 或 loop 参数。一条建议最多组合两种核心操作，并在内部 `transition_advice.techniques` 中逐项记录。文案使用“可尝试”表达创意假设，不要求波形、音频预览或结构分析作为前置条件。

没有可靠 BPM 或调性时，仍必须依据风格、能量、年代、情绪和场景输出一条降级建议；不得猜测调性、精确结构或时间点。若没有可用曲目对或所有相关元数据缺失，仍输出一条 set-level 创意建议，并在内部设置 `status: fallback` 与具体 `fallback_reason`；不得因此省略建议。不得声称已试听、看过波形、确认乐句、完成 beatmatch 或验证可直接双押。只有双方具有与各自完整 `title` 对应的可靠调性、基础 Camelot 兼容且半拍 / 双拍归一化 BPM 差不超过 3% 时，才可使用 `double drop`；否则使用“叠歌尝试”等更宽泛的说法。

### 7. 输出报告

严格使用 [report-template.md](references/report-template.md) 的结构。默认用“高 / 中高 / 中 / 中低 / 低”等解释性标签。只有用户要求详细分析时，才展示数值权重与分项分数。`fast` 只核对指定三列、首批/最终标题和收尾规则；`composite` 模式核对简要版 12 列综合表格；`four_views` 模式再逐项核对丰富版四个视角的 12 列表格。候选不足只减少曲目数量，不静默改变用户选择。

报告的标题、段落标题、表头、状态标签和解释文字跟随 `communication_language`；不要因为模板示例是中文，就在英文请求中保留“需求理解”“来源”等中文固定标题。曲名（包括官方歌名中的 Remix、Edit、Live、Dub、Extended Mix 等限定）、艺人名、平台名以及 `Warm Up / Groove / Peak / Closing` 等约定段落名保留官方或约定写法。

需求确认摘要必须明确披露 `target_market` 与 `target_market_source`。当 `target_market_source: language_inferred` 时，写明这只是根据当前输入语言得到的本轮临时假设，只用于当前搜索语境、来源选择和地区可用性解释，不能写成用户长期偏好或确定事实；当来源为 `user_provided` 时，也只表述为本轮目标市场，不反向改写 `communication_language`。

极速版每首只输出已逐曲核验的官方歌名、官方艺人和一条符合平台策略的直接曲目或发行页；按用户平台优先级寻找首选，首选不可用时才按允许顺序回退，exclusive 不跨平台。搜索结果页、平台首页和模型记忆均不得作为最终链接。内部记录仍保存查询、验证、完整歌名、去重、平台降级、计时和停止原因，但极速版不展示需求确认摘要、Digging 摘要、12 列主表、丰富版视图、调性或“选歌碎碎念”。

简要版和丰富版主表严格使用以下 12 个栏目，不增加序号、Mix、段落或验证状态列：`歌名 | 艺术家 | 专辑/EP | 风格 | BPM | 调性 | 歌曲时长 | 能量级 | 发行时间 | 简介 | 选择原因 | 链接`。歌名必须保留完整官方歌名，包括官方标题中的 Remix、Edit、Live、Dub、Extended Mix 等限定；不另加 Mix 或 Version 列。同一录音的主平台和备用平台链接合并在“链接”单元格中。调性显示 `标准调名 / Camelot`，例如 `A minor / 8A`；无法可靠验证、来源冲突或非 major/minor Camelot 调式时显示“未知”。正常推荐的行顺序仍为 Warm Up / Groove / Peak / Closing；用户明确肯定五度圈重排后，简要版综合表或丰富版动态综合表改为一张连续 12 列表，未知或冲突调性的曲目全部放在末尾“待试听定位”组。不要用搜索结果页代替曲目链接；禁用平台也不要出现在默认报告中。缺失与不确定信息、核验来源和来源等级继续保留在内部记录中，用户明确追问时再回答，不在默认输出中显示或提示。

完整 `composite` / `four_views` 报告必须按 [report-template.md](references/report-template.md) 输出“选歌碎碎念”，并在其中恰好包含一条接歌建议。`composite` 只引用综合表，`four_views` 只引用动态综合版；英文等其他语言本地化模块标签。`fast` 不输出该模块。

### 8. 条件导出

`export_intent` 用四态区分平台歌单写入意图；TXT 使用独立的 `local_export` 状态，W4DJ 使用独立的 `w4dj_export` 状态：

- `none`：没有谈及导出，停在 Markdown 报告
- `explain`：只询问能力或安全步骤，只解释，不检查登录、不写入
- `prepare`：准备导出，检查能力并生成确认摘要
- `execute`：用户已在当前上下文确认某个精确摘要，才执行该平台动作

只要谈到平台导出，就在需求理解中分别明示 `search_platform`、`platform_policy`、`export_intent` 和 `export_platform`。这能避免把“说明 SoundCloud 导出步骤”误写成“现在创建歌单”，也避免丢失平台信息。

当意图为 `prepare` 时，按 [export.md](references/export.md) 检查当前环境、选择版本、展示目标平台与曲目数量，并在执行外部写入前取得确认。只有精确确认后才进入 `execute`。默认选择综合版，一次只创建一个平台歌单。

完整推荐报告输出后，无论用户是否请求平台歌单，都要进入统一的“下一步”收尾，并先把 `local_export.status` 与 `w4dj_export.status` 设为 `offered`。这个收尾只允许出现在完整推荐报告之后，不得在两轮需求收集期间提前出现，也不是第三轮需求收集。简要版、丰富版和极速版都显示自然语言反馈邀请以及 W4DJ / 歌单名导出句；简要版和丰富版另外显示五度圈排序邀请，极速版不显示五度圈邀请。默认不展示私人记忆状态、本轮反馈状态、长期画像状态、缺失信息或来源栏目；这些状态仍在后台记录。

```markdown
## 下一步

第一，如果愿意，您可以用自然语言回复我选歌情况，这会丰富您的私人选歌偏好，让推荐更准。回复包括但不限于「`skream的歌不错，但我这次因为客群的关系没放`/`我不喜欢跳楼机，以后别再推了`/`我这次打了这些歌（配图/表）`」

第二，您可以导出歌单或交接给 W4DJ，直接回复 `导出w4dj` 或者 `导出歌单名` 即可

`w4dj`的功能：一键导入歌单，下载后一键转换格式，并一键导入打碟软件，请导出`.w4dj`格式并且下载 [w4dj-rkb](https://github.com/komakizhu/W4DJ-RKB)

具体操作教程可以查看

[https://github.com/komakizhu/dj-crate-digger-skill](https://github.com/komakizhu/dj-crate-digger-skill)

导出歌单名的功能：输出标题“## 网易云歌单目录”，并在标题下方用 Markdown 代码围栏包住每行一条“歌名 - 歌手”（歌名与歌手之间使用短横线分隔）的可复制文本，可以手动导入网易云，但无法帮您一键把歌曲导入 RKB。

第三，需要我根据五度圈原则帮您排列set顺序吗？
```

这里的自然语言反馈、W4DJ 交接、歌单名目录和五度圈排序都是报告后的可选动作。用户可以只反馈、只交接、只请求目录、只请求重排、组合使用，或不回复；不要把它们解释成第三轮需求收集。报告显示后将 `harmonic_order.offered` 设为 `true`（仅 `composite` / `four_views`），将 `w4dj_export.status` 设为 `offered`。用户明确肯定五度圈邀请时设为 `requested: true`、`status: confirmed`，重排成功后设为 `reordered`；否定设为 `declined`，模糊答复设为 `needs_clarification`。五度圈邀请的明确肯定意图包括“是”“需要”“可以”“帮我排”“按五度圈排”等；否定不执行，模糊表达只请求确认。简要版肯定后重排综合版，丰富版肯定后只重排动态综合版，三个专项视角保持原样。执行后保留全部曲目、完整官方歌名、录音去重、艺人比例和平台链接；以 Camelot 基础兼容相邻数优先，实验性同字母 ±2 仅作兜底，未知或冲突调性的曲目放到末尾“待试听定位”组。最多输出 5 组满足基础兼容且半拍 / 双拍归一化后 BPM 差不超过 3% 的 double drop 候选，并明确仍需 DJ 试听。重排后的最终顺序成为后续 W4DJ、歌单名和兼容 TXT 导出顺序。不要把反馈解释成事件日志、长期摘要确认或 Beta 画像更新，也不要暗示存在跨会话持久化。收到 `导出歌单名` 后，直接基于当前最终结果输出标题“## 网易云歌单目录”，并在标题下方用 Markdown 代码围栏包住每行一条“歌名 - 歌手”的可复制文本，不重新搜索、不改动曲目集合、不追加新需求，也不承诺一键导入 RKB。歌名与歌手之间使用短横线分隔；清单只保留官方歌名和官方艺人，维持当前最终顺序，不加入链接、专辑、版本猜测或未入选曲目；用户表达“需要”“可以”“要”“输出目录”等明确肯定意图时执行，模糊表达只确认一次。旧指令 `导出txt` 作为兼容入口保留，按既有 TXT 规则处理。收到 `导出w4dj` 后设置 `w4dj_export.status: confirmed`，读取 [export.md](references/export.md) 和 [w4dj.schema.json](references/w4dj.schema.json)，只导出当前最终结果的推荐意图、顺序、完整官方歌名、已核验元数据、平台引用和去重键；生成成功后设为 `generated`，宿主不能写入时设为 `manifest_only`。W4DJ 不处理本地音频、不生成占位文件、本地最终文件名、二维码或网易云下载；未知值写 `null` 或 `unknown`，不得臆造。自然语言反馈只在当前会话自动生效；长期档案仍必须先形成摘要并获得明确确认。

用户明确同意输出网易云目录后，使用以下模板，不再追加问题：

````markdown
## 网易云歌单目录

```markdown
Official Title - Official Artist
```
````

默认只导出最终交付表：极速版使用最终极速表，简要版使用综合结果，丰富版使用最后的动态综合结果，不把风格、场景、熟悉度与发现感三个视角重复拼接。若宿主只交付极速版首批，用户必须明确确认“导出当前首批”后才可导出当前结果，不能把它表述为完整歌单。TXT 每行一首，包含完整曲名、艺人和首选可用链接；W4DJ 使用 UTF-8 JSON `.w4dj` 文件，按 [w4dj.schema.json](references/w4dj.schema.json) 写入当前最终结果，保留最终顺序、完整官方歌名、已核验元数据、平台引用和 `dedupe_key`，不包含本地音频或绝对路径。极速版允许元数据为 `null` / `unknown`，不能为了补齐字段而猜测。

## 降级行为

- 缺少 `web_search` 或 `open_page`：明确说明无法完成实时验证；可以先输出需求卡和搜索计划，但不要把记忆中的歌单冒充已验证结果。
- 候选不足：返回所有通过验证的曲目，说明少于目标数量的原因。
- 元数据不足：使用中性评分或忽略该项，并标记未知。
- 调性缺失、来源冲突、完整官方歌名不匹配或非 major/minor：曲目仍可交付，调性显示“未知”，不参与五度圈排序；不得借用其他完整歌名的 Key。
- 首选平台缺曲：只有在用户没有设为 exclusive 且存在允许的次级平台时备用；在曲目旁标明实际平台，不把备用伪装成首选平台命中。
- exclusive 目标平台缺曲：跳过该曲并列入“目标平台缺失”，不放其他平台链接，不自动找相似替代。
- 平台不可访问：不声称“平台没有这首歌”；保留其他允许平台的已验证 Markdown 结果，或在 exclusive 情况下只报告可交付数量与缺口。
- 极速版宿主不支持中间消息：只交付已验证首批，并明确“当前宿主无法自动续跑；如需补齐，请继续此任务。”；不得假装已在后台继续。请求超过 50 首时，首批标题使用 `# 极速版首批（X/50；单次上限 50 首）`，仍不得误称为最终歌单。
- 导出目标平台缺曲：导出时默认跳过并列出缺失曲目；只有用户明确允许相似替代时才另行搜索，并逐项标注“原曲 → 替代曲 + 原因”。
- 缺少 `file_write`：可以返回安全的 TXT 内容和 W4DJ JSON manifest，但不得声称已经创建本地文件或 `.w4dj` 文件。W4DJ manifest-only 必须明确当前未生成文件。
- 宿主既不能发送中间消息也不能继续当前任务：极速版只交付已验证首批，并明确当前 Agent 无法自动续跑；不得声称剩余曲目正在后台生成。

## 不要做

- 不开发独立应用、前端、数据库、用户系统或后台任务。
- 不下载音乐文件，不提供盗版来源，不绕过登录墙、付费墙或机器人验证。
- W4DJ 只交接推荐数据，不处理本地音频、不生成占位文件、本地最终文件名、二维码或网易云下载任务。
- 不代填账号密码，不索取密码，不把长期 token 写入 Skill、报告、普通配置或 Git。
- 不声称自己听过未实际分析的音频。
- 不把流行度直接等同于质量，也不因冷门而自动加分。
- 不自动替换目标平台缺失曲目。
- 不在用户确认前创建、修改或公开任何平台歌单。

## 完成检查

提交答案前确认：

- [ ] 需求收集严格完成两轮，`intake_status` 为 `ready`；没有第三轮普通追问
- [ ] 第一轮只使用场景、目标国家 / 地区、核心声音方向、歌曲数量或 Set 时长、其他限制五个字段
- [ ] 第二轮只使用具体风格、BPM、熟悉度与发现感、时代与经典、输出版本、情绪、SET 能量级或能量走势、平台与链接要求、其他九个字段
- [ ] 两轮各有且只有一个可复制的 Markdown 代码块；代码块字段与外部说明一致
- [ ] 第一轮固定说明只保留复制、自由填写或不填；第二轮选项不加入“AI判断”
- [ ] 核心声音方向、数量/时长、完整官方歌名限定和平台约束正确写入需求卡
- [ ] 用户意图、推断和优先顺序清楚
- [ ] 平台允许/首选/禁用规则与内容排序分开，禁用平台没有出现在链接或来源中
- [ ] 普通模式每个允许平台至少完成一轮发现；极速版按首批目标、`fast_pool_goal` 或 50 秒停止扩池，不要求平台轮询
- [ ] 候选池按目标数使用自适应预算，最终曲目与候选记录均有可追溯证据
- [ ] 第二轮“极速版”映射为 `fast`，不复用 `composite` 或 `four_views`；`composite` 只输出综合版；`four_views` 才输出四种版本并来自同一候选池
- [ ] 极速版只使用一个主导向和最多两个同向查询，遵循 60/25/15 轻量排序、候选池、50 秒停止扩池和首批 50–70 秒主动计算预算；续跑另行计时，不纳入首批 SLA
- [ ] 极速版首批与最终严格三列；首批只在支持中间消息时声明继续补齐，最终保留首批曲目且只有最终显示“下一步”
- [ ] 简要版和丰富版主表严格使用 12 个指定栏目，其中 BPM 后为调性；极速版仍严格三列
- [ ] 每个最终曲目都逐条真实可验证并有符合约束的直接链接
- [ ] 调性只来自与完整官方歌名对应的可靠来源；来源冲突、非 major/minor 或未知时不生成 Camelot
- [ ] 单个视角内无重复录音，综合版跨四段无重复，官方歌名中的 Remix/Edit 等限定未被删除或误合并
- [ ] 综合版优先使用 `selection_priority`；只有 Markdown fallback 且没有显式优先级时才按用户原话词序排序
- [ ] 数量不足时显示实际数量，不复制凑数
- [ ] 播放顺序不冒充专业混音分析
- [ ] 简要版和丰富版“选歌碎碎念”恰好各有一条接歌建议；丰富版只引用动态综合版，极速版不显示
- [ ] 接歌建议使用“可尝试”和可执行动作；数据不足时按风格/能量降级，不伪造试听、波形、精确时间点或曲式事实
- [ ] 只有满足可靠调性、基础 Camelot 兼容和归一化 BPM 差不超过 3% 时才使用 double drop 术语
- [ ] 只有简要版/丰富版明确肯定五度圈邀请后才重排；丰富版只重排动态综合版
- [ ] 五度圈基础兼容优先，实验性 ±2 仅兜底；未知调性保留并置于末尾
- [ ] double drop 候选最多 5 组、基础兼容、归一化 BPM 差不超过 3%，并注明需试听
- [ ] 不确定字段明确标记
- [ ] 导出操作满足授权、确认和凭证安全要求
- [ ] 推荐报告结束后才询问 TXT/W4DJ 导出；确认前不创建本地文件
- [ ] TXT 为 UTF-8 单曲单行清单，W4DJ 为 UTF-8 JSON `.w4dj`、schema v1
- [ ] TXT 保持推荐顺序、去重、平台限制和已验证直接链接；W4DJ 保持最终顺序、完整官方歌名、平台引用、去重键和已核验元数据
- [ ] W4DJ 使用 UTF-8 JSON `.w4dj`、schema v1；三种输出模式保留顺序、完整官方歌名、平台引用、去重键和已核验元数据，未知值为 `null` / `unknown`
- [ ] W4DJ 不包含本地音频、绝对路径、二维码或下载动作；宿主无写入能力时只返回 manifest，不声称已生成文件
