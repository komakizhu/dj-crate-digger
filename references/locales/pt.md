# Portuguese locale pack

This file is the fixed Português UI and intent contract for dj-crate-digger. The JSON block is consumed by the Skill; prose outside it is documentation.

```json
{
  "locale": "pt",
  "language_name": "Portuguese",
  "native_name": "Português",
  "direction": "ltr",
  "market_policy": {
    "language_independent": true,
    "blank_region": "Se a região ficar em branco, use apenas um mercado amplo de língua portuguesa nesta sessão.",
    "explicit_region": "Uma região explícita vence a inferência do idioma sem mudar a língua de comunicação.",
    "persistence": "Não guarde o mercado como preferência de longo prazo."
  },
  "quick_start": {
    "intro": "Bem-vindo ao assistente de seleção de DJ. Esta Skill de Agent ajuda a preparar um set. Você confirmará suas necessidades em duas rodadas e receberá recomendações de faixas. Regras de preenchimento:",
    "tutorial_label": "Tutorial de importação de Set em um clique",
    "tutorial_url": "https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md"
  },
  "intake": {
    "round_1": {
      "title": "[Primeira rodada: informações necessárias]",
      "rules": [
        "1. Você pode copiar um exemplo, preencher livremente ou deixar em branco",
        "2. Deixar um campo em branco significa que a IA julgará a resposta de forma inteligente"
      ],
      "fields": [
        {
          "key": "scene",
          "label": "Cenário",
          "example": "Ambiente da apresentação. Exemplos: `bar` / `clube` / `casamento` / `exposição de arte`"
        },
        {
          "key": "target_market",
          "label": "País / região de destino",
          "example": "Exemplos: `China continental` / `Taiwan` / `Hong Kong` / `Japão` / `mercado internacional em inglês`"
        },
        {
          "key": "core_sound",
          "label": "Direção sonora principal",
          "example": "Artista, faixa e gênero de referência. Exemplo: `Tears` de `Skrillex`, gênero `UK Bass` moderno"
        },
        {
          "key": "track_count_or_duration",
          "label": "Quantidade de faixas ou duração do set",
          "example": "Exemplos: `20 faixas` / `60 minutos`"
        },
        {
          "key": "output_mode",
          "label": "Versão de saída",
          "example": "Opções Fast / Brief / Rich"
        },
        {
          "key": "other",
          "label": "Outras restrições",
          "example": "Exemplos: `evitar faixas batidas`, `sem vocais`, `somente Remix`; opcional"
        }
      ],
      "prompt": "Bem-vindo ao assistente de seleção de DJ. Esta Skill de Agent ajuda a preparar um set. Você confirmará suas necessidades em duas rodadas e receberá recomendações de faixas. Regras de preenchimento:\n\n1. Você pode copiar um exemplo, preencher livremente ou deixar em branco\n2. Deixar um campo em branco significa que a IA julgará a resposta de forma inteligente\n\n[Primeira rodada: informações necessárias]\n\nCenário:\n“Ambiente da apresentação. Exemplos: `bar` / `clube` / `casamento` / `exposição de arte`”\nPaís / região de destino:\n“Exemplos: `China continental` / `Taiwan` / `Hong Kong` / `Japão` / `mercado internacional em inglês`”\nDireção sonora principal:\n“Artista, faixa e gênero de referência. Exemplo: `Tears` de `Skrillex`, gênero `UK Bass` moderno”\nQuantidade de faixas ou duração do set:\n“Exemplos: `20 faixas` / `60 minutos`”\nVersão de saída:\n“`Fast`: playlist rápida; a qualidade pode ser menor”\n“`Brief`: apenas uma playlist combinada”\n“`Rich`: visões separadas de estilo, cenário e descoberta, seguidas de uma playlist combinada final”\nOutras restrições:\n“Exemplos: `evitar faixas batidas`, `sem vocais`, `somente Remix`; opcional”\n\n\u0060\u0060\u0060markdown\nCenário:\nPaís / região de destino:\nDireção sonora principal:\nQuantidade de faixas ou duração do set:\nVersão de saída:\nOutras restrições:\n\u0060\u0060\u0060"
    },
    "round_2": {
      "title": "[Segunda rodada: detalhar o pedido]",
      "rules": [
        "1. Você pode copiar um exemplo, preencher livremente ou deixar em branco"
      ],
      "fields": [
        {
          "key": "style",
          "label": "Estilo específico",
          "example": "Exemplos: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`"
        },
        {
          "key": "bpm",
          "label": "Velocidade / BPM",
          "example": "Exemplos: `105` / `128` / `140` / `150` / `170`"
        },
        {
          "key": "familiarity_era",
          "label": "Familiaridade e descoberta",
          "example": "`Familiar` / `Equilibrado` / `Descoberta`"
        },
        {
          "key": "era_classic",
          "label": "Época e clássicos",
          "example": "`Contemporâneo` / `Âncoras clássicas leves` / `Ponte entre épocas` / `Clássicos primeiro`"
        },
        {
          "key": "mood",
          "label": "Clima",
          "example": "Exemplos: `nostálgico` / `frio` / `romântico`"
        },
        {
          "key": "energy",
          "label": "Nível ou curva de energia do SET",
          "example": "Exemplos: `baixo` / `alto`; `estável` / `montanha-russa`"
        },
        {
          "key": "platform",
          "label": "Plataforma e requisitos de links",
          "example": "Exemplos: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; uma plataforma significa usar apenas ela; várias seguem a prioridade indicada"
        },
        {
          "key": "other",
          "label": "Outros",
          "example": ""
        }
      ],
      "prompt": "[Segunda rodada: detalhar o pedido]\n\nEstilo específico:\n“Exemplos: `House` / `Bass` / `Garage` / `Techno` / `Breakbeat`”\nVelocidade / BPM:\n“Exemplos: `105` / `128` / `140` / `150` / `170`”\nFamiliaridade e descoberta:\n“`Familiar` / `Equilibrado` / `Descoberta`”\nÉpoca e clássicos:\n“`Contemporâneo` / `Âncoras clássicas leves` / `Ponte entre épocas` / `Clássicos primeiro`”\nClima:\n“Exemplos: `nostálgico` / `frio` / `romântico`”\nNível ou curva de energia do SET:\n“Exemplos: `baixo` / `alto`; `estável` / `montanha-russa`”\nPlataforma e requisitos de links:\n“Exemplos: `NetEase Cloud Music` / `Apple Music` / `SoundCloud` / `Bandcamp` / `Beatport` / `Spotify`; uma plataforma significa usar apenas ela; várias seguem a prioridade indicada”\nOutros:\n\n\u0060\u0060\u0060markdown\nEstilo específico:\nVelocidade / BPM:\nFamiliaridade e descoberta:\nÉpoca e clássicos:\nClima:\nNível ou curva de energia do SET:\nPlataforma e requisitos de links:\nOutros:\n\u0060\u0060\u0060"
    }
  },
  "report": {
    "fast": {
      "title": "# Modo Fast",
      "first_batch_title": "# Primeira leva Fast",
      "final_title": "# Modo Fast",
      "columns": [
        "Faixa",
        "Artista",
        "Link"
      ],
      "next_steps": [
        {
          "label": "Primeiro | Compartilhar feedback",
          "body": "Se quiser, responda em linguagem natural sobre como as faixas funcionaram. Isso melhora suas preferências privadas e futuras recomendações."
        },
        {
          "label": "Segundo | Exportar ou entregar a playlist",
          "body": "Você pode gerar uma playlist de texto ou entregá-la ao W4DJ. Responda `output text playlist` ou `export to w4dj`."
        }
      ],
      "digging_notes": "Notas de digging",
      "mix_suggestion": "Sugestão de mixagem",
      "unknown": "Desconhecido",
      "verified": "Verificado",
      "target_platform_missing": "Plataforma de destino indisponível"
    },
    "brief": {
      "title": "# Modo Brief",
      "first_batch_title": "# Modo Brief",
      "final_title": "# Modo Brief",
      "columns": [
        "Faixa",
        "Artista",
        "Álbum / EP",
        "Estilo",
        "BPM",
        "Tom",
        "Duração",
        "Energia",
        "Data",
        "Notas",
        "Motivo",
        "Link"
      ],
      "next_steps": [
        {
          "label": "Primeiro | Compartilhar feedback",
          "body": "Se quiser, responda em linguagem natural sobre como as faixas funcionaram. Isso melhora suas preferências privadas e futuras recomendações."
        },
        {
          "label": "Segundo | Exportar ou entregar a playlist",
          "body": "Você pode gerar uma playlist de texto ou entregá-la ao W4DJ. Responda `output text playlist` ou `export to w4dj`."
        },
        {
          "label": "Terceiro | Ordem harmônica",
          "body": "Quer que eu organize o set usando a roda de Camelot?"
        }
      ],
      "digging_notes": "Notas de digging",
      "mix_suggestion": "Sugestão de mixagem",
      "unknown": "Desconhecido",
      "verified": "Verificado",
      "target_platform_missing": "Plataforma de destino indisponível"
    },
    "rich": {
      "title": "# Modo Rich",
      "first_batch_title": "# Modo Rich",
      "final_title": "# Modo Rich",
      "columns": [
        "Faixa",
        "Artista",
        "Álbum / EP",
        "Estilo",
        "BPM",
        "Tom",
        "Duração",
        "Energia",
        "Data",
        "Notas",
        "Motivo",
        "Link"
      ],
      "next_steps": [
        {
          "label": "Primeiro | Compartilhar feedback",
          "body": "Se quiser, responda em linguagem natural sobre como as faixas funcionaram. Isso melhora suas preferências privadas e futuras recomendações."
        },
        {
          "label": "Segundo | Exportar ou entregar a playlist",
          "body": "Você pode gerar uma playlist de texto ou entregá-la ao W4DJ. Responda `output text playlist` ou `export to w4dj`."
        },
        {
          "label": "Terceiro | Ordem harmônica",
          "body": "Quer que eu organize o set usando a roda de Camelot?"
        }
      ],
      "digging_notes": "Notas de digging",
      "mix_suggestion": "Sugestão de mixagem",
      "unknown": "Desconhecido",
      "verified": "Verificado",
      "target_platform_missing": "Plataforma de destino indisponível",
      "view_titles": [
        "Visão de estilo",
        "Visão de cenário",
        "Visão de familiaridade / descoberta",
        "Visão combinada dinâmica"
      ]
    }
  },
  "actions": {
    "share_feedback": {
      "label": "Compartilhar feedback",
      "positive": [
        "Gosto desta faixa"
      ],
      "negative": [
        "Não gosto desta faixa"
      ],
      "ambiguous": [
        "Não tenho certeza sobre esta faixa"
      ]
    },
    "export_w4dj": {
      "label": "Exportar para W4DJ",
      "positive": [
        "Exportar para W4DJ"
      ],
      "negative": [
        "Não exportar para W4DJ"
      ],
      "ambiguous": [
        "Talvez exportar para W4DJ"
      ]
    },
    "output_text_playlist": {
      "label": "Gerar playlist de texto",
      "positive": [
        "Gerar a playlist de texto"
      ],
      "negative": [
        "Não gerar a playlist de texto"
      ],
      "ambiguous": [
        "Talvez gerar a playlist de texto"
      ]
    },
    "harmonic_reorder": {
      "label": "Reordenar harmonicamente",
      "positive": [
        "Organizar pela roda de Camelot"
      ],
      "negative": [
        "Não reordenar"
      ],
      "ambiguous": [
        "Talvez organizar pela roda de Camelot"
      ]
    },
    "confirm_long_term_memory": {
      "label": "Confirmar memória de longo prazo",
      "positive": [
        "Lembrar esta preferência"
      ],
      "negative": [
        "Não salvar esta preferência"
      ],
      "ambiguous": [
        "Talvez lembrar esta preferência"
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
      "somente",
      "apenas",
      "usar somente"
    ],
    "preferred_markers": [
      "preferir",
      "preferida",
      "prioridade"
    ],
    "fallback_markers": [
      "reserva",
      "alternativa",
      "se indisponível"
    ],
    "forbidden_markers": [
      "não usar",
      "excluir",
      "sem"
    ]
  },
  "status": {
    "unknown": "Desconhecido",
    "verified": "Verificado",
    "target_platform_missing": "Plataforma de destino indisponível"
  },
  "export": {
    "text": "Gerar uma playlist de texto copiável na ordem atual.",
    "w4dj": "Criar um arquivo `.w4dj` UTF-8 para o W4DJ.",
    "harmonic": "Solicitar ordem pela roda de Camelot usando as tonalidades conhecidas.",
    "feedback": "O feedback em linguagem natural atualiza apenas a sessão; o armazenamento de longo prazo exige confirmação.",
    "memory_confirmation": "Entendi isto como um resumo curto da mudança de gosto. Salvar no perfil privado de longo prazo?"
  },
  "trigger_capsule": [
    "set de DJ",
    "playlist",
    "garimpar música",
    "buscar faixas",
    "montar um set"
  ]
}
```
