# 方法与证据 / Method and evidence

## 1. 归档范围 / Archive scope

本说明来自下载包中的 `main.py`、提交备注及 2026-10-17 查看的最终榜单，不是对完整开发历史的重建。压缩包仅包含一份 `main.py`（10,311 行）；源码保持原始字节、换行和署名，未为展示重构。

These notes are based on the downloaded `main.py`, submission description, and final leaderboard viewed on 2026-10-17. They do not reconstruct the complete development history. The archive contains one `main.py` (10,311 lines), preserved with its original bytes, line endings, and credits.

## 2. 继承的策略结构 / Inherited strategy structure

程序的底层是预计算行动路线及一系列反应式控制器。源码第 223–248 行描述路线回放框架，第 1031–1037 行载入压缩编码的路线数据，第 1125–1144 行按商店和阶段选择路线。路线不是每步重新训练出的模型；本归档没有训练日志或可核实的训练预算。

The program starts with precomputed action routes and reactive controllers. Lines 223–248 describe the route-replay framework, lines 1031–1037 load compressed route data, and lines 1125–1144 select routes by shops and game phase. Routes are not models retrained each turn; this archive contains no training logs or verified training budget.

公开继承部分还包含市场卖出时机、库存处理、作物／畜牧调整和末期清算。文件中反复包装 `agent`；最终绑定在第 10310–10311 行。因此不能把整份 10,311 行程序都归因为这次提交的新改动，也不能仅凭注释把某个历史候选层视作经过独立验证的增益。

Inherited components also cover sale timing, inventory handling, crop/livestock adjustments, and endgame liquidation. The file repeatedly wraps `agent`, with final bindings at lines 10310–10311. The whole 10,311-line program should not be attributed to this submission's new changes, and comments about historical candidate layers do not establish independently verified gains.

## 3. 本次提交的重点 / Focus of this submission

**识别对手家族。** 第 1039–1111 行将对手农场格子编码为特征，使用作物、种植日、动物类型／数量和格子类型，在第 24、48、72 步与固定参考比较。`_FR_GATE_OPTIMISTIC=False`：在确认匹配前，不乐观启用门控。匹配后若检查发现不一致，会取消匹配并锁定。

**Detect an opponent family.** Lines 1039–1111 encode opponent farm tiles using crops, planting days, animal species/counts, and tile kinds. They compare observations against fixed references at steps 24, 48, and 72. `_FR_GATE_OPTIMISTIC=False` keeps the gate off before a match. A mismatch after matching clears the family flag and locks the detector.

**按识别结果启用预测。** 第 1150–1160 行的 `_fr_router` 在匹配时把当前路线提供为 `opponent_plan`，否则设为 `None`。这是对可见状态匹配后做出的路线预测，不是读取对手的私有行动或真实未来。

**Gate the prediction.** `_fr_router` at lines 1150–1160 supplies the current route as `opponent_plan` when matching and sets it to `None` otherwise. This is a route prediction following visible-state matching, rather than access to an opponent's private actions or actual future.

**提前一步买入。** 第 701 行起的买入控制器，寻找预测对手与自身路线在未来同一步都要买入的商品。第 1115 行设置窗口为一步。数量受双方计划重叠、现金和仓储空间约束；第 703–714 行在原计划时刻扣除提前购买量，避免重复购买。目的是在预测需求影响价格之前执行购买；能否获益取决于预测是否准确与实际成交。

**Buy one step early.** The buy controller beginning at line 701 finds products that both the predicted opponent and our own route plan to buy at the same upcoming step. Line 1115 sets a one-step window. Quantities are bounded by overlapping plans, cash, and storage; lines 703–714 subtract early purchases at the original scheduled step to avoid duplication. The intent is to purchase before predicted demand affects prices; benefit depends on prediction accuracy and actual execution.

**保持保守分支。** 匹配失败时不提供对手计划，买入提前控制器因此返回。提交备注将该分支称为“pure K1”，但没有独立基线文件，不能精确证明与某份外部 K1 逐字节等价。其他继承层仍会正常运行。

**Retain the conservative branch.** With no match, no opponent plan is supplied and the early-buy controller returns. The submission note calls this branch “pure K1,” but no separate baseline file was recovered to establish byte-equivalence to an external K1. Other inherited layers continue to operate.

## 4. 结果与局限 / Results and limits

Kaggle 最终榜单显示队伍 We Forgot To Water 排名 894 / 10,148，铜牌，4419.2 分。指定提交公开分为 1849.9，详情页 Private score 为 4419.2。两个分数是不同页面字段，不应相减作为策略增益。证据见同目录截图与 `provenance.json`。

Kaggle's final leaderboard shows We Forgot To Water at 894 / 10,148, bronze, with 4419.2 points. The selected submission displays 1849.9 publicly and 4419.2 as Private score. These are different page fields and their difference should not be interpreted as a strategy gain. See the screenshots and `provenance.json` in this directory.

历史提交备注中的本地百分比没有原始评测记录支撑，无法核实其定义、样本量、对手覆盖范围或统计不确定性。固定对手特征和路线预测也可能受对手分布变化影响。本仓库不声称每一层都提高胜率，也不声称能通过当前版本模拟器重现官方评级。

Historical local percentages in the submission note lack underlying evaluation records. Their definitions, sample sizes, opponent coverage, and statistical uncertainty cannot be verified. Fixed opponent signatures and route predictions may also be sensitive to changes in the opponent population. This repository does not claim that every layer improves win rate or that a current simulator can reproduce the official rating.

只归档一个提交文件；未下载其他版本。原始提交记录中存在失败改动和负向本地结果，本说明没有把这些尝试改写成成功，也没有据此重建缺失的消融实验。

Only one submission artifact is archived; other versions were not downloaded. Historical submission records include failed changes and negative local results. These attempts are not recast as successes, and missing ablations have not been reconstructed from them.
