---
name: dj-crate-digger
description: "Use when a user asks in any supported language to discover, curate, rank, sequence, or hand off music for a DJ set with clear DJ context; trigger capsule: en set/playlist/crate digging, zh 挖歌/排set/歌单, zh-Hant 挖歌/排set/歌單, es buscar música/set, pt garimpar música/set, fr chercher des morceaux/set, de Musik suchen/DJ-Set, ja 曲探し/DJセット, ko 곡 찾기/DJ 세트, ar البحث عن موسيقى, ru искать музыку/DJ-сет, tr müzik keşfi, hi संगीत खोजना, id mencari musik, vi tìm nhạc, th ค้นหาเพลง, it cercare musica, nl muziek zoeken, pl szukać muzyki, uk шукати музику, fa جست‌وجوی موسیقی, bn গান খোঁজা, ur موسیقی تلاش, ms cari muzik, fil maghanap ng musika, sw tafuta muziki; use only with DJ planning context."
---

# 老炮DJ

`dj-crate-digger` is one portable Agent Skill package. It turns a DJ-curation request into a web-verified, deduplicated, ranked, and sequenced recommendation. The package is host-neutral: map semantic capabilities to the current Agent's available tools and never depend on a particular model, SDK, command, or vendor.

## Start here

1. Read [language-routing.json](references/language-routing.json) and resolve `communication_language` before producing any visible text; for a slash-only invocation, query recent user-language signals and identity language memory first.
2. Read [capabilities.md](references/capabilities.md) and perform the silent capability preflight before showing the first question.
3. Read [trigger-routing.md](references/trigger-routing.md) and the selected locale's `trigger` resource to decide whether the request is a direct DJ trigger, an ambiguous music trigger, or unrelated.
4. Read [locales/manifest.json](references/locales/manifest.json) and load only that locale's `trigger`, `round_1`, `round_2`, `search_context`, `report_*`, `post_report`, or `capability_errors` resource required by the current stage.
5. Apply the readiness route in [intake-routing.md](references/intake-routing.md). A sufficiently specified one-message request, or a clear instruction to decide the remaining details and proceed, sets `intake_status: direct_ready` and skips both questionnaires. Otherwise run exactly the two fixed Markdown intake rounds.
6. After `intake_status` becomes `direct_ready` or `ready`, read [search-verification.md](references/search-verification.md) and [ranking.md](references/ranking.md); then load only that locale's `search_context` and the selected mode resource under [modes](references/modes/), followed by its corresponding `report_*` resource.
7. Before rendering the report, read [report-template.md](references/report-template.md). Load [key-and-sequencing.md](references/key-and-sequencing.md), [feedback-memory.md](references/feedback-memory.md), or [export.md](references/export.md) only when the corresponding post-report action occurs, together with that locale's `post_report` resource.

## Non-negotiable boundaries

- `communication_language` controls every visible sentence, while `target_market` controls only the current search and cultural context. An explicit market never changes the response language; an empty market remains broad, temporary, and non-persistent.
- Search and open concrete pages. Model memory, snippets, search result pages, home pages, and aggregate listings are clues, not final evidence. Every delivered track needs a matching direct page or release page allowed by the platform policy.
- Preserve the complete official title exactly, including Remix, Edit, Live, Dub, Instrumental, Radio Edit, Extended Mix, and similar qualifiers. Never create a separate track-version field or borrow metadata from a different title.
- Parse platform constraints separately from musical priorities. One named platform without fallback wording is exclusive; multiple named platforms are preferred in stated order; forbidden platforms are hard-filtered from search, evidence, and links.
- Deduplicate recordings by ISRC or normalized artist plus complete official title. Merge platform links for the same recording; never merge distinct title variants.
- Unknown BPM, key, date, style, availability, or popularity stays unknown. Do not lower verification standards to fill a requested count. A short or empty result is preferable to an invented track.
- Whenever a locale resource is rendered, preserve its headings, punctuation, inline code, bold markers, field order, table columns, links, and Markdown shape literally; replace only declared placeholders and real track data.
- Lock `communication_language` before any visible response. A slash-only request is not evidence of English; use the language-routing policy and available user-language signals first. If no signal is sufficient, render only the fixed bilingual language confirmation and wait for its answer.

## Capability preflight and state

The minimum capability for a verified recommendation is `web_search` plus `open_page`. The minimum capability for a W4DJ handoff is `file_write`. Language-history and identity-language capabilities are optional; their absence triggers the documented language fallback. A host that cannot provide the required capability must say so before either the first intake round or a direct search, and must not present an unverified playlist or claim that a file exists. Do not inspect or infer the model brand, context size, reasoning tier, or host identity.

Track internal state with the semantic fields `communication_language`, `locale_pack`, `locale_source`, `locale_confidence`, `language_locked`, `language_preference_write_status`, `target_market`, `target_market_source`, `persist_target_market: false`, `platform_policy`, `intake_status`, `output_mode`, `selection_priority`, `track_count`, verification records, `dedupe_key`, `musical_key`, `harmonic_order`, `transition_advice`, feedback events, and export status. These records are internal unless a referenced report contract explicitly makes a field visible.

