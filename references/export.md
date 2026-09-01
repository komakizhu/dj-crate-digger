# Handoff and text-playlist actions

Load [locales/manifest.json](locales/manifest.json) and only the selected locale's `post_report` resource before rendering post-report actions. The visible labels, explanations, tutorial link, and action phrases come from that stage resource. Internal action names are `output_text_playlist` and `export_w4dj`; users may express them naturally in any supported language.

These actions are offered only after a complete recommendation report. They do not add a third requirements round, change the track collection, or trigger a new search. The export source is the current final order: Fast uses its final table, Brief uses its combined table, and Rich uses its dynamic-combined view. A confirmed harmonic reorder changes the order used for both actions.

## Text playlist

`output_text_playlist` displays a copyable list in chat and never creates a local text file or writes to a platform. Each line contains the official artist and complete official title, in final order. It may be manually pasted into the user's chosen service, but it cannot promise one-click import to DJ software. Do not add an unselected track, a guessed qualifier, a search page, or a hidden platform fallback.

The action is independent from W4DJ. If a track has no valid allowed-platform direct link, keep it out of link-dependent output and explain the skipped count in the current language; do not invent a URL or replace the recording silently.

## W4DJ file

`export_w4dj` creates one UTF-8 JSON file with the `.w4dj` extension. The current contract includes one fixed compatibility field: `format_version` is always the integer `2`; it is not a user-facing choice and there is no migration path. Unknown fields are rejected. Its root contains exactly:

```json
{
  "format": "w4dj",
  "format_version": 2,
  "export_id": "unique-export-id",
  "playlist": {"name": "Playlist Name"},
  "tracks": [
    {
      "position": 1,
      "title": "Complete Official Title (Extended Mix)",
      "artist_display": "Official Artist",
      "netease_track_id": "123456"
    }
  ]
}
```

`tracks[]` contains only `position`, complete official `title`, `artist_display`, and the optional string `netease_track_id`. The ID is omitted when no reliable identity is available; never write a placeholder or numeric JSON value. Remix, Edit, Live, Dub, Instrumental, Radio Edit, Extended Mix, and other official qualifiers stay embedded in `title`; there is no separate title-variant field.

W4DJ carries recommendation handoff data only. It does not contain BPM, key, album, playback URLs, platform state, source records, recording keys, local audio, local paths, filenames, downloads, or import instructions. 不生成占位文件，不处理本地音频；downstream W4DJ tools own those steps.

## Repository test artifacts

When a repository test, fixture, or manual verification needs to materialize a `.w4dj`, write it under `test-artifacts/w4dj/`. Generated files in that directory are local-only and Git-ignored; do not stage, push, or include them in the Skill package. This isolation applies only to repository test artifacts and does not override a user-requested delivery path.

## File permission and safety

Before writing, verify `file_write` in the current environment and use a safe, non-overwriting filename. If the capability is absent, refuse `export_w4dj` and say that no `.w4dj` file was created; do not return an equivalent chat manifest, pretend a download exists, or provide a local path. Do not ask for passwords or store platform tokens.
