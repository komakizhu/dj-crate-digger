# Bengali locale pack

This file is the fixed বাংলা UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "bn",
  "language_name": "Bengali",
  "native_name": "বাংলা",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "অঞ্চল ফাঁকা থাকলে এই session-এ কেবল বিস্তৃত বাংলা ভাষার বাজার ব্যবহার করুন।",
    "explicit_region": "স্পষ্ট দেশ বা অঞ্চল ভাষা থেকে অনুমানের চেয়ে অগ্রাধিকার পায়, যোগাযোগের ভাষা বদলায় না।",
    "persistence": "লক্ষ্য বাজারকে দীর্ঘমেয়াদি পছন্দ হিসেবে সংরক্ষণ করবেন না।"
  },
  "quick_start": {
    "intro": "DJ নির্বাচন সহায়কে স্বাগতম। এই Agent Skill আপনাকে একটি DJ set তৈরি করতে সাহায্য করে। দুই ধাপে আপনার প্রয়োজন নিশ্চিত করে track-এর পরামর্শ পাবেন। পূরণের নিয়ম:",
    "tutorial_label": "এক ক্লিকে Set import নির্দেশিকা",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[প্রথম ধাপ: প্রয়োজনীয় তথ্য]",
      "rules": [
        "1. উদাহরণ কপি করতে, নিজের মতো লিখতে বা ফাঁকা রাখতে পারেন",
        "2. ফাঁকা রাখলে AI ইঙ্গিত থেকে উত্তরটি বুদ্ধিমত্তার সঙ্গে নির্ধারণ করবে"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "পরিস্থিতি",
          "example": "পারফরম্যান্সের পরিবেশ। উদাহরণ: `bar` / `club` / `wedding` / `art exhibition`"
        },
        {
          "key": "target_market",
          "label": "লক্ষ্য দেশ / অঞ্চল",
          "example": "উদাহরণ: `Mainland China` / `Taiwan` / `Hong Kong` / `Japan` / `international English market`"
        },
        {
          "key": "core_sound",
          "label": "মূল সাউন্ডের দিক",
          "example": "রেফারেন্স শিল্পী, track ও genre। উদাহরণ: `Skrillex`-এর `Tears`, আধুনিক `UK Bass`"
        },
        {
          "key": "track_count_or_duration",
          "label": "track সংখ্যা বা set-এর সময়",
          "example": "উদাহরণ: `20 tracks` / `60 minutes`"
        },
        {
          "key": "output_mode",
          "label": "আউটপুট সংস্করণ",
          "example": "Fast / Brief / Rich বেছে নিন"
        },
        {
          "key": "other",
          "label": "অন্যান্য সীমা",
          "example": "উদাহরণ: `খুব বেশি বাজানো track এড়ান`, `vocal নয়`, `শুধু Remix`; ঐচ্ছিক"
        }
      ],
      "prompt": "DJ নির্বাচন সহায়কে স্বাগতম। এই Agent Skill আপনাকে একটি DJ set তৈরি করতে সাহায্য করে। দুই ধাপে আপনার প্রয়োজন নিশ্চিত করে track-এর পরামর্শ পাবেন। পূরণের নিয়ম:\n\n1. উদাহরণ কপি করতে, নিজের মতো লিখতে বা ফাঁকা রাখতে পারেন\n2. ফাঁকা রাখলে AI ইঙ্গিত থেকে উত্তরটি বুদ্ধিমত্তার সঙ্গে নির্ধারণ করবে\n\n[প্রথম ধাপ: প্রয়োজনীয় তথ্য]\n\nপরিস্থিতি:\n“পারফরম্যান্সের পরিবেশ। উদাহরণ: `bar` / `club` / `wedding` / `art exhibition`”\nলক্ষ্য দেশ / অঞ্চল:\n“উদাহরণ: `Mainland China` / `Taiwan` / `Hong Kong` / `Japan` / `international English market`”\nমূল সাউন্ডের দিক:\n“রেফারেন্স শিল্পী, track ও genre। উদাহরণ: `Skrillex`-এর `Tears`, আধুনিক `UK Bass`”\ntrack সংখ্যা বা set-এর সময়:\n“উদাহরণ: `20 tracks` / `60 minutes`”\nআউটপুট সংস্করণ:\n“`Fast`: দ্রুত playlist; মান কম হতে পারে”\n“`Brief`: শুধু একটি সম্মিলিত playlist”\n“`Rich`: style, পরিস্থিতি ও discovery-এর আলাদা দৃষ্টিভঙ্গি, শেষে সম্মিলিত playlist”\nঅন্যান্য সীমা:\n“উদাহরণ: `খুব বেশি বাজানো track এড়ান`, `vocal নয়`, `শুধু Remix`; ঐচ্ছিক”\n\n\u0060\u0060\u0060markdown\nপরিস্থিতি:\nলক্ষ্য দেশ / অঞ্চল:\nমূল সাউন্ডের দিক:\ntrack সংখ্যা বা set-এর সময়:\nআউটপুট সংস্করণ:\nঅন্যান্য সীমা:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[দ্বিতীয় ধাপ: অনুরোধ বিস্তারিত করা]",
      "rules": [
        "1. উদাহরণ কপি করতে, নিজের মতো লিখতে বা ফাঁকা রাখতে পারেন"
      ],
      "fields": [
        {
          "key": "style",
          "label": "নির্দিষ্ট style",
          "example": "উদাহরণ: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "গতি / BPM",
          "example": "উদাহরণ: `105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "পরিচিতি ও discovery",
          "example": "`পরিচিত` / `ভারসাম্যপূর্ণ` / `আবিষ্কার`"
        },
        {
          "key": "era_classic",
          "label": "যুগ ও classics",
          "example": "`সমকালীন` / `কয়েকটি classic anchor` / `নতুন-পুরোনোর সেতু` / `আগে classics`"
        },
        {
          "key": "mood",
          "label": "মেজাজ",
          "example": "উদাহরণ: `nostalgic` / `ঠান্ডা` / `romantic`"
        },
        {
          "key": "energy",
          "label": "SET-এর energy level বা curve",
          "example": "উদাহরণ: `কম` / `বেশি`; `স্থির` / `roller coaster`"
        },
        {
          "key": "platform",
          "label": "platform ও link-এর প্রয়োজন",
          "example": "উদাহরণ: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; একটি হলে শুধু সেটি, একাধিক হলে দেওয়া অগ্রাধিকার"
        },
        {
          "key": "other",
          "label": "অন্যান্য",
          "example": ""
        }
      ],
      "prompt": "[দ্বিতীয় ধাপ: অনুরোধ বিস্তারিত করা]\n\nনির্দিষ্ট style:\n“উদাহরণ: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`”\nগতি / BPM:\n“উদাহরণ: `105` / `128` / `140` / `150` / `170`”\nপরিচিতি ও discovery:\n“`পরিচিত` / `ভারসাম্যপূর্ণ` / `আবিষ্কার`”\nযুগ ও classics:\n“`সমকালীন` / `কয়েকটি classic anchor` / `নতুন-পুরোনোর সেতু` / `আগে classics`”\nমেজাজ:\n“উদাহরণ: `nostalgic` / `ঠান্ডা` / `romantic`”\nSET-এর energy level বা curve:\n“উদাহরণ: `কম` / `বেশি`; `স্থির` / `roller coaster`”\nplatform ও link-এর প্রয়োজন:\n“উদাহরণ: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; একটি হলে শুধু সেটি, একাধিক হলে দেওয়া অগ্রাধিকার”\nঅন্যান্য:\n\n\u0060\u0060\u0060markdown\nনির্দিষ্ট style:\nগতি / BPM:\nপরিচিতি ও discovery:\nযুগ ও classics:\nমেজাজ:\nSET-এর energy level বা curve:\nplatform ও link-এর প্রয়োজন:\nঅন্যান্য:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# Fast mode",
      "first_batch_title": "# Fast-এর প্রথম batch",
      "final_title": "# Fast mode",
      "columns": [
        "Track",
        "শিল্পী",
        "Link"
      ],
      "next_steps": [
        {
          "label": "প্রথম | নির্বাচন সম্পর্কে মতামত",
          "body": "ইচ্ছা হলে স্বাভাবিক ভাষায় বলুন নির্বাচিত track কেমন কাজ করেছে। এতে ব্যক্তিগত পছন্দ ও পরের পরামর্শ উন্নত হবে।"
        },
        {
          "label": "দ্বিতীয় | playlist export বা হস্তান্তর",
          "body": "Text playlist তৈরি করতে বা W4DJ-তে দিতে পারেন। `output text playlist` অথবা `export to w4dj` লিখুন।"
        }
      ],
      "digging_notes": "Digging নোট",
      "mix_suggestion": "Mix পরামর্শ",
      "unknown": "অজানা",
      "verified": "যাচাই করা",
      "target_platform_missing": "লক্ষ্য platform পাওয়া যায়নি"
    },
    "brief": {
      "title": "# Brief mode",
      "first_batch_title": "# Brief mode",
      "final_title": "# Brief mode",
      "columns": [
        "Track",
        "শিল্পী",
        "Album / EP",
        "Style",
        "BPM",
        "Key",
        "সময়কাল",
        "Energy",
        "প্রকাশের তারিখ",
        "নোট",
        "বাছাইয়ের কারণ",
        "Link"
      ],
      "next_steps": [
        {
          "label": "প্রথম | নির্বাচন সম্পর্কে মতামত",
          "body": "ইচ্ছা হলে স্বাভাবিক ভাষায় বলুন নির্বাচিত track কেমন কাজ করেছে। এতে ব্যক্তিগত পছন্দ ও পরের পরামর্শ উন্নত হবে।"
        },
        {
          "label": "দ্বিতীয় | playlist export বা হস্তান্তর",
          "body": "Text playlist তৈরি করতে বা W4DJ-তে দিতে পারেন। `output text playlist` অথবা `export to w4dj` লিখুন।"
        },
        {
          "label": "তৃতীয় | Harmonic set order",
          "body": "Camelot wheel ব্যবহার করে set সাজাব?"
        }
      ],
      "digging_notes": "Digging নোট",
      "mix_suggestion": "Mix পরামর্শ",
      "unknown": "অজানা",
      "verified": "যাচাই করা",
      "target_platform_missing": "লক্ষ্য platform পাওয়া যায়নি"
    },
    "rich": {
      "title": "# Rich mode",
      "first_batch_title": "# Rich mode",
      "final_title": "# Rich mode",
      "columns": [
        "Track",
        "শিল্পী",
        "Album / EP",
        "Style",
        "BPM",
        "Key",
        "সময়কাল",
        "Energy",
        "প্রকাশের তারিখ",
        "নোট",
        "বাছাইয়ের কারণ",
        "Link"
      ],
      "next_steps": [
        {
          "label": "প্রথম | নির্বাচন সম্পর্কে মতামত",
          "body": "ইচ্ছা হলে স্বাভাবিক ভাষায় বলুন নির্বাচিত track কেমন কাজ করেছে। এতে ব্যক্তিগত পছন্দ ও পরের পরামর্শ উন্নত হবে।"
        },
        {
          "label": "দ্বিতীয় | playlist export বা হস্তান্তর",
          "body": "Text playlist তৈরি করতে বা W4DJ-তে দিতে পারেন। `output text playlist` অথবা `export to w4dj` লিখুন।"
        },
        {
          "label": "তৃতীয় | Harmonic set order",
          "body": "Camelot wheel ব্যবহার করে set সাজাব?"
        }
      ],
      "digging_notes": "Digging নোট",
      "mix_suggestion": "Mix পরামর্শ",
      "unknown": "অজানা",
      "verified": "যাচাই করা",
      "target_platform_missing": "লক্ষ্য platform পাওয়া যায়নি",
      "view_titles": [
        "Style view",
        "পরিস্থিতির view",
        "পরিচিতি / discovery view",
        "Dynamic combined view"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "নির্বাচন সম্পর্কে মতামত",
      "positive": [
        "এই track আমার ভালো লেগেছে"
      ],
      "negative": [
        "এই track আমার ভালো লাগেনি"
      ],
      "ambiguous": [
        "এই track নিয়ে নিশ্চিত নই"
      ]
    },
    "export_w4dj": {
      "label": "W4DJ-তে export",
      "positive": [
        "W4DJ-তে export করুন"
      ],
      "negative": [
        "W4DJ-তে export করবেন না"
      ],
      "ambiguous": [
        "হয়তো W4DJ-তে export করুন"
      ]
    },
    "output_text_playlist": {
      "label": "Text playlist তৈরি",
      "positive": [
        "Text playlist তৈরি করুন"
      ],
      "negative": [
        "Text playlist তৈরি করবেন না"
      ],
      "ambiguous": [
        "হয়তো text playlist তৈরি করুন"
      ]
    },
    "harmonic_reorder": {
      "label": "Harmonic reorder",
      "positive": [
        "Camelot wheel অনুযায়ী সাজান"
      ],
      "negative": [
        "পুনরায় সাজাবেন না"
      ],
      "ambiguous": [
        "হয়তো Camelot wheel অনুযায়ী সাজান"
      ]
    },
    "confirm_long_term_memory": {
      "label": "দীর্ঘমেয়াদি memory নিশ্চিত",
      "positive": [
        "এই পছন্দ মনে রাখুন"
      ],
      "negative": [
        "এই পছন্দ সংরক্ষণ করবেন না"
      ],
      "ambiguous": [
        "হয়তো এই পছন্দ মনে রাখুন"
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
      "শুধু",
      "একমাত্র",
      "শুধু ব্যবহার"
    ],
    "preferred_markers": [
      "অগ্রাধিকার",
      "পছন্দ",
      "আগে"
    ],
    "fallback_markers": [
      "বিকল্প",
      "backup",
      "না পাওয়া গেলে"
    ],
    "forbidden_markers": [
      "ব্যবহার করবেন না",
      "বাদ দিন",
      "ছাড়া"
    ]
  },
  "status": {
    "unknown": "অজানা",
    "verified": "যাচাই করা",
    "target_platform_missing": "লক্ষ্য platform পাওয়া যায়নি"
  },
  "export": {
    "text": "বর্তমান ক্রমে কপি করা যায় এমন text playlist তৈরি করুন।",
    "w4dj": "W4DJ-এর জন্য UTF-8 `.w4dj` handoff file তৈরি করুন।",
    "harmonic": "জানা key দিয়ে Camelot wheel order চাইুন।",
    "feedback": "স্বাভাবিক ভাষার মতামত শুধু session বদলায়; দীর্ঘমেয়াদি সংরক্ষণে নিশ্চিতকরণ দরকার।",
    "memory_confirmation": "আমি এটিকে রুচির পরিবর্তনের সংক্ষিপ্ত সারাংশ হিসেবে বুঝেছি। ব্যক্তিগত দীর্ঘমেয়াদি profile-এ সংরক্ষণ করব?"
  },
  "trigger_capsule": [
    "ডিজে সেট",
    "প্লেলিস্ট",
    "গান খোঁজা",
    "ট্র্যাক খোঁজা",
    "সেট সাজানো",
    "দ্রুত মোড",
    "সংক্ষিপ্ত মোড",
    "সম্পূর্ণ মোড",
    "DJ সেট তৈরি করা",
    "DJ সেট",
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
