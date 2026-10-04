# 🚀 Git-Based Collaboration for an ML Project

## 📊 Telco Customer Churn Prediction & Pipeline

This repository implements a production-grade, end-to-end Machine Learning pipeline built with strict team collaboration guardrails using **Git, DVC, DagsHub, and GitHub Actions**.

---

## 👥 Team Members & Roles

| Name | Role | Core Focus |
| :--- | :--- | :--- |
| **Usairum Khan** | **Platform Owner** | Repository scaffolding, pre-commit guardrails, GitHub Actions CI workflow, branch protections, release orchestration |
| **Muhammad Mujtaba** | **Data Owner** | DVC dataset versioning, DagsHub remote integration, dataset schema checks, exploratory data analysis |
| **Abdul Muneeb** | **Model Owner** | ML pipeline architecture (`prepare`, `train`, `evaluate`), hyperparameter tuning experiments, model evaluation |

---

## 🌟 Key Architecture & Features

- 🌿 **Structured Branching Model:** Multi-environment strategy (`dev` $\rightarrow$ `staging` $\rightarrow$ `main`) with short-lived `feat/` and `data/` branches.
- 🛡️ **Pre-commit Guardrails:** Automated linting (`ruff`), notebook cell-output stripping (`nbstripout`), 1 MB file size limit, and secret scanning (`detect-secrets`).
- 📦 **Data & Model Versioning (DVC):** Raw dataset and trained model weights versioned outside Git using **DagsHub** remote storage.
- 🧪 **Automated CI/CD (GitHub Actions):** 4-job CI workflow running lint checks, unit tests (`pytest`), dataset schema verification, and end-to-end smoke training runs.
- 📊 **Reproducible Pipeline:** Deterministic execution using `params.yaml` and `dvc.yaml` tracking commit SHAs and metric artifacts.

---

## 📈 Production Model Performance (`model-v1.0`)

| Metric | Score |
| :--- | :---: |
| **Accuracy** | **`80.62%`** |
| **F1 Score** | **`0.5832`** |
| **ROC AUC** | **`0.8432`** |
| **Precision** | **`0.6797`** |
| **Recall** | **`0.5107`** |

*Promoted Random Forest Model (`n_estimators=200`, `max_depth=8`).*

---

## 🛠️ Quickstart & Reproduction Guide

To reproduce the exact production model results from scratch:

```bash
# 1. Clone the repository
git clone https://github.com/UsairumKhan/coders-ml-collab.git
cd coders-ml-collab

# 2. Checkout the release tag
git checkout model-v1.0

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install pre-commit hooks
python -m pre-commit install

# 5. Pull versioned data and reproduce pipeline
dvc pull
dvc repro
```

---

## 📂 Repository Structure

```text
.
├── .github/
│   ├── workflows/ci.yml           # GitHub Actions CI workflow
│   └── pull_request_template.md   # Automated PR review checklist
├── .pre-commit-config.yaml         # Code quality & secret scanner hooks
├── configs/                        # Environment configurations
├── data/                           # Data storage (Tracked by DVC)
│   └── raw/
├── models/                         # Model artifacts (Tracked by DVC)
├── notebooks/                      # EDA analysis (paired with Jupytext)
├── src/                            # Modular Python code
│   ├── cleaning.py                 # Feature engineering & cleaning
│   ├── prepare.py                  # Dataset splitting stage
│   ├── train.py                    # Model training stage
│   └── evaluate.py                 # Evaluation & metrics logging
├── tests/                          # Unit tests (pytest)
├── CONTRIBUTING.md                 # Branch rules & Conventional Commits policy
├── dvc.yaml                        # DVC pipeline stage definition
├── params.yaml                     # Hyperparameters & split settings
├── README.md                       # Project landing documentation
└── REPORT.md                       # Full assignment report & evidence links
```

---

## 📄 Complete Project Report
For detailed experiment comparison tables (`dvc exp show`), reproducibility tables, evidence links, and team retrospective, check out **[REPORT.md](REPORT.md)**.
