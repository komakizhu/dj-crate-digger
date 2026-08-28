# Indonesian locale pack

This file is the fixed Bahasa Indonesia UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "id",
  "language_name": "Indonesian",
  "native_name": "Bahasa Indonesia",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "Jika wilayah kosong, gunakan pasar berbahasa Indonesia yang luas hanya untuk sesi ini.",
    "explicit_region": "Negara atau wilayah yang disebutkan secara eksplisit mengalahkan inferensi bahasa tanpa mengubah bahasa komunikasi.",
    "persistence": "Jangan simpan pasar target sebagai preferensi jangka panjang."
  },
  "quick_start": {
    "intro": "Selamat datang di Asisten Pemilihan DJ. Skill Agent ini membantu Anda menyiapkan set DJ. Anda akan mengonfirmasi kebutuhan dalam dua putaran dan menerima rekomendasi track. Aturan pengisian:",
    "tutorial_label": "Panduan impor Set sekali klik",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[Putaran 1: informasi penting]",
      "rules": [
        "1. Anda dapat menyalin contoh, mengisi dengan bebas, atau membiarkannya kosong",
        "2. Kolom kosong berarti AI akan menilai jawabannya secara cerdas"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "Situasi",
          "example": "Konteks pertunjukan. Contoh: `bar` / `klub` / `pernikahan` / `pameran seni`"
        },
        {
          "key": "target_market",
          "label": "Negara / wilayah target",
          "example": "Contoh: `Tiongkok daratan` / `Taiwan` / `Hong Kong` / `Jepang` / `pasar internasional berbahasa Inggris`"
        },
        {
          "key": "core_sound",
          "label": "Arah suara utama",
          "example": "Artis, track, dan genre referensi. Contoh: `Tears` oleh `Skrillex`, genre `UK Bass` modern"
        },
        {
          "key": "track_count_or_duration",
          "label": "Jumlah track atau durasi set",
          "example": "Contoh: `20 track` / `60 menit`"
        },
        {
          "key": "output_mode",
          "label": "Versi keluaran",
          "example": "Pilihan Fast / Brief / Rich"
        },
        {
          "key": "other",
          "label": "Batasan lain",
          "example": "Contoh: `hindari track yang terlalu sering diputar`, `tanpa vokal`, `hanya Remix`; opsional"
        }
      ],
      "prompt": "Selamat datang di Asisten Pemilihan DJ. Skill Agent ini membantu Anda menyiapkan set DJ. Anda akan mengonfirmasi kebutuhan dalam dua putaran dan menerima rekomendasi track. Aturan pengisian:\n\n1. Anda dapat menyalin contoh, mengisi dengan bebas, atau membiarkannya kosong\n2. Kolom kosong berarti AI akan menilai jawabannya secara cerdas\n\n[Putaran 1: informasi penting]\n\nSituasi:\n“Konteks pertunjukan. Contoh: `bar` / `klub` / `pernikahan` / `pameran seni`”\nNegara / wilayah target:\n“Contoh: `Tiongkok daratan` / `Taiwan` / `Hong Kong` / `Jepang` / `pasar internasional berbahasa Inggris`”\nArah suara utama:\n“Artis, track, dan genre referensi. Contoh: `Tears` oleh `Skrillex`, genre `UK Bass` modern”\nJumlah track atau durasi set:\n“Contoh: `20 track` / `60 menit`”\nVersi keluaran:\n“`Fast`: playlist cepat; kualitas mungkin lebih rendah”\n“`Brief`: hanya satu playlist gabungan”\n“`Rich`: tampilan gaya, situasi, dan penemuan terpisah, lalu playlist gabungan akhir”\nBatasan lain:\n“Contoh: `hindari track yang terlalu sering diputar`, `tanpa vokal`, `hanya Remix`; opsional”\n\n\u0060\u0060\u0060markdown\nSituasi:\nNegara / wilayah target:\nArah suara utama:\nJumlah track atau durasi set:\nVersi keluaran:\nBatasan lain:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[Putaran 2: merinci permintaan]",
      "rules": [
        "1. Anda dapat menyalin contoh, mengisi dengan bebas, atau membiarkannya kosong"
      ],
      "fields": [
        {
          "key": "style",
          "label": "Gaya spesifik",
          "example": "Contoh: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "Kecepatan / BPM",
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
          "example": "`Kontemporer` / `Sedikit jangkar klasik` / `Jembatan baru-lama` / `Klasik dahulu`"
        },
        {
          "key": "mood",
          "label": "Suasana",
          "example": "Contoh: `nostalgia` / `dingin` / `romantis`"
        },
        {
          "key": "energy",
          "label": "Level atau kurva energi SET",
          "example": "Contoh: `rendah` / `tinggi`; `stabil` / `naik turun tajam`"
        },
        {
          "key": "platform",
          "label": "Platform dan persyaratan tautan",
          "example": "Contoh: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; satu platform berarti hanya itu, beberapa mengikuti urutan prioritas"
        },
        {
          "key": "other",
          "label": "Lainnya",
          "example": ""
        }
      ],
      "prompt": "[Putaran 2: merinci permintaan]\n\nGaya spesifik:\n“Contoh: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`”\nKecepatan / BPM:\n“Contoh: `105` / `128` / `140` / `150` / `170`”\nKeakraban dan penemuan:\n“`Akrab` / `Seimbang` / `Penemuan`”\nEra dan klasik:\n“`Kontemporer` / `Sedikit jangkar klasik` / `Jembatan baru-lama` / `Klasik dahulu`”\nSuasana:\n“Contoh: `nostalgia` / `dingin` / `romantis`”\nLevel atau kurva energi SET:\n“Contoh: `rendah` / `tinggi`; `stabil` / `naik turun tajam`”\nPlatform dan persyaratan tautan:\n“Contoh: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; satu platform berarti hanya itu, beberapa mengikuti urutan prioritas”\nLainnya:\n\n\u0060\u0060\u0060markdown\nGaya spesifik:\nKecepatan / BPM:\nKeakraban dan penemuan:\nEra dan klasik:\nSuasana:\nLevel atau kurva energi SET:\nPlatform dan persyaratan tautan:\nLainnya:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# Mode Fast",
      "first_batch_title": "# Batch pertama Fast",
      "final_title": "# Mode Fast",
      "columns": [
        "Track",
        "Artis",
        "Tautan"
      ],
      "next_steps": [
        {
          "label": "Pertama | Bagikan masukan pilihan",
          "body": "Jika mau, balas dengan bahasa alami tentang hasil pilihan. Ini membantu memperbaiki preferensi pilihan pribadi dan rekomendasi berikutnya."
        },
        {
          "label": "Kedua | Ekspor atau serahkan playlist",
          "body": "Anda dapat membuat playlist teks atau menyerahkannya ke W4DJ. Balas `output text playlist` atau `export to w4dj`."
        }
      ],
      "digging_notes": "Catatan digging",
      "mix_suggestion": "Saran mixing",
      "unknown": "Tidak diketahui",
      "verified": "Terverifikasi",
      "target_platform_missing": "Platform target tidak tersedia"
    },
    "brief": {
      "title": "# Mode Brief",
      "first_batch_title": "# Mode Brief",
      "final_title": "# Mode Brief",
      "columns": [
        "Track",
        "Artis",
        "Album / EP",
        "Gaya",
        "BPM",
        "Nada",
        "Durasi",
        "Energi",
        "Tanggal rilis",
        "Catatan",
        "Alasan dipilih",
        "Tautan"
      ],
      "next_steps": [
        {
          "label": "Pertama | Bagikan masukan pilihan",
          "body": "Jika mau, balas dengan bahasa alami tentang hasil pilihan. Ini membantu memperbaiki preferensi pilihan pribadi dan rekomendasi berikutnya."
        },
        {
          "label": "Kedua | Ekspor atau serahkan playlist",
          "body": "Anda dapat membuat playlist teks atau menyerahkannya ke W4DJ. Balas `output text playlist` atau `export to w4dj`."
        },
        {
          "label": "Ketiga | Urutan harmonis set",
          "body": "Ingin saya mengurutkan set menggunakan roda Camelot?"
        }
      ],
      "digging_notes": "Catatan digging",
      "mix_suggestion": "Saran mixing",
      "unknown": "Tidak diketahui",
      "verified": "Terverifikasi",
      "target_platform_missing": "Platform target tidak tersedia"
    },
    "rich": {
      "title": "# Mode Rich",
      "first_batch_title": "# Mode Rich",
      "final_title": "# Mode Rich",
      "columns": [
        "Track",
        "Artis",
        "Album / EP",
        "Gaya",
        "BPM",
        "Nada",
        "Durasi",
        "Energi",
        "Tanggal rilis",
        "Catatan",
        "Alasan dipilih",
        "Tautan"
      ],
      "next_steps": [
        {
          "label": "Pertama | Bagikan masukan pilihan",
          "body": "Jika mau, balas dengan bahasa alami tentang hasil pilihan. Ini membantu memperbaiki preferensi pilihan pribadi dan rekomendasi berikutnya."
        },
        {
          "label": "Kedua | Ekspor atau serahkan playlist",
          "body": "Anda dapat membuat playlist teks atau menyerahkannya ke W4DJ. Balas `output text playlist` atau `export to w4dj`."
        },
        {
          "label": "Ketiga | Urutan harmonis set",
          "body": "Ingin saya mengurutkan set menggunakan roda Camelot?"
        }
      ],
      "digging_notes": "Catatan digging",
      "mix_suggestion": "Saran mixing",
      "unknown": "Tidak diketahui",
      "verified": "Terverifikasi",
      "target_platform_missing": "Platform target tidak tersedia",
      "view_titles": [
        "Tampilan gaya",
        "Tampilan situasi",
        "Tampilan keakraban / penemuan",
        "Tampilan gabungan dinamis"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "Bagikan masukan",
      "positive": [
        "Saya suka track ini"
      ],
      "negative": [
        "Saya tidak suka track ini"
      ],
      "ambiguous": [
        "Saya belum yakin tentang track ini"
      ]
    },
    "export_w4dj": {
      "label": "Ekspor ke W4DJ",
      "positive": [
        "Ekspor ke W4DJ"
      ],
      "negative": [
        "Jangan ekspor ke W4DJ"
      ],
      "ambiguous": [
        "Mungkin ekspor ke W4DJ"
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
      "label": "Susun ulang harmonis",
      "positive": [
        "Susun dengan roda Camelot"
      ],
      "negative": [
        "Jangan susun ulang"
      ],
      "ambiguous": [
        "Mungkin susun dengan roda Camelot"
      ]
    },
    "confirm_long_term_memory": {
      "label": "Konfirmasi memori jangka panjang",
      "positive": [
        "Ingat preferensi ini"
      ],
      "negative": [
        "Jangan simpan preferensi ini"
      ],
      "ambiguous": [
        "Mungkin ingat preferensi ini"
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
      "hanya",
      "saja",
      "gunakan hanya"
    ],
    "preferred_markers": [
      "prioritas",
      "lebih suka",
      "pilihan utama"
    ],
    "fallback_markers": [
      "cadangan",
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
    "verified": "Terverifikasi",
    "target_platform_missing": "Platform target tidak tersedia"
  },
  "export": {
    "text": "Keluarkan playlist teks yang dapat disalin dalam urutan saat ini.",
    "w4dj": "Buat berkas serah-terima UTF-8 `.w4dj` untuk W4DJ.",
    "harmonic": "Minta pengurutan roda Camelot menggunakan nada yang diketahui.",
    "feedback": "Masukan bahasa alami hanya memperbarui sesi; penyimpanan jangka panjang memerlukan konfirmasi.",
    "memory_confirmation": "Saya memahami ini sebagai ringkasan singkat perubahan selera. Simpan ke profil pribadi jangka panjang?"
  },
  "trigger_capsule": [
    "set DJ",
    "playlist",
    "mencari musik",
    "mencari track",
    "menyusun set"
  ]
}
```
