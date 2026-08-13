# DJ Crate Digger Phase A 交互基础 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (- [ ]) syntax for tracking.

**Goal:** 在不引入长期私人画像、五视图排序或外部证据适配器的前提下，实现语言与目标市场分离、第一轮地区字段、第二轮熟悉度/经典字段，以及每次完整 SOP 后的记忆状态和可选反馈邀请。

**Architecture:** 继续使用现有 Markdown 指令型 Skill。第一轮和第二轮生成只服务当前会话的 Session Brief；目标市场带来源标记且明确不持久化。新字段通过兼容映射接入现有搜索与四视图排序，报告末尾把本地导出、记忆状态和反馈邀请合并为同一个“可选后续”区域。Phase A 不创建私人数据文件，也不声称已经具备 Phase B/C/D 能力。

**Tech Stack:** Markdown Skill 合同、JSON 行为评测、jq JSON 校验、rg 静态一致性检查、Git diff 人工复核。

## Global Constraints

- 书面规格以 docs/superpowers/specs/2026-08-13-dj-crate-digger-personalization-design.md 为唯一设计依据。
- 本计划只实施第 18 节“阶段 A：交互基础”。事件日志、Beta 画像、正式反馈解析器、五视图、经典脉络召回、1001Tracklists 和媒体适配器分别留给 Phase B/C/D。
- 严格保留两轮 Markdown 问卷、逐曲平台验证、版本识别、录音级去重、11 列主表、TXT/M3U8 导出和现有授权安全边界。
- 丰富版在 Phase A 仍为四视图；只把现有“流行度优先”语义改名为“熟悉度与发现感优先”，不增加“DJ 品味优先”视图。
- “少量经典锚点”在 Phase A 只进入需求卡和现有搜索约束，不设置最终曲目固定比例，也不宣称已完成独立经典脉络召回。
- 长期记忆在 Phase A 始终显示为未启用；不得创建长期存储、显示待确认长期摘要，或暗示反馈会跨会话保存。
- 不新增 hash、冻结 contract、baseline 或发布 gate；不删除现有安全措施。
- 当前仓库没有本地 eval runner。先用 evals/evals.json 固化行为，再用 jq、rg、Git diff 和人工场景回放验证；不要虚构不存在的自动化测试命令。
- 未收到用户明确的“定稿”前，不创建 Git commit，不 push。完成实施后只展示测试结果、git status 和 diff 摘要并等待确认。

---

## Task 1: 先把 Phase A 行为写入 eval 语料

**Files:**

- Modify: evals/evals.json
- Verify unchanged: evals/trigger-evals.json

### Interface contract

保留现有 25 个行为评测及其 ID；只更新受新问卷影响的断言，并追加 ID 26–33。触发边界没有变化，因此 33 个 trigger eval 不修改。

新增场景必须分别覆盖：

- ID 26：中文沟通、明确英国市场；报告保持中文，目标市场采用英国。
- ID 27：英文沟通、明确日本市场；报告保持英文，目标市场采用日本。
- ID 28：简体中文且地区留空；本轮推断中国大陆，来源为 language_inferred，不持久化。
- ID 29：一般繁体中文且无足够地区词；不得武断指定香港或台湾。
- ID 30：一般英文且地区留空；使用“英语国际市场”，不得武断指定美国或英国。
- ID 31：第二轮把熟悉度与时代/经典分开；“少量经典锚点”不产生固定最终配额。
- ID 32：Phase A 收尾显示未启用的长期记忆、无反馈/未更新状态和自然语言可选反馈邀请。
- ID 33：Phase A 回归；丰富版仍为四视图、主表仍为 11 列，导出与反馈邀请都不算第三轮需求收集。

### Steps

- [ ] 更新 ID 14–15、17–23 中仍写着旧第一轮四字段、旧“流行度”字段或旧收尾流程的 expectations。ID 7、10 等既有四视图测试只更新视图名称，不改变数量和共享候选池要求。
- [ ] 追加 ID 26–33；每条 expected_output 描述可观察行为，每条 expectations 分开断言语言、市场来源、非持久化、两轮边界或回归能力。
- [ ] 不把 Phase B 的“长期摘要确认”、Phase C 的“DJ 品味优先版”或 Phase D 的外部适配器写成 Phase A 已实现能力。
- [ ] 校验 JSON 语法和 ID 唯一性：

~~~bash
jq empty evals/evals.json evals/trigger-evals.json
jq -e '(.evals | length) == 33 and (([.evals[].id] | unique | length) == 33)' evals/evals.json
jq -e 'length == 33' evals/trigger-evals.json
~~~

