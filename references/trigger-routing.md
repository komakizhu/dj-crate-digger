# Trigger routing

Activate for a request to discover, curate, rank, sequence, or hand off music for a DJ performance. Lock the communication language first using [language-routing.json](language-routing.json). Then load the selected locale's `trigger` resource from `references/locales/manifest.json`; it is the source of the full localized trigger list and the one-line ambiguous confirmation. Once activated, initialize `output_mode: composite`; readiness decides whether to ask the fixed intake, not which mode is the default. The frontmatter capsule is only for discovery.

## Decision order

1. If the message contains a clear DJ planning action plus context—such as building a set, mixing, performing, a venue, dancefloor, warm-up, peak-time, closing, genre direction, reference artist/track, BPM, mood, or energy—activate and apply the readiness decision in [intake-routing.md](intake-routing.md). A bare `DJ` is not enough.
2. If it contains only an ambiguous music term such as playlist, DJ, find tracks, dig, digging, 找歌, 歌单, 排歌, or the equivalent in a locale pack, ask once using that locale's confirmation. A positive answer enters round one; a negative answer exits; an unclear answer may receive one final clarification only. The canonical Chinese direct trigger `挖歌` remains direct; a phrase like `找歌` remains ambiguous without DJ context.
3. Do not activate for song identification, “what song is this?”, programming playlist objects, generic non-DJ listening lists, or Skill-development discussion.

Natural-language direct triggers include, but are not limited to, “排个 set”, “排个 DJ set”, “排一套 set”, “挖歌”, “build a DJ set”, “sequence a DJ set”, and the full-locale equivalents. Keep artist and track names in their original text when routing. If direct and ambiguous cues appear together, the clear planning action wins; a bare ambiguous token never bypasses the confirmation.

## Scope boundary

Once activated, search only after `intake_status` is `direct_ready` or `ready`. A post-report feedback, export, memory, or harmonic-order action is not a new intake round.
