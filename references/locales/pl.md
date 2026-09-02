# Polish locale pack

This file is the fixed Polski UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "pl",
  "language_name": "Polish",
  "native_name": "Polski",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "Jeśli region pozostanie pusty, użyj w tej sesji tylko szerokiego rynku polskojęzycznego.",
    "explicit_region": "Jawnie podany kraj lub region ma pierwszeństwo przed wnioskowaniem z języka, ale nie zmienia języka komunikacji.",
    "persistence": "Nie zapisuj rynku docelowego jako preferencji długoterminowej."
  },
  "quick_start": {
    "intro": "Witamy w asystencie wyboru DJ. Ta Agent Skill pomaga przygotować set DJ. W dwóch rundach potwierdzisz potrzeby i otrzymasz propozycje utworów. Zasady wypełniania:",
    "tutorial_label": "Przewodnik importu Set jednym kliknięciem",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[Runda 1: podstawowe informacje]",
      "rules": [
        "1. Możesz skopiować przykład, wpisać własną treść albo zostawić pole puste",
        "2. Puste pole oznacza, że AI inteligentnie oceni odpowiedź"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "Kontekst",
          "example": "Kontekst występu. Przykłady: `bar` / `klub` / `wesele` / `wystawa sztuki`"
        },
        {
          "key": "target_market",
          "label": "Docelowy kraj / region",
          "example": "Przykłady: `Chiny kontynentalne` / `Tajwan` / `Hongkong` / `Japonia` / `międzynarodowy rynek anglojęzyczny`"
        },
        {
          "key": "core_sound",
          "label": "Główny kierunek brzmienia",
          "example": "Artysta, utwór i gatunek referencyjny. Przykład: `Tears` od `Skrillex`, nowoczesny `UK Bass`"
        },
        {
          "key": "track_count_or_duration",
          "label": "Liczba utworów lub długość seta",
          "example": "Przykłady: `20 utworów` / `60 minut`"
        },
        {
          "key": "output_mode",
          "label": "Wersja wyjścia",
          "example": "Wybór Fast / Brief / Rich"
        },
        {
          "key": "other",
          "label": "Inne ograniczenia",
          "example": "Przykłady: `unikaj ogranych utworów`, `bez wokalu`, `tylko Remix`; opcjonalne"
        }
      ],
      "prompt": "Witamy w asystencie wyboru DJ. Ta Agent Skill pomaga przygotować set DJ. W dwóch rundach potwierdzisz potrzeby i otrzymasz propozycje utworów. Zasady wypełniania:\n\n1. Możesz skopiować przykład, wpisać własną treść albo zostawić pole puste\n2. Puste pole oznacza, że AI inteligentnie oceni odpowiedź\n\n[Runda 1: podstawowe informacje]\n\nKontekst:\n“Kontekst występu. Przykłady: `bar` / `klub` / `wesele` / `wystawa sztuki`”\nDocelowy kraj / region:\n“Przykłady: `Chiny kontynentalne` / `Tajwan` / `Hongkong` / `Japonia` / `międzynarodowy rynek anglojęzyczny`”\nGłówny kierunek brzmienia:\n“Artysta, utwór i gatunek referencyjny. Przykład: `Tears` od `Skrillex`, nowoczesny `UK Bass`”\nLiczba utworów lub długość seta:\n“Przykłady: `20 utworów` / `60 minut`”\nWersja wyjścia:\n“`Fast`: szybka playlista; jakość może być niższa”\n“`Brief`: tylko jedna połączona playlista”\n“`Rich`: osobne widoki stylu, kontekstu i odkrywania, a potem końcowa playlista połączona”\nInne ograniczenia:\n“Przykłady: `unikaj ogranych utworów`, `bez wokalu`, `tylko Remix`; opcjonalne”\n\n\u0060\u0060\u0060markdown\nKontekst:\nDocelowy kraj / region:\nGłówny kierunek brzmienia:\nLiczba utworów lub długość seta:\nWersja wyjścia:\nInne ograniczenia:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[Runda 2: doprecyzowanie prośby]",
      "rules": [
        "1. Możesz skopiować przykład, wpisać własną treść albo zostawić pole puste"
      ],
      "fields": [
        {
          "key": "style",
          "label": "Konkretny styl",
          "example": "Przykłady: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "Szybkość / BPM",
          "example": "Przykłady: `105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "Znajomość i odkrywanie",
          "example": "`Znane` / `Zrównoważone` / `Odkrywanie`"
        },
        {
          "key": "era_classic",
          "label": "Epoka i klasyka",
          "example": "`Współczesne` / `Kilka klasycznych kotwic` / `Most między nowym i starym` / `Najpierw klasyka`"
        },
        {
          "key": "mood",
          "label": "Nastrój",
          "example": "Przykłady: `nostalgiczny` / `chłodny` / `romantyczny`"
        },
        {
          "key": "energy",
          "label": "Poziom lub przebieg energii SET",
          "example": "Przykłady: `niski` / `wysoki`; `stały` / `rollercoaster`"
        },
        {
          "key": "platform",
          "label": "Platforma i wymagania dotyczące linków",
          "example": "Przykłady: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; jedna platforma oznacza tylko ją, kilka zachowuje podaną kolejność"
        },
        {
          "key": "other",
          "label": "Inne",
          "example": ""
        }
      ],
      "prompt": "[Runda 2: doprecyzowanie prośby]\n\nKonkretny styl:\n“Przykłady: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`”\nSzybkość / BPM:\n“Przykłady: `105` / `128` / `140` / `150` / `170`”\nZnajomość i odkrywanie:\n“`Znane` / `Zrównoważone` / `Odkrywanie`”\nEpoka i klasyka:\n“`Współczesne` / `Kilka klasycznych kotwic` / `Most między nowym i starym` / `Najpierw klasyka`”\nNastrój:\n“Przykłady: `nostalgiczny` / `chłodny` / `romantyczny`”\nPoziom lub przebieg energii SET:\n“Przykłady: `niski` / `wysoki`; `stały` / `rollercoaster`”\nPlatforma i wymagania dotyczące linków:\n“Przykłady: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; jedna platforma oznacza tylko ją, kilka zachowuje podaną kolejność”\nInne:\n\n\u0060\u0060\u0060markdown\nKonkretny styl:\nSzybkość / BPM:\nZnajomość i odkrywanie:\nEpoka i klasyka:\nNastrój:\nPoziom lub przebieg energii SET:\nPlatforma i wymagania dotyczące linków:\nInne:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# Tryb Fast",
      "first_batch_title": "# Pierwsza partia Fast",
      "final_title": "# Tryb Fast",
      "columns": [
        "Utwór",
        "Artysta",
        "Link"
      ],
      "next_steps": [
        {
          "label": "Po pierwsze | Podziel się opinią",
          "body": "Jeśli chcesz, opisz naturalnym językiem, jak sprawdziły się wybory. To poprawia prywatne preferencje i kolejne rekomendacje."
        },
        {
          "label": "Po drugie | Eksportuj lub przekaż playlistę",
          "body": "Możesz wyprowadzić playlistę tekstową albo przekazać ją do W4DJ. Odpowiedz `output text playlist` lub `export to w4dj`."
        }
      ],
      "digging_notes": "Notatki z diggingu",
      "mix_suggestion": "Sugestia miksu",
      "unknown": "Nieznane",
      "verified": "Zweryfikowane",
      "target_platform_missing": "Platforma docelowa niedostępna"
    },
    "brief": {
      "title": "# Tryb Brief",
      "first_batch_title": "# Tryb Brief",
      "final_title": "# Tryb Brief",
      "columns": [
        "Utwór",
        "Artysta",
        "Album / EP",
        "Styl",
        "BPM",
        "Tonacja",
        "Długość",
        "Energia",
        "Data wydania",
        "Notatki",
        "Powód wyboru",
        "Link"
      ],
      "next_steps": [
        {
          "label": "Po pierwsze | Podziel się opinią",
          "body": "Jeśli chcesz, opisz naturalnym językiem, jak sprawdziły się wybory. To poprawia prywatne preferencje i kolejne rekomendacje."
        },
        {
          "label": "Po drugie | Eksportuj lub przekaż playlistę",
          "body": "Możesz wyprowadzić playlistę tekstową albo przekazać ją do W4DJ. Odpowiedz `output text playlist` lub `export to w4dj`."
        },
        {
          "label": "Po trzecie | Harmoniczna kolejność seta",
          "body": "Czy mam ułożyć set według koła Camelota?"
        }
      ],
      "digging_notes": "Notatki z diggingu",
      "mix_suggestion": "Sugestia miksu",
      "unknown": "Nieznane",
      "verified": "Zweryfikowane",
      "target_platform_missing": "Platforma docelowa niedostępna"
    },
    "rich": {
      "title": "# Tryb Rich",
      "first_batch_title": "# Tryb Rich",
      "final_title": "# Tryb Rich",
      "columns": [
        "Utwór",
        "Artysta",
        "Album / EP",
        "Styl",
        "BPM",
        "Tonacja",
        "Długość",
        "Energia",
        "Data wydania",
        "Notatki",
        "Powód wyboru",
        "Link"
      ],
      "next_steps": [
        {
          "label": "Po pierwsze | Podziel się opinią",
          "body": "Jeśli chcesz, opisz naturalnym językiem, jak sprawdziły się wybory. To poprawia prywatne preferencje i kolejne rekomendacje."
        },
        {
          "label": "Po drugie | Eksportuj lub przekaż playlistę",
          "body": "Możesz wyprowadzić playlistę tekstową albo przekazać ją do W4DJ. Odpowiedz `output text playlist` lub `export to w4dj`."
        },
        {
          "label": "Po trzecie | Harmoniczna kolejność seta",
          "body": "Czy mam ułożyć set według koła Camelota?"
        }
      ],
      "digging_notes": "Notatki z diggingu",
      "mix_suggestion": "Sugestia miksu",
      "unknown": "Nieznane",
      "verified": "Zweryfikowane",
      "target_platform_missing": "Platforma docelowa niedostępna",
      "view_titles": [
        "Widok stylu",
        "Widok kontekstu",
        "Widok znajomości / odkrywania",
        "Dynamiczny widok połączony"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "Podziel się opinią",
      "positive": [
        "Podoba mi się ten utwór"
      ],
      "negative": [
        "Nie podoba mi się ten utwór"
      ],
      "ambiguous": [
        "Nie mam pewności co do tego utworu"
      ]
    },
    "export_w4dj": {
      "label": "Eksportuj do W4DJ",
      "positive": [
        "Eksportuj do W4DJ"
      ],
      "negative": [
        "Nie eksportuj do W4DJ"
      ],
      "ambiguous": [
        "Może eksportuj do W4DJ"
      ]
    },
    "output_text_playlist": {
      "label": "Wyprowadź playlistę tekstową",
      "positive": [
        "Wyprowadź playlistę tekstową"
      ],
      "negative": [
        "Nie wyprowadzaj playlisty tekstowej"
      ],
      "ambiguous": [
        "Może wyprowadź playlistę tekstową"
      ]
    },
    "harmonic_reorder": {
      "label": "Przestaw harmonicznie",
      "positive": [
        "Ułóż według koła Camelota"
      ],
      "negative": [
        "Nie przestawiaj"
      ],
      "ambiguous": [
        "Może ułóż według koła Camelota"
      ]
    },
    "confirm_long_term_memory": {
      "label": "Potwierdź pamięć długoterminową",
      "positive": [
        "Zapamiętaj tę preferencję"
      ],
      "negative": [
        "Nie zapisuj tej preferencji"
      ],
      "ambiguous": [
        "Może zapamiętaj tę preferencję"
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
      "tylko",
      "wyłącznie",
      "użyj tylko"
    ],
    "preferred_markers": [
      "preferuj",
      "preferowana",
      "priorytet"
    ],
    "fallback_markers": [
      "zapasowa",
      "alternatywa",
      "jeśli niedostępna"
    ],
    "forbidden_markers": [
      "nie używaj",
      "wyklucz",
      "bez"
    ]
  },
  "status": {
    "unknown": "Nieznane",
    "verified": "Zweryfikowane",
    "target_platform_missing": "Platforma docelowa niedostępna"
  },
  "export": {
    "text": "Wyprowadź kopiowalną playlistę tekstową w bieżącej kolejności.",
    "w4dj": "Utwórz plik przekazania UTF-8 `.w4dj` dla W4DJ.",
    "harmonic": "Poproś o kolejność według koła Camelota z użyciem znanych tonacji.",
    "feedback": "Opinia w języku naturalnym aktualizuje tylko sesję; zapis długoterminowy wymaga potwierdzenia.",
    "memory_confirmation": "Rozumiem to jako krótkie podsumowanie zmiany gustu. Zapisać je w prywatnym profilu długoterminowym?"
  },
  "trigger_capsule": [
    "set DJ",
    "playlista",
    "szukać muzyki",
    "znaleźć utwory",
    "ułożyć set",
    "szybki tryb",
    "krótki tryb",
    "pełny tryb",
    "stworzyć set DJ",
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
