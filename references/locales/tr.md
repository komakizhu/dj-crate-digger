# Turkish locale pack

This file is the fixed Türkçe UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "tr",
  "language_name": "Turkish",
  "native_name": "Türkçe",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "Bölge boş bırakılırsa bu oturum için yalnızca geniş Türkçe konuşulan pazarı kullanın.",
    "explicit_region": "Açıkça belirtilen ülke veya bölge dil çıkarımının önüne geçer, iletişim dilini değiştirmez.",
    "persistence": "Hedef pazarı uzun vadeli tercih olarak kaydetmeyin."
  },
  "quick_start": {
    "intro": "DJ seçim asistanına hoş geldiniz. Bu Agent Skill bir DJ seti hazırlamanıza yardımcı olur. İhtiyaçlarınızı iki turda doğrulayacak ve parça önerileri alacaksınız. Doldurma kuralları:",
    "tutorial_label": "Tek tıkla Set içe aktarma rehberi",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[Birinci tur: gerekli bilgiler]",
      "rules": [
        "1. Bir örneği kopyalayabilir, serbestçe doldurabilir veya boş bırakabilirsiniz",
        "2. Boş bırakmak, yanıtı yapay zekânın akıllıca değerlendirmesi anlamına gelir"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "Sahne",
          "example": "Performans bağlamı. Örnek: `bar` / `kulüp` / `düğün` / `sanat sergisi`"
        },
        {
          "key": "target_market",
          "label": "Hedef ülke / bölge",
          "example": "Örnek: `Çin ana karası` / `Tayvan` / `Hong Kong` / `Japonya` / `uluslararası İngilizce pazar"
        },
        {
          "key": "core_sound",
          "label": "Ana ses yönü",
          "example": "Referans sanatçı, parça ve tür. Örnek: `Skrillex` - `Tears`, modern `UK Bass`"
        },
        {
          "key": "track_count_or_duration",
          "label": "Parça sayısı veya set süresi",
          "example": "Örnek: `20 parça` / `60 dakika`"
        },
        {
          "key": "output_mode",
          "label": "Çıktı sürümü",
          "example": "Fast / Brief / Rich seçenekleri"
        },
        {
          "key": "other",
          "label": "Diğer kısıtlar",
          "example": "Örnek: `fazla çalınmış parçalardan kaçın`, `vokal olmasın`, `yalnızca Remix`; isteğe bağlı"
        }
      ],
      "prompt": "DJ seçim asistanına hoş geldiniz. Bu Agent Skill bir DJ seti hazırlamanıza yardımcı olur. İhtiyaçlarınızı iki turda doğrulayacak ve parça önerileri alacaksınız. Doldurma kuralları:\n\n1. Bir örneği kopyalayabilir, serbestçe doldurabilir veya boş bırakabilirsiniz\n2. Boş bırakmak, yanıtı yapay zekânın akıllıca değerlendirmesi anlamına gelir\n\n[Birinci tur: gerekli bilgiler]\n\nSahne:\n“Performans bağlamı. Örnek: `bar` / `kulüp` / `düğün` / `sanat sergisi`”\nHedef ülke / bölge:\n“Örnek: `Çin ana karası` / `Tayvan` / `Hong Kong` / `Japonya` / `uluslararası İngilizce pazar”\nAna ses yönü:\n“Referans sanatçı, parça ve tür. Örnek: `Skrillex` - `Tears`, modern `UK Bass`”\nParça sayısı veya set süresi:\n“Örnek: `20 parça` / `60 dakika`”\nÇıktı sürümü:\n“`Fast`: hızlı playlist çıktısı; kalite daha düşük olabilir”\n“`Brief`: yalnızca tek bir birleşik playlist”\n“`Rich`: stil, sahne ve keşif görünümleri; ardından son birleşik playlist”\nDiğer kısıtlar:\n“Örnek: `fazla çalınmış parçalardan kaçın`, `vokal olmasın`, `yalnızca Remix`; isteğe bağlı”\n\n\u0060\u0060\u0060markdown\nSahne:\nHedef ülke / bölge:\nAna ses yönü:\nParça sayısı veya set süresi:\nÇıktı sürümü:\nDiğer kısıtlar:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[İkinci tur: isteği ayrıntılandırma]",
      "rules": [
        "1. Bir örneği kopyalayabilir, serbestçe doldurabilir veya boş bırakabilirsiniz"
      ],
      "fields": [
        {
          "key": "style",
          "label": "Belirli stil",
          "example": "Örnek: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "Hız / BPM",
          "example": "Örnek: `105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "Aşinalık ve keşif",
          "example": "`Tanıdık` / `Dengeli` / `Keşif`"
        },
        {
          "key": "era_classic",
          "label": "Dönem ve klasikler",
          "example": "`Güncel` / `Az sayıda klasik çapa` / `Yeni-eski köprüsü` / `Klasikler önce`"
        },
        {
          "key": "mood",
          "label": "Ruh hâli",
          "example": "Örnek: `nostaljik` / `soğuk` / `romantik`"
        },
        {
          "key": "energy",
          "label": "SET enerji seviyesi veya enerji eğrisi",
          "example": "Örnek: `düşük` / `yüksek`; `sabit` / `lunapark treni`"
        },
        {
          "key": "platform",
          "label": "Platform ve bağlantı gereksinimleri",
          "example": "Örnek: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; tek platform yalnızca onu, birden fazla belirtilen önceliği kullanır"
        },
        {
          "key": "other",
          "label": "Diğer",
          "example": ""
        }
      ],
      "prompt": "[İkinci tur: isteği ayrıntılandırma]\n\nBelirli stil:\n“Örnek: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`”\nHız / BPM:\n“Örnek: `105` / `128` / `140` / `150` / `170`”\nAşinalık ve keşif:\n“`Tanıdık` / `Dengeli` / `Keşif`”\nDönem ve klasikler:\n“`Güncel` / `Az sayıda klasik çapa` / `Yeni-eski köprüsü` / `Klasikler önce`”\nRuh hâli:\n“Örnek: `nostaljik` / `soğuk` / `romantik`”\nSET enerji seviyesi veya enerji eğrisi:\n“Örnek: `düşük` / `yüksek`; `sabit` / `lunapark treni`”\nPlatform ve bağlantı gereksinimleri:\n“Örnek: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; tek platform yalnızca onu, birden fazla belirtilen önceliği kullanır”\nDiğer:\n\n\u0060\u0060\u0060markdown\nBelirli stil:\nHız / BPM:\nAşinalık ve keşif:\nDönem ve klasikler:\nRuh hâli:\nSET enerji seviyesi veya enerji eğrisi:\nPlatform ve bağlantı gereksinimleri:\nDiğer:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# Fast modu",
      "first_batch_title": "# Fast ilk parti",
      "final_title": "# Fast modu",
      "columns": [
        "Parça",
        "Sanatçı",
        "Bağlantı"
      ],
      "next_steps": [
        {
          "label": "Birinci | Seçim geri bildirimi",
          "body": "İsterseniz seçimlerin nasıl çalıştığını doğal dille anlatın. Bu, özel seçim tercihlerinizi ve sonraki önerileri geliştirir."
        },
        {
          "label": "İkinci | Playlist'i dışa aktarma veya aktarma",
          "body": "Metin playlist'i çıkarabilir ya da W4DJ'e aktarabilirsiniz. `output text playlist` veya `export to w4dj` diye yanıt verin."
        }
      ],
      "digging_notes": "Digging notları",
      "mix_suggestion": "Mix önerisi",
      "unknown": "Bilinmiyor",
      "verified": "Doğrulandı",
      "target_platform_missing": "Hedef platform kullanılamıyor"
    },
    "brief": {
      "title": "# Brief modu",
      "first_batch_title": "# Brief modu",
      "final_title": "# Brief modu",
      "columns": [
        "Parça",
        "Sanatçı",
        "Albüm / EP",
        "Stil",
        "BPM",
        "Ton",
        "Süre",
        "Enerji",
        "Yayın tarihi",
        "Notlar",
        "Seçim nedeni",
        "Bağlantı"
      ],
      "next_steps": [
        {
          "label": "Birinci | Seçim geri bildirimi",
          "body": "İsterseniz seçimlerin nasıl çalıştığını doğal dille anlatın. Bu, özel seçim tercihlerinizi ve sonraki önerileri geliştirir."
        },
        {
          "label": "İkinci | Playlist'i dışa aktarma veya aktarma",
          "body": "Metin playlist'i çıkarabilir ya da W4DJ'e aktarabilirsiniz. `output text playlist` veya `export to w4dj` diye yanıt verin."
        },
        {
          "label": "Üçüncü | Harmonik set sırası",
          "body": "Seti Camelot çarkını kullanarak sıralamamı ister misiniz?"
        }
      ],
      "digging_notes": "Digging notları",
      "mix_suggestion": "Mix önerisi",
      "unknown": "Bilinmiyor",
      "verified": "Doğrulandı",
      "target_platform_missing": "Hedef platform kullanılamıyor"
    },
    "rich": {
      "title": "# Rich modu",
      "first_batch_title": "# Rich modu",
      "final_title": "# Rich modu",
      "columns": [
        "Parça",
        "Sanatçı",
        "Albüm / EP",
        "Stil",
        "BPM",
        "Ton",
        "Süre",
        "Enerji",
        "Yayın tarihi",
        "Notlar",
        "Seçim nedeni",
        "Bağlantı"
      ],
      "next_steps": [
        {
          "label": "Birinci | Seçim geri bildirimi",
          "body": "İsterseniz seçimlerin nasıl çalıştığını doğal dille anlatın. Bu, özel seçim tercihlerinizi ve sonraki önerileri geliştirir."
        },
        {
          "label": "İkinci | Playlist'i dışa aktarma veya aktarma",
          "body": "Metin playlist'i çıkarabilir ya da W4DJ'e aktarabilirsiniz. `output text playlist` veya `export to w4dj` diye yanıt verin."
        },
        {
          "label": "Üçüncü | Harmonik set sırası",
          "body": "Seti Camelot çarkını kullanarak sıralamamı ister misiniz?"
        }
      ],
      "digging_notes": "Digging notları",
      "mix_suggestion": "Mix önerisi",
      "unknown": "Bilinmiyor",
      "verified": "Doğrulandı",
      "target_platform_missing": "Hedef platform kullanılamıyor",
      "view_titles": [
        "Stil görünümü",
        "Sahne görünümü",
        "Aşinalık / keşif görünümü",
        "Dinamik birleşik görünüm"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "Seçim geri bildirimi",
      "positive": [
        "Bu parçayı beğendim"
      ],
      "negative": [
        "Bu parçayı beğenmedim"
      ],
      "ambiguous": [
        "Bu parça hakkında emin değilim"
      ]
    },
    "export_w4dj": {
      "label": "W4DJ'e aktar",
      "positive": [
        "W4DJ'e aktar"
      ],
      "negative": [
        "W4DJ'e aktarma"
      ],
      "ambiguous": [
        "Belki W4DJ'e aktar"
      ]
    },
    "output_text_playlist": {
      "label": "Metin playlist'i çıkar",
      "positive": [
        "Metin playlist'ini çıkar"
      ],
      "negative": [
        "Metin playlist'ini çıkarma"
      ],
      "ambiguous": [
        "Belki metin playlist'i çıkar"
      ]
    },
    "harmonic_reorder": {
      "label": "Harmonik yeniden sırala",
      "positive": [
        "Camelot çarkına göre sırala"
      ],
      "negative": [
        "Yeniden sıralama"
      ],
      "ambiguous": [
        "Belki Camelot çarkına göre sırala"
      ]
    },
    "confirm_long_term_memory": {
      "label": "Uzun vadeli belleği onayla",
      "positive": [
        "Bu tercihi hatırla"
      ],
      "negative": [
        "Bu tercihi kaydetme"
      ],
      "ambiguous": [
        "Belki bu tercihi hatırla"
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
      "yalnızca",
      "sadece",
      "tek"
    ],
    "preferred_markers": [
      "tercih",
      "öncelik",
      "tercihen"
    ],
    "fallback_markers": [
      "yedek",
      "alternatif",
      "kullanılamazsa"
    ],
    "forbidden_markers": [
      "kullanma",
      "hariç",
      "olmasın"
    ]
  },
  "status": {
    "unknown": "Bilinmiyor",
    "verified": "Doğrulandı",
    "target_platform_missing": "Hedef platform kullanılamıyor"
  },
  "export": {
    "text": "Mevcut sırada kopyalanabilir bir metin playlist'i çıkarın.",
    "w4dj": "W4DJ için UTF-8 `.w4dj` aktarım dosyası oluşturun.",
    "harmonic": "Bilinen tonlarla Camelot çarkına göre sıralama isteyin.",
    "feedback": "Doğal dil geri bildirimi yalnızca oturumu günceller; uzun vadeli kayıt onay gerektirir.",
    "memory_confirmation": "Bunu zevk değişikliğinin kısa bir özeti olarak anladım. Özel uzun vadeli profile kaydedilsin mi?"
  },
  "trigger_capsule": [
    "DJ seti",
    "çalma listesi",
    "müzik keşfi",
    "parça bul",
    "set oluştur",
    "hızlı mod",
    "kısa mod",
    "tam mod",
    "DJ seti oluştur",
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
