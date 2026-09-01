# Report template contract

This document defines report shape. It is intentionally language-neutral: all visible words, headings, status labels, action phrases, tutorial labels, and localized examples come from the selected locale's stage resource listed in [locales/manifest.json](locales/manifest.json). Do not copy a Chinese or English sample into a report rendered in another language.

The resolved `locale_pack` remains the semantic source for those stage resources; visible action text is exposed as the locale's `action_intent` wording.

## Locale and market

Before rendering, load only the selected locale's `report_fast`, `report_brief`, or `report_rich` resource. Use `communication_language` to select it and use `target_market` only as the current search and cultural-context constraint. An explicit market never changes the communication language. A blank market gets the pack’s broad-language fallback for this session only; it must not be persisted as a preference.

## Shared report rules

- Preserve complete official titles, including `Remix`, `Edit`, `Live`, `Dub`, `Instrumental`, `Radio Edit`, and `Extended Mix` qualifiers. Do not add a separate Mix or Version column.
- Show only tracks with a track-level direct page or release page that passed the platform policy. Search pages, home pages, snippets, and model memory are not final links.
- Keep source evidence, missing metadata, platform fallback, timing, deduplication, and stop reasons in the internal record. Do not display “sources” or “missing information” sections unless the user asks for them.
- Use the locale's `search_context.status` labels for unknown, verified, and target-platform-missing values. Unknown data stays unknown; it is never filled from memory.
- Keep the locale's `post_report.actions` `action_intent` phrases available for natural-language parsing. A user may reply in any supported language; do not require a localized command in a particular language.

## Protected and dynamic report regions

Treat the selected `report_*` resource as a literal render template, not as explanatory prose. The following are protected and must be copied exactly from that resource: mode and view titles; column labels and order; `next_steps` item count, order, labels, and bodies; action phrases; tutorial links; punctuation; inline code; bold markers; and Markdown shape. Do not translate, paraphrase, shorten, merge, reorder, or omit any protected value. The direct-ready path and the questionnaire path use the same report contract.

Only the declared dynamic regions may be generated or filled: real track rows and their verified values, a playlist name, the content under the fixed digging-notes label, and the one creative mix suggestion under its fixed label. A dynamic region must not change a protected label or body. If a complete report cannot include the protected region in full, do not silently replace it with a summary.

## Fast mode

Use `report_resource.first_batch_title` for a first-batch message and `report_resource.final_title` for the completed message. The table must contain exactly the three columns in `report_resource.columns`: track title, artist, and one verified direct link. Fast mode omits the requirement summary, digging notes, key data, 12-column metadata, rich views, mix suggestion, and harmonic-order invitation.

Only a completed Fast report renders `report_resource.next_steps`, copying every item label and body exactly as stored. It must contain exactly two items: the optional natural-language feedback invitation and the text-playlist/W4DJ handoff action. If the host cannot continue after a first batch, use the locale's localized stop message and do not call the first batch a complete playlist.

## Brief mode

Use `report_resource.title` and exactly the 12 columns in `report_resource.columns`, in this order:

`title | artist | album_or_ep | style | bpm | musical_key | duration | energy | release_date | notes | selection_reason | link`

Render the locale's localized labels rather than these field identifiers. After the table, include the report resource's digging-notes label and exactly one creative mix suggestion. The suggestion may propose a long blend, EQ swap, loop relay, FX transition, layering, hard cut, contrast, or another creative handoff, but must use tentative language and never claim to have heard the audio or examined its waveform. A `double drop` label is allowed only when both tracks have reliable matching keys and pass the BPM rule.

Render `report_resource.next_steps` only after the complete report, copying every item label and body exactly as stored. It must contain exactly three items: feedback, text/W4DJ export, and harmonic reorder. A positive `harmonic_reorder` intent reorders the Brief combined table without changing tracks, versions embedded in titles, links, dedupe keys, or artist caps.

## Rich mode

Render the four view titles in `report_resource.view_titles`: style, scene, familiarity/discovery, and dynamic combined. Each view uses the same 12-column list shape from `report_resource.columns`. The dynamic combined view is the only Rich view used for the final recommendation, harmonic reorder, and export; the three specialist views retain their original order.

After the dynamic combined view, include the report resource's digging-notes label and exactly one creative mix suggestion. Render exactly three localized next-step items from `report_resource.next_steps`, copying every item label and body exactly as stored. The first two have the same feedback and export meaning as Brief; the third is the harmonic-order invitation. Do not show memory-state, event-log, profile-update, source, or missing-information panels by default.

## Creative mix suggestion

The suggestion is a compact creative card, not an audio-analysis claim. Choose at most two techniques from `long_blend`, `eq_swap`, `loop_relay`, `fx_transition`, `layering`, `double_drop`, `hard_cut`, and `contrast`. Give one actionable idea, such as where to introduce a loop, when to exchange low end, or how to use filter/echo/reverb. Exact bars, phrases, waveform landmarks, and key compatibility are only stated when verified; otherwise say “try” and explain the uncertainty. Always keep one suggestion in Brief and Rich, even when it is set-level and metadata-light.

## Action and export rendering

Use these stable intents internally and the selected pack’s localized wording externally:

| Intent | Visible behavior |
|---|---|
| `share_feedback` | Invite optional natural-language feedback; update the current session immediately. |
| `export_w4dj` | Offer the current final order as a UTF-8 `.w4dj` handoff after the user asks. |
| `output_text_playlist` | Return a copyable text playlist in the current final order. |
| `harmonic_reorder` | In Brief/Rich only, reorder after an unambiguous positive response. |
| `confirm_long_term_memory` | Present one concise taste-change summary; save only after explicit confirmation. |

Do not treat these actions as a third requirements round. The pack’s `positive`, `negative`, and `ambiguous` expression lists are parsing examples, not a restriction on what the user may say.

## Final-order invariant

Text-playlist and `.w4dj` exports use the current final order. A harmonic reorder may change order, but never changes the collection, complete official title, verified link, recording deduplication, platform policy, or artist cap. Unknown-key tracks remain available and are placed in the localized “awaiting listening” group when a harmonic reorder is performed.