Expected: 三条命令退出码均为 0。行为 eval 数量从 25 变为 33；trigger eval 仍为 33。

- [ ] 在实现文件尚未修改时运行以下合同探针，记录它们缺失或仍命中旧字段，作为 red 阶段证据：

~~~bash
rg -n '目标国家 / 地区：|熟悉度与发现感：|时代与经典：' SKILL.md
rg -n '^流行度：$|流行度优先版' SKILL.md references/report-template.md references/ranking.md
rg -n '私人记忆状态|不会跨会话保存' SKILL.md references/report-template.md references/export.md
~~~

Expected before implementation: 第一、三条没有完整命中；第二条仍命中旧合同。

---

## Task 2: 修改两轮问卷、语言/地区推断和需求卡

**Files:**

- Modify: SKILL.md
- Modify: references/ranking.md
- Test: evals/evals.json

### Interface contract

第一轮代码块严格为：

~~~markdown
场景：
目标国家 / 地区：
核心声音方向：
歌曲数量或 Set 时长：
其他限制：
~~~

第二轮代码块严格为：

~~~markdown
具体风格：
速度 / BPM：
熟悉度与发现感：
时代与经典：
输出版本：
情绪：
SET 能量级或能量走势：
平台与链接要求：
其他：
~~~

需求卡新增：

~~~yaml
communication_language: auto
target_market: unknown
target_market_source: unknown  # user_provided | language_inferred
persist_target_market: false
familiarity_intent: balanced  # familiar | balanced | discovery | ai
era_classic_intent: ai        # contemporary | light_classic_anchors | new_old_bridge | classic_first | ai
~~~

为避免一次迁移破坏现有排序，暂时保留 popularity_intent 和 freshness_intent 作为兼容投影字段，但同一信号只能计分一次。后续实现不得把 compatibility 字段视为第二份用户证据。

### Steps

- [ ] 在 SKILL.md 第一轮说明与 fenced Markdown 模板中加入“目标国家 / 地区”，位置固定在“场景”之后。
- [ ] 明确用户填写值优先；留空时只生成本轮临时市场。规则为：

  - 简体中文默认中国大陆。
  - 繁体中文只有在词汇和用字证据足够时才区分香港或台湾；证据不足时保留宽泛繁体中文市场。
  - 一般英文默认英语国际市场，不默认美国或英国。
  - 明确地区永远覆盖语言推断，但不改变沟通语言。

- [ ] 将“报告语言跟随用户”扩展为独立 communication_language 规则；标题、问卷、状态与解释跟随用户，曲名、艺人、版本和平台名保留官方原文。
- [ ] 把第二轮“流行度”替换为两个字段并写入固定示例：

  - 熟悉度与发现感：热门熟悉 / 平衡 / 小众发现 / AI判断。
  - 时代与经典：当代为主 / 少量经典锚点 / 新旧桥接 / 经典优先 / AI判断。

- [ ] 更新字段映射、解析清单、priority_order 和 selection_priority。familiarity_intent 投影到现有 popularity_fit；era_classic_intent 投影到现有 freshness_fit 或搜索约束。“少量经典锚点”只表示候选覆盖意图，不固定最终名额。
- [ ] 在内部需求卡中加入上述六个字段；保留 scene_context.region 作为当前会话兼容字段，并说明其值来自 target_market、不会被写入长期数据。
- [ ] 将 output_mode 保持为 composite | four_views。把现有第三专项视图及 ranking.md 的标签统一改为“熟悉度与发现感优先”，仍然只输出风格、场景、熟悉度与发现感、动态综合四个视图。
- [ ] 保留旧式自然语言中的“流行度/热门/冷门”解析兼容性，但第二轮模板和需求摘要不再把经典与熟悉度混成一个字段。
- [ ] 运行合同检查：

~~~bash
rg -n '目标国家 / 地区：|communication_language|target_market_source|persist_target_market|familiarity_intent|era_classic_intent' SKILL.md
rg -n '热门熟悉 / 平衡 / 小众发现 / AI判断|当代为主 / 少量经典锚点 / 新旧桥接 / 经典优先 / AI判断' SKILL.md
rg -n '熟悉度与发现感优先' SKILL.md references/ranking.md
~~~

Expected: 每组新字段均有定义、映射和使用位置；四视图名称一致。

- [ ] 运行旧字段复核：

~~~bash
rg -n '^流行度：$|根据您选择的风格、场景、流行度|流行度优先版' SKILL.md references/ranking.md
~~~

