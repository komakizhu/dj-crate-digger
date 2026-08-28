# Italian locale pack

This file is the fixed Italiano UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "it",
  "language_name": "Italian",
  "native_name": "Italiano",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "Se la regione è vuota, usa solo un ampio mercato italofono per questa sessione.",
    "explicit_region": "Una regione esplicita prevale sull’inferenza linguistica senza cambiare la lingua di comunicazione.",
    "persistence": "Non salvare il mercato target come preferenza a lungo termine."
  },
  "quick_start": {
    "intro": "Benvenuto nell’assistente per la selezione DJ. Questa Skill di Agent ti aiuta a preparare un set DJ. Confermerai le tue esigenze in due turni e riceverai consigli sui brani. Regole di compilazione:",
    "tutorial_label": "Guida all’importazione Set con un clic",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[Primo turno: informazioni necessarie]",
      "rules": [
        "1. Puoi copiare un esempio, compilare liberamente o lasciare vuoto",
        "2. Lasciare vuoto significa che l’IA valuterà intelligentemente la risposta"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "Contesto",
          "example": "Contesto della performance. Esempi: `bar` / `club` / `matrimonio` / `mostra d’arte`"
        },
        {
          "key": "target_market",
          "label": "Paese / regione target",
          "example": "Esempi: `Cina continentale` / `Taiwan` / `Hong Kong` / `Giappone` / `mercato internazionale anglofono`"
        },
        {
          "key": "core_sound",
          "label": "Direzione sonora principale",
          "example": "Artista, brano e genere di riferimento. Esempio: `Tears` di `Skrillex`, genere `UK Bass` moderno"
        },
        {
          "key": "track_count_or_duration",
          "label": "Numero di brani o durata del set",
          "example": "Esempi: `20 brani` / `60 minuti`"
        },
        {
          "key": "output_mode",
          "label": "Versione di output",
          "example": "Scelta Fast / Brief / Rich"
        },
        {
          "key": "other",
          "label": "Altri vincoli",
          "example": "Esempi: `evitare brani abusati`, `senza voce`, `solo Remix`; facoltativo"
        }
      ],
      "prompt": "Benvenuto nell’assistente per la selezione DJ. Questa Skill di Agent ti aiuta a preparare un set DJ. Confermerai le tue esigenze in due turni e riceverai consigli sui brani. Regole di compilazione:\n\n1. Puoi copiare un esempio, compilare liberamente o lasciare vuoto\n2. Lasciare vuoto significa che l’IA valuterà intelligentemente la risposta\n\n[Primo turno: informazioni necessarie]\n\nContesto:\n“Contesto della performance. Esempi: `bar` / `club` / `matrimonio` / `mostra d’arte`”\nPaese / regione target:\n“Esempi: `Cina continentale` / `Taiwan` / `Hong Kong` / `Giappone` / `mercato internazionale anglofono`”\nDirezione sonora principale:\n“Artista, brano e genere di riferimento. Esempio: `Tears` di `Skrillex`, genere `UK Bass` moderno”\nNumero di brani o durata del set:\n“Esempi: `20 brani` / `60 minuti`”\nVersione di output:\n“`Fast`: playlist rapida; la qualità può essere inferiore”\n“`Brief`: una sola playlist combinata”\n“`Rich`: viste separate di stile, contesto e scoperta, poi playlist combinata finale”\nAltri vincoli:\n“Esempi: `evitare brani abusati`, `senza voce`, `solo Remix`; facoltativo”\n\n\u0060\u0060\u0060markdown\nContesto:\nPaese / regione target:\nDirezione sonora principale:\nNumero di brani o durata del set:\nVersione di output:\nAltri vincoli:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[Secondo turno: definire la richiesta]",
      "rules": [
        "1. Puoi copiare un esempio, compilare liberamente o lasciare vuoto"
      ],
      "fields": [
        {
          "key": "style",
          "label": "Stile specifico",
          "example": "Esempi: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "Velocità / BPM",
          "example": "Esempi: `105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "Familiarità e scoperta",
          "example": "`Familiare` / `Bilanciato` / `Scoperta`"
        },
        {
          "key": "era_classic",
          "label": "Epoca e classici",
          "example": "`Contemporaneo` / `Pochi ancoraggi classici` / `Ponte tra nuovo e vecchio` / `Classici prima`"
        },
        {
          "key": "mood",
          "label": "Umore",
          "example": "Esempi: `nostalgico` / `freddo` / `romantico`"
        },
        {
          "key": "energy",
          "label": "Livello o curva energetica del SET",
          "example": "Esempi: `basso` / `alto`; `costante` / `montagne russe`"
        },
        {
          "key": "platform",
          "label": "Piattaforma e requisiti dei link",
          "example": "Esempi: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; una piattaforma significa solo quella, più piattaforme seguono l’ordine"
        },
        {
          "key": "other",
          "label": "Altro",
          "example": ""
        }
      ],
      "prompt": "[Secondo turno: definire la richiesta]\n\nStile specifico:\n“Esempi: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`”\nVelocità / BPM:\n“Esempi: `105` / `128` / `140` / `150` / `170`”\nFamiliarità e scoperta:\n“`Familiare` / `Bilanciato` / `Scoperta`”\nEpoca e classici:\n“`Contemporaneo` / `Pochi ancoraggi classici` / `Ponte tra nuovo e vecchio` / `Classici prima`”\nUmore:\n“Esempi: `nostalgico` / `freddo` / `romantico`”\nLivello o curva energetica del SET:\n“Esempi: `basso` / `alto`; `costante` / `montagne russe`”\nPiattaforma e requisiti dei link:\n“Esempi: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; una piattaforma significa solo quella, più piattaforme seguono l’ordine”\nAltro:\n\n\u0060\u0060\u0060markdown\nStile specifico:\nVelocità / BPM:\nFamiliarità e scoperta:\nEpoca e classici:\nUmore:\nLivello o curva energetica del SET:\nPiattaforma e requisiti dei link:\nAltro:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# Modalità Fast",
      "first_batch_title": "# Prima selezione Fast",
      "final_title": "# Modalità Fast",
      "columns": [
        "Brano",
        "Artista",
        "Link"
      ],
      "next_steps": [
        {
          "label": "Primo | Condividi il feedback",
          "body": "Se vuoi, descrivi in linguaggio naturale come hanno funzionato le selezioni. Questo migliora le tue preferenze private e i prossimi consigli."
        },
        {
          "label": "Secondo | Esporta o consegna la playlist",
          "body": "Puoi produrre una playlist testuale o consegnarla a W4DJ. Rispondi `output text playlist` o `export to w4dj`."
        }
      ],
      "digging_notes": "Note di digging",
      "mix_suggestion": "Suggerimento di mix",
      "unknown": "Sconosciuto",
      "verified": "Verificato",
      "target_platform_missing": "Piattaforma target non disponibile"
    },
    "brief": {
      "title": "# Modalità Brief",
      "first_batch_title": "# Modalità Brief",
      "final_title": "# Modalità Brief",
      "columns": [
        "Brano",
        "Artista",
        "Album / EP",
        "Stile",
        "BPM",
        "Tonalità",
        "Durata",
        "Energia",
        "Data di uscita",
        "Note",
        "Motivo della scelta",
        "Link"
      ],
      "next_steps": [
        {
          "label": "Primo | Condividi il feedback",
          "body": "Se vuoi, descrivi in linguaggio naturale come hanno funzionato le selezioni. Questo migliora le tue preferenze private e i prossimi consigli."
        },
        {
          "label": "Secondo | Esporta o consegna la playlist",
          "body": "Puoi produrre una playlist testuale o consegnarla a W4DJ. Rispondi `output text playlist` o `export to w4dj`."
        },
        {
          "label": "Terzo | Ordine armonico del set",
          "body": "Vuoi che ordini il set usando la ruota di Camelot?"
        }
      ],
      "digging_notes": "Note di digging",
      "mix_suggestion": "Suggerimento di mix",
      "unknown": "Sconosciuto",
      "verified": "Verificato",
      "target_platform_missing": "Piattaforma target non disponibile"
    },
    "rich": {
      "title": "# Modalità Rich",
      "first_batch_title": "# Modalità Rich",
      "final_title": "# Modalità Rich",
      "columns": [
        "Brano",
        "Artista",
        "Album / EP",
        "Stile",
        "BPM",
        "Tonalità",
        "Durata",
        "Energia",
        "Data di uscita",
        "Note",
        "Motivo della scelta",
        "Link"
      ],
      "next_steps": [
        {
          "label": "Primo | Condividi il feedback",
          "body": "Se vuoi, descrivi in linguaggio naturale come hanno funzionato le selezioni. Questo migliora le tue preferenze private e i prossimi consigli."
        },
        {
          "label": "Secondo | Esporta o consegna la playlist",
          "body": "Puoi produrre una playlist testuale o consegnarla a W4DJ. Rispondi `output text playlist` o `export to w4dj`."
        },
        {
          "label": "Terzo | Ordine armonico del set",
          "body": "Vuoi che ordini il set usando la ruota di Camelot?"
        }
      ],
      "digging_notes": "Note di digging",
      "mix_suggestion": "Suggerimento di mix",
      "unknown": "Sconosciuto",
      "verified": "Verificato",
      "target_platform_missing": "Piattaforma target non disponibile",
      "view_titles": [
        "Vista stile",
        "Vista contesto",
        "Vista familiarità / scoperta",
        "Vista combinata dinamica"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "Condividi feedback",
      "positive": [
        "Mi piace questo brano"
      ],
      "negative": [
        "Non mi piace questo brano"
      ],
      "ambiguous": [
        "Non sono sicuro di questo brano"
      ]
    },
    "export_w4dj": {
      "label": "Esporta in W4DJ",
      "positive": [
        "Esporta in W4DJ"
      ],
      "negative": [
        "Non esportare in W4DJ"
      ],
      "ambiguous": [
        "Forse esporta in W4DJ"
      ]
    },
    "output_text_playlist": {
      "label": "Produci playlist testuale",
      "positive": [
        "Produci la playlist testuale"
      ],
      "negative": [
        "Non produrre la playlist testuale"
      ],
      "ambiguous": [
        "Forse produci la playlist testuale"
      ]
    },
    "harmonic_reorder": {
      "label": "Riordina armonicamente",
      "positive": [
        "Ordina con la ruota di Camelot"
      ],
      "negative": [
        "Non riordinare"
      ],
      "ambiguous": [
        "Forse ordina con la ruota di Camelot"
      ]
    },
    "confirm_long_term_memory": {
      "label": "Conferma memoria a lungo termine",
      "positive": [
        "Ricorda questa preferenza"
      ],
      "negative": [
        "Non salvare questa preferenza"
      ],
      "ambiguous": [
        "Forse ricorda questa preferenza"
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
      "solo",
      "unicamente",
      "usare solo"
    ],
    "preferred_markers": [
      "preferire",
      "preferita",
      "priorità"
    ],
    "fallback_markers": [
      "riserva",
      "alternativa",
      "se non disponibile"
    ],
    "forbidden_markers": [
      "non usare",
      "escludere",
      "senza"
    ]
  },
  "status": {
    "unknown": "Sconosciuto",
    "verified": "Verificato",
    "target_platform_missing": "Piattaforma target non disponibile"
  },
  "export": {
    "text": "Produci una playlist testuale copiabile nell’ordine attuale.",
    "w4dj": "Crea un file di consegna UTF-8 `.w4dj` per W4DJ.",
    "harmonic": "Richiedi l’ordine secondo la ruota di Camelot usando le tonalità note.",
    "feedback": "Il feedback naturale aggiorna solo la sessione; la memoria a lungo termine richiede conferma.",
    "memory_confirmation": "Ho interpretato questo come un breve riepilogo di un cambiamento di gusto. Salvarlo nel profilo privato a lungo termine?"
  }
}
```
