# Fast mode

`fast` is an independent delivery path, not a shortened Brief or Rich report. It returns only `title | artist | link`, with one verified direct track or release page per row. It never displays key data, the 12-column table, digging notes, a mix suggestion, harmonic ordering, internal sources, or memory state.

## Recall and scoring

Choose one dominant recall channel: reference track/artist/style → `anchor_style`; scene/market/mood/energy → `scene_context`; familiarity/era/classics → `familiarity_era`. BPM can refine a concrete style but cannot recall alone. When signals are empty, choose the most specific available signal in that order. Run one exact query and at most one same-channel one-level fallback. Do not change channel or weights.

Use one light score: dominant direction 60%, other round constraints 25%, artist/title-variant/sound diversity 15%. Hard-filter explicit exclusions, forbidden platforms, exclusive platforms, complete-title mismatch, unavailable pages, and duplicate recordings before scoring.

## Count and time

- A request of 1–20 tracks targets that number and ends after the first complete delivery.
- A request of 21–50 targets the requested final count; first batch targets 15 and may stop between 10 and 20 at the active-computation cutoff, then continues from the same two query results.
- A request above 50 is capped at 50 and says so in the title.
- No count defaults to about 15, allowed range 10–20, with the first batch as the final result.
- `fast_pool_goal = min(max(2 × first_batch_target, first_batch_target + 5), 40)`; verify five candidates in parallel per batch where the host permits.
- Allocate active computation approximately 5 seconds for parsing/query planning, 20 for normalization/scoring, 20 for deduplication/order, 10 for output/checks, and 5 for buffer. Network waiting is excluded. Stop expanding at 50 seconds; the intended active range is 50–70 seconds.

For continuation use `continuation_pool_goal = min(max(2 × final_target, final_target + 10), 100)`. Read only more results from the same exact/fallback queries, reuse the same score, preserve every first-batch track, and stop at the target, pool goal, exhausted results, or two batches without a new deliverable recording. Without progress and continued-execution capabilities, do not promise automatic continuation.

## Output contract

First batch:

```markdown
# <localized fast first-batch title> (X/N)

| <title> | <artist> | <link> |
|---|---|---|
| Official Title | Official Artist | [Platform](direct-url) |

<localized continuation status>
```

Final output uses the same three columns, retains all first-batch tracks, and is the only Fast response that renders the locale's two optional next-step items. If no verified track exists, return zero rows and the reason; never fill with an unverified, wrong-version, wrong-platform, or duplicate recording.
