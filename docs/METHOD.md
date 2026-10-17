# Method and Evidence

## Archive scope

For score screenshots, submission metadata, and file verification instructions, see the [Results and Archive Guide](ARCHIVE.md).

These notes are based on the downloaded `main.py`, submission description, and final leaderboard viewed on 2026-10-17. They do not reconstruct the complete development history. The archive contains one `main.py` (10,311 lines), preserved with its original bytes, line endings, and credits.

## Inherited strategy structure

The program starts with precomputed action routes and reactive controllers. Lines 223–248 describe the route-replay framework, lines 1031–1037 load compressed route data, and lines 1125–1144 select routes by shops and game phase. Routes are not models retrained each turn; this archive contains no training logs or verified training budget.

Inherited components also cover sale timing, inventory handling, crop/livestock adjustments, and endgame liquidation. The file repeatedly wraps `agent`, with final bindings at lines 10310–10311. The whole 10,311-line program should not be attributed to this submission's new changes, and comments about historical candidate layers do not establish independently verified gains.

## Focus of this submission

**Detect an opponent family.** Lines 1039–1111 encode opponent farm tiles using crops, planting days, animal species/counts, and tile kinds. They compare observations against fixed references at steps 24, 48, and 72. `_FR_GATE_OPTIMISTIC=False` keeps the gate off before a match. A mismatch after matching clears the family flag and locks the detector.

**Gate the prediction.** `_fr_router` at lines 1150–1160 supplies the current route as `opponent_plan` when matching and sets it to `None` otherwise. This is a route prediction following visible-state matching, rather than access to an opponent's private actions or actual future.

**Buy one step early.** The buy controller beginning at line 701 finds products that both the predicted opponent and our own route plan to buy at the same upcoming step. Line 1115 sets a one-step window. Quantities are bounded by overlapping plans, cash, and storage; lines 703–714 subtract early purchases at the original scheduled step to avoid duplication. The intent is to purchase before predicted demand affects prices; benefit depends on prediction accuracy and actual execution.

**Retain the conservative branch.** With no match, no opponent plan is supplied and the early-buy controller returns. The submission note calls this branch “pure K1,” but no separate baseline file was recovered to establish byte-equivalence to an external K1. Other inherited layers continue to operate.

## Results and limits

Kaggle's final leaderboard shows We Forgot To Water at 894 / 10,148, bronze, with 4419.2 points. The selected submission displays 1849.9 publicly and 4419.2 as Private score. These are different page fields and their difference should not be interpreted as a strategy gain. See the screenshots and `provenance.json` in this directory.

Historical local percentages in the submission note lack underlying evaluation records. Their definitions, sample sizes, opponent coverage, and statistical uncertainty cannot be verified. Fixed opponent signatures and route predictions may also be sensitive to changes in the opponent population. This repository does not claim that every layer improves win rate or that a current simulator can reproduce the official rating.

Only one submission artifact is archived; other versions were not downloaded. Historical submission records include failed changes and negative local results. These attempts are not recast as successes, and missing ablations have not been reconstructed from them.
