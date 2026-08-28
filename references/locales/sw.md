# Swahili locale pack

This file is the fixed Kiswahili UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "sw",
  "language_name": "Swahili",
  "native_name": "Kiswahili",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "Eneo likiachwa wazi, tumia soko pana la Kiswahili kwa kipindi hiki pekee.",
    "explicit_region": "Nchi au eneo lililotajwa wazi hushinda makisio ya lugha bila kubadilisha lugha ya mawasiliano.",
    "persistence": "Usihifadhi soko lengwa kama upendeleo wa muda mrefu."
  },
  "quick_start": {
    "intro": "Karibu kwenye Msaidizi wa Uchaguzi wa DJ. Agent Skill hii hukusaidia kuandaa set ya DJ. Utathibitisha mahitaji katika raundi mbili na kupata mapendekezo ya nyimbo. Kanuni za kujaza:",
    "tutorial_label": "Mwongozo wa kuingiza Set kwa kubofya mara moja",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[Raundi ya kwanza: taarifa muhimu]",
      "rules": [
        "1. Unaweza kunakili mfano, kujaza kwa uhuru, au kuacha tupu",
        "2. Kuacha tupu kunamaanisha AI itatathmini jibu kwa akili"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "Muktadha",
          "example": "Muktadha wa onyesho. Mfano: `bar` / `club` / `wedding` / `art exhibition`"
        },
        {
          "key": "target_market",
          "label": "Nchi / eneo lengwa",
          "example": "Mfano: `Mainland China` / `Taiwan` / `Hong Kong` / `Japan` / `international English market`"
        },
        {
          "key": "core_sound",
          "label": "Mwelekeo mkuu wa sauti",
          "example": "Msanii, wimbo na aina ya rejea. Mfano: `Tears` ya `Skrillex`, `UK Bass` ya kisasa"
        },
        {
          "key": "track_count_or_duration",
          "label": "Idadi ya nyimbo au muda wa set",
          "example": "Mfano: `20 tracks` / `60 minutes`"
        },
        {
          "key": "output_mode",
          "label": "Toleo la matokeo",
          "example": "Chagua Fast / Brief / Rich"
        },
        {
          "key": "other",
          "label": "Vikwazo vingine",
          "example": "Mfano: `epuka nyimbo zilizochezwa sana`, `bila sauti`, `Remix pekee`; hiari"
        }
      ],
      "prompt": "Karibu kwenye Msaidizi wa Uchaguzi wa DJ. Agent Skill hii hukusaidia kuandaa set ya DJ. Utathibitisha mahitaji katika raundi mbili na kupata mapendekezo ya nyimbo. Kanuni za kujaza:\n\n1. Unaweza kunakili mfano, kujaza kwa uhuru, au kuacha tupu\n2. Kuacha tupu kunamaanisha AI itatathmini jibu kwa akili\n\n[Raundi ya kwanza: taarifa muhimu]\n\nMuktadha:\n“Muktadha wa onyesho. Mfano: `bar` / `club` / `wedding` / `art exhibition`”\nNchi / eneo lengwa:\n“Mfano: `Mainland China` / `Taiwan` / `Hong Kong` / `Japan` / `international English market`”\nMwelekeo mkuu wa sauti:\n“Msanii, wimbo na aina ya rejea. Mfano: `Tears` ya `Skrillex`, `UK Bass` ya kisasa”\nIdadi ya nyimbo au muda wa set:\n“Mfano: `20 tracks` / `60 minutes`”\nToleo la matokeo:\n“`Fast`: playlist ya haraka; ubora unaweza kuwa chini”\n“`Brief`: playlist moja iliyounganishwa pekee”\n“`Rich`: mitazamo tofauti ya mtindo, muktadha na ugunduzi, kisha playlist iliyounganishwa”\nVikwazo vingine:\n“Mfano: `epuka nyimbo zilizochezwa sana`, `bila sauti`, `Remix pekee`; hiari”\n\n\u0060\u0060\u0060markdown\nMuktadha:\nNchi / eneo lengwa:\nMwelekeo mkuu wa sauti:\nIdadi ya nyimbo au muda wa set:\nToleo la matokeo:\nVikwazo vingine:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[Raundi ya pili: fafanua ombi]",
      "rules": [
        "1. Unaweza kunakili mfano, kujaza kwa uhuru, au kuacha tupu"
      ],
      "fields": [
        {
          "key": "style",
          "label": "Mtindo mahususi",
          "example": "Mfano: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "Kasi / BPM",
          "example": "Mfano: `105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "Uzoefu na ugunduzi",
          "example": "`Inayojulikana` / `Mizani` / `Ugunduzi`"
        },
        {
          "key": "era_classic",
          "label": "Enzi na classics",
          "example": "`Ya sasa` / `Nanga chache za classics` / `Daraja la mpya na ya zamani` / `Classics kwanza`"
        },
        {
          "key": "mood",
          "label": "Hisia",
          "example": "Mfano: `ya kumbukumbu` / `baridi` / `ya kimapenzi`"
        },
        {
          "key": "energy",
          "label": "Kiwango au mkondo wa nishati wa SET",
          "example": "Mfano: `chini` / `juu`; `thabiti` / `roller coaster`"
        },
        {
          "key": "platform",
          "label": "Jukwaa na mahitaji ya viungo",
          "example": "Mfano: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; jukwaa moja litumie hilo pekee, mengi yafuate kipaumbele"
        },
        {
          "key": "other",
          "label": "Mengine",
          "example": ""
        }
      ],
      "prompt": "[Raundi ya pili: fafanua ombi]\n\nMtindo mahususi:\n“Mfano: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`”\nKasi / BPM:\n“Mfano: `105` / `128` / `140` / `150` / `170`”\nUzoefu na ugunduzi:\n“`Inayojulikana` / `Mizani` / `Ugunduzi`”\nEnzi na classics:\n“`Ya sasa` / `Nanga chache za classics` / `Daraja la mpya na ya zamani` / `Classics kwanza`”\nHisia:\n“Mfano: `ya kumbukumbu` / `baridi` / `ya kimapenzi`”\nKiwango au mkondo wa nishati wa SET:\n“Mfano: `chini` / `juu`; `thabiti` / `roller coaster`”\nJukwaa na mahitaji ya viungo:\n“Mfano: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; jukwaa moja litumie hilo pekee, mengi yafuate kipaumbele”\nMengine:\n\n\u0060\u0060\u0060markdown\nMtindo mahususi:\nKasi / BPM:\nUzoefu na ugunduzi:\nEnzi na classics:\nHisia:\nKiwango au mkondo wa nishati wa SET:\nJukwaa na mahitaji ya viungo:\nMengine:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# Hali ya Fast",
      "first_batch_title": "# Kundi la kwanza la Fast",
      "final_title": "# Hali ya Fast",
      "columns": [
        "Wimbo",
        "Msanii",
        "Kiungo"
      ],
      "next_steps": [
        {
          "label": "Kwanza | Shiriki maoni ya uchaguzi",
          "body": "Ukitaka, jibu kwa lugha ya kawaida kuhusu jinsi uchaguzi ulivyofanya kazi. Hii huboresha mapendeleo yako binafsi na mapendekezo yajayo."
        },
        {
          "label": "Pili | Hamisha au kabidhi playlist",
          "body": "Unaweza kutoa playlist ya maandishi au kuikabidhi kwa W4DJ. Jibu `output text playlist` au `export to w4dj`."
        }
      ],
      "digging_notes": "Maelezo ya digging",
      "mix_suggestion": "Pendekezo la mix",
      "unknown": "Haijulikani",
      "verified": "Imethibitishwa",
      "target_platform_missing": "Jukwaa lengwa halipatikani"
    },
    "brief": {
      "title": "# Hali ya Brief",
      "first_batch_title": "# Hali ya Brief",
      "final_title": "# Hali ya Brief",
      "columns": [
        "Wimbo",
        "Msanii",
        "Album / EP",
        "Mtindo",
        "BPM",
        "Key",
        "Muda",
        "Nishati",
        "Tarehe ya kutolewa",
        "Maelezo",
        "Sababu ya kuchagua",
        "Kiungo"
      ],
      "next_steps": [
        {
          "label": "Kwanza | Shiriki maoni ya uchaguzi",
          "body": "Ukitaka, jibu kwa lugha ya kawaida kuhusu jinsi uchaguzi ulivyofanya kazi. Hii huboresha mapendeleo yako binafsi na mapendekezo yajayo."
        },
        {
          "label": "Pili | Hamisha au kabidhi playlist",
          "body": "Unaweza kutoa playlist ya maandishi au kuikabidhi kwa W4DJ. Jibu `output text playlist` au `export to w4dj`."
        },
        {
          "label": "Tatu | Mpangilio wa harmoniki wa set",
          "body": "Ungependa nipange set kwa kutumia gurudumu la Camelot?"
        }
      ],
      "digging_notes": "Maelezo ya digging",
      "mix_suggestion": "Pendekezo la mix",
      "unknown": "Haijulikani",
      "verified": "Imethibitishwa",
      "target_platform_missing": "Jukwaa lengwa halipatikani"
    },
    "rich": {
      "title": "# Hali ya Rich",
      "first_batch_title": "# Hali ya Rich",
      "final_title": "# Hali ya Rich",
      "columns": [
        "Wimbo",
        "Msanii",
        "Album / EP",
        "Mtindo",
        "BPM",
        "Key",
        "Muda",
        "Nishati",
        "Tarehe ya kutolewa",
        "Maelezo",
        "Sababu ya kuchagua",
        "Kiungo"
      ],
      "next_steps": [
        {
          "label": "Kwanza | Shiriki maoni ya uchaguzi",
          "body": "Ukitaka, jibu kwa lugha ya kawaida kuhusu jinsi uchaguzi ulivyofanya kazi. Hii huboresha mapendeleo yako binafsi na mapendekezo yajayo."
        },
        {
          "label": "Pili | Hamisha au kabidhi playlist",
          "body": "Unaweza kutoa playlist ya maandishi au kuikabidhi kwa W4DJ. Jibu `output text playlist` au `export to w4dj`."
        },
        {
          "label": "Tatu | Mpangilio wa harmoniki wa set",
          "body": "Ungependa nipange set kwa kutumia gurudumu la Camelot?"
        }
      ],
      "digging_notes": "Maelezo ya digging",
      "mix_suggestion": "Pendekezo la mix",
      "unknown": "Haijulikani",
      "verified": "Imethibitishwa",
      "target_platform_missing": "Jukwaa lengwa halipatikani",
      "view_titles": [
        "Mtazamo wa mtindo",
        "Mtazamo wa muktadha",
        "Mtazamo wa uzoefu / ugunduzi",
        "Mtazamo wa muunganiko wa nguvu"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "Shiriki maoni",
      "positive": [
        "Napenda wimbo huu"
      ],
      "negative": [
        "Sipendi wimbo huu"
      ],
      "ambiguous": [
        "Sina uhakika kuhusu wimbo huu"
      ]
    },
    "export_w4dj": {
      "label": "Hamisha kwa W4DJ",
      "positive": [
        "Hamisha kwa W4DJ"
      ],
      "negative": [
        "Usihamishe kwa W4DJ"
      ],
      "ambiguous": [
        "Labda hamisha kwa W4DJ"
      ]
    },
    "output_text_playlist": {
      "label": "Toa playlist ya maandishi",
      "positive": [
        "Toa playlist ya maandishi"
      ],
      "negative": [
        "Usitoe playlist ya maandishi"
      ],
      "ambiguous": [
        "Labda toa playlist ya maandishi"
      ]
    },
    "harmonic_reorder": {
      "label": "Panga upya kwa harmoniki",
      "positive": [
        "Panga kwa gurudumu la Camelot"
      ],
      "negative": [
        "Usipange upya"
      ],
      "ambiguous": [
        "Labda panga kwa gurudumu la Camelot"
      ]
    },
    "confirm_long_term_memory": {
      "label": "Thibitisha kumbukumbu ya muda mrefu",
      "positive": [
        "Kumbuka upendeleo huu"
      ],
      "negative": [
        "Usihifadhi upendeleo huu"
      ],
      "ambiguous": [
        "Labda kumbuka upendeleo huu"
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
      "pekee",
      "tu",
      "tumia tu"
    ],
    "preferred_markers": [
      "pendelea",
      "kipaumbele",
      "inayopendelewa"
    ],
    "fallback_markers": [
      "mbadala",
      "akiba",
      "ikiwa haipatikani"
    ],
    "forbidden_markers": [
      "usitumie",
      "toa",
      "bila"
    ]
  },
  "status": {
    "unknown": "Haijulikani",
    "verified": "Imethibitishwa",
    "target_platform_missing": "Jukwaa lengwa halipatikani"
  },
  "export": {
    "text": "Toa playlist ya maandishi inayoweza kunakiliwa kwa mpangilio wa sasa.",
    "w4dj": "Unda faili ya UTF-8 `.w4dj` ya kukabidhi kwa W4DJ.",
    "harmonic": "Omba mpangilio wa gurudumu la Camelot ukitumia keys zinazojulikana.",
    "feedback": "Maoni ya lugha ya kawaida husasisha kipindi pekee; kuhifadhi muda mrefu kunahitaji uthibitisho.",
    "memory_confirmation": "Nimeelewa hili kama muhtasari mfupi wa mabadiliko ya ladha. Ihifadhi kwenye wasifu binafsi wa muda mrefu?"
  }
}
```
