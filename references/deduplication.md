# Recording identity and deduplication

Deduplicate before ranking and sequencing. Use ISRC when available. Otherwise normalize Unicode punctuation, case, whitespace, and feature notation, then compare artist identity plus the complete official title. Keep all official qualifiers inside the title, including Remix, Edit, Live, Dub, Instrumental, Radio Edit, Extended Mix, and similar wording.

The same recording found on several allowed platforms becomes one candidate with multiple platform references. Different official title variants remain different recordings unless the source gives the same ISRC. Never use a similar title, a shared artist, or a platform URL slug as proof of identity.

Every delivered table must be checked again after view allocation:

- Fast: no repeated recording in the single table; artist cap is `max(1, floor(0.15 × actual_target))`, unless the user explicitly requests an artist-only set.
- Brief: the combined table is one continuous collection; no recording is repeated.
- Rich: each view is unique; across the four views use no duplicate by default and at most one deliberate high-quality overlap when the documented cross-view conditions are satisfied. Never use a reference artist as an automatic exemption.

If identity, version, availability, or platform evidence is uncertain, omit the candidate rather than merge or duplicate it to meet a count.