## Fixed interaction

The trigger aliases `/dj-crate-digger`, `/crate-digger`, `/迪歌`, and their natural-language equivalents are supported. A slash-only invocation first completes language resolution, then routes the trigger. A bare “playlist”, “DJ”, “找歌”, or “歌单” is ambiguous unless the surrounding message contains DJ planning context; ask the selected locale's one-line confirmation at most once, and do not trigger for song identification, programming objects, or Skill-development discussion.

Set `output_mode: composite` as soon as a DJ request is activated. This is the default on every path, regardless of message length or whether the fixed intake runs; only an explicit `fast`, `composite`, or `four_views` request overrides it. For an initial one-message request, first decide whether it is ready to execute. Treat it as `direct_ready` when it has clear DJ planning context and either supplies a usable scene/use, core sound or reference, and track count/set duration, or explicitly delegates missing choices with wording equivalent to “decide the rest”, “use your judgment”, or “go straight to the result”. Do not show an intake template or ask for confirmation on this path.

Requests that are not direct-ready use the fixed intake path. The first round has exactly six fields: scene; target country/region; core sound direction; track count or set duration; output mode; and other constraints. The second has exactly eight: specific style; BPM; familiarity/discovery; era/classics; mood; set energy level or curve; platform/link requirements; and other. Each round is the selected locale's literal Markdown block with one copyable fenced section. Empty fields mean intelligent judgment, not a new question; an empty output-mode field keeps `composite`. The first round's explicit mode maps to `fast`, `composite`, or `four_views`; mode-specific quantity and continuation rules live in [modes/fast.md](references/modes/fast.md).

Before searching on either path, parse explicit priority signals and project supplied facts without inventing constraints. On the direct-ready path, intelligently judge undeclared low-impact fields. Keep the target market in the session only. A user-provided market wins over language inference; a language-inferred market is broad and must never become a long-term preference. Do not add ordinary clarification questions for missing low-impact fields.

## Discovery, verification, and output

Use the global search protocol and mode-specific resource without switching algorithms between hosts. Official artists, labels, distributors, and authorized DJ stores verify identity, complete titles, BPM, keys, and release facts. Cultural and DJ-use sources such as 1001Tracklists, Resident Advisor, Pitchfork, Mixmag, DJ Mag, and The Quietus may improve recall and context, but never replace the final playback link. Use the user's allowed platforms for delivery; the default cross-platform policy applies only when the user supplied no platform constraint.

`fast` is an independent three-column path with the established single-channel recall, 60/25/15 light scoring, 50–70 second active-computation budget, first-batch rules, continuation rules, platform hard filters, recording deduplication, and artist cap. `composite` is one 12-column combined table. `four_views` shares one verified pool and renders style, scene, familiarity/discovery, and dynamic-combined views; only the dynamic-combined view is the final export/reorder source. Full modes include exactly one creative, tentative transition suggestion in the selected locale's digging-notes section; fast never includes it. Full-mode tables use exactly twelve columns, with key after BPM.

Load [key-and-sequencing.md](references/key-and-sequencing.md) only for an explicit positive harmonic-order action. Preserve the collection, complete titles, links, deduplication, and artist cap; unknown-key tracks remain in the final result and are placed in the locale's awaiting-listening group. Never claim to have listened, inspected a waveform, beatmatched, or verified a double drop.

## Post-report actions

Only after a complete report render the selected locale's “next step” actions. They are optional actions, not a third requirements round. Map natural language to `share_feedback`, `export_w4dj`, `output_text_playlist`, `harmonic_reorder`, or `confirm_long_term_memory`; ambiguous actions get one confirmation and otherwise do nothing. Current-session feedback applies immediately. Long-term memory is private, optional, and saved only after one concise summary is explicitly confirmed; use the event log plus rebuildable profile described in [feedback-memory.md](references/feedback-memory.md), with long-term memory contributing no more than 10% of recommendation weight.

`output_text_playlist` displays copyable text in chat and never creates a text file. `export_w4dj` creates only the UTF-8 `.w4dj` handoff defined in [export.md](references/export.md) and [w4dj.schema.json](references/w4dj.schema.json); its root is exactly `format`, `format_version`, `export_id`, `playlist`, and `tracks`, with `format_version` always equal to integer `2` and optional string `netease_track_id`. The version field is a fixed W4DJ compatibility value, never a user-facing format choice. It contains no local audio, path, download, or platform-internal data. If file writing is unavailable, refuse the file action rather than returning a pretend file or chat-only substitute.

## Safety

Do not download music, provide piracy sources, bypass paywalls, ask for passwords, store tokens, create platform playlists without explicit confirmation, or build an application, database, user system, or background service. W4DJ receives recommendation data only; downstream tools handle local downloads and DJ-software import.

Before answering, verify the language is locked, the selected locale is used consistently, the exact two-round state, platform hard filters, per-track evidence, complete titles, recording deduplication, mode table shape, output action timing, and any requested harmonic-order or export invariants. If a required capability or evidence is missing, report the limitation clearly and reduce scope rather than guessing.
