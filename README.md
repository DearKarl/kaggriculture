<div align="center">

# Kaggriculture

### Bronze Medal Solution · Top 8.81%

**894th / 10,148 teams · Final score: 4419.2**

An opponent-aware farming agent built on public route-based strategies, with family detection and gated early buying.

[Competition](https://www.kaggle.com/competitions/kaggriculture) · [Leaderboard](https://www.kaggle.com/competitions/kaggriculture/leaderboard?search=We+Forgot+To+Water) · [Official Certificate](https://www.kaggle.com/certification/competitions/dearkarl/kaggriculture) · [Method Notes](docs/METHOD.md)

</div>

[![DearKarl's Kaggriculture Bronze Medal certificate: 894th of 10,148 teams, awarded October 15, 2026](assets/kaggle-bronze-certificate.png)](https://www.kaggle.com/certification/competitions/dearkarl/kaggriculture)

## Competition Result

Our team, **We Forgot To Water**, earned a **Kaggle Competition Bronze Medal**. This repository preserves the selected submission whose private score matches the team's final leaderboard score, together with its original source and a walkthrough of the strategy.

| Metric | Result |
| --- | --- |
| Final rank | **894 / 10,148 teams** |
| Placement | **Top 8.81%** |
| Award | **Competition Bronze Medal** |
| Final leaderboard score | **4419.2** |
| Selected submission's public score | 1849.9 |
| Selected submission's private score | 4419.2 |
| Team | We Forgot To Water |
| Members | [Shuang Xue](https://www.kaggle.com/shuangxue) · [DearKarl](https://www.kaggle.com/dearkarl) |
| Medal awarded | October 15, 2026 |

The certificate above belongs to DearKarl; the ranking and final score are team results. The final score and public score are distinct ratings displayed by Kaggle, rather than a before-and-after measurement of our changes.

## The Challenge

[Kaggriculture](https://www.kaggle.com/competitions/kaggriculture) is a farming simulation competition: an agent coordinates workers, crops, livestock, inventory, and market transactions to maximize income while competing against another agent. Production decisions and trading decisions interact, so a useful action depends on both the farm's state and the timing of market activity.

## Solution Overview

The submitted agent combines **precomputed farming routes**, **reactive controls**, and **opponent-aware purchase timing**. Its core idea is to use an opponent prediction selectively: enable early buying when visible farm behavior matches a known strategy family, and disable that prediction otherwise.

| Component | What it does | Purpose |
| --- | --- | --- |
| Route-based foundation | Replays precomputed actions and selects routes using shops and game phase | Coordinates production and worker activity |
| Reactive controls | Adjusts inherited production, sale timing, inventory handling, and endgame behavior | Responds to the current farm and market state |
| Opponent-family detector | Compares visible opponent farm signatures at steps **24, 48, and 72** | Decides whether a reference route is a plausible prediction |
| Gated early buying | Advances overlapping planned purchases by **one step** when the detector matches | Attempts to buy before predicted competing demand affects prices |
| Quantity accounting | Bounds purchases by plans, cash, and storage; subtracts early buys from later orders | Limits exposure and avoids duplicate purchases |

### How the Opponent-Aware Layer Works

1. **Observe.** Encode the opponent's visible farm tiles, including crop type, planting day, animal species/counts, and tile kind.
2. **Match.** Compare these signatures with fixed references at the three checkpoints. The gate starts disabled; a later mismatch after a match clears and locks the detector.
3. **Predict.** While matching, supply the selected route as an expected opponent plan. Without a match, disable that plan.
4. **Act selectively.** If both routes plan to buy the same product at the next step, consider buying the overlapping quantity now, within cash and storage bounds.
5. **Account.** Reduce the corresponding later purchase order by the amount bought early.

The intended advantage is better purchase timing against predictable opponents. The official final result establishes the submitted agent's competition outcome; it does not isolate the causal contribution of this layer. See [Method Notes](docs/METHOD.md) for code references and evaluation limits.

### Team Contribution and Public Foundations

The selected submission is labeled `our__fr-router`. Its description identifies the family-gated buy-side lead as the focus of the submission. The archived code contains that detector and its connection to the buy controller.

The farming foundation, route data, and many reactive wrappers come from public competition work. We preserve those credits and the source unchanged. `K1` is the baseline label used in the original submission note; a separate baseline artifact was not recovered. Full attribution is recorded in [NOTICE.md](NOTICE.md).

## Explore the Repository

| File | Contents |
| --- | --- |
| [Original submission](submission/submission.tar.gz) | The single preserved Kaggle submission archive |
| [Agent source](src/main.py) | Byte-identical source extracted from the archive |
| [Method notes](docs/METHOD.md) | Strategy walkthrough, source references, and evidence limits |
| [Result provenance](docs/provenance.json) | Score fields, submission details, sources, and SHA-256 hashes |
| [Certificate](assets/kaggle-bronze-certificate.png) | Original certificate image supplied by DearKarl |
| [Archive verifier](tools/verify_archive.py) | File-integrity and syntax checks without executing the agent |

## Use the Archived Submission

Clone the repository and verify the preserved artifact with Python 3:

```bash
git clone https://github.com/DearKarl/kaggriculture.git
cd kaggriculture
python3 tools/verify_archive.py
```

The check validates SHA-256 hashes, archive contents, source byte identity, and Python syntax using the standard library. The competition entry point is `agent(observation, configuration=None)` in `src/main.py`; the original `submission/submission.tar.gz` contains `main.py` at its root.

The historical simulator version and evaluation harness were not recovered with the submission. Archive verification does not run matches or reproduce Kaggle's final rating.

## Result Evidence

The certificate, final leaderboard screenshot, and submission detail screenshot support the result recorded above. The archive contains the selected version matching the final team score; older submissions displayed higher historical public scores.

<details>
<summary>View the final leaderboard and submission details</summary>

### Final Leaderboard

![Final leaderboard: We Forgot To Water, rank 894, score 4419.2, bronze medal](docs/leaderboard.png)

### Selected Submission

![Selected submission details showing public score 1849.9 and private score 4419.2](docs/submission-details.png)

</details>

The original submission note includes local percentages (`95.8/91.7 pct vs family`, `93.8 pct non-family`) and a `no regression` statement. These are preserved as historical notes in [provenance.json](docs/provenance.json). Their raw logs, metric definitions, and sample sizes are unavailable, so they are not presented as independently verified win rates or ablation results.

## Acknowledgments and License

Thank you to the Kaggle community and the public authors whose routes and controllers underpin this submission. The source retains its embedded Apache-2.0 license and contributor notices. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md) for the license text and attribution summary.
