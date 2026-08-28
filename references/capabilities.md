# Agent capability contract

This Skill uses semantic capabilities, not vendor-specific tool names. Map the current Agent's available tools to these capabilities before the first visible response:

| Capability | Purpose | Required condition |
|---|---|---|
| `web_search` | Find candidate tracks, releases, artist pages, DJ stores, and cultural context | Required for a verified recommendation |
| `open_page` | Open a concrete page and compare the complete official title, artist, availability, and metadata | Required for a verified recommendation |
| `file_write` | Create and return the UTF-8 `.w4dj` handoff file | Required only when the user asks for W4DJ export |
| `progress_message` | Send a first Fast batch while the same task continues | Optional; absence means no automatic continuation |

A capability is present only when the Agent can actually perform the action in the current task. Do not infer capability from a product name, a remembered integration, a link, or a model identity. Do not require a particular search engine, connector name, SDK, shell, or programming runtime.

## Preflight

1. Resolve the locale pack and communication language.
2. Check `web_search` and `open_page`. If either is absent, explain the limitation in the selected language before the first intake round and do not present a verified playlist.
3. Check `file_write` only when `export_w4dj` is requested. If absent, refuse the file action; do not substitute a chat manifest, pretend file, download link, or local path.
4. For Fast continuation, check whether both `progress_message` and continued execution are available. If not, deliver only the verified first batch and state that automatic continuation is unavailable.

## Failure language

Capability failure is not a search failure. Say which semantic capability is unavailable, what cannot be verified or written, and what the user can do next. Never claim that a track is absent merely because a page cannot be opened, and never claim that a file was created when `file_write` was not available.
