# English locale pack

This file is the fixed English UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "en",
  "language_name": "English",
  "native_name": "English",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "Use a broad English-language market for this session only when the user leaves the region blank.",
    "explicit_region": "An explicitly named country or region overrides language inference without changing the communication language.",
    "persistence": "Never persist the inferred or user-provided target market as a long-term preference."
  },
  "quick_start": {
    "intro": "Welcome to DJ Selection Assistant. This Agent Skill helps you build a DJ set. You will confirm your request in two rounds and receive AI track recommendations. Fill-in rules:",
    "tutorial_label": "One-Click Set Import Tutorial",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[Round 1: Essentials]",
      "rules": [
        "1. You can copy from an example, fill freely, or leave blank",
        "2. Leaving a field blank means the AI will judge the answer intelligently"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "Scene",
          "example": "Performance setting. Examples: `bar` / `club` / `wedding` / `art exhibition`"
        },
        {
          "key": "target_market",
          "label": "Target country / region",
          "example": "Examples: `Mainland China` / `Taiwan` / `Hong Kong` / `Japan` / `international English-language market`"
        },
        {
          "key": "core_sound",
          "label": "Core sound direction",
          "example": "Reference artist, track, and genre. Example: `Tears` by `Skrillex`, `modern UK Bass` genre"
        },
        {
          "key": "track_count_or_duration",
          "label": "Track count or set duration",
          "example": "Examples: `20 tracks` / `60 minutes`"
        },
        {
          "key": "output_mode",
          "label": "Output version",
          "example": "Fast / Brief / Rich output choices"
        },
        {
          "key": "other",
          "label": "Other constraints",
          "example": "Examples: `avoid overplayed tracks`, `no vocals`, `Remix only`; optional"
        }
      ],
      "prompt": "Welcome to DJ Selection Assistant. This Agent Skill helps you build a DJ set. You will confirm your request in two rounds and receive AI track recommendations. Fill-in rules:\n\n1. You can copy from an example, fill freely, or leave blank\n2. Leaving a field blank means the AI will judge the answer intelligently\n\n[Round 1: Essentials]\n\nScene:\n“Performance setting. Examples: `bar` / `club` / `wedding` / `art exhibition`”\nTarget country / region:\n“Examples: `Mainland China` / `Taiwan` / `Hong Kong` / `Japan` / `international English-language market`”\nCore sound direction:\n“Reference artist, track, and genre. Example: `Tears` by `Skrillex`, `modern UK Bass` genre”\nTrack count or set duration:\n“Examples: `20 tracks` / `60 minutes`”\nOutput version:\n“`Fast`: quick playlist output; quality may be lower”\n“`Brief`: one combined playlist only”\n“`Rich`: separate style, scene, familiarity/discovery views, followed by a final combined playlist”\nOther constraints:\n“Examples: `avoid overplayed tracks`, `no vocals`, `Remix only`; optional”\n\n\u0060\u0060\u0060markdown\nScene:\nTarget country / region:\nCore sound direction:\nTrack count or set duration:\nOutput version:\nOther constraints:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[Round 2: Refine the request]",
      "rules": [
        "1. You can copy from an example, fill freely, or leave blank"
      ],
      "fields": [
        {
          "key": "style",
          "label": "Specific style",
          "example": "Examples: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "Speed / BPM",
          "example": "Examples: `105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "Familiarity and discovery",
          "example": "`Familiar` / `Balanced` / `Discovery`"
        },
        {
          "key": "era_classic",
          "label": "Era and classics",
          "example": "`Contemporary` / `Light classic anchors` / `New-old bridge` / `Classics first`"
        },
        {
          "key": "mood",
          "label": "Mood",
          "example": "Examples: `nostalgic` / `cold` / `romantic`"
        },
        {
          "key": "energy",
          "label": "SET energy level or energy curve",
          "example": "Examples: `low` / `high`; `steady` / `roller coaster`"
        },
        {
          "key": "platform",
          "label": "Platform and link requirements",
          "example": "Examples: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; one platform means use it only; multiple platforms follow the listed priority"
        },
        {
          "key": "other",
          "label": "Other",
          "example": ""
        }
      ],
      "prompt": "[Round 2: Refine the request]\n\nSpecific style:\n“Examples: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`”\nSpeed / BPM:\n“Examples: `105` / `128` / `140` / `150` / `170`”\nFamiliarity and discovery:\n“`Familiar` / `Balanced` / `Discovery`”\nEra and classics:\n“`Contemporary` / `Light classic anchors` / `New-old bridge` / `Classics first`”\nMood:\n“Examples: `nostalgic` / `cold` / `romantic`”\nSET energy level or energy curve:\n“Examples: `low` / `high`; `steady` / `roller coaster`”\nPlatform and link requirements:\n“Examples: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; one platform means use it only; multiple platforms follow the listed priority”\nOther:\n\n\u0060\u0060\u0060markdown\nSpecific style:\nSpeed / BPM:\nFamiliarity and discovery:\nEra and classics:\nMood:\nSET energy level or energy curve:\nPlatform and link requirements:\nOther:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# Fast Mode",
      "first_batch_title": "# Fast Mode First Batch",
      "final_title": "# Fast Mode",
      "columns": [
        "Track",
        "Artist",
        "Link"
      ],
      "next_steps": [
        {
          "label": "First | Share selection feedback",
          "body": "If you want, reply in natural language with how the selections worked for you. This improves your private selection preferences and future recommendations. For example: “I like Skream, but I did not play it for this crowd” / “I do not like Jumping Machine; do not recommend it again” / “These are the tracks I played (image/list).”"
        },
        {
          "label": "Second | Export or hand off the playlist",
          "body": "You can output a text playlist or hand it to W4DJ. Reply `export to w4dj` or `output text playlist`.\n\nW4DJ provides one-click playlist import, converts formats after download, and imports into DJ software. Export the `.w4dj` format and download [w4dj-rkb](https://github.com/komakizhu/W4DJ-RKB). For detailed instructions, see [One-Click Set Import Tutorial](https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md).\n\n`.w4dj` uses a new minimal v2 format containing only the playlist name, positions, complete official titles, artists, and an optional string `netease_track_id`; v1 is rejected without migration.\n\nThe text-playlist action outputs copyable text that can be imported manually into NetEase Cloud Music, but it cannot import tracks into RKB with one click."
        }
      ],
      "digging_notes": "Digging notes",
      "mix_suggestion": "Mix suggestion",
      "unknown": "Unknown",
      "verified": "Verified",
      "target_platform_missing": "Target platform unavailable"
    },
    "brief": {
      "title": "# Brief Mode",
      "first_batch_title": "# Brief Mode",
      "final_title": "# Brief Mode",
      "columns": [
        "Track",
        "Artist",
        "Album / EP",
        "Style",
        "BPM",
        "Key",
        "Duration",
        "Energy",
        "Release date",
        "Notes",
        "Why selected",
        "Link"
      ],
      "next_steps": [
        {
          "label": "First | Share selection feedback",
          "body": "If you want, reply in natural language with how the selections worked for you. This improves your private selection preferences and future recommendations. For example: “I like Skream, but I did not play it for this crowd” / “I do not like Jumping Machine; do not recommend it again” / “These are the tracks I played (image/list).”"
        },
        {
          "label": "Second | Export or hand off the playlist",
          "body": "You can output a text playlist or hand it to W4DJ. Reply `export to w4dj` or `output text playlist`.\n\nW4DJ provides one-click playlist import, converts formats after download, and imports into DJ software. Export the `.w4dj` format and download [w4dj-rkb](https://github.com/komakizhu/W4DJ-RKB). For detailed instructions, see [One-Click Set Import Tutorial](https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md).\n\n`.w4dj` uses a new minimal v2 format containing only the playlist name, positions, complete official titles, artists, and an optional string `netease_track_id`; v1 is rejected without migration.\n\nThe text-playlist action outputs copyable text that can be imported manually into NetEase Cloud Music, but it cannot import tracks into RKB with one click."
        },
        {
          "label": "Third | Harmonic set order",
          "body": "Would you like me to arrange the set using the Camelot wheel?"
        }
      ],
      "digging_notes": "Digging notes",
      "mix_suggestion": "Mix suggestion",
      "unknown": "Unknown",
      "verified": "Verified",
      "target_platform_missing": "Target platform unavailable"
    },
    "rich": {
      "title": "# Rich Mode",
      "first_batch_title": "# Rich Mode",
      "final_title": "# Rich Mode",
      "columns": [
        "Track",
        "Artist",
        "Album / EP",
        "Style",
        "BPM",
        "Key",
        "Duration",
        "Energy",
        "Release date",
        "Notes",
        "Why selected",
        "Link"
      ],
      "next_steps": [
        {
          "label": "First | Share selection feedback",
          "body": "If you want, reply in natural language with how the selections worked for you. This improves your private selection preferences and future recommendations. For example: “I like Skream, but I did not play it for this crowd” / “I do not like Jumping Machine; do not recommend it again” / “These are the tracks I played (image/list).”"
        },
        {
          "label": "Second | Export or hand off the playlist",
          "body": "You can output a text playlist or hand it to W4DJ. Reply `export to w4dj` or `output text playlist`.\n\nW4DJ provides one-click playlist import, converts formats after download, and imports into DJ software. Export the `.w4dj` format and download [w4dj-rkb](https://github.com/komakizhu/W4DJ-RKB). For detailed instructions, see [One-Click Set Import Tutorial](https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md).\n\n`.w4dj` uses a new minimal v2 format containing only the playlist name, positions, complete official titles, artists, and an optional string `netease_track_id`; v1 is rejected without migration.\n\nThe text-playlist action outputs copyable text that can be imported manually into NetEase Cloud Music, but it cannot import tracks into RKB with one click."
        },
        {
          "label": "Third | Harmonic set order",
          "body": "Would you like me to arrange the set using the Camelot wheel?"
        }
      ],
      "digging_notes": "Digging notes",
      "mix_suggestion": "Mix suggestion",
      "unknown": "Unknown",
      "verified": "Verified",
      "target_platform_missing": "Target platform unavailable",
      "view_titles": [
        "Style view",
        "Scene view",
        "Familiarity / discovery view",
        "Dynamic combined view"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "Share selection feedback",
      "positive": [
        "I like this track"
      ],
      "negative": [
        "I do not like this track"
      ],
      "ambiguous": [
        "I am unsure about this track"
      ]
    },
    "export_w4dj": {
      "label": "Export to W4DJ",
      "positive": [
        "Export to W4DJ"
      ],
      "negative": [
        "Do not export to W4DJ"
      ],
      "ambiguous": [
        "Maybe export to W4DJ"
      ]
    },
    "output_text_playlist": {
      "label": "Output text playlist",
      "positive": [
        "Output the text playlist"
      ],
      "negative": [
        "Do not output the text playlist"
      ],
      "ambiguous": [
        "Maybe output the text playlist"
      ]
    },
    "harmonic_reorder": {
      "label": "Harmonic reorder",
      "positive": [
        "Arrange it by the Camelot wheel"
      ],
      "negative": [
        "Do not reorder it"
      ],
      "ambiguous": [
        "Maybe arrange it by the Camelot wheel"
      ]
    },
    "confirm_long_term_memory": {
      "label": "Confirm long-term memory",
      "positive": [
        "Remember this preference"
      ],
      "negative": [
        "Do not save this preference"
      ],
      "ambiguous": [
        "Maybe remember this preference"
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
      "only",
      "Spotify only",
      "use only"
    ],
    "preferred_markers": [
      "prefer",
      "preferred",
      "priority"
    ],
    "fallback_markers": [
      "fallback",
      "backup",
      "if unavailable"
    ],
    "forbidden_markers": [
      "do not use",
      "exclude",
      "no"
    ]
  },
  "status": {
    "unknown": "Unknown",
    "verified": "Verified",
    "target_platform_missing": "Target platform unavailable"
  },
  "export": {
    "text": "Output a copyable text playlist in the current order.",
    "w4dj": "Create a UTF-8 `.w4dj` handoff for W4DJ.",
    "harmonic": "Request Camelot-wheel ordering using known keys.",
    "feedback": "Use natural-language feedback to update the current session; long-term storage requires confirmation.",
    "memory_confirmation": "I understood this as a concise taste-change summary. Save it to the private long-term profile?"
  }
}
```
