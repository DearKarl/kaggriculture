<div align="center">

# Kaggriculture

### Kaggle Bronze Medal Solution

**894th of 10,148 teams · Top 8.81% · Final score 4419.2**

Opponent-aware market timing for a competitive farming simulation.

[Competition](https://www.kaggle.com/competitions/kaggriculture) · [Final Leaderboard](https://www.kaggle.com/competitions/kaggriculture/leaderboard?search=We+Forgot+To+Water) · [Official Certificate](https://www.kaggle.com/certification/competitions/dearkarl/kaggriculture) · [Technical Walkthrough](docs/METHOD.md)

</div>

[![DearKarl's Kaggriculture Competition Bronze Medal certificate, awarded October 15, 2026](assets/kaggle-bronze-certificate.png)](https://www.kaggle.com/certification/competitions/dearkarl/kaggriculture)

## Competition Result

**We Forgot To Water** earned a **Competition Bronze Medal** in Kaggriculture. This repository presents our selected submission, its source code, and the strategy behind its opponent-aware trading layer.

| Achievement | Result |
| --- | --- |
| Final placement | **894 / 10,148 teams — Top 8.81%** |
| Final leaderboard score | **4419.2** |
| Award | **Kaggle Competition Bronze Medal** |
| Team | **We Forgot To Water** |
| Members | [Shuang Xue](https://www.kaggle.com/shuangxue) · [DearKarl](https://www.kaggle.com/dearkarl) |
| Award date | October 15, 2026 |

The certificate is issued to DearKarl; the placement and score are team results. [Result evidence and submission details →](docs/ARCHIVE.md#competition-result-and-selected-submission)

## The Challenge

Kaggriculture is a competitive farming simulation in which agents manage workers, crops, livestock, storage, and market orders to maximize income. Production planning determines what the farm can trade; market timing determines the value of those trades. An opponent's predictable purchases create an opportunity to adjust when our own planned purchases execute.

## Our Strategy

**Recognize predictable opponents, then bring forward the purchases we already intend to make.**

Our submission combines an established route-based farming controller with a selective opponent-aware trading layer. Rather than applying the same market adjustment in every matchup, it checks whether the opponent's visible farm state matches a known strategy family and uses that match to gate early buying.

| Stage | Strategy |
| --- | --- |
| **Plan production** | Use inherited precomputed routes, selected by shops and game phase, with reactive farming and market controls. |
| **Recognize the opponent** | Compare visible farm signatures with fixed references at steps **24, 48, and 72**. |
| **Gate the prediction** | Supply an expected opponent route while matching; disable that plan when the detector does not match. |
| **Advance overlapping purchases** | Consider buying **one step early** when our route and the predicted opponent route plan to purchase the same product. |
| **Control exposure** | Bound quantities by planned demand, available cash, and storage; reduce later orders to avoid buying twice. |

The central design choice is **selective use of prediction**: the early-buy layer starts disabled and relies on observable farm behavior before using an opponent plan. Its intended advantage is to execute purchases before predicted competing demand affects prices.

### Contribution and Foundations

The selected submission, `our__fr-router`, focuses on **opponent-family detection and gated buy-side lead**. Its detector and connection to the purchase controller are present in the submitted source. The farming routes, production controller, and many reactive layers build on public community solutions; their original credits are retained in [NOTICE.md](NOTICE.md).

The final competition result measures the complete submitted agent. The [technical walkthrough](docs/METHOD.md) explains the implementation and the available evidence for individual components.

## Code and Documentation

| Resource | Description |
| --- | --- |
| [Agent source](src/main.py) | The submitted policy, with its original source and credits preserved. |
| [Kaggle submission](submission/submission.tar.gz) | The single selected submission archive. |
| [Technical walkthrough](docs/METHOD.md) | Strategy details, code references, and evaluation context. |
| [Results and archive guide](docs/ARCHIVE.md) | Score evidence, repository contents, integrity checks, and reproduction scope. |

The policy entry point is `agent(observation, configuration=None)`. For download and verification instructions, see the [archive guide](docs/ARCHIVE.md#download-and-verify).

## Acknowledgments

We thank the public competition authors and the Kaggle community whose routes and controllers form the foundation of this solution. The source retains its Apache-2.0 license and contributor notices. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md).
