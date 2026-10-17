# 🌾 Kaggriculture — Bronze Medal Solution

**Bronze medal · 894 / 10,148 · Final score 4419.2**

Team **We Forgot To Water**: [Shuang Xue](https://www.kaggle.com/shuangxue) and [DearKarl](https://www.kaggle.com/dearkarl). Approximately **top 8.81%** in the final standings. This repository archives one selected submission and its unchanged extracted source.

[Competition](https://www.kaggle.com/competitions/kaggriculture) · [Final standings](https://www.kaggle.com/competitions/kaggriculture/leaderboard?search=We+Forgot+To+Water) · [Certificate](https://www.kaggle.com/certification/competitions/dearkarl/kaggriculture)

![Final leaderboard evidence](docs/leaderboard.png)

## Result and archive

| Item | Record |
| --- | --- |
| Medal | 🥉 Bronze |
| Final rank | 894 / 10,148 |
| Final leaderboard score | **4419.2** |
| Selected submission public score | 1849.9 |
| Detail-page private score | **4419.2** |
| Submitted by | Shuang Xue |
| Submitted at | 2026-09-30 23:15:59 UTC |
| Submission label | `our__fr-router` |
| Verified on | 2026-10-17 |

1849.9 is the displayed public score; 4419.2 is the final leaderboard score and matches the detail page's Private score. Older submissions displayed higher public scores. This archive preserves the user-selected version matching the final team score, rather than claiming the historical public-score maximum.

## How we approached it

Kaggriculture asks agents to coordinate production, workers, and market transactions to maximize income in a farming simulation. The archived program builds on public strategies, combining precomputed action routes, shop-dependent routing, and reactive production, market-timing, and endgame controls.

The submission's distinguishing addition is **opponent-family detection with gated early buying**. It checks the opponent's farm signature at steps 24, 48, and 72. Matching observations enable route-based opponent predictions for early buying; otherwise that opponent plan is disabled. Early purchases are bounded by planned quantities, cash, and storage, with later planned buys reduced to avoid duplication.

The description of team contributions is grounded in the submission note and archived code. Inherited controllers, route data, and numerous wrapper layers retain their upstream credits. `K1` is the original submission label; the available material does not independently establish its exact baseline definition. See the [method notes](docs/METHOD.md) and [attribution](NOTICE.md).

## Files

- [`submission/submission.tar.gz`](submission/submission.tar.gz): Original Kaggle download; the only archived submission.
- [`src/main.py`](src/main.py): Source extracted unchanged from that archive.
- [`docs/METHOD.md`](docs/METHOD.md): Code references, strategy details, and evaluation limits.
- [`docs/provenance.json`](docs/provenance.json): Results, provenance, and SHA-256 hashes.
- [`docs/submission-details.png`](docs/submission-details.png): Submission-detail evidence.

## Verify the archive

```bash
python3 tools/verify_archive.py
```

This checks archive/source hashes, byte identity, and Python syntax. It does not execute the agent or reproduce the competition score. The competition entry point is `agent(observation, configuration=None)` in `src/main.py`; the original archive is retained for Kaggle environments supporting this format. The historical environment and local evaluation harness were not recovered with the submission.

## Evaluation evidence and license

The submission note records `95.8/91.7 pct vs family`, `93.8 pct non-family`, and `no regression`. Raw logs, seeds, denominators, and metric definitions were not provided; these remain historical notes rather than independently verified win rates or ablation findings. This repository verifies the archived files and the final result displayed by Kaggle.

The archived code includes Apache-2.0 licensing and credits to multiple public contributors, all preserved unchanged. The root [LICENSE](LICENSE) reproduces the complete license text embedded in the source; [NOTICE.md](NOTICE.md) summarizes available credits and sources. This result builds on the community's public work.
