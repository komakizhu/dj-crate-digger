# Spanish locale pack

This file is the fixed Español UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "es",
  "language_name": "Spanish",
  "native_name": "Español",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "Si deja la región en blanco, use solo un mercado amplio de habla hispana durante esta sesión.",
    "explicit_region": "Una región explícita tiene prioridad sobre la inferencia lingüística sin cambiar el idioma de comunicación.",
    "persistence": "No guarde el mercado objetivo como preferencia a largo plazo."
  },
  "quick_start": {
    "intro": "Bienvenido al asistente de selección de DJ. Esta Skill de Agent le ayuda a preparar un set. Confirmará sus necesidades en dos rondas y recibirá recomendaciones de temas. Reglas de llenado:",
    "tutorial_label": "Tutorial de importación de sets en un clic",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[Primera ronda: información necesaria]",
      "rules": [
        "1. Puede copiar un ejemplo, escribir libremente o dejarlo en blanco",
        "2. Dejar un campo en blanco significa que la IA juzgará la respuesta de forma inteligente"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "Escenario",
          "example": "Entorno de actuación. Ejemplos: `bar` / `club` / `boda` / `exposición de arte`"
        },
        {
          "key": "target_market",
          "label": "País / región objetivo",
          "example": "Ejemplos: `China continental` / `Taiwán` / `Hong Kong` / `Japón` / `mercado internacional en inglés`"
        },
        {
          "key": "core_sound",
          "label": "Dirección sonora principal",
          "example": "Artista, tema y género de referencia. Ejemplo: `Tears` de `Skrillex`, género `UK Bass` moderno"
        },
        {
          "key": "track_count_or_duration",
          "label": "Cantidad de temas o duración del set",
          "example": "Ejemplos: `20 temas` / `60 minutos`"
        },
        {
          "key": "output_mode",
          "label": "Versión de salida",
          "example": "Opciones Fast / Brief / Rich"
        },
        {
          "key": "other",
          "label": "Otras restricciones",
          "example": "Ejemplos: `evitar temas muy trillados`, `sin voces`, `solo Remix`; opcional"
        }
      ],
      "prompt": "Bienvenido al asistente de selección de DJ. Esta Skill de Agent le ayuda a preparar un set. Confirmará sus necesidades en dos rondas y recibirá recomendaciones de temas. Reglas de llenado:\n\n1. Puede copiar un ejemplo, escribir libremente o dejarlo en blanco\n2. Dejar un campo en blanco significa que la IA juzgará la respuesta de forma inteligente\n\n[Primera ronda: información necesaria]\n\nEscenario:\n“Entorno de actuación. Ejemplos: `bar` / `club` / `boda` / `exposición de arte`”\nPaís / región objetivo:\n“Ejemplos: `China continental` / `Taiwán` / `Hong Kong` / `Japón` / `mercado internacional en inglés`”\nDirección sonora principal:\n“Artista, tema y género de referencia. Ejemplo: `Tears` de `Skrillex`, género `UK Bass` moderno”\nCantidad de temas o duración del set:\n“Ejemplos: `20 temas` / `60 minutos`”\nVersión de salida:\n“`Fast`: lista rápida; la calidad puede ser menor”\n“`Brief`: solo una playlist combinada”\n“`Rich`: vistas separadas de estilo, escena y descubrimiento, seguidas de una playlist combinada final”\nOtras restricciones:\n“Ejemplos: `evitar temas muy trillados`, `sin voces`, `solo Remix`; opcional”\n\n\u0060\u0060\u0060markdown\nEscenario:\nPaís / región objetivo:\nDirección sonora principal:\nCantidad de temas o duración del set:\nVersión de salida:\nOtras restricciones:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[Segunda ronda: precisar la solicitud]",
      "rules": [
        "1. Puede copiar un ejemplo, escribir libremente o dejarlo en blanco"
      ],
      "fields": [
        {
          "key": "style",
          "label": "Estilo específico",
          "example": "Ejemplos: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "Velocidad / BPM",
          "example": "Ejemplos: `105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "Familiaridad y descubrimiento",
          "example": "`Familiar` / `Equilibrado` / `Descubrimiento`"
        },
        {
          "key": "era_classic",
          "label": "Época y clásicos",
          "example": "`Contemporáneo` / `Anclajes clásicos ligeros` / `Puente entre épocas` / `Clásicos primero`"
        },
        {
          "key": "mood",
          "label": "Ánimo",
          "example": "Ejemplos: `nostálgico` / `frío` / `romántico`"
        },
        {
          "key": "energy",
          "label": "Nivel o curva de energía del SET",
          "example": "Ejemplos: `bajo` / `alto`; `estable` / `montaña rusa`"
        },
        {
          "key": "platform",
          "label": "Plataforma y requisitos de enlaces",
          "example": "Ejemplos: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; una plataforma significa usar solo esa; varias siguen el orden indicado"
        },
        {
          "key": "other",
          "label": "Otros",
          "example": ""
        }
      ],
      "prompt": "[Segunda ronda: precisar la solicitud]\n\nEstilo específico:\n“Ejemplos: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`”\nVelocidad / BPM:\n“Ejemplos: `105` / `128` / `140` / `150` / `170`”\nFamiliaridad y descubrimiento:\n“`Familiar` / `Equilibrado` / `Descubrimiento`”\nÉpoca y clásicos:\n“`Contemporáneo` / `Anclajes clásicos ligeros` / `Puente entre épocas` / `Clásicos primero`”\nÁnimo:\n“Ejemplos: `nostálgico` / `frío` / `romántico`”\nNivel o curva de energía del SET:\n“Ejemplos: `bajo` / `alto`; `estable` / `montaña rusa`”\nPlataforma y requisitos de enlaces:\n“Ejemplos: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; una plataforma significa usar solo esa; varias siguen el orden indicado”\nOtros:\n\n\u0060\u0060\u0060markdown\nEstilo específico:\nVelocidad / BPM:\nFamiliaridad y descubrimiento:\nÉpoca y clásicos:\nÁnimo:\nNivel o curva de energía del SET:\nPlataforma y requisitos de enlaces:\nOtros:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# Modo Fast",
      "first_batch_title": "# Primera tanda Fast",
      "final_title": "# Modo Fast",
      "columns": [
        "Tema",
        "Artista",
        "Enlace"
      ],
      "next_steps": [
        {
          "label": "Primero | Compartir comentarios",
          "body": "Si quiere, responda en lenguaje natural sobre cómo funcionaron las selecciones. Esto mejora sus preferencias privadas y futuras recomendaciones."
        },
        {
          "label": "Segundo | Exportar o entregar la playlist",
          "body": "Puede sacar una playlist de texto o entregarla a W4DJ. Responda `output text playlist` o `export to w4dj`."
        }
      ],
      "digging_notes": "Notas de digging",
      "mix_suggestion": "Sugerencia de mezcla",
      "unknown": "Desconocido",
      "verified": "Verificado",
      "target_platform_missing": "Plataforma objetivo no disponible"
    },
    "brief": {
      "title": "# Modo Brief",
      "first_batch_title": "# Modo Brief",
      "final_title": "# Modo Brief",
      "columns": [
        "Tema",
        "Artista",
        "Álbum / EP",
        "Estilo",
        "BPM",
        "Tonalidad",
        "Duración",
        "Energía",
        "Fecha",
        "Notas",
        "Motivo",
        "Enlace"
      ],
      "next_steps": [
        {
          "label": "Primero | Compartir comentarios",
          "body": "Si quiere, responda en lenguaje natural sobre cómo funcionaron las selecciones. Esto mejora sus preferencias privadas y futuras recomendaciones."
        },
        {
          "label": "Segundo | Exportar o entregar la playlist",
          "body": "Puede sacar una playlist de texto o entregarla a W4DJ. Responda `output text playlist` o `export to w4dj`."
        },
        {
          "label": "Tercero | Orden armónico",
          "body": "¿Quiere que ordene el set usando la rueda de Camelot?"
        }
      ],
      "digging_notes": "Notas de digging",
      "mix_suggestion": "Sugerencia de mezcla",
      "unknown": "Desconocido",
      "verified": "Verificado",
      "target_platform_missing": "Plataforma objetivo no disponible"
    },
    "rich": {
      "title": "# Modo Rich",
      "first_batch_title": "# Modo Rich",
      "final_title": "# Modo Rich",
      "columns": [
        "Tema",
        "Artista",
        "Álbum / EP",
        "Estilo",
        "BPM",
        "Tonalidad",
        "Duración",
        "Energía",
        "Fecha",
        "Notas",
        "Motivo",
        "Enlace"
      ],
      "next_steps": [
        {
          "label": "Primero | Compartir comentarios",
          "body": "Si quiere, responda en lenguaje natural sobre cómo funcionaron las selecciones. Esto mejora sus preferencias privadas y futuras recomendaciones."
        },
        {
          "label": "Segundo | Exportar o entregar la playlist",
          "body": "Puede sacar una playlist de texto o entregarla a W4DJ. Responda `output text playlist` o `export to w4dj`."
        },
        {
          "label": "Tercero | Orden armónico",
          "body": "¿Quiere que ordene el set usando la rueda de Camelot?"
        }
      ],
      "digging_notes": "Notas de digging",
      "mix_suggestion": "Sugerencia de mezcla",
      "unknown": "Desconocido",
      "verified": "Verificado",
      "target_platform_missing": "Plataforma objetivo no disponible",
      "view_titles": [
        "Vista de estilo",
        "Vista de escena",
        "Vista de familiaridad / descubrimiento",
        "Vista combinada dinámica"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "Compartir comentarios",
      "positive": [
        "Me gusta este tema"
      ],
      "negative": [
        "No me gusta este tema"
      ],
      "ambiguous": [
        "No estoy seguro sobre este tema"
      ]
    },
    "export_w4dj": {
      "label": "Exportar a W4DJ",
      "positive": [
        "Exportar a W4DJ"
      ],
      "negative": [
        "No exportar a W4DJ"
      ],
      "ambiguous": [
        "Quizá exportar a W4DJ"
      ]
    },
    "output_text_playlist": {
      "label": "Sacar playlist de texto",
      "positive": [
        "Sacar la playlist de texto"
      ],
      "negative": [
        "No sacar la playlist de texto"
      ],
      "ambiguous": [
        "Quizá sacar la playlist de texto"
      ]
    },
    "harmonic_reorder": {
      "label": "Reordenar armónicamente",
      "positive": [
        "Ordenar con la rueda de Camelot"
      ],
      "negative": [
        "No reordenar"
      ],
      "ambiguous": [
        "Quizá ordenar con la rueda de Camelot"
      ]
    },
    "confirm_long_term_memory": {
      "label": "Confirmar memoria a largo plazo",
      "positive": [
        "Recordar esta preferencia"
      ],
      "negative": [
        "No guardar esta preferencia"
      ],
      "ambiguous": [
        "Quizá recordar esta preferencia"
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
      "únicamente",
      "usar solo"
    ],
    "preferred_markers": [
      "preferir",
      "preferida",
      "prioridad"
    ],
    "fallback_markers": [
      "reserva",
      "alternativa",
      "si no está disponible"
    ],
    "forbidden_markers": [
      "no usar",
      "excluir",
      "sin"
    ]
  },
  "status": {
    "unknown": "Desconocido",
    "verified": "Verificado",
    "target_platform_missing": "Plataforma objetivo no disponible"
  },
  "export": {
    "text": "Sacar una playlist de texto copiable en el orden actual.",
    "w4dj": "Crear un archivo `.w4dj` UTF-8 para W4DJ.",
    "harmonic": "Solicitar orden según la rueda de Camelot usando las tonalidades conocidas.",
    "feedback": "Los comentarios en lenguaje natural actualizan solo la sesión; guardar a largo plazo requiere confirmación.",
    "memory_confirmation": "Entiendo esto como un resumen breve del cambio de gustos. ¿Guardarlo en el perfil privado a largo plazo?"
  },
  "trigger_capsule": [
    "set de DJ",
    "playlist",
    "buscar música",
    "buscar pistas",
    "ordenar un set",
    "rápido",
    "breve",
    "completo",
    "crear un set de DJ",
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