Expected: 不再命中作为问卷字段或视图标题的旧文案；允许在“兼容解析旧式流行度表达”的说明中出现“流行度”一词。

---

## Task 3: 让目标市场进入搜索上下文和报告摘要

**Files:**

- Modify: references/search-verification.md
- Modify: references/report-template.md
- Modify: SKILL.md
- Test: evals/evals.json

### Interface contract

target_market 只影响本轮：

- 当地听众熟悉度和文化语境。
- 搜索词与编辑/平台来源的地区选择。
- 平台可用性和地区受限状态的解释。

它不改变 communication_language，不进入长期偏好，也不能覆盖用户的 allowed / forbidden / exclusive 平台策略。

### Steps

- [ ] 在 search-verification.md 搜索策略中加入 target_market 上下文：明确市场值优先；推断市场只作为宽泛检索线索，不能写成用户长期偏好或确定事实。
- [ ] 补充地区与语言降级：地区不明时继续使用宽泛市场，不阻塞搜索；平台页面无法验证地区可用性时写 unknown/region_limited，不声称“当地没有”。
- [ ] 让“时代与经典”参与现有查询拆分，但写清 Phase A 不做独立经典关系图或固定配额。少量经典锚点可以扩大候选查询，最终仍走现有验证、排序和编排。
- [ ] 在 report-template.md 的需求确认摘要加入：

~~~markdown
- 沟通语言：...
- 目标国家 / 地区：...
- 地区来源：用户填写 / 根据语言临时推断
- 熟悉度与发现感：...
- 时代与经典：...
~~~

- [ ] 删除模板中的单一“流行度”摘要项，更新丰富版第三视图标题为“熟悉度与发现感优先版”；四视图数量不变。
- [ ] 在 SKILL.md 输出报告规则中要求披露 target_market_source，并明确 language_inferred 只是本轮假设。
- [ ] 校验：

~~~bash
rg -n 'target_market|language_inferred|英语国际市场|中国大陆|香港|台湾' SKILL.md references/search-verification.md
rg -n '沟通语言|目标国家 / 地区|地区来源|熟悉度与发现感|时代与经典' references/report-template.md
rg -n '歌名 \| 艺术家 \| 专辑/EP \| 风格 \| BPM \| 歌曲时长 \| 能量级 \| 发行时间 \| 简介 \| 选择原因 \| 链接' SKILL.md references/report-template.md
~~~

Expected: 地区来源可见、语言和市场独立、11 列表头原样保留。

---

## Task 4: 合并“可选后续”区域并诚实显示 Phase A 记忆状态

**Files:**

- Modify: SKILL.md
- Modify: references/report-template.md
- Modify: references/export.md
- Test: evals/evals.json

### Interface contract

完整报告后固定显示：

~~~markdown
## 可选后续

### 私人记忆状态
- 长期记忆：未启用（本轮不会跨会话保存）
- 本轮反馈：无
- 长期画像：本轮未更新

如果愿意，可以直接告诉我哪些曲目你喜欢、这场会用，或哪些不合适、版本不对；我可以在当前会话中按你的说明继续调整，但不会跨会话保存。回复序号、曲名、链接或粘贴表格行都可以。不回复不会影响本次歌单和导出。

### 本地 TXT / M3U8 导出

是否导出本次最终综合歌单？
- TXT
- M3U8
- TXT + M3U8
- 不导出
~~~

反馈邀请与本地导出都属于报告后的可选动作，不是第三轮需求收集。用户可以只反馈、只导出、两者都做或不回复。

### Steps

- [ ] 在 SKILL.md 报告与条件导出之间定义统一“可选后续”收尾。保证它只出现在完整推荐报告后，不在两轮问卷中提前出现。
- [ ] 使用上面的 Phase A 固定状态，不出现“已启用”“等待确认 N 项”“已确认更新”等只有 Phase B 才能产生的状态。
- [ ] 保留自然语言反馈的低认知负载入口，但只承诺当前会话继续调整，不创建事件日志、不写长期画像、不生成长期保存摘要。
- [ ] 在 report-template.md 把现有独立“本地 TXT/M3U8 导出”段改为统一“可选后续”区域；保留导出选项和用户确认后才生成文件的规则。
- [ ] 在 export.md 明确导出问题可以与记忆状态/反馈邀请并列展示，但导出状态机、UTF-8、顺序、去重、直接链接、M3U8 安全和不覆盖旧文件规则完全不变。
- [ ] 运行检查：

