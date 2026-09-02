# Persian locale pack

This file is the fixed فارسی UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "fa",
  "language_name": "Persian",
  "native_name": "فارسی",
  "direction": "rtl",
  "market_policy": {
    "language_independent": true,
    "blank_region": "اگر منطقه خالی باشد، فقط یک بازار گسترده فارسی‌زبان را برای همین جلسه در نظر بگیر.",
    "explicit_region": "کشور یا منطقه صریح بر استنباط زبانی مقدم است، اما زبان ارتباط را تغییر نمی‌دهد.",
    "persistence": "بازار هدف را به‌عنوان ترجیح بلندمدت ذخیره نکن."
  },
  "quick_start": {
    "intro": "به دستیار انتخاب موسیقی DJ خوش آمدید. این Agent Skill به آماده‌سازی ست DJ کمک می‌کند. نیازها را در دو مرحله تأیید می‌کنید و پیشنهاد قطعه می‌گیرید. قوانین تکمیل:",
    "tutorial_label": "راهنمای ورود Set با یک کلیک",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[مرحله اول: اطلاعات ضروری]",
      "rules": [
        "1. می‌توانید یک نمونه را کپی کنید، آزادانه بنویسید یا خالی بگذارید",
        "2. خالی گذاشتن یعنی هوش مصنوعی پاسخ را هوشمندانه تشخیص می‌دهد"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "موقعیت",
          "example": "زمینه اجرا. نمونه: `bar` / `club` / `wedding` / `art exhibition`"
        },
        {
          "key": "target_market",
          "label": "کشور / منطقه هدف",
          "example": "نمونه: `چین mainland` / `تایوان` / `هنگ‌کنگ` / `ژاپن` / `بازار بین‌المللی انگلیسی‌زبان`"
        },
        {
          "key": "core_sound",
          "label": "جهت صوتی اصلی",
          "example": "هنرمند، قطعه و سبک مرجع. نمونه: `Tears` از `Skrillex`، سبک مدرن `UK Bass`"
        },
        {
          "key": "track_count_or_duration",
          "label": "تعداد قطعه یا مدت ست",
          "example": "نمونه: `20 tracks` / `60 minutes`"
        },
        {
          "key": "output_mode",
          "label": "نسخه خروجی",
          "example": "انتخاب Fast / Brief / Rich"
        },
        {
          "key": "other",
          "label": "محدودیت‌های دیگر",
          "example": "نمونه: `قطعات بیش‌ازحد شنیده‌شده نباشد`، `بدون وکال`، `فقط Remix`؛ اختیاری"
        }
      ],
      "prompt": "به دستیار انتخاب موسیقی DJ خوش آمدید. این Agent Skill به آماده‌سازی ست DJ کمک می‌کند. نیازها را در دو مرحله تأیید می‌کنید و پیشنهاد قطعه می‌گیرید. قوانین تکمیل:\n\n1. می‌توانید یک نمونه را کپی کنید، آزادانه بنویسید یا خالی بگذارید\n2. خالی گذاشتن یعنی هوش مصنوعی پاسخ را هوشمندانه تشخیص می‌دهد\n\n[مرحله اول: اطلاعات ضروری]\n\nموقعیت:\n«زمینه اجرا. نمونه: `bar` / `club` / `wedding` / `art exhibition`»\nکشور / منطقه هدف:\n«نمونه: `چین mainland` / `تایوان` / `هنگ‌کنگ` / `ژاپن` / `بازار بین‌المللی انگلیسی‌زبان`»\nجهت صوتی اصلی:\n«هنرمند، قطعه و سبک مرجع. نمونه: `Tears` از `Skrillex`، سبک مدرن `UK Bass`»\nتعداد قطعه یا مدت ست:\n«نمونه: `20 tracks` / `60 minutes`»\nنسخه خروجی:\n«`Fast`: خروجی سریع playlist؛ ممکن است کیفیت پایین‌تر باشد»\n«`Brief`: فقط یک playlist ترکیبی»\n«`Rich`: نماهای جداگانه سبک، موقعیت و کشف، سپس playlist ترکیبی نهایی»\nمحدودیت‌های دیگر:\n«نمونه: `قطعات بیش‌ازحد شنیده‌شده نباشد`، `بدون وکال`، `فقط Remix`؛ اختیاری»\n\n\u0060\u0060\u0060markdown\nموقعیت:\nکشور / منطقه هدف:\nجهت صوتی اصلی:\nتعداد قطعه یا مدت ست:\nنسخه خروجی:\nمحدودیت‌های دیگر:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[مرحله دوم: دقیق‌کردن درخواست]",
      "rules": [
        "1. می‌توانید یک نمونه را کپی کنید، آزادانه بنویسید یا خالی بگذارید"
      ],
      "fields": [
        {
          "key": "style",
          "label": "سبک مشخص",
          "example": "نمونه: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "سرعت / BPM",
          "example": "نمونه: `105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "آشنایی و کشف",
          "example": "`آشنا` / `متعادل` / `کشف`"
        },
        {
          "key": "era_classic",
          "label": "دوره و کلاسیک‌ها",
          "example": "`معاصر` / `چند لنگر کلاسیک` / `پل جدید و قدیم` / `کلاسیک‌ها اول`"
        },
        {
          "key": "mood",
          "label": "حال‌وهوا",
          "example": "نمونه: `نوستالژیک` / `سرد` / `رمانتیک`"
        },
        {
          "key": "energy",
          "label": "سطح یا منحنی انرژی SET",
          "example": "نمونه: `کم` / `زیاد`؛ `یکنواخت` / `رولرکوستر`"
        },
        {
          "key": "platform",
          "label": "پلتفرم و نیازهای پیوند",
          "example": "نمونه: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`؛ یک پلتفرم یعنی فقط همان، چند پلتفرم طبق ترتیب داده‌شده"
        },
        {
          "key": "other",
          "label": "سایر",
          "example": ""
        }
      ],
      "prompt": "[مرحله دوم: دقیق‌کردن درخواست]\n\nسبک مشخص:\n«نمونه: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`»\nسرعت / BPM:\n«نمونه: `105` / `128` / `140` / `150` / `170`»\nآشنایی و کشف:\n«`آشنا` / `متعادل` / `کشف`»\nدوره و کلاسیک‌ها:\n«`معاصر` / `چند لنگر کلاسیک` / `پل جدید و قدیم` / `کلاسیک‌ها اول`»\nحال‌وهوا:\n«نمونه: `نوستالژیک` / `سرد` / `رمانتیک`»\nسطح یا منحنی انرژی SET:\n«نمونه: `کم` / `زیاد`؛ `یکنواخت` / `رولرکوستر`»\nپلتفرم و نیازهای پیوند:\n«نمونه: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`؛ یک پلتفرم یعنی فقط همان، چند پلتفرم طبق ترتیب داده‌شده»\nسایر:\n\n\u0060\u0060\u0060markdown\nسبک مشخص:\nسرعت / BPM:\nآشنایی و کشف:\nدوره و کلاسیک‌ها:\nحال‌وهوا:\nسطح یا منحنی انرژی SET:\nپلتفرم و نیازهای پیوند:\nسایر:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# حالت Fast",
      "first_batch_title": "# دسته اول Fast",
      "final_title": "# حالت Fast",
      "columns": [
        "قطعه",
        "هنرمند",
        "پیوند"
      ],
      "next_steps": [
        {
          "label": "اول | ارسال بازخورد انتخاب",
          "body": "اگر مایلید، به زبان طبیعی بگویید انتخاب‌ها چگونه بودند. این کار ترجیحات خصوصی و پیشنهادهای بعدی را بهتر می‌کند."
        },
        {
          "label": "دوم | خروجی یا تحویل playlist",
          "body": "می‌توانید playlist متنی بگیرید یا آن را به W4DJ تحویل دهید. `output text playlist` یا `export to w4dj` را پاسخ دهید."
        }
      ],
      "digging_notes": "یادداشت‌های digging",
      "mix_suggestion": "پیشنهاد میکس",
      "unknown": "نامشخص",
      "verified": "تأییدشده",
      "target_platform_missing": "پلتفرم هدف در دسترس نیست"
    },
    "brief": {
      "title": "# حالت Brief",
      "first_batch_title": "# حالت Brief",
      "final_title": "# حالت Brief",
      "columns": [
        "قطعه",
        "هنرمند",
        "آلبوم / EP",
        "سبک",
        "BPM",
        "گام",
        "مدت",
        "انرژی",
        "تاریخ انتشار",
        "یادداشت",
        "دلیل انتخاب",
        "پیوند"
      ],
      "next_steps": [
        {
          "label": "اول | ارسال بازخورد انتخاب",
          "body": "اگر مایلید، به زبان طبیعی بگویید انتخاب‌ها چگونه بودند. این کار ترجیحات خصوصی و پیشنهادهای بعدی را بهتر می‌کند."
        },
        {
          "label": "دوم | خروجی یا تحویل playlist",
          "body": "می‌توانید playlist متنی بگیرید یا آن را به W4DJ تحویل دهید. `output text playlist` یا `export to w4dj` را پاسخ دهید."
        },
        {
          "label": "سوم | ترتیب هارمونیک ست",
          "body": "آیا می‌خواهید ست را با چرخ Camelot مرتب کنم؟"
        }
      ],
      "digging_notes": "یادداشت‌های digging",
      "mix_suggestion": "پیشنهاد میکس",
      "unknown": "نامشخص",
      "verified": "تأییدشده",
      "target_platform_missing": "پلتفرم هدف در دسترس نیست"
    },
    "rich": {
      "title": "# حالت Rich",
      "first_batch_title": "# حالت Rich",
      "final_title": "# حالت Rich",
      "columns": [
        "قطعه",
        "هنرمند",
        "آلبوم / EP",
        "سبک",
        "BPM",
        "گام",
        "مدت",
        "انرژی",
        "تاریخ انتشار",
        "یادداشت",
        "دلیل انتخاب",
        "پیوند"
      ],
      "next_steps": [
        {
          "label": "اول | ارسال بازخورد انتخاب",
          "body": "اگر مایلید، به زبان طبیعی بگویید انتخاب‌ها چگونه بودند. این کار ترجیحات خصوصی و پیشنهادهای بعدی را بهتر می‌کند."
        },
        {
          "label": "دوم | خروجی یا تحویل playlist",
          "body": "می‌توانید playlist متنی بگیرید یا آن را به W4DJ تحویل دهید. `output text playlist` یا `export to w4dj` را پاسخ دهید."
        },
        {
          "label": "سوم | ترتیب هارمونیک ست",
          "body": "آیا می‌خواهید ست را با چرخ Camelot مرتب کنم؟"
        }
      ],
      "digging_notes": "یادداشت‌های digging",
      "mix_suggestion": "پیشنهاد میکس",
      "unknown": "نامشخص",
      "verified": "تأییدشده",
      "target_platform_missing": "پلتفرم هدف در دسترس نیست",
      "view_titles": [
        "نمای سبک",
        "نمای موقعیت",
        "نمای آشنایی / کشف",
        "نمای ترکیبی پویا"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "ارسال بازخورد",
      "positive": [
        "این قطعه را دوست دارم"
      ],
      "negative": [
        "این قطعه را دوست ندارم"
      ],
      "ambiguous": [
        "درباره این قطعه مطمئن نیستم"
      ]
    },
    "export_w4dj": {
      "label": "خروجی برای W4DJ",
      "positive": [
        "خروجی برای W4DJ"
      ],
      "negative": [
        "برای W4DJ خروجی نگیر"
      ],
      "ambiguous": [
        "شاید برای W4DJ خروجی بگیر"
      ]
    },
    "output_text_playlist": {
      "label": "خروجی playlist متنی",
      "positive": [
        "playlist متنی را خروجی بگیر"
      ],
      "negative": [
        "playlist متنی را خروجی نگیر"
      ],
      "ambiguous": [
        "شاید playlist متنی را خروجی بگیر"
      ]
    },
    "harmonic_reorder": {
      "label": "مرتب‌سازی هارمونیک",
      "positive": [
        "با چرخ Camelot مرتب کن"
      ],
      "negative": [
        "مرتب نکن"
      ],
      "ambiguous": [
        "شاید با چرخ Camelot مرتب کن"
      ]
    },
    "confirm_long_term_memory": {
      "label": "تأیید حافظه بلندمدت",
      "positive": [
        "این ترجیح را به خاطر بسپار"
      ],
      "negative": [
        "این ترجیح را ذخیره نکن"
      ],
      "ambiguous": [
        "شاید این ترجیح را به خاطر بسپار"
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
      "فقط",
      "تنها",
      "فقط استفاده کن"
    ],
    "preferred_markers": [
      "ترجیح",
      "اولویت",
      "ترجیحاً"
    ],
    "fallback_markers": [
      "جایگزین",
      "پشتیبان",
      "اگر در دسترس نبود"
    ],
    "forbidden_markers": [
      "استفاده نکن",
      "حذف کن",
      "بدون"
    ]
  },
  "status": {
    "unknown": "نامشخص",
    "verified": "تأییدشده",
    "target_platform_missing": "پلتفرم هدف در دسترس نیست"
  },
  "export": {
    "text": "یک playlist متنی قابل‌کپی را با ترتیب فعلی تولید کن.",
    "w4dj": "یک فایل تحویل UTF-8 با پسوند `.w4dj` برای W4DJ بساز.",
    "harmonic": "ترتیب چرخ Camelot را با گام‌های شناخته‌شده درخواست کن.",
    "feedback": "بازخورد طبیعی فقط جلسه را به‌روزرسانی می‌کند؛ ذخیره بلندمدت نیازمند تأیید است.",
    "memory_confirmation": "این را به‌عنوان خلاصه‌ای کوتاه از تغییر سلیقه فهمیدم. در پروفایل خصوصی بلندمدت ذخیره شود؟"
  },
  "trigger_capsule": [
    "ست دی‌جی",
    "پلی‌لیست",
    "جست‌وجوی موسیقی",
    "پیدا کردن ترک",
    "چیدن ست",
    "حالت سریع",
    "حالت مختصر",
    "حالت کامل",
    "ساختن ست DJ",
    "ست DJ",
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
