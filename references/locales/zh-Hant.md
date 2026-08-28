# Traditional Chinese locale pack

This file is the fixed 繁體中文 UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "zh-Hant",
  "language_name": "Traditional Chinese",
  "native_name": "繁體中文",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "留空時只使用寬泛的繁體中文市場作為本輪臨時線索。",
    "explicit_region": "明確填寫的國家或地區覆蓋語言推斷，但不改變溝通語言。",
    "persistence": "目標市場只保留在當前會話，不寫入長期偏好。"
  },
  "quick_start": {
    "intro": "歡迎來到 DJ 選歌助手。這是一個利用 Agent 幫您排 set 的 skill。您將在兩輪對話中確認需求，並取得 AI 選歌建議。填寫規則為：",
    "tutorial_label": "一鍵導入 Set 教程",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.md"
  },
  "intake": {
    "round_1": {
      "title": "【第一輪：必要資訊】",
      "rules": [
        "1. 可以從例子中複製，也可以自由填寫或不填",
        "2. 不填表示由 AI 智能判斷答案"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "場景",
          "example": "表演場景。如：`酒吧` / `俱樂部` / `婚禮` / `藝術展`"
        },
        {
          "key": "target_market",
          "label": "目標國家 / 地區",
          "example": "如：`中國大陸` / `台灣` / `香港` / `日本` / `英語國際市場`"
        },
        {
          "key": "core_sound",
          "label": "核心聲音方向",
          "example": "參考藝人、參考曲目以及參考流派。如：`Skrillex` 的 `Tears`，`現代 UK Bass` 流派"
        },
        {
          "key": "track_count_or_duration",
          "label": "歌曲數量或 Set 時長",
          "example": "如：`20 首` / `60 分鐘`"
        },
        {
          "key": "output_mode",
          "label": "輸出版本",
          "example": "極速版 / 簡要版 / 豐富版"
        },
        {
          "key": "other",
          "label": "其他限制",
          "example": "如：`不要口水歌`、`不要人聲`、`只要 Remix`；可以不填"
        }
      ],
      "prompt": "歡迎來到 DJ 選歌助手。這是一個利用 Agent 幫您排 set 的 skill。您將在兩輪對話中確認需求，並取得 AI 選歌建議。填寫規則為：\n\n1. 可以從例子中複製，也可以自由填寫或不填\n2. 不填表示由 AI 智能判斷答案\n\n【第一輪：必要資訊】\n\n場景:\n“表演場景。如：`酒吧` / `俱樂部` / `婚禮` / `藝術展`”\n目標國家 / 地區:\n“如：`中國大陸` / `台灣` / `香港` / `日本` / `英語國際市場`”\n核心聲音方向:\n“參考藝人、參考曲目以及參考流派。如：`Skrillex` 的 `Tears`，`現代 UK Bass` 流派”\n歌曲數量或 Set 時長:\n“如：`20 首` / `60 分鐘`”\n輸出版本:\n“「`極速版`：快速輸出 playlist，但是品質會下降」”\n“「`簡要版`：只給一個綜合的 playlist」”\n“「`豐富版`：根據您選擇的風格、場景、熟悉度與發現感分別提供建議，並最終輸出成簡要版」”\n其他限制:\n“如：`不要口水歌`、`不要人聲`、`只要 Remix`；可以不填”\n\n\u0060\u0060\u0060markdown\n場景:\n目標國家 / 地區:\n核心聲音方向:\n歌曲數量或 Set 時長:\n輸出版本:\n其他限制:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "【第二輪：需求細化】",
      "rules": [
        "1. 可以從例子中複製，也可以自由填寫或不填"
      ],
      "fields": [
        {
          "key": "style",
          "label": "具體風格",
          "example": "如：`House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "速度 / BPM",
          "example": "如：`105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "熟悉度與發現感",
          "example": "`熱門熟悉` / `平衡` / `小眾發現`"
        },
        {
          "key": "era_classic",
          "label": "時代與經典",
          "example": "`當代為主` / `少量經典錨點` / `新舊橋接` / `經典優先`"
        },
        {
          "key": "mood",
          "label": "情緒",
          "example": "如：`懷舊` / `陰冷` / `浪漫`"
        },
        {
          "key": "energy",
          "label": "SET 能量級或能量走勢",
          "example": "如：`低`/`高`；`平穩` / `過山車`"
        },
        {
          "key": "platform",
          "label": "平台與連結要求",
          "example": "如：`網易雲` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`；填寫一個平台時只使用該平台，填寫多個平台按先後順序優先"
        },
        {
          "key": "other",
          "label": "其他",
          "example": ""
        }
      ],
      "prompt": "【第二輪：需求細化】\n\n具體風格:\n“如：`House` / `Bass` / `Garage` / `Techno` / `Breakbeat`”\n速度 / BPM:\n“如：`105` / `128` / `140` / `150` / `170`”\n熟悉度與發現感:\n“`熱門熟悉` / `平衡` / `小眾發現`”\n時代與經典:\n“`當代為主` / `少量經典錨點` / `新舊橋接` / `經典優先`”\n情緒:\n“如：`懷舊` / `陰冷` / `浪漫`”\nSET 能量級或能量走勢:\n“如：`低`/`高`；`平穩` / `過山車`”\n平台與連結要求:\n“如：`網易雲` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`；填寫一個平台時只使用該平台，填寫多個平台按先後順序優先”\n其他:\n\n\u0060\u0060\u0060markdown\n具體風格:\n速度 / BPM:\n熟悉度與發現感:\n時代與經典:\n情緒:\nSET 能量級或能量走勢:\n平台與連結要求:\n其他:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# 極速版",
      "first_batch_title": "# 極速版首批",
      "final_title": "# 極速版",
      "columns": [
        "歌名",
        "歌手",
        "連結"
      ],
      "next_steps": [
        {
          "label": "第一｜回饋選歌情況",
          "body": "如果願意，您可以用自然語言回覆選歌情況，這會豐富您的私人選歌偏好，讓推薦更準。回覆包括但不限於「`skream的歌不錯，但我這次因為客群的關係沒放`/`我不喜歡跳樓機，以後別再推了`/`我這次播放了這些歌（配圖/表）`」"
        },
        {
          "label": "第二｜輸出或交接歌單",
          "body": "您可以輸出文字版歌單或交接給 W4DJ，直接回覆 `交接到 W4DJ` 或 `輸出文字版歌單` 即可。\n\nW4DJ 的功能是一鍵導入歌單、下載後一鍵轉換格式，並一鍵導入打碟軟體；請輸出 `.w4dj` 格式並下載 [w4dj-rkb](https://github.com/komakizhu/W4DJ-RKB)。具體操作教程可以查看 [一鍵導入 Set 教程](https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.md)。\n\n`輸出文字版歌單` 的功能是輸出可複製文字，可以手動導入網易雲，但無法幫您一鍵把歌曲導入 RKB。"
        }
      ],
      "digging_notes": "選歌碎碎念",
      "mix_suggestion": "接歌建議",
      "unknown": "未知",
      "verified": "已核驗",
      "target_platform_missing": "目標平台缺失"
    },
    "brief": {
      "title": "# 簡要版",
      "first_batch_title": "# 簡要版",
      "final_title": "# 簡要版",
      "columns": [
        "歌名",
        "藝人",
        "專輯/EP",
        "風格",
        "BPM",
        "調性",
        "歌曲時長",
        "能量級",
        "發行時間",
        "簡介",
        "選擇原因",
        "連結"
      ],
      "next_steps": [
        {
          "label": "第一｜回饋選歌情況",
          "body": "如果願意，您可以用自然語言回覆選歌情況，這會豐富您的私人選歌偏好，讓推薦更準。回覆包括但不限於「`skream的歌不錯，但我這次因為客群的關係沒放`/`我不喜歡跳樓機，以後別再推了`/`我這次播放了這些歌（配圖/表）`」"
        },
        {
          "label": "第二｜輸出或交接歌單",
          "body": "您可以輸出文字版歌單或交接給 W4DJ，直接回覆 `交接到 W4DJ` 或 `輸出文字版歌單` 即可。\n\nW4DJ 的功能是一鍵導入歌單、下載後一鍵轉換格式，並一鍵導入打碟軟體；請輸出 `.w4dj` 格式並下載 [w4dj-rkb](https://github.com/komakizhu/W4DJ-RKB)。具體操作教程可以查看 [一鍵導入 Set 教程](https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.md)。\n\n`輸出文字版歌單` 的功能是輸出可複製文字，可以手動導入網易雲，但無法幫您一鍵把歌曲導入 RKB。"
        },
        {
          "label": "第三｜五度圈排序",
          "body": "需要我根據五度圈原則幫您排列 set 順序嗎？"
        }
      ],
      "digging_notes": "選歌碎碎念",
      "mix_suggestion": "接歌建議",
      "unknown": "未知",
      "verified": "已核驗",
      "target_platform_missing": "目標平台缺失"
    },
    "rich": {
      "title": "# 豐富版",
      "first_batch_title": "# 豐富版",
      "final_title": "# 豐富版",
      "columns": [
        "歌名",
        "藝人",
        "專輯/EP",
        "風格",
        "BPM",
        "調性",
        "歌曲時長",
        "能量級",
        "發行時間",
        "簡介",
        "選擇原因",
        "連結"
      ],
      "next_steps": [
        {
          "label": "第一｜回饋選歌情況",
          "body": "如果願意，您可以用自然語言回覆選歌情況，這會豐富您的私人選歌偏好，讓推薦更準。回覆包括但不限於「`skream的歌不錯，但我這次因為客群的關係沒放`/`我不喜歡跳樓機，以後別再推了`/`我這次播放了這些歌（配圖/表）`」"
        },
        {
          "label": "第二｜輸出或交接歌單",
          "body": "您可以輸出文字版歌單或交接給 W4DJ，直接回覆 `交接到 W4DJ` 或 `輸出文字版歌單` 即可。\n\nW4DJ 的功能是一鍵導入歌單、下載後一鍵轉換格式，並一鍵導入打碟軟體；請輸出 `.w4dj` 格式並下載 [w4dj-rkb](https://github.com/komakizhu/W4DJ-RKB)。具體操作教程可以查看 [一鍵導入 Set 教程](https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.md)。\n\n`輸出文字版歌單` 的功能是輸出可複製文字，可以手動導入網易雲，但無法幫您一鍵把歌曲導入 RKB。"
        },
        {
          "label": "第三｜五度圈排序",
          "body": "需要我根據五度圈原則幫您排列 set 順序嗎？"
        }
      ],
      "digging_notes": "選歌碎碎念",
      "mix_suggestion": "接歌建議",
      "unknown": "未知",
      "verified": "已核驗",
      "target_platform_missing": "目標平台缺失",
      "view_titles": [
        "風格視角",
        "場景視角",
        "熟悉度與發現感視角",
        "動態綜合視角"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "回饋選歌情況",
      "positive": [
        "我喜歡這首歌"
      ],
      "negative": [
        "我不喜歡這首歌"
      ],
      "ambiguous": [
        "我不確定這首歌"
      ]
    },
    "export_w4dj": {
      "label": "交接給 W4DJ",
      "positive": [
        "交接到 W4DJ"
      ],
      "negative": [
        "不要交接到 W4DJ"
      ],
      "ambiguous": [
        "也許交接到 W4DJ"
      ]
    },
    "output_text_playlist": {
      "label": "輸出文字版歌單",
      "positive": [
        "輸出文字版歌單"
      ],
      "negative": [
        "不要輸出文字版歌單"
      ],
      "ambiguous": [
        "也許輸出文字版歌單"
      ]
    },
    "harmonic_reorder": {
      "label": "五度圈排序",
      "positive": [
        "按五度圈原則排列"
      ],
      "negative": [
        "不要重排"
      ],
      "ambiguous": [
        "也許按五度圈原則排列"
      ]
    },
    "confirm_long_term_memory": {
      "label": "確認長期記憶",
      "positive": [
        "記住這個偏好"
      ],
      "negative": [
        "不要保存這個偏好"
      ],
      "ambiguous": [
        "也許記住這個偏好"
      ]
    }
  },
  "platform_policy": {
    "aliases": {
      "spotify": "Spotify",
      "apple_music": "Apple Music",
      "soundcloud": "SoundCloud",
      "netease_cloud_music": "網易雲",
      "bandcamp": "Bandcamp",
      "beatport": "Beatport",
      "beatsource": "Beatsource"
    },
    "exclusive_markers": [
      "唯一平台",
      "僅限",
      "只使用",
      "只在",
      "只要",
      "僅接受"
    ],
    "preferred_markers": [
      "優先",
      "最好有",
      "首選"
    ],
    "fallback_markers": [
      "備用",
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
    "verified": "已核驗",
    "target_platform_missing": "目標平台缺失"
  },
  "export": {
    "text": "輸出目前順序的可複製文字版歌單。",
    "w4dj": "生成交給 W4DJ 的 UTF-8 `.w4dj` 交接檔。",
    "harmonic": "根據已知調性請求按五度圈原則排序。",
    "feedback": "自然語言回饋只更新目前會話；長期保存必須先確認。",
    "memory_confirmation": "我理解這是一段簡短的品味變化摘要。是否保存到私人長期檔案？"
  },
  "trigger_capsule": [
    "挖歌",
    "排set",
    "排一套set",
    "找歌單",
    "排歌"
  ]
}
```
