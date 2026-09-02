# 跨语言触发验收计划 / Cross-Language Trigger Acceptance Plan

本文件定义 `dj-crate-digger` 触发修复的可重复验收口径。它只验收宿主发现、Skill 内部路由、intake readiness 和产物一致性，不验收推荐算法、真实歌曲质量或第三方平台集成。

This document defines the repeatable acceptance contract for the `dj-crate-digger` trigger repair. It covers host discovery, internal Skill routing, intake readiness, and artifact parity only; it does not evaluate recommendation quality, real-song quality, or third-party integrations.

## 分层字段 / Layered fields

| 中文 | English | Meaning |
|---|---|---|
| 宿主是否调用 | Host invocation | Whether the host actually loaded the Skill; static runs record `not_observed` and keep the reference prediction in evidence. |
| Skill 内部路由 | Skill route | `direct`, `ambiguous_confirmation`, or `non_trigger` after the Skill is loaded. |
| intake 路由 | Intake route | `direct_ready`, `route_choice_pending`, `round_1`, or `not_applicable`; evaluated only after a direct Skill route. |
| 预期置信度 | Expected confidence | Oracle band declared by the acceptance case. |
| 实际置信度 | Actual confidence | Band calculated by the portable reference router. |
| 证据 | Evidence | Matched signal families, terms, score, contribution breakdown, and execution layer. |
| 通过/失败 | Pass/Fail | Static semantic assertion result; overall acceptance also requires a real host trace. |

## 100 条矩阵 / 100-case matrix

- 26 languages × 3 baselines = 78: one direct DJ-curation request, one generic/ambiguous request, and one hard-negative request per locale.
- 22 stress cases: 6 mode combinations, 6 genre-family combinations covering the full central family list, 4 normalization/boundary cases, 3 mixed-language cases, and 3 hard-negative overrides.
- Every case records `locale`, `language`, `input`/`query`, `style_family`, `signal_families`, expected confidence, expected host invocation, expected Skill route, expected intake route, `intake_signals`, and compatibility `should_trigger`.
- Result runs add `actual_host_invocation`, `actual_skill_route`, `actual_intake_route`, `actual_confidence`, `evidence`, and `pass`.

## 验收步骤 / Acceptance sequence

1. Validate JSON, frontmatter, manifest, locale projections, signal families, and resource structure.
2. Validate the 100 static cases against the independent reference router and the existing intake router.
3. Run the same matrix against the workspace, clean package, and installed copy.
4. Compare package-owned files byte-for-byte across the three artifacts; preserve but never delete target-only local files.
5. Run a real host replay and record whether the host actually loaded the Skill for each case.
6. Keep the existing 312-run multilingual cold-start specification separate. Its `not_run` state must not be replaced by this 100-case matrix.

## 报告门槛 / Gate semantics

The static matrix may be reported as passed when all 100 expected routes, confidence bands, intake routes, and evidence fields are present and correct. Overall acceptance is **incomplete/failed** when host invocation is not observable, even if the static matrix is 100/100. The report must never convert `not_run` or `not_observed` into `passed`.

An acceptance report must show the 100 row-level results, per-locale coverage, per-genre-family coverage, workspace/package/installed parity, host end-to-end status, and all unexecuted layers with their explicit reason.
