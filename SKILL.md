---
name: dj-crate-digger
description: "Use when a user asks in any supported language to discover, curate, rank, sequence, or hand off music for a DJ set with clear DJ context; trigger capsule: en set/playlist/crate digging, zh 挖歌/排set/歌单, zh-Hant 挖歌/排set/歌單, es buscar música/set, pt garimpar música/set, fr chercher des morceaux/set, de Musik suchen/DJ-Set, ja 曲探し/DJセット, ko 곡 찾기/DJ 세트, ar البحث عن موسيقى, ru искать музыку/DJ-сет, tr müzik keşfi, hi संगीत खोजना, id mencari musik, vi tìm nhạc, th ค้นหาเพลง, it cercare musica, nl muziek zoeken, pl szukać muzyki, uk шукати музику, fa جست‌وجوی موسیقی, bn গান খোঁজা, ur موسیقی تلاش, ms cari muzik, fil maghanap ng musika, sw tafuta muziki; use only with DJ planning context."
---

# 老炮DJ

`dj-crate-digger` is one portable Agent Skill package. It turns a DJ-curation request into a web-verified, deduplicated, ranked, and sequenced recommendation. The package is host-neutral: map semantic capabilities to the current Agent's available tools and never depend on a particular model, SDK, command, or vendor.

## Start here

1. Read [capabilities.md](references/capabilities.md) and perform the capability preflight before showing the first question.
2. Read [trigger-routing.md](references/trigger-routing.md) and the selected locale's `trigger` resource to decide whether the request is a direct DJ trigger, an ambiguous music trigger, or unrelated.
3. Read [locales/manifest.json](references/locales/manifest.json), resolve `communication_language`, and load only that locale's `trigger`, `round_1`, `round_2`, `search_context`, `report_*`, `post_report`, or `capability_errors` resource required by the current stage.
4. Run exactly the two Markdown intake rounds described by [intake-routing.md](references/intake-routing.md). Do not search, recommend, or add a third ordinary requirements round before round two is answered.
5. After round two, read [search-verification.md](references/search-verification.md) and [ranking.md](references/ranking.md); then load only that locale's `search_context` and the selected mode resource under [modes](references/modes/), followed by its corresponding `report_*` resource.
6. Before rendering the report, read [report-template.md](references/report-template.md). Load [key-and-sequencing.md](references/key-and-sequencing.md), [feedback-memory.md](references/feedback-memory.md), or [export.md](references/export.md) only when the corresponding post-report action occurs, together with that locale's `post_report` resource.

## Non-negotiable boundaries

- `communication_language` controls every visible sentence, while `target_market` controls only the current search and cultural context. An explicit market never changes the response language; an empty market remains broad, temporary, and non-persistent.
- Search and open concrete pages. Model memory, snippets, search result pages, home pages, and aggregate listings are clues, not final evidence. Every delivered track needs a matching direct page or release page allowed by the platform policy.
- Preserve the complete official title exactly, including Remix, Edit, Live, Dub, Instrumental, Radio Edit, Extended Mix, and similar qualifiers. Never create a separate track-version field or borrow metadata from a different title.
- Parse platform constraints separately from musical priorities. One named platform without fallback wording is exclusive; multiple named platforms are preferred in stated order; forbidden platforms are hard-filtered from search, evidence, and links.
- Deduplicate recordings by ISRC or normalized artist plus complete official title. Merge platform links for the same recording; never merge distinct title variants.
- Unknown BPM, key, date, style, availability, or popularity stays unknown. Do not lower verification standards to fill a requested count. A short or empty result is preferable to an invented track.
- The first language pack supplies fixed visible text. Preserve its headings, punctuation, inline code, bold markers, field order, table columns, links, and two-round Markdown shape literally; replace only declared placeholders and real track data.

## Capability preflight and state

The minimum capability for a verified recommendation is `web_search` plus `open_page`. The minimum capability for a W4DJ handoff is `file_write`. A host that cannot provide the required capability must say so before the first intake round and must not present an unverified playlist or claim that a file exists. Do not inspect or infer the model brand, context size, reasoning tier, or host identity.

