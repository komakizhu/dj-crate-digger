# 搜索、验证与去重

## 搜索策略

把需求拆成多个查询，不依赖一次宽泛搜索。至少覆盖：

1. 核心风格 + 参考艺人或参考曲目
2. 场景 + mood + energy
3. 平台 + 风格 + 年代、时代与经典线索或 freshness
4. 相邻子流派或同厂牌线索
5. 用户明确的热门、冷门或熟悉度要求
6. 目标国家 / 地区 + 平台、编辑、厂牌或本地场景线索

用户未指定平台时，默认链接展示顺序为 SoundCloud → Apple Music → Spotify，但发现阶段采用均衡轮询或并行抽样，并用 Bandcamp、Beatport、Discogs、MusicBrainz、艺人官网和厂牌官网补充验证。用户指定平台时，目标平台中的可用性优先于跨平台覆盖。

推荐类信息可能变化，使用联网工具获取当前结果。优先并行搜索不同查询，但最终逐条核验候选。

平台策略要落实到实际检索，不只是写在报告里：`cross-platform` 和 `preferred` 模式下，对每个允许平台至少完成一轮发现，再按轮次继续补充候选；`exclusive` 模式只建立目标平台的可交付候选。用户给出的平台顺序用于主链接和回退链接，不能让首选平台提前满足停止条件后跳过其他允许平台。候选在任一平台已有可访问、版本吻合的直接页时，可以将该页设为主链接；其他来源作为补充证据，不得复制同一录音占用多个位置。

`target_market` 只影响当前轮次的搜索上下文、编辑/平台来源选择、熟悉度解释和地区可用性判断，不改变 `communication_language`，也不写成长期偏好。用户明确填写的国家或地区永远优先；`target_market_source: language_inferred` 只能作为宽泛检索线索，用来扩展平台、厂牌、媒体或本地场景关键词，不能在报告里写成用户已确认事实。

## 极速版搜索策略

`output_mode: fast` 不沿用普通模式的多通道、多轮发现。先且只选择一个 `fast_recall_channel`：`anchor_style` 用于参考曲目、参考艺人或具体风格；`scene_context` 用于没有更具体锚点时的明确场景、目标市场、情绪或能量；`familiarity_era` 只在前两类信号不足时使用熟悉度与发现感或时代与经典。BPM 只能作为风格的限定词，不能独立成为召回通道。

留空或信号冲突时，按参考曲目 → 参考艺人 → 具体风格 → 明确场景 → 模糊情绪的具体度选择一个通道；不得把其它通道并入本次极速召回。每次最多执行两个同向查询变体：一个精确查询和一个仅放宽一级的回退查询。例如 `anchor_style` 可以从“参考艺人 + 子风格 + BPM”放宽到“参考艺人 + 子风格”，不能改为场景或年代查询。

极速版按用户 `link_priority` 查找首选可用平台直接页，首选不可用时才尝试下一个允许平台；`exclusive` 只查询和交付目标平台。普通模式的“每个允许平台至少一轮发现”不适用于极速版。无论模式，禁用平台不得搜索、引用或输出。

地区与语言信息不足时不要阻塞搜索：可以继续使用宽泛市场，如 `英语国际市场`、宽泛繁体中文市场或 `unknown`，再配合风格、场景和平台策略完成检索。平台页面无法验证某地区是否可用时，`availability` 标为 `unknown` 或 `region_limited`，并说明“当前无法确认当地可用性”；不要据此写成“当地没有这首歌”。

“时代与经典”参与查询拆分，但 Phase A 只把它当作扩展候选覆盖的线索，不做独立经典关系图、固定经典配额或额外输出结构。“少量经典锚点”可以用于补充查询、桥接年代和校准熟悉度，最终仍按现有逐曲验证、排序、编排和去重流程决定是否入选。

### 平台约束的执行顺序

在发出查询前，把平台分成三类：

1. `priority` / `link_priority`：用户给出的主链接和回退顺序；没有时才使用默认顺序。
2. `allowed`：可以作为最终链接的平台；其他权威来源可以进入内部核验记录。
3. `forbidden`：不要搜索、不要引用、不要放进默认报告的平台；相关限制保留在内部核验记录。

`discovery_strategy` 默认设为 `balanced_round_robin`。`discovery_order` 只用于记录实际覆盖顺序，不等同于内容排序权重；平台优先级永远不进入 style、scene 或 popularity 的评分。

“优先/最好有”只改变链接顺序和回退顺序；“只要/仅接受”则要求最终曲目必须有该平台直接页面。不要因为某平台更容易找到结果，就把它偷偷升级为用户的唯一目标。候选记录的 `primary_source` 应是第一顺序中已验证的允许平台页；Bandcamp、Beatport 等权威页放入补充证据，只有没有任何允许平台直接页时才可作为非 exclusive 报告的主证据。

