| Experiment           | Created   | accuracy   | precision   | recall   | f1     | roc_auc   | train.max_depth   |
|----------------------|-----------|------------|-------------|----------|--------|-----------|-------------------|
| exp/muneeb-max-depth | 10:07 PM  | 0.7903     | 0.6458      | 0.4679   | 0.5426 | 0.8344    | 6                 |
|  2bde84c [md12]   | 10:19 PM  | 0.7889     | 0.623       | 0.5214   | 0.5677 | 0.8237    | 12                |
|  ef2c1fc [md8]    | 10:19 PM  | 0.7903     | 0.6367      | 0.492    | 0.5551 | 0.8348    | 8                 |
|  4db0de7 [md4]    | 10:18 PM  | 0.7903     | 0.6804      | 0.3984   | 0.5025 | 0.8292    | 4                 |


Winner: md12 (max_depth=12), f1 0.5677 vs baseline 0.5426, driven by recall (0.468 -> 0.521).
Trade-off: roc_auc fell (0.8344 -> 0.8237) and accuracy dipped slightly, so deeper trees may overfit; md8 has the best roc_auc but a lower f1.

Abandoned because: dev moved to max_depth=8, n_estimators=200 (PR #10) after these runs, so this table (baseline max_depth=6, n_estimators=100) is no longer comparable to current dev. Re-run on a fresh branch from the updated dev.
