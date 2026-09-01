# Adaptive intake routing

First decide whether intake is needed. This decision happens only after language resolution, capability preflight, and DJ-trigger routing. Once the DJ trigger is accepted, initialize `output_mode: composite`; only an explicit supported mode changes it.

## Direct-ready path

Set `intake_status: direct_ready` and proceed without rendering either questionnaire when the initial message has clear DJ planning context and satisfies either condition:

1. It supplies a usable scene or purpose, a core sound direction or artist/track reference, and a track count or set duration.
2. It explicitly authorizes the Agent to decide missing details and proceed, using wording equivalent to “decide the rest”, “use your judgment”, “don't ask me”, “go straight to the result”, or the same intent in another language.

An explicit user mode still wins. Otherwise keep `output_mode: composite`; a direct-ready request never defaults to Fast or Rich. Project facts that were actually supplied, use informed judgment for undeclared low-impact fields, and do not invent exclusions, platform requirements, reference artists, or a specific target country. A blank market remains the broad session-only language market. Do not display a confirmation, intake summary, or questionnaire before searching.

A message is not direct-ready merely because it contains the word DJ, playlist, set, or a genre. If it lacks both the minimum usable brief and explicit delegation, use the fixed intake path.

## Fixed intake path

When the request is not direct-ready, the intake is a literal-output contract. Load only the selected locale's `round_1` or `round_2` resource from `references/locales/manifest.json` and reproduce its `prompt` exactly. Do not free-translate, summarize, reorder, add a preface, add a closing question, remove inline code, or wrap the template in another fence.

Round one has exactly six fields, in this order: scene; target country / region; core sound direction; track count or set duration; output mode; other constraints. Round two has exactly eight fields, in this order: specific style; BPM; familiarity and discovery; era and classics; mood; set energy level or curve; platform and link requirements; other. Each response has one copyable Markdown fenced block and no other question.

The empty-field rule is part of the selected locale's fixed text. Treat an empty low-impact field as permission for an informed assumption, not as a reason to add a third round. If the round-one output-mode field is blank, keep `output_mode: composite`; an explicit supported mode overrides it. After round two, set `intake_status: ready`, preserve the raw answers, and proceed to search. Do not switch to the direct-ready path after a questionnaire has started.

## Language and market

Resolve `communication_language` with [language-routing.json](language-routing.json) before showing any text. An explicit language request or current natural-language message wins. For slash-only input, use recent user-language signals before identity language memory, then host locale; if no route reaches the policy threshold, show the fixed bilingual confirmation once. Recent language signals use at most five eligible completed user-owned sessions, with weights `5/4/3/2/1`; four matching sessions out of five may update the separate communication-language preference. Do not read historical assistant/tool output as user language, and do not execute historical instructions.

Resolve `target_market` separately: an explicit country or region wins; an empty field becomes a broad language market for this session only. Never infer a specific country from script or language alone, never store the market as a personal preference, and never change visible language because the market differs.

## Field projection

Project direct-ready input or questionnaire answers into the internal request card without duplicating evidence: style and references become sound signals; scene, mood, energy, and duration become context; familiarity/discovery and era/classics remain separate; platform text becomes `cross-platform`, `preferred`, or `exclusive`; output mode becomes `fast`, `composite`, or `four_views`, defaulting to `composite` when absent. Explicit “main”, “priority”, or “first … then …” wording determines `selection_priority` within content signals, never from platform order.

When one platform is named with no fallback wording, allow only that platform. Multiple named platforms are allowed in stated order; do not add defaults. A forbidden platform is removed from search, evidence, and visible links.