### 中文 DJ 需求的检索展开

保留用户原词，同时为搜索生成等价的中英文线索。例如：`暖场/开场/收场/推峰` 可展开为 warm-up、opening、closing、energy arc；`左场/地下/怪` 可展开为 leftfield、underground、experimental；`大家熟/有反应/不俗` 可展开为 familiar、crowd response、crossover、avoid overplayed。展开词只用于提高召回，不把搜索词当作已验证的流派或音频事实。

艺人、歌曲和场景词要分开查询：如果用户说“像 X”或“把 X 当采样语汇”，用 X 发现相邻作品，不把 X 本身的全部目录当成必选结果。

## 来源等级

### A：可直接用于曲目验证

- SoundCloud、Apple Music、Spotify 的官方曲目页面
- 网易云音乐的官方曲目页面
- Bandcamp、Beatport 的具体发行或曲目页面
- 艺人或唱片公司的官方发行页面

媒体评测、采访、Wikipedia 或普通专辑介绍可以补充背景，但不能单独充当最终曲目的直接播放/发行链接；如果它只列出整张专辑而没有把该曲与发行准确对应，也不能替代逐曲核验。一个通用评测 URL 不能被复制到多首曲目上冒充逐曲证据。

### B：可补充元数据

- MusicBrainz
- Discogs
- 权威音乐媒体或厂牌目录

### C：仅作为发现线索

- 普通搜索摘要
- 用户生成列表、论坛、社交帖子
- 聚合站结果

C 级来源不能单独证明曲目存在、版本正确或元数据准确。不要引用搜索结果页作为最终播放链接。

## 候选记录

为每首候选维护以下字段；无法验证的字段保留 `unknown`：

```yaml
title: official title
artist: official artist name
version: original | remix | edit | live | unknown
version_label: exact official version text | unknown
version_kind: original | remix | dub | edit | instrumental | live | radio_edit | extended | other | unknown
platforms:
  soundcloud: url | null
  apple_music: url | null
  spotify: url | null
  netease_cloud_music: url | null
  other: []
playback_urls:
  - platform: soundcloud
    url: https://...
    availability: available | region_limited | login_required | unavailable | unknown
verification_sources:
  - type: platform_track | official_release | metadata
    url: https://...
    checked_at: YYYY-MM-DD
primary_source: url
source_platform: soundcloud | apple_music | spotify | netease_cloud_music | bandcamp | other
platform_match: preferred | allowed_fallback | exclusive | unavailable
isrc: value | unknown
dedupe_key: isrc-or-normalized-recording-key
genres: []
bpm: number | unknown
energy: low | medium | high | unknown
moods: []
release_date: value | unknown
availability: available | region_limited | login_required | unavailable | unknown
popularity_evidence:
  description: unknown
  source: unknown
  observed_at: unknown
  region: unknown
verification: verified | partial | unknown
```

在内部候选表中保留每首的播放链接、实际查看过的页面字段、核验来源、`platform_match`、`availability`、`verification` 和去重键。`platforms` 是兼容字段，最终交付优先使用 `playback_urls`；`verification_sources` 只说明证据，不自动成为用户可用的播放链接。最终四个版本只从这张表生成；如果一首歌没有可追溯的记录，就不要凭记忆把它补进报告。

## 自适应候选池与验证预算

简要版以综合版目标数 `final_target` 作为共享候选池基准。丰富版先计算所有视角的实际目标数之和 `rich_total_slots`。重复是严格例外而不是容量假设，因此候选池默认按完全零重复准备，令 `required_unique = rich_total_slots`。候选池目标为：

```text
fast: fast_pool_goal = min(max(2 × first_batch_target, first_batch_target + 5), 40)
composite: pool_goal = min(max(2 × final_target, final_target + 8), 120)
four_views: pool_goal = min(max(2 × final_target, final_target + 8, required_unique + 8), 120)
```

极速版每批并行核验 5 首。首批主动计算预算固定为：需求解析与查询规划 5 秒、归一化和轻量评分 20 秒、去重与播放顺序 20 秒、输出及检查 10 秒、缓冲 5 秒，总计 60 秒；网络等待不计入。首批在达到 `fast_pool_goal`、达到首批目标或主动计算达到 50 秒时停止扩池，只完成当前已验证结果，允许总主动计算在 50–70 秒；不要求每个允许平台完成一轮发现。内部计时须与查询、验证、去重、平台降级和停止原因一起保留；不要把此协议伪称为已完成的真实性能实测。

