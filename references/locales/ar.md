# Arabic locale pack

This file is the fixed العربية UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "ar",
  "language_name": "Arabic",
  "native_name": "العربية",
  "direction": "rtl",
  "market_policy": {
    "language_independent": true,
    "blank_region": "إذا تُركت المنطقة فارغة، استخدم سوقًا عربيًا واسعًا لهذه الجلسة فقط.",
    "explicit_region": "المنطقة المحددة صراحةً تتغلب على استنتاج اللغة ولا تغير لغة التواصل.",
    "persistence": "لا تحفظ السوق المستهدف كتفضيل طويل الأمد."
  },
  "quick_start": {
    "intro": "مرحبًا بك في مساعد اختيار موسيقى DJ. تساعدك مهارة Agent هذه على إعداد مجموعة DJ. ستؤكد احتياجاتك في جولتين وتحصل على اقتراحات للمقاطع. قواعد الإدخال:",
    "tutorial_label": "دليل استيراد Set بنقرة واحدة",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[الجولة الأولى: المعلومات الأساسية]",
      "rules": [
        "1. يمكنك نسخ مثال أو الكتابة بحرية أو ترك الحقل فارغًا",
        "2. ترك الحقل فارغًا يعني أن الذكاء الاصطناعي سيحكم على الإجابة بذكاء"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "المشهد",
          "example": "سياق الأداء. أمثلة: `bar` / `club` / `wedding` / `art exhibition`"
        },
        {
          "key": "target_market",
          "label": "الدولة / المنطقة المستهدفة",
          "example": "أمثلة: `Mainland China` / `Taiwan` / `Hong Kong` / `Japan` / `international English market`"
        },
        {
          "key": "core_sound",
          "label": "الاتجاه الصوتي الأساسي",
          "example": "فنان ومقطع ونوع مرجعي. مثال: `Tears` لـ `Skrillex`، ونوع `UK Bass` حديث"
        },
        {
          "key": "track_count_or_duration",
          "label": "عدد المقاطع أو مدة المجموعة",
          "example": "أمثلة: `20 tracks` / `60 minutes`"
        },
        {
          "key": "output_mode",
          "label": "نسخة الإخراج",
          "example": "خيارات Fast / Brief / Rich"
        },
        {
          "key": "other",
          "label": "قيود أخرى",
          "example": "أمثلة: `تجنب المقاطع المستهلكة`، `بدون غناء`، `Remix فقط`؛ اختياري"
        }
      ],
      "prompt": "مرحبًا بك في مساعد اختيار موسيقى DJ. تساعدك مهارة Agent هذه على إعداد مجموعة DJ. ستؤكد احتياجاتك في جولتين وتحصل على اقتراحات للمقاطع. قواعد الإدخال:\n\n1. يمكنك نسخ مثال أو الكتابة بحرية أو ترك الحقل فارغًا\n2. ترك الحقل فارغًا يعني أن الذكاء الاصطناعي سيحكم على الإجابة بذكاء\n\n[الجولة الأولى: المعلومات الأساسية]\n\nالمشهد:\n«سياق الأداء. أمثلة: `bar` / `club` / `wedding` / `art exhibition`»\nالدولة / المنطقة المستهدفة:\n«أمثلة: `Mainland China` / `Taiwan` / `Hong Kong` / `Japan` / `international English market`»\nالاتجاه الصوتي الأساسي:\n«فنان ومقطع ونوع مرجعي. مثال: `Tears` لـ `Skrillex`، ونوع `UK Bass` حديث»\nعدد المقاطع أو مدة المجموعة:\n«أمثلة: `20 tracks` / `60 minutes`»\nنسخة الإخراج:\n«`Fast`: إخراج سريع لقائمة التشغيل؛ قد تنخفض الجودة»\n«`Brief`: قائمة تشغيل موحدة واحدة فقط»\n«`Rich`: مناظر منفصلة للأسلوب والمشهد والاكتشاف، ثم قائمة موحدة نهائية»\nقيود أخرى:\n«أمثلة: `تجنب المقاطع المستهلكة`، `بدون غناء`، `Remix فقط`؛ اختياري»\n\n\u0060\u0060\u0060markdown\nالمشهد:\nالدولة / المنطقة المستهدفة:\nالاتجاه الصوتي الأساسي:\nعدد المقاطع أو مدة المجموعة:\nنسخة الإخراج:\nقيود أخرى:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[الجولة الثانية: تفصيل الطلب]",
      "rules": [
        "1. يمكنك نسخ مثال أو الكتابة بحرية أو ترك الحقل فارغًا"
      ],
      "fields": [
        {
          "key": "style",
          "label": "الأسلوب المحدد",
          "example": "أمثلة: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "السرعة / BPM",
          "example": "أمثلة: `105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "الألفة والاكتشاف",
          "example": "`مألوف` / `متوازن` / `اكتشاف`"
        },
        {
          "key": "era_classic",
          "label": "العصر والكلاسيكيات",
          "example": "`معاصر` / `مراسي كلاسيكية قليلة` / `جسر بين الجديد والقديم` / `الكلاسيكيات أولًا`"
        },
        {
          "key": "mood",
          "label": "المزاج",
          "example": "أمثلة: `حنين` / `بارد` / `رومانسي`"
        },
        {
          "key": "energy",
          "label": "مستوى طاقة SET أو منحنى الطاقة",
          "example": "أمثلة: `منخفض` / `مرتفع`؛ `ثابت` / `أفعواني`"
        },
        {
          "key": "platform",
          "label": "المنصة ومتطلبات الروابط",
          "example": "أمثلة: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`؛ منصة واحدة تعني استخدامها وحدها، والمنصات المتعددة تتبع ترتيبها"
        },
        {
          "key": "other",
          "label": "أخرى",
          "example": ""
        }
      ],
      "prompt": "[الجولة الثانية: تفصيل الطلب]\n\nالأسلوب المحدد:\n«أمثلة: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`»\nالسرعة / BPM:\n«أمثلة: `105` / `128` / `140` / `150` / `170`»\nالألفة والاكتشاف:\n«`مألوف` / `متوازن` / `اكتشاف`»\nالعصر والكلاسيكيات:\n«`معاصر` / `مراسي كلاسيكية قليلة` / `جسر بين الجديد والقديم` / `الكلاسيكيات أولًا`»\nالمزاج:\n«أمثلة: `حنين` / `بارد` / `رومانسي`»\nمستوى طاقة SET أو منحنى الطاقة:\n«أمثلة: `منخفض` / `مرتفع`؛ `ثابت` / `أفعواني`»\nالمنصة ومتطلبات الروابط:\n«أمثلة: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`؛ منصة واحدة تعني استخدامها وحدها، والمنصات المتعددة تتبع ترتيبها»\nأخرى:\n\n\u0060\u0060\u0060markdown\nالأسلوب المحدد:\nالسرعة / BPM:\nالألفة والاكتشاف:\nالعصر والكلاسيكيات:\nالمزاج:\nمستوى طاقة SET أو منحنى الطاقة:\nالمنصة ومتطلبات الروابط:\nأخرى:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# وضع Fast",
      "first_batch_title": "# الدفعة الأولى من Fast",
      "final_title": "# وضع Fast",
      "columns": [
        "المقطع",
        "الفنان",
        "الرابط"
      ],
      "next_steps": [
        {
          "label": "أولًا | مشاركة ملاحظات الاختيار",
          "body": "إذا رغبت، أجب بلغة طبيعية عن كيفية نجاح الاختيارات. يساعد ذلك على تحسين تفضيلاتك الخاصة والاقتراحات اللاحقة."
        },
        {
          "label": "ثانيًا | تصدير قائمة التشغيل أو تسليمها",
          "body": "يمكنك إخراج قائمة نصية أو تسليمها إلى W4DJ. أجب `output text playlist` أو `export to w4dj`."
        }
      ],
      "digging_notes": "ملاحظات التنقيب",
      "mix_suggestion": "اقتراح المزج",
      "unknown": "غير معروف",
      "verified": "تم التحقق",
      "target_platform_missing": "المنصة المستهدفة غير متاحة"
    },
    "brief": {
      "title": "# وضع Brief",
      "first_batch_title": "# وضع Brief",
      "final_title": "# وضع Brief",
      "columns": [
        "المقطع",
        "الفنان",
        "الألبوم / EP",
        "الأسلوب",
        "BPM",
        "المقام",
        "المدة",
        "الطاقة",
        "تاريخ الإصدار",
        "ملاحظات",
        "سبب الاختيار",
        "الرابط"
      ],
      "next_steps": [
        {
          "label": "أولًا | مشاركة ملاحظات الاختيار",
          "body": "إذا رغبت، أجب بلغة طبيعية عن كيفية نجاح الاختيارات. يساعد ذلك على تحسين تفضيلاتك الخاصة والاقتراحات اللاحقة."
        },
        {
          "label": "ثانيًا | تصدير قائمة التشغيل أو تسليمها",
          "body": "يمكنك إخراج قائمة نصية أو تسليمها إلى W4DJ. أجب `output text playlist` أو `export to w4dj`."
        },
        {
          "label": "ثالثًا | ترتيب هارموني للمجموعة",
          "body": "هل تريد أن أرتب المجموعة باستخدام عجلة Camelot؟"
        }
      ],
      "digging_notes": "ملاحظات التنقيب",
      "mix_suggestion": "اقتراح المزج",
      "unknown": "غير معروف",
      "verified": "تم التحقق",
      "target_platform_missing": "المنصة المستهدفة غير متاحة"
    },
    "rich": {
      "title": "# وضع Rich",
      "first_batch_title": "# وضع Rich",
      "final_title": "# وضع Rich",
      "columns": [
        "المقطع",
        "الفنان",
        "الألبوم / EP",
        "الأسلوب",
        "BPM",
        "المقام",
        "المدة",
        "الطاقة",
        "تاريخ الإصدار",
        "ملاحظات",
        "سبب الاختيار",
        "الرابط"
      ],
      "next_steps": [
        {
          "label": "أولًا | مشاركة ملاحظات الاختيار",
          "body": "إذا رغبت، أجب بلغة طبيعية عن كيفية نجاح الاختيارات. يساعد ذلك على تحسين تفضيلاتك الخاصة والاقتراحات اللاحقة."
        },
        {
          "label": "ثانيًا | تصدير قائمة التشغيل أو تسليمها",
          "body": "يمكنك إخراج قائمة نصية أو تسليمها إلى W4DJ. أجب `output text playlist` أو `export to w4dj`."
        },
        {
          "label": "ثالثًا | ترتيب هارموني للمجموعة",
          "body": "هل تريد أن أرتب المجموعة باستخدام عجلة Camelot؟"
        }
      ],
      "digging_notes": "ملاحظات التنقيب",
      "mix_suggestion": "اقتراح المزج",
      "unknown": "غير معروف",
      "verified": "تم التحقق",
      "target_platform_missing": "المنصة المستهدفة غير متاحة",
      "view_titles": [
        "منظور الأسلوب",
        "منظور المشهد",
        "منظور الألفة / الاكتشاف",
        "المنظور الموحد الديناميكي"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "مشاركة ملاحظات الاختيار",
      "positive": [
        "أحب هذا المقطع"
      ],
      "negative": [
        "لا أحب هذا المقطع"
      ],
      "ambiguous": [
        "لست متأكدًا من هذا المقطع"
      ]
    },
    "export_w4dj": {
      "label": "تصدير إلى W4DJ",
      "positive": [
        "تصدير إلى W4DJ"
      ],
      "negative": [
        "عدم التصدير إلى W4DJ"
      ],
      "ambiguous": [
        "ربما التصدير إلى W4DJ"
      ]
    },
    "output_text_playlist": {
      "label": "إخراج قائمة نصية",
      "positive": [
        "إخراج القائمة النصية"
      ],
      "negative": [
        "عدم إخراج القائمة النصية"
      ],
      "ambiguous": [
        "ربما إخراج القائمة النصية"
      ]
    },
    "harmonic_reorder": {
      "label": "إعادة ترتيب هارموني",
      "positive": [
        "رتبها بعجلة Camelot"
      ],
      "negative": [
        "لا تعِد الترتيب"
      ],
      "ambiguous": [
        "ربما رتبها بعجلة Camelot"
      ]
    },
    "confirm_long_term_memory": {
      "label": "تأكيد الذاكرة طويلة الأمد",
      "positive": [
        "تذكر هذا التفضيل"
      ],
      "negative": [
        "لا تحفظ هذا التفضيل"
      ],
      "ambiguous": [
        "ربما تذكر هذا التفضيل"
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
      "حصريًا",
      "استخدم فقط"
    ],
    "preferred_markers": [
      "أفضل",
      "مفضلة",
      "أولوية"
    ],
    "fallback_markers": [
      "بديل",
      "احتياطي",
      "عند عدم التوفر"
    ],
    "forbidden_markers": [
      "لا تستخدم",
      "استبعد",
      "بدون"
    ]
  },
  "status": {
    "unknown": "غير معروف",
    "verified": "تم التحقق",
    "target_platform_missing": "المنصة المستهدفة غير متاحة"
  },
  "export": {
    "text": "إخراج قائمة نصية قابلة للنسخ بالترتيب الحالي.",
    "w4dj": "إنشاء ملف تسليم UTF-8 بصيغة `.w4dj` لـ W4DJ.",
    "harmonic": "طلب ترتيب بعجلة Camelot باستخدام المقامات المعروفة.",
    "feedback": "تحديث الجلسة فقط عبر الملاحظات الطبيعية؛ التخزين طويل الأمد يحتاج إلى تأكيد.",
    "memory_confirmation": "فهمت هذا كملخص موجز لتغير الذوق. هل أحفظه في الملف الخاص طويل الأمد؟"
  },
  "trigger_capsule": [
    "مجموعة DJ",
    "قائمة تشغيل",
    "البحث عن موسيقى",
    "العثور على مقاطع",
    "ترتيب مجموعة",
    "سريع",
    "مختصر",
    "كامل",
    "إنشاء مجموعة DJ",
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
