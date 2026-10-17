# 🌾 Kaggriculture — Bronze Medal Solution

**铜牌 · 894 / 10,148 · 最终分 4419.2**  
**Bronze medal · 894 / 10,148 · Final score 4419.2**

队伍 **We Forgot To Water**： [Shuang Xue](https://www.kaggle.com/shuangxue) 与 [DearKarl](https://www.kaggle.com/dearkarl)。最终排名前约 **8.81%**。本仓库仅归档一份选定提交，以及从该压缩包原样提取的源码。

Team **We Forgot To Water**: [Shuang Xue](https://www.kaggle.com/shuangxue) and [DearKarl](https://www.kaggle.com/dearkarl). Approximately **top 8.81%** in the final standings. This repository archives one selected submission and its unchanged extracted source.

[比赛 / Competition](https://www.kaggle.com/competitions/kaggriculture) · [最终榜单 / Final standings](https://www.kaggle.com/competitions/kaggriculture/leaderboard?search=We+Forgot+To+Water) · [证书 / Certificate](https://www.kaggle.com/certification/competitions/dearkarl/kaggriculture)

![Final leaderboard evidence](docs/leaderboard.png)

## 成绩与归档 / Result and archive

| 项目 / Item | 记录 / Record |
| --- | --- |
| 奖牌 / Medal | 🥉 Bronze |
| 最终排名 / Final rank | 894 / 10,148 |
| 最终榜单分 / Final leaderboard score | **4419.2** |
| 指定提交的公开分 / Selected submission public score | 1849.9 |
| 详情页 Private score / Detail-page private score | **4419.2** |
| 提交者 / Submitted by | Shuang Xue |
| 提交时间 / Submitted at | 2026-09-30 23:15:59 UTC |
| 策略标签 / Submission label | `our__fr-router` |
| 核实日期 / Verified on | 2026-10-17 |

1849.9 是该提交页面显示的公开分，4419.2 是最终榜单分，也与详情页标记的 Private score 一致。旧提交曾显示更高公开分，因此本仓库不把 1849.9 称为历史最高公开分；归档的是用户选定、与最终队伍分数一致的版本。

1849.9 is the displayed public score; 4419.2 is the final leaderboard score and matches the detail page's Private score. Older submissions displayed higher public scores. This archive preserves the user-selected version matching the final team score, rather than claiming the historical public-score maximum.

## 我们怎么做 / How we approached it

Kaggriculture 要求智能体在农业模拟中安排生产、工人和市场交易，尽可能增加收入。归档程序以公开策略为基础，包含预计算行动路线、按商店情况选择路线，以及生产、交易时机和终局清算等反应式控制。

Kaggriculture asks agents to coordinate production, workers, and market transactions to maximize income in a farming simulation. The archived program builds on public strategies, combining precomputed action routes, shop-dependent routing, and reactive production, market-timing, and endgame controls.

本次提交的特色是**对手家族识别 + 有条件提前买入**：在第 24、48、72 步检查对手农场特征；检测匹配时，使用路线预测启用买入提前量；未匹配时不使用这份对手计划。提前买入受计划购买量、现金和仓储限制，并在原计划时刻扣除已提前买入数量。

The submission's distinguishing addition is **opponent-family detection with gated early buying**. It checks the opponent's farm signature at steps 24, 48, and 72. Matching observations enable route-based opponent predictions for early buying; otherwise that opponent plan is disabled. Early purchases are bounded by planned quantities, cash, and storage, with later planned buys reduced to avoid duplication.

团队贡献的描述依据提交备注和归档代码；继承的控制器、路线数据与众多后续包装层均保留上游署名。`K1` 是原提交标签，当前材料不足以独立重建其精确基线定义。详见[方法说明 / Method notes](docs/METHOD.md)与[署名说明 / Attribution](NOTICE.md)。

The description of team contributions is grounded in the submission note and archived code. Inherited controllers, route data, and numerous wrapper layers retain their upstream credits. `K1` is the original submission label; the available material does not independently establish its exact baseline definition. See the [method notes](docs/METHOD.md) and [attribution](NOTICE.md).

## 文件 / Files

- [`submission/submission.tar.gz`](submission/submission.tar.gz)：Kaggle 下载的原始文件，仅保留这一份提交。 / Original Kaggle download; the only archived submission.
- [`src/main.py`](src/main.py)：从原包原样提取的源码。 / Source extracted unchanged from that archive.
- [`docs/METHOD.md`](docs/METHOD.md)：代码依据、策略细节与评测边界。 / Code references, strategy details, and evaluation limits.
- [`docs/provenance.json`](docs/provenance.json)：成绩记录、来源与 SHA-256。 / Results, provenance, and SHA-256 hashes.
- [`docs/submission-details.png`](docs/submission-details.png)：提交详情凭证。 / Submission-detail evidence.

## 检查归档 / Verify the archive

```bash
python3 tools/verify_archive.py
```

检查压缩包与源码哈希、逐字节一致性及 Python 语法；不会运行智能体或重现比赛成绩。实际比赛入口为 `src/main.py` 中的 `agent(observation, configuration=None)`，原始提交包可直接用于支持此格式的 Kaggle 环境。历史环境与本地评测工具未随提交保存。

This checks archive/source hashes, byte identity, and Python syntax. It does not execute the agent or reproduce the competition score. The competition entry point is `agent(observation, configuration=None)` in `src/main.py`; the original archive is retained for Kaggle environments supporting this format. The historical environment and local evaluation harness were not recovered with the submission.

## 评测证据与许可 / Evaluation evidence and license

提交备注记录了 `95.8/91.7 pct vs family`、`93.8 pct non-family` 和 `no regression`。原始日志、种子、分母及指标定义未提供，因此这些仅作为历史备注保存，不作为独立验证的胜率或消融结论。该仓库验证的是已归档文件和 Kaggle 显示的最终成绩。

The submission note records `95.8/91.7 pct vs family`, `93.8 pct non-family`, and `no regression`. Raw logs, seeds, denominators, and metric definitions were not provided; these remain historical notes rather than independently verified win rates or ablation findings. This repository verifies the archived files and the final result displayed by Kaggle.

归档代码包含 Apache-2.0 许可及多位公开作者署名，均原样保留。根目录 [LICENSE](LICENSE) 提取自源码中完整的许可文本；[NOTICE.md](NOTICE.md) 汇总现有署名和来源。此成果建立在社区公开工作的基础上。

The archived code includes Apache-2.0 licensing and credits to multiple public contributors, all preserved unchanged. The root [LICENSE](LICENSE) reproduces the complete license text embedded in the source; [NOTICE.md](NOTICE.md) summarizes available credits and sources. This result builds on the community's public work.
