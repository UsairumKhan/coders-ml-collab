# 📊 Assignment 01 Report: Git-Based Collaboration for an ML Project

**Repository URL:** [https://github.com/UsairumKhan/coders-ml-collab](https://github.com/UsairumKhan/coders-ml-collab)  
**DVC Remote:** DagsHub (`https://dagshub.com/UsairumKhan/coders-ml-collab.dvc`)  
**Dataset Source:** [Kaggle Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)  

---

## 👥 Team Members & Role Assignments

| Member | Assigned Role | Primary Responsibilities |
| :--- | :--- | :--- |
| **Usairum Khan** | **Platform Owner** | Scaffold layout, `.gitignore`, `.pre-commit-config.yaml`, GitHub Actions CI (`.github/workflows/ci.yml`), branch protection rules |
| **Muhammad Mujtaba** | **Data Owner** | DVC setup, dataset tracking (`data/raw/*.csv.dvc`), DagsHub remote configuration, data cleaning functions (`src/cleaning.py`) |
| **Abdul Muneeb** | **Model Owner** | ML pipeline architecture (`src/prepare.py`, `src/train.py`, `src/evaluate.py`), `params.yaml`, `dvc.yaml`, hyperparameter experiments |

---

## 🔁 Released Model Reproducibility Table (`model-v1.0`)

| Parameter / Metric | Value |
| :--- | :--- |
| **Release Tag** | `model-v1.0` |
| **Target Branch** | `main` |
| **Random Seed** | `42` |
| **Test Split Ratio** | `0.2` (20%) |
| **Raw Dataset `.dvc` Hash** | `0f9de68e012bd3aed5fa7cdc9fc421af` |
| **Hyperparameters (`params.yaml`)** | `model: random_forest`, `n_estimators: 200`, `max_depth: 8` |
| **`dvc.lock` Status** | Locked and verified via `dvc repro` |
| **Final Accuracy** | **`0.8062`** (80.62%) |
| **Final Precision** | **`0.6797`** |
| **Final Recall** | **`0.5107`** |
| **Final F1-Score** | **`0.5832`** |
| **Final ROC-AUC** | **`0.8432`** |

---

## 🧪 Hyperparameter Experiments Comparison (`dvc exp show`)

| Experiment | `max_depth` | `n_estimators` | Accuracy | Precision | Recall | F1 Score | ROC AUC | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Baseline (Exp 1)** | 6 | 100 | 0.8006 | 0.6824 | 0.4652 | 0.5533 | 0.8426 | Baseline |
| **Exp 2** | 10 | 150 | 0.7984 | 0.6520 | 0.5160 | 0.5761 | 0.8355 | Improved Recall |
| **Exp 3 (Winner)** | **8** | **200** | **0.8062** | **0.6797** | **0.5107** | **0.5832** | **0.8432** | 🏆 **Promoted Winner** |

### Winner Rationale:
Experiment 3 achieved the best overall performance, increasing **Accuracy to 80.62%**, **F1 Score to 0.5832**, and **ROC-AUC to 0.8432**. Setting `max_depth=8` provided optimal model capacity without overfitting, while `n_estimators=200` stabilized prediction variance.

---

## 🔗 Evidence & Pull Request Links

1. **Data Update PR:** [PR #4: Track raw dataset with DVC](https://github.com/UsairumKhan/coders-ml-collab/pull/4)
2. **Conflict Resolution PR:** [PR #9: Conflict resolution on params.yaml / dvc.lock](https://github.com/UsairumKhan/coders-ml-collab/pull/9)
3. **Changes Requested Review:** [Review on PR #10 with feedback requested](https://github.com/UsairumKhan/coders-ml-collab/pull/10)
4. **Release PR (`dev` $\rightarrow$ `staging`):** [Release Candidate v1.0 PR](https://github.com/UsairumKhan/coders-ml-collab/pulls?q=is%3Apr+release)
5. **Abandoned Experiment Branch:** [PR #9: feat: tune max_depth to 8 from top-performing experiment](https://github.com/UsairumKhan/coders-ml-collab/pull/9) *(Left unmerged to demonstrate experiment drift).*

---

## 📸 Checkpoint Evidence

### 1. Blocked Secret / Large File Checkpoint
Pre-commit hook `detect-secrets` and `check-added-large-files` automatically blocked an attempted commit containing a fake AWS API key:
```text
ERROR: Potential secrets about to be committed to git repo!
Secret Type: AWS Access Key
Location: fake_secret.txt:1
```

### 2. Failing CI Checkpoint
GitHub Actions CI automatically blocked a PR when code formatting and linting failed:
```text
RUF100 [*] Unused `noqa` directive
--> notebooks/01-eda.py:36:1: E402 Module level import not at top of file
Error: Process completed with exit code 1.
```

### 3. Passing CI Checkpoint
All 4 automated GitHub Actions CI jobs (`lint`, `unit-tests`, `data-checks`, `smoke-train`) passed with green checkmarks:
- 🧹 Code Linting & Formatting Check: **PASS**
- 🧪 Run Unit Tests (pytest): **PASS** (2/2 tests passed)
- 📊 Data Schema & Quality Check: **PASS**
- ⚡ End-to-End Smoke Training Run: **PASS**

---

## 📝 Team Retrospective

### What Broke & Challenges Faced:
- **Windows Path & DVC Cache Locking:** DVC initially encountered `[WinError 3]` on Windows due to directory hash handling and single quotes in `.dvc/config`. We fixed this by explicit target paths in `dvc.yaml` and setting `cache.type = copy`.
- **Linting with Jupytext:** Jupytext python exports initially triggered `ruff` rule `E402` ("import not at top of file"). We standardized placing module imports in the top cell of notebooks.

### Standardization & `CONTRIBUTING.md` Additions:
- Mandated **Conventional Commits** (`feat:`, `data:`, `exp:`, `ci:`, `fix:`).
- Enforced **Squash-Merge** policy for all feature PRs into `dev`.
- Added pre-commit installation (`python -m pre-commit install`) as a mandatory step for all collaborators.

---

## 👤 Member Contribution Statements

- **Usairum Khan (Platform Owner):** Created the repository structure, configured `.gitignore`, `.pre-commit-config.yaml` (ruff, nbstripout, 1MB size limit, detect-secrets), set up protected branches (`main`, `staging`, `dev`), built the 4-job GitHub Actions CI workflow (`.github/workflows/ci.yml`), authored winning model promotion PR, and compiled `REPORT.md`.
- **Muhammad Mujtaba (Data Owner):** Initialized DVC tracking (`dvc init`), integrated DagsHub remote storage, tracked raw Telco Churn CSV data (`.dvc` pointers), authored EDA notebook (`notebooks/01-eda.ipynb`) with Jupytext pairing, wrote unit tests (`tests/test_cleaning.py`), and reviewed team PRs.
- **Abdul Muneeb (Model Owner):** Refactored ML code into modular scripts (`src/prepare.py`, `src/train.py`, `src/evaluate.py`), constructed `dvc.yaml` and `params.yaml`, executed hyperparameter tuning experiments (`exp/` branches), resolved merge conflicts on `params.yaml`, and participated in peer reviews.
