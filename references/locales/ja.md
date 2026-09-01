# Japanese locale pack

This file is the fixed 日本語 UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "ja",
  "language_name": "Japanese",
  "native_name": "日本語",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "地域が空欄なら、このセッションでは広い日本語圏市場だけを仮定します。",
    "explicit_region": "明示された国や地域は言語推定より優先しますが、会話言語は変えません。",
    "persistence": "対象市場は長期の好みとして保存しません。"
  },
  "quick_start": {
    "intro": "DJ 選曲アシスタントへようこそ。この Agent Skill は DJ セット作成を支援します。2 回のラウンドで要件を確認し、トラック候補を提案します。入力ルール：",
    "tutorial_label": "ワンクリック Set インポート手順",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "【第1ラウンド：必要情報】",
      "rules": [
        "1. 例からコピーしても、自由に入力しても、空欄にしてもかまいません",
        "2. 空欄は AI が手がかりから回答を賢く判断することを意味します"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "シーン",
          "example": "演奏の場面。例：`バー` / `クラブ` / `結婚式` / `アート展示`"
        },
        {
          "key": "target_market",
          "label": "対象国 / 地域",
          "example": "例：`中国大陸` / `台湾` / `香港` / `日本` / `英語圏の国際市場`"
        },
        {
          "key": "core_sound",
          "label": "中心となるサウンド",
          "example": "参考アーティスト、曲、ジャンル。例：`Skrillex` の `Tears`、現代的な `UK Bass`"
        },
        {
          "key": "track_count_or_duration",
          "label": "曲数またはセット時間",
          "example": "例：`20 曲` / `60 分`"
        },
        {
          "key": "output_mode",
          "label": "出力バージョン",
          "example": "Fast / Brief / Rich の選択"
        },
        {
          "key": "other",
          "label": "その他の制約",
          "example": "例：`定番すぎる曲は避ける`、`ボーカルなし`、`Remix のみ`。任意"
        }
      ],
      "prompt": "DJ 選曲アシスタントへようこそ。この Agent Skill は DJ セット作成を支援します。2 回のラウンドで要件を確認し、トラック候補を提案します。入力ルール：\n\n1. 例からコピーしても、自由に入力しても、空欄にしてもかまいません\n2. 空欄は AI が手がかりから回答を賢く判断することを意味します\n\n【第1ラウンド：必要情報】\n\nシーン:\n「演奏の場面。例：`バー` / `クラブ` / `結婚式` / `アート展示`」\n対象国 / 地域:\n「例：`中国大陸` / `台湾` / `香港` / `日本` / `英語圏の国際市場`」\n中心となるサウンド:\n「参考アーティスト、曲、ジャンル。例：`Skrillex` の `Tears`、現代的な `UK Bass`」\n曲数またはセット時間:\n「例：`20 曲` / `60 分`」\n出力バージョン:\n「`Fast`：高速出力。品質が下がる場合があります」\n「`Brief`：統合 playlist のみ」\n「`Rich`：スタイル、シーン、親しみやすさ／発見の各視点と、最後に統合 playlist を出力」\nその他の制約:\n「例：`定番すぎる曲は避ける`、`ボーカルなし`、`Remix のみ`。任意」\n\n\u0060\u0060\u0060markdown\nシーン:\n対象国 / 地域:\n中心となるサウンド:\n曲数またはセット時間:\n出力バージョン:\nその他の制約:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "【第2ラウンド：要件の詳細化】",
      "rules": [
        "1. 例からコピーしても、自由に入力しても、空欄にしてもかまいません"
      ],
      "fields": [
        {
          "key": "style",
          "label": "具体的なスタイル",
          "example": "例：`House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "速度 / BPM",
          "example": "例：`105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "親しみやすさと発見",
          "example": "`親しみやすい` / `バランス` / `発見`"
        },
        {
          "key": "era_classic",
          "label": "時代とクラシック",
          "example": "`現代中心` / `少数のクラシック軸` / `新旧の橋渡し` / `クラシック優先`"
        },
        {
          "key": "mood",
          "label": "ムード",
          "example": "例：`ノスタルジック` / `冷たい` / `ロマンチック`"
        },
        {
          "key": "energy",
          "label": "SET のエネルギーまたは推移",
          "example": "例：`低` / `高`；`安定` / `ジェットコースター`"
        },
        {
          "key": "platform",
          "label": "プラットフォームとリンク要件",
          "example": "例：`NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`。1 つならそれだけ、複数なら記載順を優先"
        },
        {
          "key": "other",
          "label": "その他",
          "example": ""
        }
      ],
      "prompt": "【第2ラウンド：要件の詳細化】\n\n具体的なスタイル:\n「例：`House` / `Bass` / `Garage` / `Techno` / `Breakbeat`」\n速度 / BPM:\n「例：`105` / `128` / `140` / `150` / `170`」\n親しみやすさと発見:\n「`親しみやすい` / `バランス` / `発見`」\n時代とクラシック:\n「`現代中心` / `少数のクラシック軸` / `新旧の橋渡し` / `クラシック優先`」\nムード:\n「例：`ノスタルジック` / `冷たい` / `ロマンチック`」\nSET のエネルギーまたは推移:\n「例：`低` / `高`；`安定` / `ジェットコースター`」\nプラットフォームとリンク要件:\n「例：`NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`。1 つならそれだけ、複数なら記載順を優先」\nその他:\n\n\u0060\u0060\u0060markdown\n具体的なスタイル:\n速度 / BPM:\n親しみやすさと発見:\n時代とクラシック:\nムード:\nSET のエネルギーまたは推移:\nプラットフォームとリンク要件:\nその他:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# Fast モード",
      "first_batch_title": "# Fast モード（初回分）",
      "final_title": "# Fast モード",
      "columns": [
        "曲名",
        "アーティスト",
        "リンク"
      ],
      "next_steps": [
        {
          "label": "第一｜選曲フィードバック",
          "body": "よければ、選曲がどう機能したかを自然な言葉で返信してください。個人の選曲傾向と次の推薦がより正確になります。"
        },
        {
          "label": "第二｜playlist の出力または W4DJ への引き継ぎ",
          "body": "テキスト playlist を出力するか、W4DJ に引き継げます。`output text playlist` または `export to w4dj` と返信してください。"
        }
      ],
      "digging_notes": "Digging メモ",
      "mix_suggestion": "ミックス提案",
      "unknown": "不明",
      "verified": "検証済み",
      "target_platform_missing": "対象プラットフォームなし"
    },
    "brief": {
      "title": "# Brief モード",
      "first_batch_title": "# Brief モード",
      "final_title": "# Brief モード",
      "columns": [
        "曲名",
        "アーティスト",
        "アルバム / EP",
        "スタイル",
        "BPM",
        "キー",
        "長さ",
        "エネルギー",
        "リリース日",
        "メモ",
        "選曲理由",
        "リンク"
      ],
      "next_steps": [
        {
          "label": "第一｜選曲フィードバック",
          "body": "よければ、選曲がどう機能したかを自然な言葉で返信してください。個人の選曲傾向と次の推薦がより正確になります。"
        },
        {
          "label": "第二｜playlist の出力または W4DJ への引き継ぎ",
          "body": "テキスト playlist を出力するか、W4DJ に引き継げます。`output text playlist` または `export to w4dj` と返信してください。"
        },
        {
          "label": "第三｜ハーモニックなセット順",
          "body": "Camelot ホイールを使ってセットを並べ替えますか？"
        }
      ],
      "digging_notes": "Digging メモ",
      "mix_suggestion": "ミックス提案",
      "unknown": "不明",
      "verified": "検証済み",
      "target_platform_missing": "対象プラットフォームなし"
    },
    "rich": {
      "title": "# Rich モード",
      "first_batch_title": "# Rich モード",
      "final_title": "# Rich モード",
      "columns": [
        "曲名",
        "アーティスト",
        "アルバム / EP",
        "スタイル",
        "BPM",
        "キー",
        "長さ",
        "エネルギー",
        "リリース日",
        "メモ",
        "選曲理由",
        "リンク"
      ],
      "next_steps": [
        {
          "label": "第一｜選曲フィードバック",
          "body": "よければ、選曲がどう機能したかを自然な言葉で返信してください。個人の選曲傾向と次の推薦がより正確になります。"
        },
        {
          "label": "第二｜playlist の出力または W4DJ への引き継ぎ",
          "body": "テキスト playlist を出力するか、W4DJ に引き継げます。`output text playlist` または `export to w4dj` と返信してください。"
        },
        {
          "label": "第三｜ハーモニックなセット順",
          "body": "Camelot ホイールを使ってセットを並べ替えますか？"
        }
      ],
      "digging_notes": "Digging メモ",
      "mix_suggestion": "ミックス提案",
      "unknown": "不明",
      "verified": "検証済み",
      "target_platform_missing": "対象プラットフォームなし",
      "view_titles": [
        "スタイル視点",
        "シーン視点",
        "親しみやすさ／発見視点",
        "動的な統合視点"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "選曲フィードバック",
      "positive": [
        "この曲が好きです"
      ],
      "negative": [
        "この曲は好きではありません"
      ],
      "ambiguous": [
        "この曲はまだ判断できません"
      ]
    },
    "export_w4dj": {
      "label": "W4DJ に書き出す",
      "positive": [
        "W4DJ に書き出す"
      ],
      "negative": [
        "W4DJ に書き出さない"
      ],
      "ambiguous": [
        "W4DJ に書き出すかもしれません"
      ]
    },
    "output_text_playlist": {
      "label": "テキスト playlist を出力",
      "positive": [
        "テキスト playlist を出力する"
      ],
      "negative": [
        "テキスト playlist を出力しない"
      ],
      "ambiguous": [
        "テキスト playlist を出力するかもしれません"
      ]
    },
    "harmonic_reorder": {
      "label": "ハーモニック並べ替え",
      "positive": [
        "Camelot ホイールで並べる"
      ],
      "negative": [
        "並べ替えない"
      ],
      "ambiguous": [
        "Camelot ホイールで並べるかもしれません"
      ]
    },
    "confirm_long_term_memory": {
      "label": "長期記憶を確認",
      "positive": [
        "この好みを記憶する"
      ],
      "negative": [
        "この好みを保存しない"
      ],
      "ambiguous": [
        "この好みを記憶するかもしれません"
      ]
    }
  },
  "platform_policy": {
    "aliases": {
      "spotify": "Spotify",
      "apple_music": "Apple Music",
      "soundcloud": "SoundCloud",
      "netease_cloud_music": "NetEase Cloud Music",
      "bandcamp": "Bandcamp",
      "beatport": "Beatport",
      "beatsource": "Beatsource"
    },
    "exclusive_markers": [
      "のみ",
      "だけ",
      "のみ使用"
    ],
    "preferred_markers": [
      "優先",
      "希望",
      "優先順位"
    ],
    "fallback_markers": [
      "代替",
      "予備",
      "利用できない場合"
    ],
    "forbidden_markers": [
      "使わない",
      "除外",
      "なし"
    ]
  },
  "status": {
    "unknown": "不明",
    "verified": "検証済み",
    "target_platform_missing": "対象プラットフォームなし"
  },
  "export": {
    "text": "現在の順序でコピー可能なテキスト playlist を出力します。",
    "w4dj": "W4DJ に渡す UTF-8 `.w4dj` 引き継ぎファイルを作成します。",
    "harmonic": "判明しているキーで Camelot ホイール順を依頼します。",
    "feedback": "自然言語のフィードバックは現在のセッションだけを更新し、長期保存には確認が必要です。",
    "memory_confirmation": "これは好みの変化をまとめた短い要約だと理解しました。個人の長期プロフィールに保存しますか？"
  },
  "trigger_capsule": [
    "DJセット",
    "プレイリスト",
    "曲探し",
    "トラックを探す",
    "セットを組む"
  ]
}
```
