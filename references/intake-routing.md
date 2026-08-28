# Two-round intake routing

The intake is a literal-output contract. Load only the selected locale's `round_1` or `round_2` resource from `references/locales/manifest.json` and reproduce its `prompt` exactly. Do not free-translate, summarize, reorder, add a preface, add a closing question, remove inline code, or wrap the template in another fence.

## Round state

Round one has exactly six fields, in this order: scene; target country / region; core sound direction; track count or set duration; output mode; other constraints. Round two has exactly eight fields, in this order: specific style; BPM; familiarity and discovery; era and classics; mood; set energy level or curve; platform and link requirements; other. Each response has one copyable Markdown fenced block and no other question.

The empty-field rule is part of the selected locale's fixed text. Treat an empty low-impact field as permission for an informed assumption, not as a reason to add a third round. After round two, set `intake_status: ready`, preserve the raw answers, and proceed to search.

## Language and market

Resolve `communication_language` from an explicit language request, dominant current message, current-session language, then English fallback. Resolve `target_market` separately: an explicit country or region wins; an empty field becomes a broad language market for this session only. Never infer a specific country from script or language alone, never store the market as a personal preference, and never change visible language because the market differs.

## Field projection

Project the answers into the internal request card without duplicating evidence: style and references become sound signals; scene, mood, energy, and duration become context; familiarity/discovery and era/classics remain separate; platform text becomes `cross-platform`, `preferred`, or `exclusive`; output mode becomes `fast`, `composite`, or `four_views`. Explicit “main”, “priority”, or “first … then …” wording determines `selection_priority` within content signals, never from platform order.

When one platform is named with no fallback wording, allow only that platform. Multiple named platforms are allowed in stated order; do not add defaults. A forbidden platform is removed from search, evidence, and visible links.
