import json
import subprocess
from pathlib import Path

import joblib
import pandas as pd
import yaml
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)


def git_sha() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def code_is_dirty() -> bool:
    result = subprocess.run(
        ["git", "diff", "--quiet", "HEAD", "--", "src", "params.yaml", "dvc.yaml"]
    )
    return result.returncode != 0


def main() -> None:
    with open("params.yaml") as f:
        params = yaml.safe_load(f)

    test_df = pd.read_csv(Path(params["data"]["prepared_dir"]) / "test.csv")
    X_test = test_df.drop(columns=["Churn"])
    y_test = test_df["Churn"]

    model = joblib.load("models/model.joblib")
    pred = model.predict(X_test)
    proba = model.predict_proba(X_test)[:, 1]

    metrics = {
        "accuracy": round(accuracy_score(y_test, pred), 4),
        "precision": round(precision_score(y_test, pred), 4),
        "recall": round(recall_score(y_test, pred), 4),
        "f1": round(f1_score(y_test, pred), 4),
        "roc_auc": round(roc_auc_score(y_test, proba), 4),
        "seed": params["seed"],
        "commit_sha": git_sha(),
        "code_dirty": code_is_dirty(),
    }
    Path("metrics.json").write_text(json.dumps(metrics, indent=2) + "\n")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
