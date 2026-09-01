# German locale pack

This file is the fixed Deutsch UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "de",
  "language_name": "German",
  "native_name": "Deutsch",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "Wenn die Region leer bleibt, verwende für diese Sitzung nur einen breiten deutschsprachigen Markt.",
    "explicit_region": "Eine ausdrücklich genannte Region überstimmt die Sprachinferenz, ändert aber nicht die Kommunikationssprache.",
    "persistence": "Der Zielmarkt wird nicht als langfristige Präferenz gespeichert."
  },
  "quick_start": {
    "intro": "Willkommen beim DJ-Auswahlassistenten. Dieses Agent Skill hilft dir, ein DJ-Set zusammenzustellen. Du bestätigst deine Wünsche in zwei Runden und erhältst Track-Empfehlungen. Ausfüllregeln:",
    "tutorial_label": "Anleitung für den Ein-Klick-Set-Import",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[Runde 1: Grundinformationen]",
      "rules": [
        "1. Du kannst ein Beispiel kopieren, frei ausfüllen oder das Feld leer lassen",
        "2. Ein leeres Feld bedeutet, dass die KI die Antwort intelligent einschätzt"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "Situation",
          "example": "Auftrittssituation. Beispiele: `Bar` / `Club` / `Hochzeit` / `Kunstausstellung`"
        },
        {
          "key": "target_market",
          "label": "Zielland / Zielregion",
          "example": "Beispiele: `Festlandchina` / `Taiwan` / `Hongkong` / `Japan` / `internationaler englischsprachiger Markt`"
        },
        {
          "key": "core_sound",
          "label": "Zentrale Klangrichtung",
          "example": "Referenzkünstler, Track und Genre. Beispiel: `Tears` von `Skrillex`, modernes `UK Bass`"
        },
        {
          "key": "track_count_or_duration",
          "label": "Anzahl Tracks oder Set-Dauer",
          "example": "Beispiele: `20 Tracks` / `60 Minuten`"
        },
        {
          "key": "output_mode",
          "label": "Ausgabeversion",
          "example": "Auswahl Fast / Brief / Rich"
        },
        {
          "key": "other",
          "label": "Weitere Einschränkungen",
          "example": "Beispiele: `keine überstrapazierten Tracks`, `keine Vocals`, `nur Remix`; optional"
        }
      ],
      "prompt": "Willkommen beim DJ-Auswahlassistenten. Dieses Agent Skill hilft dir, ein DJ-Set zusammenzustellen. Du bestätigst deine Wünsche in zwei Runden und erhältst Track-Empfehlungen. Ausfüllregeln:\n\n1. Du kannst ein Beispiel kopieren, frei ausfüllen oder das Feld leer lassen\n2. Ein leeres Feld bedeutet, dass die KI die Antwort intelligent einschätzt\n\n[Runde 1: Grundinformationen]\n\nSituation:\n“Auftrittssituation. Beispiele: `Bar` / `Club` / `Hochzeit` / `Kunstausstellung`”\nZielland / Zielregion:\n“Beispiele: `Festlandchina` / `Taiwan` / `Hongkong` / `Japan` / `internationaler englischsprachiger Markt`”\nZentrale Klangrichtung:\n“Referenzkünstler, Track und Genre. Beispiel: `Tears` von `Skrillex`, modernes `UK Bass`”\nAnzahl Tracks oder Set-Dauer:\n“Beispiele: `20 Tracks` / `60 Minuten`”\nAusgabeversion:\n“`Fast`: schnelle Playlist-Ausgabe; die Qualität kann geringer sein”\n“`Brief`: nur eine kombinierte Playlist”\n“`Rich`: getrennte Ansichten für Stil, Situation und Entdeckung, danach eine kombinierte Playlist”\nWeitere Einschränkungen:\n“Beispiele: `keine überstrapazierten Tracks`, `keine Vocals`, `nur Remix`; optional”\n\n\u0060\u0060\u0060markdown\nSituation:\nZielland / Zielregion:\nZentrale Klangrichtung:\nAnzahl Tracks oder Set-Dauer:\nAusgabeversion:\nWeitere Einschränkungen:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[Runde 2: Anfrage verfeinern]",
      "rules": [
        "1. Du kannst ein Beispiel kopieren, frei ausfüllen oder das Feld leer lassen"
      ],
      "fields": [
        {
          "key": "style",
          "label": "Konkreter Stil",
          "example": "Beispiele: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "Geschwindigkeit / BPM",
          "example": "Beispiele: `105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "Vertrautheit und Entdeckung",
          "example": "`Vertraut` / `Ausgewogen` / `Entdeckung`"
        },
        {
          "key": "era_classic",
          "label": "Epoche und Klassiker",
          "example": "`Zeitgenössisch` / `Wenige klassische Anker` / `Brücke zwischen neu und alt` / `Klassiker zuerst`"
        },
        {
          "key": "mood",
          "label": "Stimmung",
          "example": "Beispiele: `nostalgisch` / `kalt` / `romantisch`"
        },
        {
          "key": "energy",
          "label": "SET-Energie oder Energieverlauf",
          "example": "Beispiele: `niedrig` / `hoch`; `gleichmäßig` / `Achterbahn`"
        },
        {
          "key": "platform",
          "label": "Plattform und Link-Anforderungen",
          "example": "Beispiele: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; eine Plattform bedeutet nur diese; mehrere folgen der angegebenen Priorität"
        },
        {
          "key": "other",
          "label": "Sonstiges",
          "example": ""
        }
      ],
      "prompt": "[Runde 2: Anfrage verfeinern]\n\nKonkreter Stil:\n“Beispiele: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`”\nGeschwindigkeit / BPM:\n“Beispiele: `105` / `128` / `140` / `150` / `170`”\nVertrautheit und Entdeckung:\n“`Vertraut` / `Ausgewogen` / `Entdeckung`”\nEpoche und Klassiker:\n“`Zeitgenössisch` / `Wenige klassische Anker` / `Brücke zwischen neu und alt` / `Klassiker zuerst`”\nStimmung:\n“Beispiele: `nostalgisch` / `kalt` / `romantisch`”\nSET-Energie oder Energieverlauf:\n“Beispiele: `niedrig` / `hoch`; `gleichmäßig` / `Achterbahn`”\nPlattform und Link-Anforderungen:\n“Beispiele: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; eine Plattform bedeutet nur diese; mehrere folgen der angegebenen Priorität”\nSonstiges:\n\n\u0060\u0060\u0060markdown\nKonkreter Stil:\nGeschwindigkeit / BPM:\nVertrautheit und Entdeckung:\nEpoche und Klassiker:\nStimmung:\nSET-Energie oder Energieverlauf:\nPlattform und Link-Anforderungen:\nSonstiges:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# Fast-Modus",
      "first_batch_title": "# Erste Fast-Auswahl",
      "final_title": "# Fast-Modus",
      "columns": [
        "Track",
        "Künstler",
        "Link"
      ],
      "next_steps": [
        {
          "label": "Erstens | Auswahl-Feedback teilen",
          "body": "Wenn du möchtest, beschreibe in natürlicher Sprache, wie die Auswahl funktioniert hat. Das verbessert deine privaten Auswahlpräferenzen und künftige Empfehlungen."
        },
        {
          "label": "Zweitens | Playlist exportieren oder übergeben",
          "body": "Du kannst eine Text-Playlist ausgeben oder sie an W4DJ übergeben. Antworte mit `output text playlist` oder `export to w4dj`."
        }
      ],
      "digging_notes": "Digging-Notizen",
      "mix_suggestion": "Mix-Vorschlag",
      "unknown": "Unbekannt",
      "verified": "Verifiziert",
      "target_platform_missing": "Zielplattform nicht verfügbar"
    },
    "brief": {
      "title": "# Brief-Modus",
      "first_batch_title": "# Brief-Modus",
      "final_title": "# Brief-Modus",
      "columns": [
        "Track",
        "Künstler",
        "Album / EP",
        "Stil",
        "BPM",
        "Tonart",
        "Dauer",
        "Energie",
        "Veröffentlichung",
        "Notizen",
        "Auswahlgrund",
        "Link"
      ],
      "next_steps": [
        {
          "label": "Erstens | Auswahl-Feedback teilen",
          "body": "Wenn du möchtest, beschreibe in natürlicher Sprache, wie die Auswahl funktioniert hat. Das verbessert deine privaten Auswahlpräferenzen und künftige Empfehlungen."
        },
        {
          "label": "Zweitens | Playlist exportieren oder übergeben",
          "body": "Du kannst eine Text-Playlist ausgeben oder sie an W4DJ übergeben. Antworte mit `output text playlist` oder `export to w4dj`."
        },
        {
          "label": "Drittens | Harmonische Set-Reihenfolge",
          "body": "Soll ich das Set mit dem Camelot-Rad ordnen?"
        }
      ],
      "digging_notes": "Digging-Notizen",
      "mix_suggestion": "Mix-Vorschlag",
      "unknown": "Unbekannt",
      "verified": "Verifiziert",
      "target_platform_missing": "Zielplattform nicht verfügbar"
    },
    "rich": {
      "title": "# Rich-Modus",
      "first_batch_title": "# Rich-Modus",
      "final_title": "# Rich-Modus",
      "columns": [
        "Track",
        "Künstler",
        "Album / EP",
        "Stil",
        "BPM",
        "Tonart",
        "Dauer",
        "Energie",
        "Veröffentlichung",
        "Notizen",
        "Auswahlgrund",
        "Link"
      ],
      "next_steps": [
        {
          "label": "Erstens | Auswahl-Feedback teilen",
          "body": "Wenn du möchtest, beschreibe in natürlicher Sprache, wie die Auswahl funktioniert hat. Das verbessert deine privaten Auswahlpräferenzen und künftige Empfehlungen."
        },
        {
          "label": "Zweitens | Playlist exportieren oder übergeben",
          "body": "Du kannst eine Text-Playlist ausgeben oder sie an W4DJ übergeben. Antworte mit `output text playlist` oder `export to w4dj`."
        },
        {
          "label": "Drittens | Harmonische Set-Reihenfolge",
          "body": "Soll ich das Set mit dem Camelot-Rad ordnen?"
        }
      ],
      "digging_notes": "Digging-Notizen",
      "mix_suggestion": "Mix-Vorschlag",
      "unknown": "Unbekannt",
      "verified": "Verifiziert",
      "target_platform_missing": "Zielplattform nicht verfügbar",
      "view_titles": [
        "Stilansicht",
        "Situationsansicht",
        "Vertrautheit / Entdeckung",
        "Dynamische kombinierte Ansicht"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "Auswahl-Feedback teilen",
      "positive": [
        "Diesen Track mag ich"
      ],
      "negative": [
        "Diesen Track mag ich nicht"
      ],
      "ambiguous": [
        "Bei diesem Track bin ich unsicher"
      ]
    },
    "export_w4dj": {
      "label": "An W4DJ exportieren",
      "positive": [
        "An W4DJ exportieren"
      ],
      "negative": [
        "Nicht an W4DJ exportieren"
      ],
      "ambiguous": [
        "Vielleicht an W4DJ exportieren"
      ]
    },
    "output_text_playlist": {
      "label": "Text-Playlist ausgeben",
      "positive": [
        "Text-Playlist ausgeben"
      ],
      "negative": [
        "Keine Text-Playlist ausgeben"
      ],
      "ambiguous": [
        "Vielleicht Text-Playlist ausgeben"
      ]
    },
    "harmonic_reorder": {
      "label": "Harmonisch neu ordnen",
      "positive": [
        "Mit dem Camelot-Rad ordnen"
      ],
      "negative": [
        "Nicht neu ordnen"
      ],
      "ambiguous": [
        "Vielleicht mit dem Camelot-Rad ordnen"
      ]
    },
    "confirm_long_term_memory": {
      "label": "Langzeitgedächtnis bestätigen",
      "positive": [
        "Diese Präferenz merken"
      ],
      "negative": [
        "Diese Präferenz nicht speichern"
      ],
      "ambiguous": [
        "Diese Präferenz vielleicht merken"
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
      "nur",
      "ausschließlich",
      "nur verwenden"
    ],
    "preferred_markers": [
      "bevorzugen",
      "bevorzugt",
      "Priorität"
    ],
    "fallback_markers": [
      "Ersatz",
      "Ausweichoption",
      "falls nicht verfügbar"
    ],
    "forbidden_markers": [
      "nicht verwenden",
      "ausschließen",
      "ohne"
    ]
  },
  "status": {
    "unknown": "Unbekannt",
    "verified": "Verifiziert",
    "target_platform_missing": "Zielplattform nicht verfügbar"
  },
  "export": {
    "text": "Eine kopierbare Text-Playlist in der aktuellen Reihenfolge ausgeben.",
    "w4dj": "Eine UTF-8-`.w4dj`-Übergabedatei für W4DJ erstellen.",
    "harmonic": "Eine Anordnung nach dem Camelot-Rad mit bekannten Tonarten anfordern.",
    "feedback": "Feedback in natürlicher Sprache aktualisiert nur die Sitzung; langfristiges Speichern braucht Bestätigung.",
    "memory_confirmation": "Ich verstehe das als kurze Zusammenfassung einer Geschmacksänderung. Im privaten Langzeitprofil speichern?"
  },
  "trigger_capsule": [
    "DJ-Set",
    "Playlist",
    "Musik suchen",
    "Tracks finden",
    "Set zusammenstellen"
  ]
}
```
