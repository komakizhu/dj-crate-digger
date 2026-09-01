# Filipino locale pack

This file is the fixed Filipino UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "fil",
  "language_name": "Filipino",
  "native_name": "Filipino",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "Kung blangko ang rehiyon, malawak na Filipino-language market lang ang gamitin para sa session na ito.",
    "explicit_region": "Ang tahasang bansa o rehiyon ay mas mahalaga kaysa language inference nang hindi binabago ang communication language.",
    "persistence": "Huwag i-save ang target market bilang pangmatagalang preference."
  },
  "quick_start": {
    "intro": "Maligayang pagdating sa DJ Selection Assistant. Tinutulungan ka ng Agent Skill na ito na bumuo ng DJ set. Kukumpirmahin mo ang pangangailangan sa dalawang round at makakatanggap ng mga track recommendation. Mga tuntunin sa pag-fill:",
    "tutorial_label": "Gabay sa one-click Set import",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[Unang round: kinakailangang impormasyon]",
      "rules": [
        "1. Maaaring kopyahin ang halimbawa, magsulat nang malaya, o iwang blangko",
        "2. Ang blangkong field ay nangangahulugang AI ang matalinong huhusga sa sagot"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "Konteksto",
          "example": "Konteksto ng performance. Halimbawa: `bar` / `club` / `kasal` / `art exhibition`"
        },
        {
          "key": "target_market",
          "label": "Target na bansa / rehiyon",
          "example": "Halimbawa: `Mainland China` / `Taiwan` / `Hong Kong` / `Japan` / `international English market`"
        },
        {
          "key": "core_sound",
          "label": "Pangunahing direksiyon ng tunog",
          "example": "Reference artist, track, at genre. Halimbawa: `Tears` ni `Skrillex`, modernong `UK Bass`"
        },
        {
          "key": "track_count_or_duration",
          "label": "Bilang ng track o haba ng set",
          "example": "Halimbawa: `20 tracks` / `60 minutes`"
        },
        {
          "key": "output_mode",
          "label": "Bersyon ng output",
          "example": "Piliin ang Fast / Brief / Rich"
        },
        {
          "key": "other",
          "label": "Iba pang limitasyon",
          "example": "Halimbawa: `iwasan ang gasgas na track`, `walang vocal`, `Remix lang`; opsyonal"
        }
      ],
      "prompt": "Maligayang pagdating sa DJ Selection Assistant. Tinutulungan ka ng Agent Skill na ito na bumuo ng DJ set. Kukumpirmahin mo ang pangangailangan sa dalawang round at makakatanggap ng mga track recommendation. Mga tuntunin sa pag-fill:\n\n1. Maaaring kopyahin ang halimbawa, magsulat nang malaya, o iwang blangko\n2. Ang blangkong field ay nangangahulugang AI ang matalinong huhusga sa sagot\n\n[Unang round: kinakailangang impormasyon]\n\nKonteksto:\n“Konteksto ng performance. Halimbawa: `bar` / `club` / `kasal` / `art exhibition`”\nTarget na bansa / rehiyon:\n“Halimbawa: `Mainland China` / `Taiwan` / `Hong Kong` / `Japan` / `international English market`”\nPangunahing direksiyon ng tunog:\n“Reference artist, track, at genre. Halimbawa: `Tears` ni `Skrillex`, modernong `UK Bass`”\nBilang ng track o haba ng set:\n“Halimbawa: `20 tracks` / `60 minutes`”\nBersyon ng output:\n“`Fast`: mabilis na playlist; maaaring mas mababa ang kalidad”\n“`Brief`: isang pinagsamang playlist lamang”\n“`Rich`: magkahiwalay na style, context, at discovery view, kasunod ang final na pinagsamang playlist”\nIba pang limitasyon:\n“Halimbawa: `iwasan ang gasgas na track`, `walang vocal`, `Remix lang`; opsyonal”\n\n\u0060\u0060\u0060markdown\nKonteksto:\nTarget na bansa / rehiyon:\nPangunahing direksiyon ng tunog:\nBilang ng track o haba ng set:\nBersyon ng output:\nIba pang limitasyon:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[Ikalawang round: linawin ang request]",
      "rules": [
        "1. Maaaring kopyahin ang halimbawa, magsulat nang malaya, o iwang blangko"
      ],
      "fields": [
        {
          "key": "style",
          "label": "Tiyak na style",
          "example": "Halimbawa: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "Bilis / BPM",
          "example": "Halimbawa: `105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "Pagkakakilala at discovery",
          "example": "`Pamilyar` / `Balanse` / `Discovery`"
        },
        {
          "key": "era_classic",
          "label": "Panahon at classics",
          "example": "`Contemporary` / `Kaunting classic anchor` / `Tulay ng bago at luma` / `Classics muna`"
        },
        {
          "key": "mood",
          "label": "Mood",
          "example": "Halimbawa: `nostalgic` / `malamig` / `romantic`"
        },
        {
          "key": "energy",
          "label": "Antas o kurba ng enerhiya ng SET",
          "example": "Halimbawa: `mababa` / `mataas`; `steady` / `roller coaster`"
        },
        {
          "key": "platform",
          "label": "Platform at mga kinakailangan sa link",
          "example": "Halimbawa: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; kung isa, iyon lang; kung marami, sundin ang pagkakasunod"
        },
        {
          "key": "other",
          "label": "Iba pa",
          "example": ""
        }
      ],
      "prompt": "[Ikalawang round: linawin ang request]\n\nTiyak na style:\n“Halimbawa: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`”\nBilis / BPM:\n“Halimbawa: `105` / `128` / `140` / `150` / `170`”\nPagkakakilala at discovery:\n“`Pamilyar` / `Balanse` / `Discovery`”\nPanahon at classics:\n“`Contemporary` / `Kaunting classic anchor` / `Tulay ng bago at luma` / `Classics muna`”\nMood:\n“Halimbawa: `nostalgic` / `malamig` / `romantic`”\nAntas o kurba ng enerhiya ng SET:\n“Halimbawa: `mababa` / `mataas`; `steady` / `roller coaster`”\nPlatform at mga kinakailangan sa link:\n“Halimbawa: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; kung isa, iyon lang; kung marami, sundin ang pagkakasunod”\nIba pa:\n\n\u0060\u0060\u0060markdown\nTiyak na style:\nBilis / BPM:\nPagkakakilala at discovery:\nPanahon at classics:\nMood:\nAntas o kurba ng enerhiya ng SET:\nPlatform at mga kinakailangan sa link:\nIba pa:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# Fast mode",
      "first_batch_title": "# Unang Fast batch",
      "final_title": "# Fast mode",
      "columns": [
        "Track",
        "Artist",
        "Link"
      ],
      "next_steps": [
        {
          "label": "Una | Magbahagi ng feedback sa pagpili",
          "body": "Kung gusto, tumugon sa natural na wika tungkol sa naging gamit ng mga napili. Pinapahusay nito ang pribadong preference at susunod na recommendation."
        },
        {
          "label": "Ikalawa | I-export o ipasa ang playlist",
          "body": "Maaari kang maglabas ng text playlist o ipasa ito sa W4DJ. Tumugon ng `output text playlist` o `export to w4dj`."
        }
      ],
      "digging_notes": "Digging notes",
      "mix_suggestion": "Mix suggestion",
      "unknown": "Hindi alam",
      "verified": "Na-verify",
      "target_platform_missing": "Hindi available ang target platform"
    },
    "brief": {
      "title": "# Brief mode",
      "first_batch_title": "# Brief mode",
      "final_title": "# Brief mode",
      "columns": [
        "Track",
        "Artist",
        "Album / EP",
        "Style",
        "BPM",
        "Key",
        "Tagal",
        "Energy",
        "Petsa ng release",
        "Notes",
        "Dahilan ng pagpili",
        "Link"
      ],
      "next_steps": [
        {
          "label": "Una | Magbahagi ng feedback sa pagpili",
          "body": "Kung gusto, tumugon sa natural na wika tungkol sa naging gamit ng mga napili. Pinapahusay nito ang pribadong preference at susunod na recommendation."
        },
        {
          "label": "Ikalawa | I-export o ipasa ang playlist",
          "body": "Maaari kang maglabas ng text playlist o ipasa ito sa W4DJ. Tumugon ng `output text playlist` o `export to w4dj`."
        },
        {
          "label": "Ikatlo | Harmonic set order",
          "body": "Gusto mo bang ayusin ko ang set gamit ang Camelot wheel?"
        }
      ],
      "digging_notes": "Digging notes",
      "mix_suggestion": "Mix suggestion",
      "unknown": "Hindi alam",
      "verified": "Na-verify",
      "target_platform_missing": "Hindi available ang target platform"
    },
    "rich": {
      "title": "# Rich mode",
      "first_batch_title": "# Rich mode",
      "final_title": "# Rich mode",
      "columns": [
        "Track",
        "Artist",
        "Album / EP",
        "Style",
        "BPM",
        "Key",
        "Tagal",
        "Energy",
        "Petsa ng release",
        "Notes",
        "Dahilan ng pagpili",
        "Link"
      ],
      "next_steps": [
        {
          "label": "Una | Magbahagi ng feedback sa pagpili",
          "body": "Kung gusto, tumugon sa natural na wika tungkol sa naging gamit ng mga napili. Pinapahusay nito ang pribadong preference at susunod na recommendation."
        },
        {
          "label": "Ikalawa | I-export o ipasa ang playlist",
          "body": "Maaari kang maglabas ng text playlist o ipasa ito sa W4DJ. Tumugon ng `output text playlist` o `export to w4dj`."
        },
        {
          "label": "Ikatlo | Harmonic set order",
          "body": "Gusto mo bang ayusin ko ang set gamit ang Camelot wheel?"
        }
      ],
      "digging_notes": "Digging notes",
      "mix_suggestion": "Mix suggestion",
      "unknown": "Hindi alam",
      "verified": "Na-verify",
      "target_platform_missing": "Hindi available ang target platform",
      "view_titles": [
        "Style view",
        "Context view",
        "Familiarity / discovery view",
        "Dynamic combined view"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "Magbahagi ng feedback",
      "positive": [
        "Gusto ko ang track na ito"
      ],
      "negative": [
        "Hindi ko gusto ang track na ito"
      ],
      "ambiguous": [
        "Hindi ako sigurado sa track na ito"
      ]
    },
    "export_w4dj": {
      "label": "I-export sa W4DJ",
      "positive": [
        "I-export sa W4DJ"
      ],
      "negative": [
        "Huwag i-export sa W4DJ"
      ],
      "ambiguous": [
        "Baka i-export sa W4DJ"
      ]
    },
    "output_text_playlist": {
      "label": "Maglabas ng text playlist",
      "positive": [
        "Maglabas ng text playlist"
      ],
      "negative": [
        "Huwag maglabas ng text playlist"
      ],
      "ambiguous": [
        "Baka maglabas ng text playlist"
      ]
    },
    "harmonic_reorder": {
      "label": "Harmonic reorder",
      "positive": [
        "Ayusin gamit ang Camelot wheel"
      ],
      "negative": [
        "Huwag i-reorder"
      ],
      "ambiguous": [
        "Baka ayusin gamit ang Camelot wheel"
      ]
    },
    "confirm_long_term_memory": {
      "label": "Kumpirmahin ang long-term memory",
      "positive": [
        "Tandaan ang preference na ito"
      ],
      "negative": [
        "Huwag i-save ang preference na ito"
      ],
      "ambiguous": [
        "Baka tandaan ang preference na ito"
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
      "lang",
      "lamang",
      "gamitin lang"
    ],
    "preferred_markers": [
      "mas gusto",
      "priority",
      "unang pili"
    ],
    "fallback_markers": [
      "backup",
      "alternatibo",
      "kung hindi available"
    ],
    "forbidden_markers": [
      "huwag gamitin",
      "ibukod",
      "walang"
    ]
  },
  "status": {
    "unknown": "Hindi alam",
    "verified": "Na-verify",
    "target_platform_missing": "Hindi available ang target platform"
  },
  "export": {
    "text": "Maglabas ng makokopyang text playlist sa kasalukuyang ayos.",
    "w4dj": "Gumawa ng UTF-8 `.w4dj` handoff file para sa W4DJ.",
    "harmonic": "Humiling ng ayos ayon sa Camelot wheel gamit ang mga kilalang key.",
    "feedback": "Ang natural-language feedback ay nag-a-update lang ng session; kailangan ng kumpirmasyon para sa long-term storage.",
    "memory_confirmation": "Naiintindihan ko ito bilang maikling buod ng pagbabago sa panlasa. I-save sa pribadong long-term profile?"
  },
  "trigger_capsule": [
    "DJ set",
    "playlist",
    "maghanap ng musika",
    "maghanap ng track",
    "bumuo ng set"
  ]
}
```
