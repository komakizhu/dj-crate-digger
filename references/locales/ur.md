# Urdu locale pack

This file is the fixed اردو UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "ur",
  "language_name": "Urdu",
  "native_name": "اردو",
  "direction": "rtl",
  "market_policy": {
    "language_independent": true,
    "blank_region": "اگر خطہ خالی ہو تو اس session کے لیے صرف ایک وسیع اردو بولنے والی مارکیٹ استعمال کریں۔",
    "explicit_region": "واضح ملک یا خطہ زبان کے اندازے پر مقدم ہے، مگر رابطے کی زبان نہیں بدلتا۔",
    "persistence": "ہدف مارکیٹ کو طویل مدتی ترجیح کے طور پر محفوظ نہ کریں۔"
  },
  "quick_start": {
    "intro": "DJ انتخاب معاون میں خوش آمدید۔ یہ Agent Skill آپ کو DJ set تیار کرنے میں مدد دیتا ہے۔ آپ دو مرحلوں میں اپنی ضرورت کی تصدیق کریں گے اور tracks کی تجاویز پائیں گے۔ پُر کرنے کے اصول:",
    "tutorial_label": "ایک کلک سے Set import کرنے کی رہنما",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[پہلا مرحلہ: ضروری معلومات]",
      "rules": [
        "1. آپ مثال نقل کر سکتے ہیں، آزادانہ لکھ سکتے ہیں یا خانہ خالی چھوڑ سکتے ہیں",
        "2. خانہ خالی چھوڑنے کا مطلب ہے کہ AI اشاروں سے جواب سمجھ لے گا"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "پس منظر",
          "example": "پرفارمنس کا context۔ مثال: `bar` / `club` / `wedding` / `art exhibition`"
        },
        {
          "key": "target_market",
          "label": "ہدف ملک / خطہ",
          "example": "مثال: `Mainland China` / `Taiwan` / `Hong Kong` / `Japan` / `international English market`"
        },
        {
          "key": "core_sound",
          "label": "بنیادی صوتی سمت",
          "example": "حوالہ فنکار، track اور genre۔ مثال: `Skrillex` کا `Tears`، جدید `UK Bass`"
        },
        {
          "key": "track_count_or_duration",
          "label": "tracks کی تعداد یا set کا دورانیہ",
          "example": "مثال: `20 tracks` / `60 minutes`"
        },
        {
          "key": "output_mode",
          "label": "آؤٹ پٹ ورژن",
          "example": "Fast / Brief / Rich کا انتخاب"
        },
        {
          "key": "other",
          "label": "دیگر پابندیاں",
          "example": "مثال: `بہت زیادہ بجے tracks نہیں`، `vocal نہیں`، `صرف Remix`؛ اختیاری"
        }
      ],
      "prompt": "DJ انتخاب معاون میں خوش آمدید۔ یہ Agent Skill آپ کو DJ set تیار کرنے میں مدد دیتا ہے۔ آپ دو مرحلوں میں اپنی ضرورت کی تصدیق کریں گے اور tracks کی تجاویز پائیں گے۔ پُر کرنے کے اصول:\n\n1. آپ مثال نقل کر سکتے ہیں، آزادانہ لکھ سکتے ہیں یا خانہ خالی چھوڑ سکتے ہیں\n2. خانہ خالی چھوڑنے کا مطلب ہے کہ AI اشاروں سے جواب سمجھ لے گا\n\n[پہلا مرحلہ: ضروری معلومات]\n\nپس منظر:\n«پرفارمنس کا context۔ مثال: `bar` / `club` / `wedding` / `art exhibition`»\nہدف ملک / خطہ:\n«مثال: `Mainland China` / `Taiwan` / `Hong Kong` / `Japan` / `international English market`»\nبنیادی صوتی سمت:\n«حوالہ فنکار، track اور genre۔ مثال: `Skrillex` کا `Tears`، جدید `UK Bass`»\ntracks کی تعداد یا set کا دورانیہ:\n«مثال: `20 tracks` / `60 minutes`»\nآؤٹ پٹ ورژن:\n«`Fast`: تیز playlist؛ معیار کم ہو سکتا ہے»\n«`Brief`: صرف ایک مشترکہ playlist»\n«`Rich`: style، context اور discovery کے الگ زاویے، پھر آخری مشترکہ playlist»\nدیگر پابندیاں:\n«مثال: `بہت زیادہ بجے tracks نہیں`، `vocal نہیں`، `صرف Remix`؛ اختیاری»\n\n\u0060\u0060\u0060markdown\nپس منظر:\nہدف ملک / خطہ:\nبنیادی صوتی سمت:\ntracks کی تعداد یا set کا دورانیہ:\nآؤٹ پٹ ورژن:\nدیگر پابندیاں:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[دوسرا مرحلہ: درخواست کی تفصیل]",
      "rules": [
        "1. آپ مثال نقل کر سکتے ہیں، آزادانہ لکھ سکتے ہیں یا خانہ خالی چھوڑ سکتے ہیں"
      ],
      "fields": [
        {
          "key": "style",
          "label": "مخصوص style",
          "example": "مثال: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "رفتار / BPM",
          "example": "مثال: `105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "واقفیت اور discovery",
          "example": "`واقف` / `متوازن` / `دریافت`"
        },
        {
          "key": "era_classic",
          "label": "دور اور classics",
          "example": "`عصری` / `چند classic anchors` / `نئے اور پرانے کا پل` / `classics پہلے`"
        },
        {
          "key": "mood",
          "label": "مزاج",
          "example": "مثال: `nostalgic` / `سرد` / `رومانوی`"
        },
        {
          "key": "energy",
          "label": "SET کی energy level یا curve",
          "example": "مثال: `کم` / `زیادہ`؛ `مستحکم` / `roller coaster`"
        },
        {
          "key": "platform",
          "label": "platform اور link کی ضروریات",
          "example": "مثال: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`؛ ایک platform ہو تو صرف وہ، کئی ہوں تو دی گئی ترجیح"
        },
        {
          "key": "other",
          "label": "دیگر",
          "example": ""
        }
      ],
      "prompt": "[دوسرا مرحلہ: درخواست کی تفصیل]\n\nمخصوص style:\n«مثال: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`»\nرفتار / BPM:\n«مثال: `105` / `128` / `140` / `150` / `170`»\nواقفیت اور discovery:\n«`واقف` / `متوازن` / `دریافت`»\nدور اور classics:\n«`عصری` / `چند classic anchors` / `نئے اور پرانے کا پل` / `classics پہلے`»\nمزاج:\n«مثال: `nostalgic` / `سرد` / `رومانوی`»\nSET کی energy level یا curve:\n«مثال: `کم` / `زیادہ`؛ `مستحکم` / `roller coaster`»\nplatform اور link کی ضروریات:\n«مثال: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`؛ ایک platform ہو تو صرف وہ، کئی ہوں تو دی گئی ترجیح»\nدیگر:\n\n\u0060\u0060\u0060markdown\nمخصوص style:\nرفتار / BPM:\nواقفیت اور discovery:\nدور اور classics:\nمزاج:\nSET کی energy level یا curve:\nplatform اور link کی ضروریات:\nدیگر:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# Fast mode",
      "first_batch_title": "# Fast کی پہلی کھیپ",
      "final_title": "# Fast mode",
      "columns": [
        "Track",
        "فنکار",
        "Link"
      ],
      "next_steps": [
        {
          "label": "اول | انتخاب پر رائے",
          "body": "اگر چاہیں تو قدرتی زبان میں بتائیں کہ انتخاب کیسا رہا۔ اس سے نجی ترجیحات اور اگلی تجاویز بہتر ہوں گی۔"
        },
        {
          "label": "دوم | playlist export یا حوالگی",
          "body": "Text playlist نکال سکتے ہیں یا W4DJ کو دے سکتے ہیں۔ `output text playlist` یا `export to w4dj` جواب دیں۔"
        }
      ],
      "digging_notes": "Digging نوٹس",
      "mix_suggestion": "Mix تجویز",
      "unknown": "نامعلوم",
      "verified": "تصدیق شدہ",
      "target_platform_missing": "ہدف platform دستیاب نہیں"
    },
    "brief": {
      "title": "# Brief mode",
      "first_batch_title": "# Brief mode",
      "final_title": "# Brief mode",
      "columns": [
        "Track",
        "فنکار",
        "Album / EP",
        "Style",
        "BPM",
        "Key",
        "دورانیہ",
        "Energy",
        "ریلیز تاریخ",
        "نوٹس",
        "انتخاب کی وجہ",
        "Link"
      ],
      "next_steps": [
        {
          "label": "اول | انتخاب پر رائے",
          "body": "اگر چاہیں تو قدرتی زبان میں بتائیں کہ انتخاب کیسا رہا۔ اس سے نجی ترجیحات اور اگلی تجاویز بہتر ہوں گی۔"
        },
        {
          "label": "دوم | playlist export یا حوالگی",
          "body": "Text playlist نکال سکتے ہیں یا W4DJ کو دے سکتے ہیں۔ `output text playlist` یا `export to w4dj` جواب دیں۔"
        },
        {
          "label": "سوم | Harmonic set order",
          "body": "کیا Camelot wheel سے set ترتیب دوں؟"
        }
      ],
      "digging_notes": "Digging نوٹس",
      "mix_suggestion": "Mix تجویز",
      "unknown": "نامعلوم",
      "verified": "تصدیق شدہ",
      "target_platform_missing": "ہدف platform دستیاب نہیں"
    },
    "rich": {
      "title": "# Rich mode",
      "first_batch_title": "# Rich mode",
      "final_title": "# Rich mode",
      "columns": [
        "Track",
        "فنکار",
        "Album / EP",
        "Style",
        "BPM",
        "Key",
        "دورانیہ",
        "Energy",
        "ریلیز تاریخ",
        "نوٹس",
        "انتخاب کی وجہ",
        "Link"
      ],
      "next_steps": [
        {
          "label": "اول | انتخاب پر رائے",
          "body": "اگر چاہیں تو قدرتی زبان میں بتائیں کہ انتخاب کیسا رہا۔ اس سے نجی ترجیحات اور اگلی تجاویز بہتر ہوں گی۔"
        },
        {
          "label": "دوم | playlist export یا حوالگی",
          "body": "Text playlist نکال سکتے ہیں یا W4DJ کو دے سکتے ہیں۔ `output text playlist` یا `export to w4dj` جواب دیں۔"
        },
        {
          "label": "سوم | Harmonic set order",
          "body": "کیا Camelot wheel سے set ترتیب دوں؟"
        }
      ],
      "digging_notes": "Digging نوٹس",
      "mix_suggestion": "Mix تجویز",
      "unknown": "نامعلوم",
      "verified": "تصدیق شدہ",
      "target_platform_missing": "ہدف platform دستیاب نہیں",
      "view_titles": [
        "Style view",
        "Context view",
        "واقفیت / discovery view",
        "Dynamic combined view"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "انتخاب پر رائے",
      "positive": [
        "مجھے یہ track پسند ہے"
      ],
      "negative": [
        "مجھے یہ track پسند نہیں"
      ],
      "ambiguous": [
        "اس track کے بارے میں یقین نہیں"
      ]
    },
    "export_w4dj": {
      "label": "W4DJ کو export",
      "positive": [
        "W4DJ کو export کریں"
      ],
      "negative": [
        "W4DJ کو export نہ کریں"
      ],
      "ambiguous": [
        "شاید W4DJ کو export کریں"
      ]
    },
    "output_text_playlist": {
      "label": "Text playlist نکالیں",
      "positive": [
        "Text playlist نکالیں"
      ],
      "negative": [
        "Text playlist نہ نکالیں"
      ],
      "ambiguous": [
        "شاید text playlist نکالیں"
      ]
    },
    "harmonic_reorder": {
      "label": "Harmonic reorder",
      "positive": [
        "Camelot wheel کے مطابق ترتیب دیں"
      ],
      "negative": [
        "دوبارہ ترتیب نہ دیں"
      ],
      "ambiguous": [
        "شاید Camelot wheel کے مطابق ترتیب دیں"
      ]
    },
    "confirm_long_term_memory": {
      "label": "طویل مدتی memory کی تصدیق",
      "positive": [
        "یہ ترجیح یاد رکھیں"
      ],
      "negative": [
        "یہ ترجیح محفوظ نہ کریں"
      ],
      "ambiguous": [
        "شاید یہ ترجیح یاد رکھیں"
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
      "صرف",
      "واحد",
      "صرف استعمال کریں"
    ],
    "preferred_markers": [
      "ترجیح",
      "پسندیدہ",
      "اولویت"
    ],
    "fallback_markers": [
      "متبادل",
      "backup",
      "اگر دستیاب نہ ہو"
    ],
    "forbidden_markers": [
      "استعمال نہ کریں",
      "خارج کریں",
      "بغیر"
    ]
  },
  "status": {
    "unknown": "نامعلوم",
    "verified": "تصدیق شدہ",
    "target_platform_missing": "ہدف platform دستیاب نہیں"
  },
  "export": {
    "text": "موجودہ ترتیب میں copy ہونے والی text playlist نکالیں۔",
    "w4dj": "W4DJ کے لیے UTF-8 `.w4dj` handoff file بنائیں۔",
    "harmonic": "معلوم keys سے Camelot wheel ترتیب کی درخواست کریں۔",
    "feedback": "قدرتی زبان کی رائے صرف session اپڈیٹ کرتی ہے؛ طویل مدتی محفوظ کرنے کے لیے تصدیق ضروری ہے۔",
    "memory_confirmation": "میں نے اسے ذوق میں تبدیلی کے مختصر خلاصے کے طور پر سمجھا ہے۔ نجی طویل مدتی profile میں محفوظ کروں؟"
  },
  "trigger_capsule": [
    "DJ سیٹ",
    "پلے لسٹ",
    "موسیقی تلاش",
    "ٹریک تلاش",
    "سیٹ ترتیب",
    "تیز موڈ",
    "مختصر موڈ",
    "مکمل موڈ",
    "DJ سیٹ بنانا",
    "DJ",
    "house",
    "techno",
    "drum & bass",
    "jungle"
  ],
  "trigger_contract": {
    "path": "references/trigger-signals.json",
    "version": 1
  },
  "trigger_signal_families": [
    "mode",
    "dj_action",
    "dj_object",
    "dj_context",
    "reference",
    "set_detail",
    "genre_context",
    "generic_music_term",
    "negative_context",
    "explanatory_context",
    "genre_families"
  ]
}
```
