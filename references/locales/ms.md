# Malay locale pack

This file is the fixed Bahasa Melayu UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "ms",
  "language_name": "Malay",
  "native_name": "Bahasa Melayu",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "Jika wilayah kosong, gunakan pasaran bahasa Melayu yang luas untuk sesi ini sahaja.",
    "explicit_region": "Negara atau wilayah yang dinyatakan mengatasi inferens bahasa tanpa mengubah bahasa komunikasi.",
    "persistence": "Jangan simpan pasaran sasaran sebagai pilihan jangka panjang."
  },
  "quick_start": {
    "intro": "Selamat datang ke Pembantu Pemilihan DJ. Agent Skill ini membantu anda menyediakan set DJ. Anda akan mengesahkan keperluan dalam dua pusingan dan menerima cadangan trek. Peraturan pengisian:",
    "tutorial_label": "Panduan import Set satu klik",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[Pusingan 1: maklumat penting]",
      "rules": [
        "1. Anda boleh menyalin contoh, mengisi secara bebas atau membiarkannya kosong",
        "2. Ruang kosong bermaksud AI akan menilai jawapan dengan bijak"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "Situasi",
          "example": "Konteks persembahan. Contoh: `bar` / `kelab` / `perkahwinan` / `pameran seni`"
        },
        {
          "key": "target_market",
          "label": "Negara / wilayah sasaran",
          "example": "Contoh: `China tanah besar` / `Taiwan` / `Hong Kong` / `Jepun` / `pasaran antarabangsa berbahasa Inggeris`"
        },
        {
          "key": "core_sound",
          "label": "Arah bunyi utama",
          "example": "Artis, trek dan genre rujukan. Contoh: `Tears` oleh `Skrillex`, genre `UK Bass` moden"
        },
        {
          "key": "track_count_or_duration",
          "label": "Bilangan trek atau tempoh set",
          "example": "Contoh: `20 trek` / `60 minit`"
        },
        {
          "key": "output_mode",
          "label": "Versi output",
          "example": "Pilihan Fast / Brief / Rich"
        },
        {
          "key": "other",
          "label": "Batasan lain",
          "example": "Contoh: `elakkan trek yang terlalu kerap dimainkan`, `tanpa vokal`, `Remix sahaja`; pilihan"
        }
      ],
      "prompt": "Selamat datang ke Pembantu Pemilihan DJ. Agent Skill ini membantu anda menyediakan set DJ. Anda akan mengesahkan keperluan dalam dua pusingan dan menerima cadangan trek. Peraturan pengisian:\n\n1. Anda boleh menyalin contoh, mengisi secara bebas atau membiarkannya kosong\n2. Ruang kosong bermaksud AI akan menilai jawapan dengan bijak\n\n[Pusingan 1: maklumat penting]\n\nSituasi:\n“Konteks persembahan. Contoh: `bar` / `kelab` / `perkahwinan` / `pameran seni`”\nNegara / wilayah sasaran:\n“Contoh: `China tanah besar` / `Taiwan` / `Hong Kong` / `Jepun` / `pasaran antarabangsa berbahasa Inggeris`”\nArah bunyi utama:\n“Artis, trek dan genre rujukan. Contoh: `Tears` oleh `Skrillex`, genre `UK Bass` moden”\nBilangan trek atau tempoh set:\n“Contoh: `20 trek` / `60 minit`”\nVersi output:\n“`Fast`: playlist pantas; kualiti mungkin lebih rendah”\n“`Brief`: satu playlist gabungan sahaja”\n“`Rich`: paparan gaya, situasi dan penemuan secara berasingan, kemudian playlist gabungan akhir”\nBatasan lain:\n“Contoh: `elakkan trek yang terlalu kerap dimainkan`, `tanpa vokal`, `Remix sahaja`; pilihan”\n\n\u0060\u0060\u0060markdown\nSituasi:\nNegara / wilayah sasaran:\nArah bunyi utama:\nBilangan trek atau tempoh set:\nVersi output:\nBatasan lain:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[Pusingan 2: perincikan permintaan]",
      "rules": [
        "1. Anda boleh menyalin contoh, mengisi secara bebas atau membiarkannya kosong"
      ],
      "fields": [
        {
          "key": "style",
          "label": "Gaya khusus",
          "example": "Contoh: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "Kelajuan / BPM",
          "example": "Contoh: `105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "Keakraban dan penemuan",
          "example": "`Akrab` / `Seimbang` / `Penemuan`"
        },
        {
          "key": "era_classic",
          "label": "Era dan klasik",
          "example": "`Kontemporari` / `Beberapa sauh klasik` / `Jambatan baharu-lama` / `Klasik dahulu`"
        },
        {
          "key": "mood",
          "label": "Suasana",
          "example": "Contoh: `nostalgia` / `sejuk` / `romantik`"
        },
        {
          "key": "energy",
          "label": "Tahap atau lengkung tenaga SET",
          "example": "Contoh: `rendah` / `tinggi`; `stabil` / `roller coaster`"
        },
        {
          "key": "platform",
          "label": "Platform dan keperluan pautan",
          "example": "Contoh: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; satu platform bermaksud hanya itu, beberapa mengikut keutamaan"
        },
        {
          "key": "other",
          "label": "Lain-lain",
          "example": ""
        }
      ],
      "prompt": "[Pusingan 2: perincikan permintaan]\n\nGaya khusus:\n“Contoh: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`”\nKelajuan / BPM:\n“Contoh: `105` / `128` / `140` / `150` / `170`”\nKeakraban dan penemuan:\n“`Akrab` / `Seimbang` / `Penemuan`”\nEra dan klasik:\n“`Kontemporari` / `Beberapa sauh klasik` / `Jambatan baharu-lama` / `Klasik dahulu`”\nSuasana:\n“Contoh: `nostalgia` / `sejuk` / `romantik`”\nTahap atau lengkung tenaga SET:\n“Contoh: `rendah` / `tinggi`; `stabil` / `roller coaster`”\nPlatform dan keperluan pautan:\n“Contoh: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; satu platform bermaksud hanya itu, beberapa mengikut keutamaan”\nLain-lain:\n\n\u0060\u0060\u0060markdown\nGaya khusus:\nKelajuan / BPM:\nKeakraban dan penemuan:\nEra dan klasik:\nSuasana:\nTahap atau lengkung tenaga SET:\nPlatform dan keperluan pautan:\nLain-lain:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# Mod Fast",
      "first_batch_title": "# Kumpulan Fast pertama",
      "final_title": "# Mod Fast",
      "columns": [
        "Trek",
        "Artis",
        "Pautan"
      ],
      "next_steps": [
        {
          "label": "Pertama | Kongsi maklum balas pilihan",
          "body": "Jika mahu, balas dalam bahasa semula jadi tentang cara pilihan itu berfungsi. Ini memperbaiki pilihan peribadi dan cadangan seterusnya."
        },
        {
          "label": "Kedua | Eksport atau serahkan playlist",
          "body": "Anda boleh keluarkan playlist teks atau menyerahkannya kepada W4DJ. Balas `output text playlist` atau `export to w4dj`."
        }
      ],
      "digging_notes": "Nota digging",
      "mix_suggestion": "Cadangan mixing",
      "unknown": "Tidak diketahui",
      "verified": "Disahkan",
      "target_platform_missing": "Platform sasaran tidak tersedia"
    },
    "brief": {
      "title": "# Mod Brief",
      "first_batch_title": "# Mod Brief",
      "final_title": "# Mod Brief",
      "columns": [
        "Trek",
        "Artis",
        "Album / EP",
        "Gaya",
        "BPM",
        "Nada",
        "Tempoh",
        "Tenaga",
        "Tarikh keluaran",
        "Nota",
        "Sebab dipilih",
        "Pautan"
      ],
      "next_steps": [
        {
          "label": "Pertama | Kongsi maklum balas pilihan",
          "body": "Jika mahu, balas dalam bahasa semula jadi tentang cara pilihan itu berfungsi. Ini memperbaiki pilihan peribadi dan cadangan seterusnya."
        },
        {
          "label": "Kedua | Eksport atau serahkan playlist",
          "body": "Anda boleh keluarkan playlist teks atau menyerahkannya kepada W4DJ. Balas `output text playlist` atau `export to w4dj`."
        },
        {
          "label": "Ketiga | Susunan harmonik set",
          "body": "Mahukah saya menyusun set menggunakan roda Camelot?"
        }
      ],
      "digging_notes": "Nota digging",
      "mix_suggestion": "Cadangan mixing",
      "unknown": "Tidak diketahui",
      "verified": "Disahkan",
      "target_platform_missing": "Platform sasaran tidak tersedia"
    },
    "rich": {
      "title": "# Mod Rich",
      "first_batch_title": "# Mod Rich",
      "final_title": "# Mod Rich",
      "columns": [
        "Trek",
        "Artis",
        "Album / EP",
        "Gaya",
        "BPM",
        "Nada",
        "Tempoh",
        "Tenaga",
        "Tarikh keluaran",
        "Nota",
        "Sebab dipilih",
        "Pautan"
      ],
      "next_steps": [
        {
          "label": "Pertama | Kongsi maklum balas pilihan",
          "body": "Jika mahu, balas dalam bahasa semula jadi tentang cara pilihan itu berfungsi. Ini memperbaiki pilihan peribadi dan cadangan seterusnya."
        },
        {
          "label": "Kedua | Eksport atau serahkan playlist",
          "body": "Anda boleh keluarkan playlist teks atau menyerahkannya kepada W4DJ. Balas `output text playlist` atau `export to w4dj`."
        },
        {
          "label": "Ketiga | Susunan harmonik set",
          "body": "Mahukah saya menyusun set menggunakan roda Camelot?"
        }
      ],
      "digging_notes": "Nota digging",
      "mix_suggestion": "Cadangan mixing",
      "unknown": "Tidak diketahui",
      "verified": "Disahkan",
      "target_platform_missing": "Platform sasaran tidak tersedia",
      "view_titles": [
        "Paparan gaya",
        "Paparan situasi",
        "Paparan keakraban / penemuan",
        "Paparan gabungan dinamik"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "Kongsi maklum balas",
      "positive": [
        "Saya suka trek ini"
      ],
      "negative": [
        "Saya tidak suka trek ini"
      ],
      "ambiguous": [
        "Saya tidak pasti tentang trek ini"
      ]
    },
    "export_w4dj": {
      "label": "Eksport ke W4DJ",
      "positive": [
        "Eksport ke W4DJ"
      ],
      "negative": [
        "Jangan eksport ke W4DJ"
      ],
      "ambiguous": [
        "Mungkin eksport ke W4DJ"
      ]
    },
    "output_text_playlist": {
      "label": "Keluarkan playlist teks",
      "positive": [
        "Keluarkan playlist teks"
      ],
      "negative": [
        "Jangan keluarkan playlist teks"
      ],
      "ambiguous": [
        "Mungkin keluarkan playlist teks"
      ]
    },
    "harmonic_reorder": {
      "label": "Susun semula secara harmonik",
      "positive": [
        "Susun mengikut roda Camelot"
      ],
      "negative": [
        "Jangan susun semula"
      ],
      "ambiguous": [
        "Mungkin susun mengikut roda Camelot"
      ]
    },
    "confirm_long_term_memory": {
      "label": "Sahkan memori jangka panjang",
      "positive": [
        "Ingat pilihan ini"
      ],
      "negative": [
        "Jangan simpan pilihan ini"
      ],
      "ambiguous": [
        "Mungkin ingat pilihan ini"
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
      "sahaja",
      "hanya",
      "gunakan hanya"
    ],
    "preferred_markers": [
      "keutamaan",
      "utamakan",
      "pilihan utama"
    ],
    "fallback_markers": [
      "sandaran",
      "alternatif",
      "jika tidak tersedia"
    ],
    "forbidden_markers": [
      "jangan gunakan",
      "kecualikan",
      "tanpa"
    ]
  },
  "status": {
    "unknown": "Tidak diketahui",
    "verified": "Disahkan",
    "target_platform_missing": "Platform sasaran tidak tersedia"
  },
  "export": {
    "text": "Keluarkan playlist teks yang boleh disalin dalam susunan semasa.",
    "w4dj": "Cipta fail serahan UTF-8 `.w4dj` untuk W4DJ.",
    "harmonic": "Minta susunan roda Camelot menggunakan nada yang diketahui.",
    "feedback": "Maklum balas bahasa semula jadi hanya mengemas kini sesi; simpanan jangka panjang memerlukan pengesahan.",
    "memory_confirmation": "Saya memahami ini sebagai ringkasan ringkas perubahan cita rasa. Simpan dalam profil peribadi jangka panjang?"
  }
}
```
