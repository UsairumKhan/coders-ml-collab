from pathlib import Path

import joblib
import pandas as pd
import yaml
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def main() -> None:
    with open("params.yaml") as f:
        params = yaml.safe_load(f)

    seed = params["seed"]
    cfg = params["train"]
    assert cfg["model"] == "random_forest", "only random_forest is supported"

    train_df = pd.read_csv(Path(params["data"]["prepared_dir"]) / "train.csv")
    X = train_df.drop(columns=["Churn"])
    y = train_df["Churn"]

    categorical = X.select_dtypes(exclude="number").columns.tolist()
    preprocess = ColumnTransformer(
        [("cat", OneHotEncoder(handle_unknown="ignore"), categorical)],
        remainder="passthrough",
    )
    model = RandomForestClassifier(
        n_estimators=cfg["n_estimators"],
        max_depth=cfg["max_depth"],
        random_state=seed,
    )
    pipeline = Pipeline([("preprocess", preprocess), ("model", model)])
    pipeline.fit(X, y)

    Path("models").mkdir(exist_ok=True)
    joblib.dump(pipeline, "models/model.joblib")
    print("saved models/model.joblib")


if __name__ == "__main__":
    main()
