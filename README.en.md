# 老炮DJ (dj-crate-digger)

[中文](README.md) | [English](README.en.md)

Chinese name: 老炮DJ; English name, Skill name, and repository name: `dj-crate-digger`.

This is a native, portable Agent Skill package for DJs, producers, and electronic-music listeners. It turns natural-language curation requests into recommendations based on web search, track-level page verification, recording deduplication, ranking, and set sequencing. Every compatible client uses the same `SKILL.md` and `references/`; there is no host-specific algorithm or second prompt copy.

## I. Core capabilities

### 1.1 Adaptive intake and personalization

The composite report is the default for every activated DJ request; only an explicitly selected alternative mode changes it. When one message supplies the scene, sound direction, and track count or set duration—or simply delegates the remaining choices and asks the Skill to proceed—the Skill skips both questionnaires and runs the composite path directly. When a request contains at least two substantive brief signals but is missing a low-impact detail such as duration, the Skill asks once whether to give the result directly or use the two-round questionnaire. A direct choice lets the Skill infer low-impact omissions; a questionnaire choice enters round one. A vague or nearly empty request goes straight to round one, and an explicit “give me the result directly” can escape an already-started first round. Round one collects the scene, target country/region, core sound direction, track count or set duration, output mode, and other constraints; round two collects specific style, BPM, familiarity/discovery, era/classics, mood, energy curve, platform/link requirements, and anything else. A blank mode still produces the composite report. There is no third ordinary requirements round.

Communication language and target market are separate. Language controls visible text, while the market controls only current search context, cultural context, and availability. An explicit market never changes response language; a blank market stays broad and temporary and is never written to long-term taste memory.

On a new chat started with a slash entry such as `/dj`, the Skill first reads recent user-language signals and the saved identity language preference before choosing visible language; recent sessions take priority. It auto-learns a communication-language preference only when four of the last five eligible sessions agree. With no usable signal, it shows one fixed bilingual language confirmation instead of silently emitting the English template. This preference remains separate from DJ taste and target-market data.

### 1.2 Three output modes

| Mode | Best for | Output |
|---|---|---|
| Fast | Getting usable tracks quickly | Independent three-column path with first-batch and continuation rules |
| Brief | Receiving one complete playlist | One exact twelve-column table, keys, reasons, and one creative transition suggestion |
| Rich | Comparing selection directions | Style, scene, familiarity/discovery views plus one dynamic combined view |

Brief and Rich use exactly: `title | artist | album/EP | style | BPM | key | duration | energy | release date | notes | selection reason | link`. All modes preserve complete official titles, platform policy, track-level evidence, and recording-level deduplication.

The final report also has protected and dynamic regions. Mode/view titles, column labels and order, the count/order/labels/bodies of `next_steps`, action phrases, tutorial links, and Markdown shape must be copied exactly; they may not be paraphrased, shortened, merged, reordered, or omitted. Brief and Rich must retain all three next steps, including both the text-playlist and W4DJ actions in the second item; Fast must retain both of its next steps. Track data, playlist names, digging-notes content, and the creative mix suggestion are the dynamic regions.

### 1.3 Search, cultural context, and ranking

Official artists, labels, distributors, and authorized DJ stores verify identity, complete titles, BPM, keys, and release facts. 1001Tracklists, Resident Advisor, Pitchfork, Mixmag, DJ Mag, and The Quietus may improve candidate recall, cultural context, and DJ-use signals, but they never replace the final track link. A user-specified platform controls allowed search and playback links; the Skill never silently falls back to another platform.

Keys are accepted only when reliable evidence matches the same complete official title; unknown or conflicting keys keep the track and remain unknown. Brief and Rich reorder only after an unambiguous positive harmonic request, using basic Camelot compatibility and at most five double-drop candidates that still require DJ audition. Without waveform or listening evidence, transition advice is creative and tentative.

### 1.4 Private feedback memory

Users can say in ordinary language what they like, dislike, would use, or actually played. Current-session feedback applies immediately; a long-term profile is saved only after one round is summarized and explicitly confirmed. Feedback events and a rebuildable profile remain local and private, long-term taste contributes no more than 10% of recommendation weight, and the first phase does not upload or anonymously collaborate.

## II. Quick start

Place the complete repository directory in the client's Agent Skills directory so that `SKILL.md`, `references/`, and the locale packs remain together. Then describe the DJ request:

```text
/dj-crate-digger
```

The legacy alias is also supported:

```text
/迪歌
```

Natural language works too:

```text
Build a 60-minute UK Bass set for an underground club in Guangzhou, using Skream and Nikita, the Wicked as references.
```

The flow is: request → search immediately when the brief is ready or delegated; choose direct execution or two-round refinement when the brief is partially specified; use the two fixed rounds when it is vague → track-level verification → composite report or the explicitly selected mode → optional feedback, text playlist, W4DJ, or harmonic reorder.

