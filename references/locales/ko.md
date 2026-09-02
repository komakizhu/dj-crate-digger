# Korean locale pack

This file is the fixed 한국어 UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "ko",
  "language_name": "Korean",
  "native_name": "한국어",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "지역을 비워 두면 이 세션에서만 넓은 한국어권 시장을 사용합니다.",
    "explicit_region": "명시한 국가나 지역은 언어 추정보다 우선하지만 대화 언어는 바꾸지 않습니다.",
    "persistence": "대상 시장은 장기 취향으로 저장하지 않습니다."
  },
  "quick_start": {
    "intro": "DJ 선곡 도우미에 오신 것을 환영합니다. 이 Agent Skill은 DJ 세트를 구성하도록 돕습니다. 두 번의 라운드에서 요구를 확인하고 트랙을 추천합니다. 입력 규칙:",
    "tutorial_label": "원클릭 Set 가져오기 안내",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[1라운드: 필수 정보]",
      "rules": [
        "1. 예시를 복사하거나 자유롭게 입력하거나 비워 둘 수 있습니다",
        "2. 빈칸은 AI가 단서를 바탕으로 답을 지능적으로 판단한다는 뜻입니다"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "상황",
          "example": "공연 상황. 예: `바` / `클럽` / `결혼식` / `아트 전시`"
        },
        {
          "key": "target_market",
          "label": "대상 국가 / 지역",
          "example": "예: `중국 본토` / `대만` / `홍콩` / `일본` / `영어권 국제 시장`"
        },
        {
          "key": "core_sound",
          "label": "핵심 사운드 방향",
          "example": "참고 아티스트, 트랙, 장르. 예: `Skrillex`의 `Tears`, 현대적인 `UK Bass` 장르"
        },
        {
          "key": "track_count_or_duration",
          "label": "곡 수 또는 세트 시간",
          "example": "예: `20곡` / `60분`"
        },
        {
          "key": "output_mode",
          "label": "출력 버전",
          "example": "Fast / Brief / Rich 선택"
        },
        {
          "key": "other",
          "label": "기타 제한",
          "example": "예: `너무 많이 알려진 곡 제외`, `보컬 없음`, `Remix만`; 선택 사항"
        }
      ],
      "prompt": "DJ 선곡 도우미에 오신 것을 환영합니다. 이 Agent Skill은 DJ 세트를 구성하도록 돕습니다. 두 번의 라운드에서 요구를 확인하고 트랙을 추천합니다. 입력 규칙:\n\n1. 예시를 복사하거나 자유롭게 입력하거나 비워 둘 수 있습니다\n2. 빈칸은 AI가 단서를 바탕으로 답을 지능적으로 판단한다는 뜻입니다\n\n[1라운드: 필수 정보]\n\n상황:\n“공연 상황. 예: `바` / `클럽` / `결혼식` / `아트 전시`”\n대상 국가 / 지역:\n“예: `중국 본토` / `대만` / `홍콩` / `일본` / `영어권 국제 시장`”\n핵심 사운드 방향:\n“참고 아티스트, 트랙, 장르. 예: `Skrillex`의 `Tears`, 현대적인 `UK Bass` 장르”\n곡 수 또는 세트 시간:\n“예: `20곡` / `60분`”\n출력 버전:\n“`Fast`: 빠른 playlist 출력; 품질이 낮아질 수 있습니다”\n“`Brief`: 통합 playlist 하나만 출력”\n“`Rich`: 스타일, 상황, 친숙함／발견 관점을 나누어 제시한 뒤 최종 통합 playlist 출력”\n기타 제한:\n“예: `너무 많이 알려진 곡 제외`, `보컬 없음`, `Remix만`; 선택 사항”\n\n\u0060\u0060\u0060markdown\n상황:\n대상 국가 / 지역:\n핵심 사운드 방향:\n곡 수 또는 세트 시간:\n출력 버전:\n기타 제한:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[2라운드: 요구 구체화]",
      "rules": [
        "1. 예시를 복사하거나 자유롭게 입력하거나 비워 둘 수 있습니다"
      ],
      "fields": [
        {
          "key": "style",
          "label": "구체적인 스타일",
          "example": "예: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "속도 / BPM",
          "example": "예: `105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "친숙함과 발견",
          "example": "`익숙한 곡` / `균형` / `발견`"
        },
        {
          "key": "era_classic",
          "label": "시대와 클래식",
          "example": "`현대 중심` / `소수의 클래식 앵커` / `신구 연결` / `클래식 우선`"
        },
        {
          "key": "mood",
          "label": "분위기",
          "example": "예: `향수 어린` / `차가운` / `로맨틱한`"
        },
        {
          "key": "energy",
          "label": "SET 에너지 수준 또는 흐름",
          "example": "예: `낮음` / `높음`; `일정` / `롤러코스터`"
        },
        {
          "key": "platform",
          "label": "플랫폼 및 링크 요구",
          "example": "예: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; 하나면 그것만, 여러 개면 적은 순서 우선"
        },
        {
          "key": "other",
          "label": "기타",
          "example": ""
        }
      ],
      "prompt": "[2라운드: 요구 구체화]\n\n구체적인 스타일:\n“예: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`”\n속도 / BPM:\n“예: `105` / `128` / `140` / `150` / `170`”\n친숙함과 발견:\n“`익숙한 곡` / `균형` / `발견`”\n시대와 클래식:\n“`현대 중심` / `소수의 클래식 앵커` / `신구 연결` / `클래식 우선`”\n분위기:\n“예: `향수 어린` / `차가운` / `로맨틱한`”\nSET 에너지 수준 또는 흐름:\n“예: `낮음` / `높음`; `일정` / `롤러코스터`”\n플랫폼 및 링크 요구:\n“예: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; 하나면 그것만, 여러 개면 적은 순서 우선”\n기타:\n\n\u0060\u0060\u0060markdown\n구체적인 스타일:\n속도 / BPM:\n친숙함과 발견:\n시대와 클래식:\n분위기:\nSET 에너지 수준 또는 흐름:\n플랫폼 및 링크 요구:\n기타:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# Fast 모드",
      "first_batch_title": "# Fast 모드 첫 묶음",
      "final_title": "# Fast 모드",
      "columns": [
        "곡명",
        "아티스트",
        "링크"
      ],
      "next_steps": [
        {
          "label": "첫째 | 선곡 피드백",
          "body": "원한다면 선곡이 어떻게 느껴졌는지 자연어로 답해 주세요. 개인 취향과 다음 추천이 더 정확해집니다."
        },
        {
          "label": "둘째 | playlist 내보내기 또는 W4DJ 전달",
          "body": "텍스트 playlist를 출력하거나 W4DJ로 넘길 수 있습니다. `output text playlist` 또는 `export to w4dj`라고 답하세요."
        }
      ],
      "digging_notes": "Digging 메모",
      "mix_suggestion": "믹스 제안",
      "unknown": "알 수 없음",
      "verified": "검증됨",
      "target_platform_missing": "대상 플랫폼 없음"
    },
    "brief": {
      "title": "# Brief 모드",
      "first_batch_title": "# Brief 모드",
      "final_title": "# Brief 모드",
      "columns": [
        "곡명",
        "아티스트",
        "앨범 / EP",
        "스타일",
        "BPM",
        "키",
        "길이",
        "에너지",
        "발매일",
        "메모",
        "선정 이유",
        "링크"
      ],
      "next_steps": [
        {
          "label": "첫째 | 선곡 피드백",
          "body": "원한다면 선곡이 어떻게 느껴졌는지 자연어로 답해 주세요. 개인 취향과 다음 추천이 더 정확해집니다."
        },
        {
          "label": "둘째 | playlist 내보내기 또는 W4DJ 전달",
          "body": "텍스트 playlist를 출력하거나 W4DJ로 넘길 수 있습니다. `output text playlist` 또는 `export to w4dj`라고 답하세요."
        },
        {
          "label": "셋째 | 하모닉 세트 순서",
          "body": "Camelot 휠을 사용해 세트를 정렬할까요?"
        }
      ],
      "digging_notes": "Digging 메모",
      "mix_suggestion": "믹스 제안",
      "unknown": "알 수 없음",
      "verified": "검증됨",
      "target_platform_missing": "대상 플랫폼 없음"
    },
    "rich": {
      "title": "# Rich 모드",
      "first_batch_title": "# Rich 모드",
      "final_title": "# Rich 모드",
      "columns": [
        "곡명",
        "아티스트",
        "앨범 / EP",
        "스타일",
        "BPM",
        "키",
        "길이",
        "에너지",
        "발매일",
        "메모",
        "선정 이유",
        "링크"
      ],
      "next_steps": [
        {
          "label": "첫째 | 선곡 피드백",
          "body": "원한다면 선곡이 어떻게 느껴졌는지 자연어로 답해 주세요. 개인 취향과 다음 추천이 더 정확해집니다."
        },
        {
          "label": "둘째 | playlist 내보내기 또는 W4DJ 전달",
          "body": "텍스트 playlist를 출력하거나 W4DJ로 넘길 수 있습니다. `output text playlist` 또는 `export to w4dj`라고 답하세요."
        },
        {
          "label": "셋째 | 하모닉 세트 순서",
          "body": "Camelot 휠을 사용해 세트를 정렬할까요?"
        }
      ],
      "digging_notes": "Digging 메모",
      "mix_suggestion": "믹스 제안",
      "unknown": "알 수 없음",
      "verified": "검증됨",
      "target_platform_missing": "대상 플랫폼 없음",
      "view_titles": [
        "스타일 관점",
        "상황 관점",
        "친숙함／발견 관점",
        "동적 통합 관점"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "선곡 피드백",
      "positive": [
        "이 곡이 좋아요"
      ],
      "negative": [
        "이 곡은 좋아하지 않아요"
      ],
      "ambiguous": [
        "이 곡은 아직 판단하기 어려워요"
      ]
    },
    "export_w4dj": {
      "label": "W4DJ로 내보내기",
      "positive": [
        "W4DJ로 내보내기"
      ],
      "negative": [
        "W4DJ로 내보내지 않기"
      ],
      "ambiguous": [
        "W4DJ로 내보낼 수도 있어요"
      ]
    },
    "output_text_playlist": {
      "label": "텍스트 playlist 출력",
      "positive": [
        "텍스트 playlist 출력"
      ],
      "negative": [
        "텍스트 playlist를 출력하지 않기"
      ],
      "ambiguous": [
        "텍스트 playlist를 출력할 수도 있어요"
      ]
    },
    "harmonic_reorder": {
      "label": "하모닉 재정렬",
      "positive": [
        "Camelot 휠로 정렬"
      ],
      "negative": [
        "재정렬하지 않기"
      ],
      "ambiguous": [
        "Camelot 휠로 정렬할 수도 있어요"
      ]
    },
    "confirm_long_term_memory": {
      "label": "장기 기억 확인",
      "positive": [
        "이 선호를 기억하기"
      ],
      "negative": [
        "이 선호를 저장하지 않기"
      ],
      "ambiguous": [
        "이 선호를 기억할 수도 있어요"
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
      "만",
      "만 사용",
      "오직"
    ],
    "preferred_markers": [
      "우선",
      "선호",
      "우선순위"
    ],
    "fallback_markers": [
      "대체",
      "백업",
      "사용할 수 없으면"
    ],
    "forbidden_markers": [
      "사용하지 않기",
      "제외",
      "없음"
    ]
  },
  "status": {
    "unknown": "알 수 없음",
    "verified": "검증됨",
    "target_platform_missing": "대상 플랫폼 없음"
  },
  "export": {
    "text": "현재 순서로 복사 가능한 텍스트 playlist를 출력합니다.",
    "w4dj": "W4DJ에 전달할 UTF-8 `.w4dj` 파일을 만듭니다.",
    "harmonic": "확인된 키를 사용해 Camelot 휠 순서를 요청합니다.",
    "feedback": "자연어 피드백은 현재 세션만 갱신하며 장기 저장에는 확인이 필요합니다.",
    "memory_confirmation": "이 내용을 취향 변화의 짧은 요약으로 이해했습니다. 개인 장기 프로필에 저장할까요?"
  },
  "trigger_capsule": [
    "DJ 세트",
    "플레이리스트",
    "곡 찾기",
    "트랙 찾기",
    "세트 구성",
    "빠른 모드",
    "종합 모드",
    "전체 모드",
    "DJ 세트 만들기",
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