当 `final_target` 大于首批目标时，续跑使用 `continuation_pool_goal = min(max(2 × final_target, final_target + 10), 100)`。续跑只能读取首批同一精确查询与放宽一级回退查询的后续结果页或更多返回项，不得新增第三查询、切换主导向或重新解释需求。新增候选继续按同一已定义的 60/25/15 函数独立评分并增量合并；不得重置或更换评分函数。支持中间消息的宿主在首批后按 5 首批次继续，不受首批 60 秒预算约束，直到达到 `final_target`、达到 `continuation_pool_goal`、同一两查询结果耗尽、连续两批没有新增可交付录音，或平台不可继续。最终可以重排合并结果，但必须保留首批全部曲目。

后续人工/真实模型验收以 GPT-5.6 medium 进行 12 次冷启动：4 次短请求、4 次 30–50 首分段请求、2 次 exclusive 请求、2 次未填写数量请求。对每次运行的首批分别记录总耗时和网络等待并计算首批主动计算时间；验收目标是首批主动计算每次不超过 70 秒、中位数不超过 60 秒。30–50 首请求的后台续跑另行记录主动计算耗时，不纳入首批 50–70 秒 SLA，因为续跑本身允许跨批次继续读取同一查询结果。此仓库当前只固化协议和行为评测，未声称已经完成该 12 次运行。

候选池阶段可以先记录搜索摘要、平台页面或权威来源，状态为 `partial` 或 `unknown`；只有进入任一最终版本的唯一录音键才进入深度核验队列。为链接失效、exclusive 平台缺失或版本冲突保留少量已核验备选。以下停止条件仅适用于 `composite` / `four_views`：

- 已达到 `pool_goal`，并且每个允许平台至少完成一轮发现；
- 连续两轮查询主要产生重复、低相关或无法验证的结果；
- 平台限制、地区限制或工具不可访问使继续搜索无法提升质量。

同一录音获准进入两个视角时只深度核验一次。极速版在预算内仍不足时报告实际数量或零条，不用未验证曲目、错误版本或重复曲目补足；普通模式仍报告各视角实际数量。

## 验证门槛

进入最终歌单前，曲目必须同时满足：

- 曲目页面或权威发行页面可访问
- 页面中的艺人和曲名与候选一致
- `version_label` 与页面版本一致，没有把 Remix、Edit、Live、Dub 或 Extended Mix 与 Original 混淆
- 至少一个符合平台策略的 `playback_urls` 或具体发行页链接可提供给用户

验证动作要逐曲完成：打开最终要给用户的 `playback_urls` 或具体发行页，核对页面中的艺人、完整曲名、版本和可用性；仅看到搜索摘要、URL slug 或聚合站条目不算通过。播放页面失效、地区受限或页面信息冲突时，记录 `availability` 和 `verification`，必要时剔除候选；`partial` 不能替代直接链接。如果平台为 exclusive，缺少该平台直接页的候选不能进入最终曲目表，只能进入缺失清单。最终报告中的每一行都要有自己可追溯的曲目/发行证据，不能只靠一条泛化媒体页面背书。

## 去重规则

1. 相同 ISRC 视为同一录音。
2. 无 ISRC 时，规范化大小写、Unicode 标点、feat./featuring、大小写混写和空格后比较艺人 + 曲名 + 版本；不要删除 Remix、Dub、Edit、Live 等版本词再去重。
3. 同一录音在多个平台出现时合并平台链接，不重复占位。
4. Remix、Edit、Dub、Instrumental、Live、Radio Edit 与 Extended Mix 保留为独立版本，但避免同一版本的拼写差异造成重复。
5. 同一艺人连续占据过多位置时，在排序阶段处理，不要在去重阶段误删有效曲目。

去重发生在四种排序和播放编排之前。极速版交付前按单表检查 `dedupe_key`，必须全部唯一；其艺人上限为 `artist_cap = max(1, floor(0.15 × actual_target))`，其中 `actual_target` 是当前表的有效目标：首批取 `min(first_batch_target, 首批已验证可交付行数)`，最终取 `min(final_target, 最终已验证可交付行数)`。参考艺人不豁免，只有用户明确请求艺人专题时才可豁免。综合版在分配 Warm Up、Groove、Peak、Closing 后再做一次全局录音键检查，确保同一录音不会跨段重复；丰富版完成四个视角后再按整份报告检查 `dedupe_key`，只允许至多一个高质量录音出现两次，其余录音只出现一次。参考艺人和参考曲目不豁免。多个平台链接仍合并在同一条记录中。

候选不足时透明报告，不降低验证门槛。