### 2.1 Trigger contract and acceptance

The single cross-language semantic trigger contract is [`references/trigger-signals.json`](references/trigger-signals.json); the 26 locale packs provide localized overlays only. Run `scripts/validate_trigger_acceptance.py` for the 100-case matrix, `scripts/build_skill_package.py` for a clean package, and `scripts/sync_installed_skill.py --target /Users/mac2/.codex/skills/dj-crate-digger --apply` for the installed copy. The complete bilingual acceptance contract is [`docs/trigger-acceptance-plan.md`](docs/trigger-acceptance-plan.md). Static 100/100 does not prove real host invocation; reports must retain the host end-to-end status.

## III. Export and handoff

Only the post-report “next step” area offers export actions:

- `output text playlist`: returns copyable text in chat in the current final order. It does not create a local text file or claim one-click import into DJ software.
- `export to w4dj`: when the current Agent truly has file-writing capability and the user explicitly triggers it, creates a UTF-8 `.w4dj` file. It contains only playlist name, order, complete official titles, and artists; every track carries the required v2 compatibility field `netease_track_id: null`, never a NetEase song ID; no local audio, paths, downloads, or internal metadata.

`.w4dj` has one current contract: root fields are `format`, `format_version`, `export_id`, `playlist`, and `tracks`. The Skill always writes integer `2` to `format_version` for W4DJ compatibility; it is not a user-selectable format. `playlist` contains only `name`; each track contains `position`, `title`, `artist_display`, and required `netease_track_id` whose value is strictly JSON `null`. The Skill does not search for, infer, complete, or validate NetEase song IDs; the playlist-level `export_id` is retained as the handoff-document ID. For the complete workflow, see [One-Click Set Import Tutorial](https://github.com/komakizhu/dj-crate-digger/blob/main/docs/w4dj/README.en.md). This Skill does not download music, create local audio, or perform downstream import steps.

Repository tests, fixture demos, and manual verification runs must write generated `.w4dj` files under `test-artifacts/w4dj/`; that directory is ignored and excluded from commits and releases. User-requested deliverables still use the explicitly requested destination.

The baseline, rationale, and removal conditions are recorded in the [W4DJ v2 compatibility memo](docs/w4dj-v2-compatibility-memo.md).

## IV. Universal Agent compatibility

This repository provides one standard Skill package. Clients that can import complete Agent Skills can load the same files according to their own directory rules. Search, page opening, file writing, and progress messages are mapped by the client; the Skill does not require a fixed tool name, SDK, command, or model.

Compatibility uses three statuses: formally supported, natively compatible but not replay-tested, and pending confirmation. Because complete cold-start replays have not yet been run for every combination, the following clients remain “natively compatible but not replay-tested”; documentation compatibility is not presented as runtime acceptance:

| Client | Status |
|---|---|
| Codex | Natively compatible, not replay-tested |
| Claude Code, Gemini CLI | Natively compatible, not replay-tested |
| VS Code / GitHub Copilot, Cursor, Windsurf, OpenCode | Natively compatible, not replay-tested |
| WorkBuddy / CodeBuddy, Qoder / QoderWork, Trae / TraeWork | Natively compatible, not replay-tested |
| Doubao Work | Pending confirmation |
| Other clients that advertise “skills” | Pending confirmation |

The repository ships 26 fixed locale packs, listed in [`references/locales/manifest.json`](references/locales/manifest.json). At runtime, only the selected stage resource for triggers, intake, search context, reports, or post-report actions is loaded; intake, reports, statuses, actions, and platform expressions are read from fixed resources rather than translated as a complete template at runtime. Unsupported languages fall back to English. Full multilingual support claims still require native-speaker review and the planned 312 cold-start replays.

Directory discovery follows each client's public Agent Skills documentation, including [Claude Code](https://code.claude.com/docs/en/skills), [Gemini CLI](https://geminicli.com/docs/cli/using-agent-skills/), [VS Code Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills), [Cursor](https://prod.cursor.com/docs/skills), [Windsurf](https://docs.windsurf.com/windsurf/cascade/skills), [OpenCode](https://opencode.ai/docs/skills/), [WorkBuddy/CodeBuddy](https://www.workbuddy.cn/docs/cli/skills), [Qoder/QoderWork](https://docs.qoder.com/qoder/skills), and [Trae](https://docs.trae.cn/ide_skills). These links describe standard import boundaries; they do not replace runtime replay acceptance for this project.

## V. Capability boundaries

Without web search or concrete page-opening capability, the Skill does not present a fake verified playlist. Without file-writing capability, it does not claim to have created a `.w4dj` file. Missing platform tracks, title mismatches, key conflicts, or insufficient candidates reduce the actual count with an explanation instead of filling with wrong links, invented titles, unverified tracks, or duplicate recordings.

This project is released under the Apache License 2.0. See [LICENSE](LICENSE).