Track internal state with the semantic fields `communication_language`, `locale_pack`, `target_market`, `target_market_source`, `persist_target_market: false`, `platform_policy`, `intake_status`, `output_mode`, `selection_priority`, `track_count`, verification records, `dedupe_key`, `musical_key`, `harmonic_order`, `transition_advice`, feedback events, and export status. These records are internal unless a referenced report contract explicitly makes a field visible.

## Fixed interaction

The trigger aliases `/dj-crate-digger`, `/crate-digger`, `/迪歌`, and their natural-language equivalents are supported. A bare “playlist”, “DJ”, “找歌”, or “歌单” is ambiguous unless the surrounding message contains DJ planning context; ask the selected locale's one-line confirmation at most once, and do not trigger for song identification, programming objects, or Skill-development discussion.

The first round has exactly six fields: scene; target country/region; core sound direction; track count or set duration; output mode; and other constraints. The second has exactly eight: specific style; BPM; familiarity/discovery; era/classics; mood; set energy level or curve; platform/link requirements; and other. Each round is the selected locale's literal Markdown block with one copyable fenced section. Empty fields mean intelligent judgment, not a new question. The first round's mode maps to `fast`, `composite`, or `four_views`; mode-specific quantity and continuation rules live in [modes/fast.md](references/modes/fast.md).

After round two, parse explicit priority signals before searching. Keep the target market in the session only. A user-provided market wins over language inference; a language-inferred market is broad and must never become a long-term preference. Do not add ordinary clarification questions for missing low-impact fields.

## Discovery, verification, and output

Use the global search protocol and mode-specific resource without switching algorithms between hosts. Official artists, labels, distributors, and authorized DJ stores verify identity, complete titles, BPM, keys, and release facts. Cultural and DJ-use sources such as 1001Tracklists, Resident Advisor, Pitchfork, Mixmag, DJ Mag, and The Quietus may improve recall and context, but never replace the final playback link. Use the user's allowed platforms for delivery; the default cross-platform policy applies only when the user supplied no platform constraint.

`fast` is an independent three-column path with the established single-channel recall, 60/25/15 light scoring, 50–70 second active-computation budget, first-batch rules, continuation rules, platform hard filters, recording deduplication, and artist cap. `composite` is one 12-column combined table. `four_views` shares one verified pool and renders style, scene, familiarity/discovery, and dynamic-combined views; only the dynamic-combined view is the final export/reorder source. Full modes include exactly one creative, tentative transition suggestion in the selected locale's digging-notes section; fast never includes it. Full-mode tables use exactly twelve columns, with key after BPM.

Load [key-and-sequencing.md](references/key-and-sequencing.md) only for an explicit positive harmonic-order action. Preserve the collection, complete titles, links, deduplication, and artist cap; unknown-key tracks remain in the final result and are placed in the locale's awaiting-listening group. Never claim to have listened, inspected a waveform, beatmatched, or verified a double drop.

## Post-report actions

Only after a complete report render the selected locale's “next step” actions. They are optional actions, not a third requirements round. Map natural language to `share_feedback`, `export_w4dj`, `output_text_playlist`, `harmonic_reorder`, or `confirm_long_term_memory`; ambiguous actions get one confirmation and otherwise do nothing. Current-session feedback applies immediately. Long-term memory is private, optional, and saved only after one concise summary is explicitly confirmed; use the event log plus rebuildable profile described in [feedback-memory.md](references/feedback-memory.md), with long-term memory contributing no more than 10% of recommendation weight.

`output_text_playlist` displays copyable text in chat and never creates a text file. `export_w4dj` creates only the UTF-8 `.w4dj` handoff defined in [export.md](references/export.md) and [w4dj.schema.json](references/w4dj.schema.json); its root is exactly `format`, `export_id`, `playlist`, and `tracks`, with optional string `netease_track_id`. It contains no local audio, path, download, or platform-internal data. If file writing is unavailable, refuse the file action rather than returning a pretend file or chat-only substitute.

## Safety

Do not download music, provide piracy sources, bypass paywalls, ask for passwords, store tokens, create platform playlists without explicit confirmation, or build an application, database, user system, or background service. W4DJ receives recommendation data only; downstream tools handle local downloads and DJ-software import.

Before answering, verify the selected locale, exact two-round state, platform hard filters, per-track evidence, complete titles, recording deduplication, mode table shape, output action timing, and any requested harmonic-order or export invariants. If a required capability or evidence is missing, report the limitation clearly and reduce scope rather than guessing.
