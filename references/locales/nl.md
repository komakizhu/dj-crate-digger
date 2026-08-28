# Dutch locale pack

This file is the fixed Nederlands UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "nl",
  "language_name": "Dutch",
  "native_name": "Nederlands",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "Als de regio leeg is, gebruik dan alleen een brede Nederlandstalige markt voor deze sessie.",
    "explicit_region": "Een expliciete regio gaat vóór taalafleiding, maar verandert de communicatietaal niet.",
    "persistence": "Sla de doelmarkt niet op als langetermijnvoorkeur."
  },
  "quick_start": {
    "intro": "Welkom bij de DJ-keuzeassistent. Deze Agent Skill helpt je een DJ-set samen te stellen. Je bevestigt je wensen in twee rondes en krijgt trackaanbevelingen. Invulregels:",
    "tutorial_label": "Handleiding voor Set-import met één klik",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[Ronde 1: noodzakelijke informatie]",
      "rules": [
        "1. Je kunt een voorbeeld kopiëren, vrij invullen of het veld leeg laten",
        "2. Een leeg veld betekent dat de AI het antwoord intelligent afleidt"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "Context",
          "example": "Context van het optreden. Voorbeelden: `bar` / `club` / `bruiloft` / `kunsttentoonstelling`"
        },
        {
          "key": "target_market",
          "label": "Doelland / doelregio",
          "example": "Voorbeelden: `vasteland China` / `Taiwan` / `Hongkong` / `Japan` / `internationale Engelstalige markt`"
        },
        {
          "key": "core_sound",
          "label": "Belangrijkste klankrichting",
          "example": "Referentieartiest, track en genre. Voorbeeld: `Tears` van `Skrillex`, modern `UK Bass`"
        },
        {
          "key": "track_count_or_duration",
          "label": "Aantal tracks of setduur",
          "example": "Voorbeelden: `20 tracks` / `60 minuten`"
        },
        {
          "key": "output_mode",
          "label": "Uitvoerversie",
          "example": "Keuze Fast / Brief / Rich"
        },
        {
          "key": "other",
          "label": "Andere beperkingen",
          "example": "Voorbeelden: `geen platgedraaide tracks`, `geen vocalen`, `alleen Remix`; optioneel"
        }
      ],
      "prompt": "Welkom bij de DJ-keuzeassistent. Deze Agent Skill helpt je een DJ-set samen te stellen. Je bevestigt je wensen in twee rondes en krijgt trackaanbevelingen. Invulregels:\n\n1. Je kunt een voorbeeld kopiëren, vrij invullen of het veld leeg laten\n2. Een leeg veld betekent dat de AI het antwoord intelligent afleidt\n\n[Ronde 1: noodzakelijke informatie]\n\nContext:\n“Context van het optreden. Voorbeelden: `bar` / `club` / `bruiloft` / `kunsttentoonstelling`”\nDoelland / doelregio:\n“Voorbeelden: `vasteland China` / `Taiwan` / `Hongkong` / `Japan` / `internationale Engelstalige markt`”\nBelangrijkste klankrichting:\n“Referentieartiest, track en genre. Voorbeeld: `Tears` van `Skrillex`, modern `UK Bass`”\nAantal tracks of setduur:\n“Voorbeelden: `20 tracks` / `60 minuten`”\nUitvoerversie:\n“`Fast`: snelle playlist; kwaliteit kan lager zijn”\n“`Brief`: alleen één gecombineerde playlist”\n“`Rich`: aparte stijl-, context- en ontdekkingsweergaven, gevolgd door een gecombineerde playlist”\nAndere beperkingen:\n“Voorbeelden: `geen platgedraaide tracks`, `geen vocalen`, `alleen Remix`; optioneel”\n\n\u0060\u0060\u0060markdown\nContext:\nDoelland / doelregio:\nBelangrijkste klankrichting:\nAantal tracks of setduur:\nUitvoerversie:\nAndere beperkingen:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[Ronde 2: verzoek verfijnen]",
      "rules": [
        "1. Je kunt een voorbeeld kopiëren, vrij invullen of het veld leeg laten"
      ],
      "fields": [
        {
          "key": "style",
          "label": "Specifieke stijl",
          "example": "Voorbeelden: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "Snelheid / BPM",
          "example": "Voorbeelden: `105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "Vertrouwdheid en ontdekking",
          "example": "`Vertrouwd` / `Gebalanceerd` / `Ontdekking`"
        },
        {
          "key": "era_classic",
          "label": "Tijdperk en klassiekers",
          "example": "`Hedendaags` / `Enkele klassieke ankers` / `Brug tussen nieuw en oud` / `Klassiekers eerst`"
        },
        {
          "key": "mood",
          "label": "Sfeer",
          "example": "Voorbeelden: `nostalgisch` / `koud` / `romantisch`"
        },
        {
          "key": "energy",
          "label": "SET-energieniveau of energiecurve",
          "example": "Voorbeelden: `laag` / `hoog`; `gelijkmatig` / `achtbaan`"
        },
        {
          "key": "platform",
          "label": "Platform en linkvereisten",
          "example": "Voorbeelden: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; één platform betekent alleen dat platform, meerdere volgen de opgegeven volgorde"
        },
        {
          "key": "other",
          "label": "Overig",
          "example": ""
        }
      ],
      "prompt": "[Ronde 2: verzoek verfijnen]\n\nSpecifieke stijl:\n“Voorbeelden: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`”\nSnelheid / BPM:\n“Voorbeelden: `105` / `128` / `140` / `150` / `170`”\nVertrouwdheid en ontdekking:\n“`Vertrouwd` / `Gebalanceerd` / `Ontdekking`”\nTijdperk en klassiekers:\n“`Hedendaags` / `Enkele klassieke ankers` / `Brug tussen nieuw en oud` / `Klassiekers eerst`”\nSfeer:\n“Voorbeelden: `nostalgisch` / `koud` / `romantisch`”\nSET-energieniveau of energiecurve:\n“Voorbeelden: `laag` / `hoog`; `gelijkmatig` / `achtbaan`”\nPlatform en linkvereisten:\n“Voorbeelden: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; één platform betekent alleen dat platform, meerdere volgen de opgegeven volgorde”\nOverig:\n\n\u0060\u0060\u0060markdown\nSpecifieke stijl:\nSnelheid / BPM:\nVertrouwdheid en ontdekking:\nTijdperk en klassiekers:\nSfeer:\nSET-energieniveau of energiecurve:\nPlatform en linkvereisten:\nOverig:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# Fast-modus",
      "first_batch_title": "# Eerste Fast-selectie",
      "final_title": "# Fast-modus",
      "columns": [
        "Track",
        "Artiest",
        "Link"
      ],
      "next_steps": [
        {
          "label": "Eerste | Deel selectiefeedback",
          "body": "Als je wilt, beschrijf in natuurlijke taal hoe de selectie werkte. Dit verbetert je privévoorkeuren en volgende aanbevelingen."
        },
        {
          "label": "Tweede | Playlist exporteren of doorgeven",
          "body": "Je kunt een tekstplaylist maken of die aan W4DJ doorgeven. Antwoord `output text playlist` of `export to w4dj`."
        }
      ],
      "digging_notes": "Digging-notities",
      "mix_suggestion": "Mixsuggestie",
      "unknown": "Onbekend",
      "verified": "Geverifieerd",
      "target_platform_missing": "Doelplatform niet beschikbaar"
    },
    "brief": {
      "title": "# Brief-modus",
      "first_batch_title": "# Brief-modus",
      "final_title": "# Brief-modus",
      "columns": [
        "Track",
        "Artiest",
        "Album / EP",
        "Stijl",
        "BPM",
        "Toonsoort",
        "Duur",
        "Energie",
        "Releasedatum",
        "Notities",
        "Reden",
        "Link"
      ],
      "next_steps": [
        {
          "label": "Eerste | Deel selectiefeedback",
          "body": "Als je wilt, beschrijf in natuurlijke taal hoe de selectie werkte. Dit verbetert je privévoorkeuren en volgende aanbevelingen."
        },
        {
          "label": "Tweede | Playlist exporteren of doorgeven",
          "body": "Je kunt een tekstplaylist maken of die aan W4DJ doorgeven. Antwoord `output text playlist` of `export to w4dj`."
        },
        {
          "label": "Derde | Harmonische setvolgorde",
          "body": "Zal ik de set ordenen met het Camelot-wiel?"
        }
      ],
      "digging_notes": "Digging-notities",
      "mix_suggestion": "Mixsuggestie",
      "unknown": "Onbekend",
      "verified": "Geverifieerd",
      "target_platform_missing": "Doelplatform niet beschikbaar"
    },
    "rich": {
      "title": "# Rich-modus",
      "first_batch_title": "# Rich-modus",
      "final_title": "# Rich-modus",
      "columns": [
        "Track",
        "Artiest",
        "Album / EP",
        "Stijl",
        "BPM",
        "Toonsoort",
        "Duur",
        "Energie",
        "Releasedatum",
        "Notities",
        "Reden",
        "Link"
      ],
      "next_steps": [
        {
          "label": "Eerste | Deel selectiefeedback",
          "body": "Als je wilt, beschrijf in natuurlijke taal hoe de selectie werkte. Dit verbetert je privévoorkeuren en volgende aanbevelingen."
        },
        {
          "label": "Tweede | Playlist exporteren of doorgeven",
          "body": "Je kunt een tekstplaylist maken of die aan W4DJ doorgeven. Antwoord `output text playlist` of `export to w4dj`."
        },
        {
          "label": "Derde | Harmonische setvolgorde",
          "body": "Zal ik de set ordenen met het Camelot-wiel?"
        }
      ],
      "digging_notes": "Digging-notities",
      "mix_suggestion": "Mixsuggestie",
      "unknown": "Onbekend",
      "verified": "Geverifieerd",
      "target_platform_missing": "Doelplatform niet beschikbaar",
      "view_titles": [
        "Stijlweergave",
        "Contextweergave",
        "Vertrouwdheid / ontdekking",
        "Dynamische gecombineerde weergave"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "Selectiefeedback delen",
      "positive": [
        "Ik vind deze track goed"
      ],
      "negative": [
        "Ik vind deze track niet goed"
      ],
      "ambiguous": [
        "Ik weet het niet zeker over deze track"
      ]
    },
    "export_w4dj": {
      "label": "Exporteren naar W4DJ",
      "positive": [
        "Exporteren naar W4DJ"
      ],
      "negative": [
        "Niet exporteren naar W4DJ"
      ],
      "ambiguous": [
        "Misschien exporteren naar W4DJ"
      ]
    },
    "output_text_playlist": {
      "label": "Tekstplaylist maken",
      "positive": [
        "De tekstplaylist maken"
      ],
      "negative": [
        "De tekstplaylist niet maken"
      ],
      "ambiguous": [
        "Misschien de tekstplaylist maken"
      ]
    },
    "harmonic_reorder": {
      "label": "Harmonisch herschikken",
      "positive": [
        "Ordenen met het Camelot-wiel"
      ],
      "negative": [
        "Niet herschikken"
      ],
      "ambiguous": [
        "Misschien ordenen met het Camelot-wiel"
      ]
    },
    "confirm_long_term_memory": {
      "label": "Langetermijngeheugen bevestigen",
      "positive": [
        "Deze voorkeur onthouden"
      ],
      "negative": [
        "Deze voorkeur niet opslaan"
      ],
      "ambiguous": [
        "Deze voorkeur misschien onthouden"
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
      "alleen",
      "uitsluitend",
      "alleen gebruiken"
    ],
    "preferred_markers": [
      "voorkeur",
      "bij voorkeur",
      "prioriteit"
    ],
    "fallback_markers": [
      "reserve",
      "alternatief",
      "als het niet beschikbaar is"
    ],
    "forbidden_markers": [
      "niet gebruiken",
      "uitsluiten",
      "zonder"
    ]
  },
  "status": {
    "unknown": "Onbekend",
    "verified": "Geverifieerd",
    "target_platform_missing": "Doelplatform niet beschikbaar"
  },
  "export": {
    "text": "Maak een kopieerbare tekstplaylist in de huidige volgorde.",
    "w4dj": "Maak een UTF-8 `.w4dj`-overdrachtsbestand voor W4DJ.",
    "harmonic": "Vraag om ordening volgens het Camelot-wiel met bekende toonsoorten.",
    "feedback": "Feedback in natuurlijke taal werkt alleen de sessie bij; langdurige opslag vereist bevestiging.",
    "memory_confirmation": "Ik begrijp dit als een korte samenvatting van een smaakverandering. Opslaan in het privé-langetermijnprofiel?"
  }
}
```
