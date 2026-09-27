# Contributing Guidelines

Welcome to the **Telco Churn ML Collaboration Project** (`coders-ml-collab`)!

## 🌿 Branch Naming Rules
Work flows strictly in one direction:
`feat/*` or `data/*` ➡️ `dev` ➡️ `staging` ➡️ `main`

- **`main`**: Production releases only. Tagged (e.g. `model-v1.0`).
- **`staging`**: Release candidates. Tested & validated by teammates.
- **`dev`**: Main integration branch for all features and data changes.
- **`feat/<name>`**: Short-lived branches for production code features or refactoring.
- **`data/<name>`**: Short-lived branches for dataset updates (tracked via DVC).
- **`exp/<member>-<idea>`**: Exploration branches for individual experiments. *Never merged directly to `dev`*.
- **`fix/<name>`**: Urgent hotfixes branched from `main`.

---

## 📝 Commit Message Convention
We strictly follow **Conventional Commits**:

- `feat:` New features or pipeline additions (e.g., `feat: add scaling step`)
- `data:` Dataset updates or DVC changes (e.g., `data: add telco raw dataset`)
- `exp:` Experimental changes (e.g., `exp: try max_depth=10`)
- `fix:` Bug fixes (e.g., `fix: handle null values in TotalCharges`)
- `docs:` Documentation updates (e.g., `docs: update CONTRIBUTING.md`)
- `ci:` Continuous Integration workflow updates

---

## 🔀 Pull Request & Merge Policy
1. **Branch Protection:** No member may push directly to `dev`, `staging`, or `main`. All changes must arrive via a reviewed Pull Request (PR).
2. **Review Policy:** Every PR requires at least **1 approval** from a teammate.
3. **PR Merge Decision:** All PRs into `dev` must be **Squash-Merged** to keep integration history clean and atomic.
4. **DVC Check:** Always run `dvc push` **BEFORE** opening a `data/` or model-related PR to prevent broken data pointers.
