# French locale pack

This file is the fixed Français UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "fr",
  "language_name": "French",
  "native_name": "Français",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "Si la région est vide, utilisez uniquement un marché francophone large pour cette session.",
    "explicit_region": "Une région explicitement indiquée prime sur l’inférence linguistique sans modifier la langue de communication.",
    "persistence": "Ne mémorisez pas le marché cible comme préférence durable."
  },
  "quick_start": {
    "intro": "Bienvenue dans l’assistant de sélection DJ. Cette Skill d’Agent vous aide à préparer un set. Vous confirmerez votre demande en deux tours et recevrez des recommandations de morceaux. Règles de saisie :",
    "tutorial_label": "Tutoriel d’importation de Set en un clic",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[Premier tour : informations essentielles]",
      "rules": [
        "1. Vous pouvez copier un exemple, remplir librement ou laisser le champ vide",
        "2. Un champ vide signifie que l’IA jugera intelligemment la réponse"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "Contexte",
          "example": "Cadre de la prestation. Exemples : `bar` / `club` / `mariage` / `exposition d’art`"
        },
        {
          "key": "target_market",
          "label": "Pays / région cible",
          "example": "Exemples : `Chine continentale` / `Taïwan` / `Hong Kong` / `Japon` / `marché international anglophone`"
        },
        {
          "key": "core_sound",
          "label": "Direction sonore principale",
          "example": "Artiste, morceau et genre de référence. Exemple : `Tears` de `Skrillex`, genre `UK Bass` moderne"
        },
        {
          "key": "track_count_or_duration",
          "label": "Nombre de morceaux ou durée du set",
          "example": "Exemples : `20 morceaux` / `60 minutes`"
        },
        {
          "key": "output_mode",
          "label": "Version de sortie",
          "example": "Choix Fast / Brief / Rich"
        },
        {
          "key": "other",
          "label": "Autres contraintes",
          "example": "Exemples : `éviter les morceaux trop joués`, `sans voix`, `Remix uniquement` ; facultatif"
        }
      ],
      "prompt": "Bienvenue dans l’assistant de sélection DJ. Cette Skill d’Agent vous aide à préparer un set. Vous confirmerez votre demande en deux tours et recevrez des recommandations de morceaux. Règles de saisie :\n\n1. Vous pouvez copier un exemple, remplir librement ou laisser le champ vide\n2. Un champ vide signifie que l’IA jugera intelligemment la réponse\n\n[Premier tour : informations essentielles]\n\nContexte:\n“Cadre de la prestation. Exemples : `bar` / `club` / `mariage` / `exposition d’art`”\nPays / région cible:\n“Exemples : `Chine continentale` / `Taïwan` / `Hong Kong` / `Japon` / `marché international anglophone`”\nDirection sonore principale:\n“Artiste, morceau et genre de référence. Exemple : `Tears` de `Skrillex`, genre `UK Bass` moderne”\nNombre de morceaux ou durée du set:\n“Exemples : `20 morceaux` / `60 minutes`”\nVersion de sortie:\n“`Fast` : playlist rapide ; la qualité peut être moindre”\n“`Brief` : une seule playlist combinée”\n“`Rich` : vues séparées du style, du contexte et de la découverte, puis playlist combinée finale”\nAutres contraintes:\n“Exemples : `éviter les morceaux trop joués`, `sans voix`, `Remix uniquement` ; facultatif”\n\n\u0060\u0060\u0060markdown\nContexte:\nPays / région cible:\nDirection sonore principale:\nNombre de morceaux ou durée du set:\nVersion de sortie:\nAutres contraintes:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[Deuxième tour : préciser la demande]",
      "rules": [
        "1. Vous pouvez copier un exemple, remplir librement ou laisser le champ vide"
      ],
      "fields": [
        {
          "key": "style",
          "label": "Style précis",
          "example": "Exemples : `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "Vitesse / BPM",
          "example": "Exemples : `105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "Familiarité et découverte",
          "example": "`Familier` / `Équilibré` / `Découverte`"
        },
        {
          "key": "era_classic",
          "label": "Époque et classiques",
          "example": "`Contemporain` / `Quelques repères classiques` / `Pont entre les époques` / `Classiques d’abord`"
        },
        {
          "key": "mood",
          "label": "Humeur",
          "example": "Exemples : `nostalgique` / `froid` / `romantique`"
        },
        {
          "key": "energy",
          "label": "Niveau ou courbe d’énergie du SET",
          "example": "Exemples : `bas` / `haut` ; `stable` / `montagnes russes`"
        },
        {
          "key": "platform",
          "label": "Plateforme et exigences de lien",
          "example": "Exemples : `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify` ; une plateforme signifie l’utiliser seule ; plusieurs suivent l’ordre indiqué"
        },
        {
          "key": "other",
          "label": "Autre",
          "example": ""
        }
      ],
      "prompt": "[Deuxième tour : préciser la demande]\n\nStyle précis:\n“Exemples : `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`”\nVitesse / BPM:\n“Exemples : `105` / `128` / `140` / `150` / `170`”\nFamiliarité et découverte:\n“`Familier` / `Équilibré` / `Découverte`”\nÉpoque et classiques:\n“`Contemporain` / `Quelques repères classiques` / `Pont entre les époques` / `Classiques d’abord`”\nHumeur:\n“Exemples : `nostalgique` / `froid` / `romantique`”\nNiveau ou courbe d’énergie du SET:\n“Exemples : `bas` / `haut` ; `stable` / `montagnes russes`”\nPlateforme et exigences de lien:\n“Exemples : `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify` ; une plateforme signifie l’utiliser seule ; plusieurs suivent l’ordre indiqué”\nAutre:\n\n\u0060\u0060\u0060markdown\nStyle précis:\nVitesse / BPM:\nFamiliarité et découverte:\nÉpoque et classiques:\nHumeur:\nNiveau ou courbe d’énergie du SET:\nPlateforme et exigences de lien:\nAutre:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# Mode Fast",
      "first_batch_title": "# Première sélection Fast",
      "final_title": "# Mode Fast",
      "columns": [
        "Morceau",
        "Artiste",
        "Lien"
      ],
      "next_steps": [
        {
          "label": "Premier | Partager un retour",
          "body": "Si vous le souhaitez, répondez en langage naturel sur l’utilité des sélections. Cela améliore vos préférences privées et les prochaines recommandations."
        },
        {
          "label": "Deuxième | Exporter ou transmettre la playlist",
          "body": "Vous pouvez produire une playlist texte ou la transmettre à W4DJ. Répondez `output text playlist` ou `export to w4dj`."
        }
      ],
      "digging_notes": "Notes de digging",
      "mix_suggestion": "Suggestion de mix",
      "unknown": "Inconnu",
      "verified": "Vérifié",
      "target_platform_missing": "Plateforme cible indisponible"
    },
    "brief": {
      "title": "# Mode Brief",
      "first_batch_title": "# Mode Brief",
      "final_title": "# Mode Brief",
      "columns": [
        "Morceau",
        "Artiste",
        "Album / EP",
        "Style",
        "BPM",
        "Tonalité",
        "Durée",
        "Énergie",
        "Date de sortie",
        "Notes",
        "Motif",
        "Lien"
      ],
      "next_steps": [
        {
          "label": "Premier | Partager un retour",
          "body": "Si vous le souhaitez, répondez en langage naturel sur l’utilité des sélections. Cela améliore vos préférences privées et les prochaines recommandations."
        },
        {
          "label": "Deuxième | Exporter ou transmettre la playlist",
          "body": "Vous pouvez produire une playlist texte ou la transmettre à W4DJ. Répondez `output text playlist` ou `export to w4dj`."
        },
        {
          "label": "Troisième | Ordre harmonique",
          "body": "Voulez-vous que j’organise le set avec la roue de Camelot ?"
        }
      ],
      "digging_notes": "Notes de digging",
      "mix_suggestion": "Suggestion de mix",
      "unknown": "Inconnu",
      "verified": "Vérifié",
      "target_platform_missing": "Plateforme cible indisponible"
    },
    "rich": {
      "title": "# Mode Rich",
      "first_batch_title": "# Mode Rich",
      "final_title": "# Mode Rich",
      "columns": [
        "Morceau",
        "Artiste",
        "Album / EP",
        "Style",
        "BPM",
        "Tonalité",
        "Durée",
        "Énergie",
        "Date de sortie",
        "Notes",
        "Motif",
        "Lien"
      ],
      "next_steps": [
        {
          "label": "Premier | Partager un retour",
          "body": "Si vous le souhaitez, répondez en langage naturel sur l’utilité des sélections. Cela améliore vos préférences privées et les prochaines recommandations."
        },
        {
          "label": "Deuxième | Exporter ou transmettre la playlist",
          "body": "Vous pouvez produire une playlist texte ou la transmettre à W4DJ. Répondez `output text playlist` ou `export to w4dj`."
        },
        {
          "label": "Troisième | Ordre harmonique",
          "body": "Voulez-vous que j’organise le set avec la roue de Camelot ?"
        }
      ],
      "digging_notes": "Notes de digging",
      "mix_suggestion": "Suggestion de mix",
      "unknown": "Inconnu",
      "verified": "Vérifié",
      "target_platform_missing": "Plateforme cible indisponible",
      "view_titles": [
        "Vue style",
        "Vue contexte",
        "Vue familiarité / découverte",
        "Vue combinée dynamique"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "Partager un retour",
      "positive": [
        "J’aime ce morceau"
      ],
      "negative": [
        "Je n’aime pas ce morceau"
      ],
      "ambiguous": [
        "Je ne suis pas sûr pour ce morceau"
      ]
    },
    "export_w4dj": {
      "label": "Exporter vers W4DJ",
      "positive": [
        "Exporter vers W4DJ"
      ],
      "negative": [
        "Ne pas exporter vers W4DJ"
      ],
      "ambiguous": [
        "Exporter peut-être vers W4DJ"
      ]
    },
    "output_text_playlist": {
      "label": "Produire la playlist texte",
      "positive": [
        "Produire la playlist texte"
      ],
      "negative": [
        "Ne pas produire la playlist texte"
      ],
      "ambiguous": [
        "Produire peut-être la playlist texte"
      ]
    },
    "harmonic_reorder": {
      "label": "Réordonner harmoniquement",
      "positive": [
        "Ordonner avec la roue de Camelot"
      ],
      "negative": [
        "Ne pas réordonner"
      ],
      "ambiguous": [
        "Ordonner peut-être avec la roue de Camelot"
      ]
    },
    "confirm_long_term_memory": {
      "label": "Confirmer la mémoire longue",
      "positive": [
        "Mémoriser cette préférence"
      ],
      "negative": [
        "Ne pas enregistrer cette préférence"
      ],
      "ambiguous": [
        "Mémoriser peut-être cette préférence"
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
      "uniquement",
      "seulement",
      "utiliser uniquement"
    ],
    "preferred_markers": [
      "préférer",
      "préférée",
      "priorité"
    ],
    "fallback_markers": [
      "secours",
      "alternative",
      "si indisponible"
    ],
    "forbidden_markers": [
      "ne pas utiliser",
      "exclure",
      "sans"
    ]
  },
  "status": {
    "unknown": "Inconnu",
    "verified": "Vérifié",
    "target_platform_missing": "Plateforme cible indisponible"
  },
  "export": {
    "text": "Produire une playlist texte copiable dans l’ordre actuel.",
    "w4dj": "Créer un fichier `.w4dj` UTF-8 à transmettre à W4DJ.",
    "harmonic": "Demander un ordre selon la roue de Camelot avec les tonalités connues.",
    "feedback": "Les retours en langage naturel ne mettent à jour que la session ; la conservation longue exige une confirmation.",
    "memory_confirmation": "J’ai compris ceci comme un bref résumé d’évolution des goûts. L’enregistrer dans le profil privé à long terme ?"
  }
}
```
