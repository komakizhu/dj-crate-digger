# Trigger routing

Activate for a request to discover, curate, rank, sequence, or hand off music for a DJ performance. Lock the communication language first using [language-routing.json](language-routing.json). Then load [trigger-signals.json](trigger-signals.json) and the selected locale's `trigger` resource from `references/locales/manifest.json`. The central resource defines the shared semantic contract; the locale resource supplies localized expressions, aliases, negative contexts, and the ambiguous confirmation. The frontmatter capsule is only for host discovery.

## Three separate decisions

Keep these decisions separate and record them independently:

1. `host_invocation`: whether the host loads this Skill. Direct and ambiguous music requests require invocation; unrelated requests must not invoke it. A host may expose this only through a real replay trace.
2. `skill_route`: after the Skill is loaded, choose `direct`, `ambiguous_confirmation`, or `non_trigger`.
3. `intake_route`: only after `skill_route` is `direct`, apply the readiness contract and choose `direct_ready`, `route_choice_pending`, or `round_1`.

## Semantic scoring

Normalize with NFKC, case-fold Latin text, collapse whitespace, and treat hyphen/underscore/slash variants as equivalent. Keep artist and track text unchanged after routing. Use the central weights:

| Signal | Weight | Examples |
|---|---:|---|
| mode | 100 | 综合版、完整版、极速版、Fast、Brief、Rich |
| dj_action | 70 | build、prepare、curate、sequence、排、挖歌、编排 |
| dj_object | 60 | DJ set、set、playlist、tracklist、歌单、播放列表 |
| dj_context | 45 | club、venue、warm-up、舞池、暖场、Peak、Closing |
| genre | 35 | House、Disco、Techno、Dubstep、Bass、DnB、Jungle 等 |
| reference | 35 | in the style of、类似、参考艺人、参考曲 |
| set_detail | 10–15 | tracks、首歌、时长、BPM、情绪、能量 |

Repeated genre mentions add only capped, diminishing credit. A direct pair adds the declared bonus; repeated identical aliases never create unbounded confidence.

## Route rules

1. Apply hard negative contexts first. API/programming, song identification, downloading, generic listening lists, Skill-development discussion, and explanatory mode/style questions are `non_trigger` even when they contain genre or mode words.
2. Use `direct` when a mode signal combines with any DJ/set/playlist/tracklist/genre/context/reference signal; when a DJ action combines with an object, context, genre, or reference; or when an object combines with a genre, context, or reference. A clear slash alias is also direct.
3. A bare generic music term such as `playlist`, `DJ`, `set`, `找歌`, `歌单`, `dig`, or `digging` is `ambiguous_confirmation` and may receive the selected locale's confirmation exactly once.
4. A genre alone, a mode alone, or an explanatory definition of either is not a DJ request. Genre repetition can raise the recorded confidence, but cannot bypass the minimum intent signal.
5. If direct and ambiguous signals coexist, direct wins unless a hard negative applies. Do not let intake readiness downgrade or replace the Skill route.

## Modes

The canonical mappings are `极速版` / `Fast` → `fast`, `综合版` / `Brief` → `composite`, and `完整版` / `Rich` → `four_views`. `简要版` and `丰富版` remain backward-compatible Chinese aliases. Locale overlays may add natural translations, but internal mode names and output contracts do not change.

## Scope boundary

Search only after `intake_status` is `direct_ready` or `ready`. A post-report feedback, export, memory, or harmonic-order action is not a new intake round.
