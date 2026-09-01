# Simplified Chinese locale pack

This file is the fixed 简体中文 UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "zh-Hans",
  "language_name": "Simplified Chinese",
  "native_name": "简体中文",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "留空时只使用宽泛的中文市场作为本轮临时线索。",
    "explicit_region": "明确填写的国家或地区覆盖语言推断，但不改变沟通语言。",
    "persistence": "目标市场只保留在当前会话，不写入长期偏好。"
  },
  "quick_start": {
    "intro": "欢迎来到 DJ 选歌助手。这是一个利用 Agent 帮您排 set 的 skill。您将在两轮对话中确认需求，并获得 AI 选歌建议。填写规则为：",
    "tutorial_label": "一键导入 Set 教程",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.md"
  },
  "intake": {
    "round_1": {
      "title": "【第一轮：必要信息】",
      "rules": [
        "1. 可以从例子中复制，也可以自由填写或不填",
        "2. 不填意味着ai智能判断答案"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "场景",
          "example": "表演场景。如：`酒吧` / `俱乐部` / `婚礼` / `艺术展`"
        },
        {
          "key": "target_market",
          "label": "目标国家 / 地区",
          "example": "如：`中国大陆` / `台湾` / `香港` / `日本` / `英语国际市场`"
        },
        {
          "key": "core_sound",
          "label": "核心声音方向",
          "example": "参考艺人、参考曲目以及参考流派。如：`Skrillex` 的 `Tears`，`现代UK_Bass`流派"
        },
        {
          "key": "track_count_or_duration",
          "label": "歌曲数量或 Set 时长",
          "example": "如：`20 首` / `60 分钟`"
        },
        {
          "key": "output_mode",
          "label": "输出版本",
          "example": "极速版 / 简要版 / 丰富版"
        },
        {
          "key": "other",
          "label": "其他限制",
          "example": "如：`不要口水歌`、`不要人声`、`只要Remix`；可以不填"
        }
      ],
      "prompt": "欢迎来到 DJ 选歌助手。这是一个利用 Agent 帮您排 set 的 skill。您将在两轮对话中确认需求，并获得 AI 选歌建议。填写规则为：\n\n1. 可以从例子中复制，也可以自由填写或不填\n2. 不填意味着ai智能判断答案\n\n【第一轮：必要信息】\n场景：\n「表演场景。如：`酒吧` / `俱乐部` / `婚礼` / `艺术展`」\n目标国家 / 地区：\n「如：`中国大陆` / `台湾` / `香港` / `日本` / `英语国际市场`」\n核心声音方向：\n「参考艺人、参考曲目以及参考流派。如：`Skrillex` 的 `Tears`，`现代UK_Bass`流派」\n歌曲数量或 Set 时长：\n「如：`20 首` / `60 分钟`」\n输出版本：\n「`极速版`：快速输出playlist，但是质量会下降」\n「`简要版`：只给一个综合的playlist」\n「`丰富版`：根据您选择的风格、场景、熟悉度与发现感分别提供建议，并最终输出成简要版」\n其他限制：\n「如：`不要口水歌`、`不要人声`、`只要Remix`；可以不填」\n\n\u0060\u0060\u0060markdown\n场景：\n目标国家 / 地区：\n核心声音方向：\n歌曲数量或 Set 时长：\n输出版本：\n其他限制：\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "【第二轮：需求细化】",
      "rules": [
        "1. 可以从例子中复制，也可以自由填写或不填"
      ],
      "fields": [
        {
          "key": "style",
          "label": "具体风格",
          "example": "如：`House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "速度 / BPM",
          "example": "如：`105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "熟悉度与发现感",
          "example": "`热门熟悉`/`平衡`/`小众发现`"
        },
        {
          "key": "era_classic",
          "label": "时代与经典",
          "example": "`当代为主`/`少量经典锚点`/`新旧桥接`/`经典优先`"
        },
        {
          "key": "mood",
          "label": "情绪",
          "example": "如：`怀旧` / `阴冷` / `浪漫`"
        },
        {
          "key": "energy",
          "label": "SET 能量级或能量走势",
          "example": "如：`低`/`高`；`平稳` / `过山车`"
        },
        {
          "key": "platform",
          "label": "平台与链接要求",
          "example": "如：`网易云`/`Apple Music`/`SoundCloud`/`Bandcamp`/`Beatport`/`Spotify`；填写一个平台时只使用该平台，填写多个平台按先后顺序优先"
        },
        {
          "key": "other",
          "label": "其他",
          "example": ""
        }
      ],
      "prompt": "【第二轮：需求细化】\n具体风格：\n「如：`House` / `Bass` / `Garage` / `Techno` / `Breakbeat`」\n速度 / BPM：\n「如：`105` / `128` / `140` / `150` / `170`」\n熟悉度与发现感：\n「`热门熟悉`/`平衡`/`小众发现`」\n时代与经典：\n「`当代为主`/`少量经典锚点`/`新旧桥接`/`经典优先`」\n情绪：\n「如：`怀旧` / `阴冷` / `浪漫`」\nSET 能量级或能量走势：\n「如：`低`/`高`；`平稳` / `过山车`」\n平台与链接要求：\n「如：`网易云`/`Apple Music`/`SoundCloud`/`Bandcamp`/`Beatport`/`Spotify`；填写一个平台时只使用该平台，填写多个平台按先后顺序优先」\n其他：\n\n\u0060\u0060\u0060markdown\n具体风格：\n速度 / BPM：\n熟悉度与发现感：\n时代与经典：\n情绪：\nSET 能量级或能量走势：\n平台与链接要求：\n其他：\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# 极速版",
      "first_batch_title": "# 极速版首批",
      "final_title": "# 极速版",
      "columns": [
        "歌名",
        "歌手",
        "链接"
      ],
      "next_steps": [
        {
          "label": "第一｜反馈选歌情况",
          "body": "如果愿意，您可以用自然语言回复我选歌情况，这会丰富您的私人选歌偏好，让推荐更准。回复包括但不限于「`skream的歌不错，但我这次因为客群的关系没放`/`我不喜欢跳楼机，以后别再推了`/`我这次打了这些歌（配图/表）`」"
        },
        {
          "label": "第二｜导出或交接歌单",
          "body": "您可以输出文字版歌单或交接给 W4DJ，直接回复 `导出到w4dj` 或者 `输出文字版歌单` 即可。\n\n`w4dj`的功能：一键导入歌单，下载后一键转换格式，并一键导入打碟软件，请导出`.w4dj`格式并且下载 [w4dj-rkb](https://github.com/komakizhu/W4DJ-RKB)。具体操作教程可以查看 [一键导入Set教程](https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.md)\n\n`输出文字版歌单`的功能：输出可复制文本，可以手动导入网易云，但无法帮您一键把歌曲导入 RKB。"
        }
      ],
      "digging_notes": "选歌碎碎念",
      "mix_suggestion": "接歌建议",
      "unknown": "未知",
      "verified": "已核验",
      "target_platform_missing": "目标平台缺失"
    },
    "brief": {
      "title": "# 简要版",
      "first_batch_title": "# 简要版",
      "final_title": "# 简要版",
      "columns": [
        "歌名",
        "艺术家",
        "专辑/EP",
        "风格",
        "BPM",
        "调性",
        "歌曲时长",
        "能量级",
        "发行时间",
        "简介",
        "选择原因",
        "链接"
      ],
      "next_steps": [
        {
          "label": "第一｜反馈选歌情况",
          "body": "如果愿意，您可以用自然语言回复我选歌情况，这会丰富您的私人选歌偏好，让推荐更准。回复包括但不限于「`skream的歌不错，但我这次因为客群的关系没放`/`我不喜欢跳楼机，以后别再推了`/`我这次打了这些歌（配图/表）`」"
        },
        {
          "label": "第二｜导出或交接歌单",
          "body": "您可以输出文字版歌单或交接给 W4DJ，直接回复 `导出到w4dj` 或者 `输出文字版歌单` 即可。\n\n`w4dj`的功能：一键导入歌单，下载后一键转换格式，并一键导入打碟软件，请导出`.w4dj`格式并且下载 [w4dj-rkb](https://github.com/komakizhu/W4DJ-RKB)。具体操作教程可以查看 [一键导入Set教程](https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.md)\n\n`输出文字版歌单`的功能：输出可复制文本，可以手动导入网易云，但无法帮您一键把歌曲导入 RKB。"
        },
        {
          "label": "第三｜五度圈排序",
          "body": "需要我根据五度圈原则帮您排列set顺序吗？"
        }
      ],
      "digging_notes": "选歌碎碎念",
      "mix_suggestion": "接歌建议",
      "unknown": "未知",
      "verified": "已核验",
      "target_platform_missing": "目标平台缺失"
    },
    "rich": {
      "title": "# 丰富版",
      "first_batch_title": "# 丰富版",
      "final_title": "# 丰富版",
      "columns": [
        "歌名",
        "艺术家",
        "专辑/EP",
        "风格",
        "BPM",
        "调性",
        "歌曲时长",
        "能量级",
        "发行时间",
        "简介",
        "选择原因",
        "链接"
      ],
      "next_steps": [
        {
          "label": "第一｜反馈选歌情况",
          "body": "如果愿意，您可以用自然语言回复我选歌情况，这会丰富您的私人选歌偏好，让推荐更准。回复包括但不限于「`skream的歌不错，但我这次因为客群的关系没放`/`我不喜欢跳楼机，以后别再推了`/`我这次打了这些歌（配图/表）`」"
        },
        {
          "label": "第二｜导出或交接歌单",
          "body": "您可以输出文字版歌单或交接给 W4DJ，直接回复 `导出到w4dj` 或者 `输出文字版歌单` 即可。\n\n`w4dj`的功能：一键导入歌单，下载后一键转换格式，并一键导入打碟软件，请导出`.w4dj`格式并且下载 [w4dj-rkb](https://github.com/komakizhu/W4DJ-RKB)。具体操作教程可以查看 [一键导入Set教程](https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.md)\n\n`输出文字版歌单`的功能：输出可复制文本，可以手动导入网易云，但无法帮您一键把歌曲导入 RKB。"
        },
        {
          "label": "第三｜五度圈排序",
          "body": "需要我根据五度圈原则帮您排列set顺序吗？"
        }
      ],
      "digging_notes": "选歌碎碎念",
      "mix_suggestion": "接歌建议",
      "unknown": "未知",
      "verified": "已核验",
      "target_platform_missing": "目标平台缺失",
      "view_titles": [
        "风格视角",
        "场景视角",
        "熟悉度与发现感视角",
        "动态综合视角"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "反馈选歌情况",
      "positive": [
        "我喜欢这首歌"
      ],
      "negative": [
        "我不喜欢这首歌"
      ],
      "ambiguous": [
        "我不确定这首歌"
      ]
    },
    "export_w4dj": {
      "label": "导出到 W4DJ",
      "positive": [
        "导出到w4dj"
      ],
      "negative": [
        "不要导出到w4dj"
      ],
      "ambiguous": [
        "也许导出到w4dj"
      ]
    },
    "output_text_playlist": {
      "label": "输出文字版歌单",
      "positive": [
        "输出文字版歌单"
      ],
      "negative": [
        "不要输出文字版歌单"
      ],
      "ambiguous": [
        "也许输出文字版歌单"
      ]
    },
    "harmonic_reorder": {
      "label": "五度圈排序",
      "positive": [
        "按五度圈原则排列"
      ],
      "negative": [
        "不要重排"
      ],
      "ambiguous": [
        "也许按五度圈原则排列"
      ]
    },
    "confirm_long_term_memory": {
      "label": "确认长期记忆",
      "positive": [
        "记住这个偏好"
      ],
      "negative": [
        "不要保存这个偏好"
      ],
      "ambiguous": [
        "也许记住这个偏好"
      ]
    }
  },
  "platform_policy": {
    "aliases": {
      "spotify": "Spotify",
      "apple_music": "Apple Music",
      "soundcloud": "SoundCloud",
      "netease_cloud_music": "网易云",
      "bandcamp": "Bandcamp",
      "beatport": "Beatport",
      "beatsource": "Beatsource"
    },
    "exclusive_markers": [
      "唯一平台",
      "仅限",
      "只使用",
      "只在",
      "只要",
      "仅接受"
    ],
    "preferred_markers": [
      "优先",
      "最好有",
      "首选"
    ],
    "fallback_markers": [
      "备用",
      "回退",
      "可回退"
    ],
    "forbidden_markers": [
      "不要",
      "不提供",
      "排除"
    ]
  },
  "status": {
    "unknown": "未知",
    "verified": "已核验",
    "target_platform_missing": "目标平台缺失"
  },
  "export": {
    "text": "输出当前顺序的可复制文字版歌单。",
    "w4dj": "生成交给 W4DJ 的 UTF-8 `.w4dj` 交接文件。",
    "harmonic": "根据已知调性请求按五度圈原则排序。",
    "feedback": "自然语言反馈只更新当前会话；长期保存必须先确认。",
    "memory_confirmation": "我理解为这是一段简短的品味变化摘要。是否保存到私人长期档案？"
  },
  "trigger_capsule": [
    "挖歌",
    "排set",
    "排一套set",
    "找歌单",
    "排歌"
  ]
}
```