~~~bash
rg -n '可选后续|私人记忆状态|长期记忆：未启用|本轮反馈：无|长期画像：本轮未更新|不会跨会话保存' SKILL.md references/report-template.md references/export.md
rg -n 'TXT \+ M3U8|不导出|不是第三轮需求收集|不算第三轮需求收集' SKILL.md references/report-template.md references/export.md
~~~

Expected: 三份文档的阶段状态、可选性和导出顺序一致。

- [ ] 复核没有提前实现 Phase B：

~~~bash
rg -n '等待确认 N 项|已确认更新|事件日志|Beta\(|sharing_consent' SKILL.md references/report-template.md references/export.md
~~~

Expected: Phase A 实现文件不出现长期存储或画像已更新的运行承诺。若在安全边界说明中出现未来术语，必须明确标记为未实现，而不能写成当前状态。

---

## Task 5: 更新 README 并完成全量回归

**Files:**

- Modify: README.md
- Verify unchanged: agents/openai.yaml
- Verify unchanged: evals/trigger-evals.json
- Verify all modified Phase A files

### Steps

- [ ] 更新 README “本版重点”：第一轮加入目标国家/地区；沟通语言与市场分离；第二轮拆成熟悉度和时代/经典；丰富版仍为四视图；完整报告后显示 Phase A 记忆状态和可选反馈。
- [ ] 把 README 行为评测数量从 25 更新为 33，并概括新增地区/语言/收尾回归场景。trigger eval 数量不变。
- [ ] 不修改 agents/openai.yaml；默认提示仍然准确，不需要把 Phase B/C/D 写进 starter prompt。
- [ ] JSON 与结构校验：

~~~bash
jq empty evals/evals.json evals/trigger-evals.json
jq -e '.skill_name == "dj-crate-digger" and (.evals | length) == 33 and (([.evals[].id] | unique | length) == 33)' evals/evals.json
jq -e 'length == 33' evals/trigger-evals.json
git diff --check
~~~

Expected: 全部退出码为 0，无 JSON 错误、重复 ID 或 whitespace error。

- [ ] 核心能力静态回归：

~~~bash
rg -n '严格两轮|目标国家 / 地区|熟悉度与发现感|时代与经典|four_views' SKILL.md README.md references/report-template.md
rg -n '逐曲|version_label|dedupe_key|11 列|TXT|M3U8|exclusive|forbidden' SKILL.md references README.md
rg -n 'DJ 品味优先版' SKILL.md README.md references
~~~

Expected: 前两条覆盖现有底座和 Phase A 新合同；第三条无命中，证明未提前输出 Phase C 视图。

- [ ] 确认本次没有修改触发边界和 agent 元数据：

~~~bash
git diff --exit-code -- evals/trigger-evals.json agents/openai.yaml
~~~

Expected: 退出码为 0。

- [ ] 人工回放八个场景，并逐项对照 eval ID 26–33：

  1. 中文 + 英国明确市场。
  2. 英文 + 日本明确市场。
  3. 简中地区留空。
  4. 一般繁中地区留空。
  5. 一般英文地区留空。
  6. 熟悉度与经典取向不同组合。
  7. 简要版完成后的状态、反馈邀请和导出。
  8. 丰富版仍为四视图且 11 列不变。

Expected: 沟通语言不被市场改变；明确市场不被语言推断覆盖；推断市场可见且不持久化；没有第三轮强制问卷；没有 Phase B/C/D 能力冒充。

- [ ] 展示变更而不提交：

~~~bash
git status --short --branch
git diff --stat
git diff -- SKILL.md README.md references evals/evals.json
~~~

Expected: 只出现设计稿、计划与 Phase A 约定文件；无 commit、无 push。向用户汇报测试结果和 diff 摘要，等待“定稿”。

## Phase A 完成定义

Phase A 只有在以下条件全部成立时才算完成：

- 两轮问卷仍是唯一强制需求收集路径，第一轮和第二轮字段顺序符合本计划。
- communication_language 与 target_market 可以不同；明确市场覆盖推断，推断市场只在本轮生效。
- 报告摘要披露市场值和来源，搜索使用该上下文但不改变平台许可。
- 熟悉度与时代/经典分开；“少量经典锚点”没有固定最终配额。
- 丰富版仍是四视图，11 列、验证、去重、导出与安全边界没有回归。
- 收尾状态诚实显示长期记忆未启用，反馈只承诺当前会话调整。
- 33 个行为 eval 和 33 个 trigger eval 均为合法 JSON 且 ID 唯一。
- 用户尚未说“定稿”时，仓库没有新增 commit，也没有 push。
