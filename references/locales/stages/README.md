# Progressive locale resources

The Markdown files one level above remain the complete, fixed locale-pack records used for audits and source review. Runtime routing uses the stage files listed in `../manifest.json` so an Agent reads only the current locale resource: `trigger`, `round_1`, `round_2`, `search_context`, one `report_*` mode, `post_report`, or `capability_errors`.

Each stage file is a generated projection of the same locale contract. It contains the literal localized text required for that stage; it is not a runtime translation layer and it does not define a second algorithm.

Before loading any stage file, the Agent must load `references/language-routing.json`, resolve and lock the communication language, and then select the matching locale path from `../manifest.json`. The stage files cannot override that routing decision.
