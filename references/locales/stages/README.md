# Progressive locale resources

The Markdown files one level above remain the complete, fixed locale-pack records used for audits and source review. Runtime routing uses the stage files listed in `../manifest.json` so an Agent reads only the current locale resource: `trigger`, `round_1`, `round_2`, `search_context`, one `report_*` mode, `post_report`, or `capability_errors`. Each `trigger` resource includes both the ambiguous-trigger confirmation and the one-time `readiness_choice` for partially specified DJ briefs.

Each stage file is a generated projection of the same locale contract. The `trigger` stage additionally contains `trigger_contract` and a `semantic_signals` locale overlay projected from `references/trigger-signals.json`; it contains localized expressions, not a second algorithm. All other stage files contain the literal localized text required for that stage; none is a runtime translation layer.

For `report_*` stage files, mode and view titles, columns, and every `next_steps` label and body are protected template text. Runtime may fill only real track data, playlist names, digging-notes content, and the creative mix suggestion; it must not summarize, translate, reorder, or omit protected report text.

Before loading any stage file, the Agent must load `references/language-routing.json`, resolve and lock the communication language, and then select the matching locale path from `../manifest.json`. The stage files cannot override that routing decision.
