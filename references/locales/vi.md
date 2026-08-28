# Vietnamese locale pack

This file is the fixed Tiếng Việt UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "vi",
  "language_name": "Vietnamese",
  "native_name": "Tiếng Việt",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "Nếu để trống khu vực, chỉ dùng một thị trường tiếng Việt rộng cho phiên này.",
    "explicit_region": "Quốc gia hoặc khu vực được nêu rõ được ưu tiên hơn suy luận ngôn ngữ nhưng không đổi ngôn ngữ giao tiếp.",
    "persistence": "Không lưu thị trường mục tiêu thành sở thích dài hạn."
  },
  "quick_start": {
    "intro": "Chào mừng đến với Trợ lý chọn nhạc DJ. Skill Agent này giúp bạn chuẩn bị một set DJ. Bạn sẽ xác nhận nhu cầu trong hai vòng và nhận gợi ý track. Quy tắc điền:",
    "tutorial_label": "Hướng dẫn nhập Set một cú nhấp",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[Vòng 1: thông tin cần thiết]",
      "rules": [
        "1. Bạn có thể sao chép ví dụ, điền tự do hoặc để trống",
        "2. Để trống nghĩa là AI sẽ tự suy xét câu trả lời một cách thông minh"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "Bối cảnh",
          "example": "Bối cảnh biểu diễn. Ví dụ: `bar` / `club` / `đám cưới` / `triển lãm nghệ thuật`"
        },
        {
          "key": "target_market",
          "label": "Quốc gia / khu vực mục tiêu",
          "example": "Ví dụ: `Trung Quốc đại lục` / `Đài Loan` / `Hồng Kông` / `Nhật Bản` / `thị trường quốc tế dùng tiếng Anh`"
        },
        {
          "key": "core_sound",
          "label": "Hướng âm thanh chính",
          "example": "Nghệ sĩ, track và thể loại tham chiếu. Ví dụ: `Tears` của `Skrillex`, thể loại `UK Bass` hiện đại"
        },
        {
          "key": "track_count_or_duration",
          "label": "Số track hoặc thời lượng set",
          "example": "Ví dụ: `20 track` / `60 phút`"
        },
        {
          "key": "output_mode",
          "label": "Phiên bản đầu ra",
          "example": "Chọn Fast / Brief / Rich"
        },
        {
          "key": "other",
          "label": "Các giới hạn khác",
          "example": "Ví dụ: `tránh bài quá phổ biến`, `không vocal`, `chỉ Remix`; tùy chọn"
        }
      ],
      "prompt": "Chào mừng đến với Trợ lý chọn nhạc DJ. Skill Agent này giúp bạn chuẩn bị một set DJ. Bạn sẽ xác nhận nhu cầu trong hai vòng và nhận gợi ý track. Quy tắc điền:\n\n1. Bạn có thể sao chép ví dụ, điền tự do hoặc để trống\n2. Để trống nghĩa là AI sẽ tự suy xét câu trả lời một cách thông minh\n\n[Vòng 1: thông tin cần thiết]\n\nBối cảnh:\n“Bối cảnh biểu diễn. Ví dụ: `bar` / `club` / `đám cưới` / `triển lãm nghệ thuật`”\nQuốc gia / khu vực mục tiêu:\n“Ví dụ: `Trung Quốc đại lục` / `Đài Loan` / `Hồng Kông` / `Nhật Bản` / `thị trường quốc tế dùng tiếng Anh`”\nHướng âm thanh chính:\n“Nghệ sĩ, track và thể loại tham chiếu. Ví dụ: `Tears` của `Skrillex`, thể loại `UK Bass` hiện đại”\nSố track hoặc thời lượng set:\n“Ví dụ: `20 track` / `60 phút`”\nPhiên bản đầu ra:\n“`Fast`: xuất playlist nhanh; chất lượng có thể thấp hơn”\n“`Brief`: chỉ một playlist tổng hợp”\n“`Rich`: các góc nhìn riêng về phong cách, bối cảnh và khám phá, sau đó là playlist tổng hợp”\nCác giới hạn khác:\n“Ví dụ: `tránh bài quá phổ biến`, `không vocal`, `chỉ Remix`; tùy chọn”\n\n\u0060\u0060\u0060markdown\nBối cảnh:\nQuốc gia / khu vực mục tiêu:\nHướng âm thanh chính:\nSố track hoặc thời lượng set:\nPhiên bản đầu ra:\nCác giới hạn khác:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[Vòng 2: làm rõ yêu cầu]",
      "rules": [
        "1. Bạn có thể sao chép ví dụ, điền tự do hoặc để trống"
      ],
      "fields": [
        {
          "key": "style",
          "label": "Phong cách cụ thể",
          "example": "Ví dụ: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "Tốc độ / BPM",
          "example": "Ví dụ: `105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "Mức quen thuộc và khám phá",
          "example": "`Quen thuộc` / `Cân bằng` / `Khám phá`"
        },
        {
          "key": "era_classic",
          "label": "Thời đại và kinh điển",
          "example": "`Đương đại` / `Một ít mốc kinh điển` / `Nối mới và cũ` / `Kinh điển trước`"
        },
        {
          "key": "mood",
          "label": "Tâm trạng",
          "example": "Ví dụ: `hoài niệm` / `lạnh` / `lãng mạn`"
        },
        {
          "key": "energy",
          "label": "Mức hoặc đường năng lượng SET",
          "example": "Ví dụ: `thấp` / `cao`; `ổn định` / `tàu lượn`"
        },
        {
          "key": "platform",
          "label": "Nền tảng và yêu cầu liên kết",
          "example": "Ví dụ: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; một nền tảng nghĩa là chỉ dùng nền tảng đó, nhiều nền tảng theo thứ tự ghi"
        },
        {
          "key": "other",
          "label": "Khác",
          "example": ""
        }
      ],
      "prompt": "[Vòng 2: làm rõ yêu cầu]\n\nPhong cách cụ thể:\n“Ví dụ: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`”\nTốc độ / BPM:\n“Ví dụ: `105` / `128` / `140` / `150` / `170`”\nMức quen thuộc và khám phá:\n“`Quen thuộc` / `Cân bằng` / `Khám phá`”\nThời đại và kinh điển:\n“`Đương đại` / `Một ít mốc kinh điển` / `Nối mới và cũ` / `Kinh điển trước`”\nTâm trạng:\n“Ví dụ: `hoài niệm` / `lạnh` / `lãng mạn`”\nMức hoặc đường năng lượng SET:\n“Ví dụ: `thấp` / `cao`; `ổn định` / `tàu lượn`”\nNền tảng và yêu cầu liên kết:\n“Ví dụ: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; một nền tảng nghĩa là chỉ dùng nền tảng đó, nhiều nền tảng theo thứ tự ghi”\nKhác:\n\n\u0060\u0060\u0060markdown\nPhong cách cụ thể:\nTốc độ / BPM:\nMức quen thuộc và khám phá:\nThời đại và kinh điển:\nTâm trạng:\nMức hoặc đường năng lượng SET:\nNền tảng và yêu cầu liên kết:\nKhác:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# Chế độ Fast",
      "first_batch_title": "# Lô Fast đầu tiên",
      "final_title": "# Chế độ Fast",
      "columns": [
        "Track",
        "Nghệ sĩ",
        "Liên kết"
      ],
      "next_steps": [
        {
          "label": "Thứ nhất | Gửi phản hồi chọn nhạc",
          "body": "Nếu muốn, hãy trả lời bằng ngôn ngữ tự nhiên về cách các lựa chọn hoạt động. Điều này giúp cải thiện sở thích riêng và gợi ý sau."
        },
        {
          "label": "Thứ hai | Xuất hoặc chuyển playlist",
          "body": "Bạn có thể xuất playlist dạng văn bản hoặc chuyển cho W4DJ. Hãy trả lời `output text playlist` hoặc `export to w4dj`."
        }
      ],
      "digging_notes": "Ghi chú digging",
      "mix_suggestion": "Gợi ý mix",
      "unknown": "Chưa biết",
      "verified": "Đã xác minh",
      "target_platform_missing": "Nền tảng mục tiêu không khả dụng"
    },
    "brief": {
      "title": "# Chế độ Brief",
      "first_batch_title": "# Chế độ Brief",
      "final_title": "# Chế độ Brief",
      "columns": [
        "Track",
        "Nghệ sĩ",
        "Album / EP",
        "Phong cách",
        "BPM",
        "Tông",
        "Thời lượng",
        "Năng lượng",
        "Ngày phát hành",
        "Ghi chú",
        "Lý do chọn",
        "Liên kết"
      ],
      "next_steps": [
        {
          "label": "Thứ nhất | Gửi phản hồi chọn nhạc",
          "body": "Nếu muốn, hãy trả lời bằng ngôn ngữ tự nhiên về cách các lựa chọn hoạt động. Điều này giúp cải thiện sở thích riêng và gợi ý sau."
        },
        {
          "label": "Thứ hai | Xuất hoặc chuyển playlist",
          "body": "Bạn có thể xuất playlist dạng văn bản hoặc chuyển cho W4DJ. Hãy trả lời `output text playlist` hoặc `export to w4dj`."
        },
        {
          "label": "Thứ ba | Thứ tự hòa âm của set",
          "body": "Bạn có muốn tôi sắp xếp set theo vòng Camelot không?"
        }
      ],
      "digging_notes": "Ghi chú digging",
      "mix_suggestion": "Gợi ý mix",
      "unknown": "Chưa biết",
      "verified": "Đã xác minh",
      "target_platform_missing": "Nền tảng mục tiêu không khả dụng"
    },
    "rich": {
      "title": "# Chế độ Rich",
      "first_batch_title": "# Chế độ Rich",
      "final_title": "# Chế độ Rich",
      "columns": [
        "Track",
        "Nghệ sĩ",
        "Album / EP",
        "Phong cách",
        "BPM",
        "Tông",
        "Thời lượng",
        "Năng lượng",
        "Ngày phát hành",
        "Ghi chú",
        "Lý do chọn",
        "Liên kết"
      ],
      "next_steps": [
        {
          "label": "Thứ nhất | Gửi phản hồi chọn nhạc",
          "body": "Nếu muốn, hãy trả lời bằng ngôn ngữ tự nhiên về cách các lựa chọn hoạt động. Điều này giúp cải thiện sở thích riêng và gợi ý sau."
        },
        {
          "label": "Thứ hai | Xuất hoặc chuyển playlist",
          "body": "Bạn có thể xuất playlist dạng văn bản hoặc chuyển cho W4DJ. Hãy trả lời `output text playlist` hoặc `export to w4dj`."
        },
        {
          "label": "Thứ ba | Thứ tự hòa âm của set",
          "body": "Bạn có muốn tôi sắp xếp set theo vòng Camelot không?"
        }
      ],
      "digging_notes": "Ghi chú digging",
      "mix_suggestion": "Gợi ý mix",
      "unknown": "Chưa biết",
      "verified": "Đã xác minh",
      "target_platform_missing": "Nền tảng mục tiêu không khả dụng",
      "view_titles": [
        "Góc nhìn phong cách",
        "Góc nhìn bối cảnh",
        "Góc nhìn quen thuộc / khám phá",
        "Góc nhìn tổng hợp động"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "Gửi phản hồi",
      "positive": [
        "Tôi thích track này"
      ],
      "negative": [
        "Tôi không thích track này"
      ],
      "ambiguous": [
        "Tôi chưa chắc về track này"
      ]
    },
    "export_w4dj": {
      "label": "Xuất sang W4DJ",
      "positive": [
        "Xuất sang W4DJ"
      ],
      "negative": [
        "Không xuất sang W4DJ"
      ],
      "ambiguous": [
        "Có thể xuất sang W4DJ"
      ]
    },
    "output_text_playlist": {
      "label": "Xuất playlist văn bản",
      "positive": [
        "Xuất playlist văn bản"
      ],
      "negative": [
        "Không xuất playlist văn bản"
      ],
      "ambiguous": [
        "Có thể xuất playlist văn bản"
      ]
    },
    "harmonic_reorder": {
      "label": "Sắp xếp hòa âm",
      "positive": [
        "Sắp xếp theo vòng Camelot"
      ],
      "negative": [
        "Không sắp xếp lại"
      ],
      "ambiguous": [
        "Có thể sắp xếp theo vòng Camelot"
      ]
    },
    "confirm_long_term_memory": {
      "label": "Xác nhận ghi nhớ dài hạn",
      "positive": [
        "Ghi nhớ sở thích này"
      ],
      "negative": [
        "Không lưu sở thích này"
      ],
      "ambiguous": [
        "Có thể ghi nhớ sở thích này"
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
      "chỉ",
      "duy nhất",
      "chỉ sử dụng"
    ],
    "preferred_markers": [
      "ưu tiên",
      "thích hơn",
      "ưu tiên cao"
    ],
    "fallback_markers": [
      "dự phòng",
      "thay thế",
      "nếu không có"
    ],
    "forbidden_markers": [
      "không dùng",
      "loại trừ",
      "không có"
    ]
  },
  "status": {
    "unknown": "Chưa biết",
    "verified": "Đã xác minh",
    "target_platform_missing": "Nền tảng mục tiêu không khả dụng"
  },
  "export": {
    "text": "Xuất playlist văn bản có thể sao chép theo thứ tự hiện tại.",
    "w4dj": "Tạo tệp bàn giao UTF-8 `.w4dj` cho W4DJ.",
    "harmonic": "Yêu cầu sắp xếp theo vòng Camelot với các tông đã biết.",
    "feedback": "Phản hồi tự nhiên chỉ cập nhật phiên hiện tại; lưu dài hạn cần xác nhận.",
    "memory_confirmation": "Tôi hiểu đây là tóm tắt ngắn về thay đổi gu nhạc. Lưu vào hồ sơ riêng dài hạn chứ?"
  }
}
```
