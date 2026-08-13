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

地区与语言信息不足时不要阻塞搜索：可以继续使用宽泛市场，如 `英语国际市场`、宽泛繁体中文市场或 `unknown`，再配合风格、场景和平台策略完成检索。平台页面无法验证某地区是否可用时，`availability` 标为 `unknown` 或 `region_limited`，并说明“当前无法确认当地可用性”；不要据此写成“当地没有这首歌”。

“时代与经典”参与查询拆分，但 Phase A 只把它当作扩展候选覆盖的线索，不做独立经典关系图、固定经典配额或额外输出结构。“少量经典锚点”可以用于补充查询、桥接年代和校准熟悉度，最终仍按现有逐曲验证、排序、编排和去重流程决定是否入选。

### 平台约束的执行顺序

在发出查询前，把平台分成三类：

1. `priority` / `link_priority`：用户给出的主链接和回退顺序；没有时才使用默认顺序。
2. `allowed`：可以作为最终链接的平台；其他权威来源可以进入内部核验记录。
3. `forbidden`：不要搜索、不要引用、不要放进“来源”段落的平台。

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

以综合版目标数 `final_target` 作为共享候选池基准：

```text
pool_goal = min(max(2 × final_target, final_target + 8), 120)
```

候选池阶段可以先记录搜索摘要、平台页面或权威来源，状态为 `partial` 或 `unknown`；只有进入任一最终版本的唯一录音键才进入深度核验队列。为链接失效、exclusive 平台缺失或版本冲突保留少量已核验备选。满足以下任一条件即可停止扩展：

- 已达到 `pool_goal`，并且每个允许平台至少完成一轮发现；
- 连续两轮查询主要产生重复、低相关或无法验证的结果；
- 平台限制、地区限制或工具不可访问使继续搜索无法提升质量。

同一录音进入多个视角时只深度核验一次。预算上限内仍不足时报告实际候选数，不用未验证曲目补足。

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

去重发生在四种排序和播放编排之前。综合版在分配 Warm Up、Groove、Peak、Closing 后再做一次全局录音键检查，确保同一录音不会跨段重复；多个平台链接仍合并在同一条记录中。

候选不足时透明报告，不降低验证门槛。
