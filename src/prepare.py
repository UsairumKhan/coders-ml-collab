from pathlib import Path

import pandas as pd
import yaml
from sklearn.model_selection import train_test_split

from src.cleaning import clean_telco


def main() -> None:
    with open("params.yaml") as f:
        params = yaml.safe_load(f)

    seed = params["seed"]
    test_size = params["split"]["test_size"]
    out_dir = Path(params["data"]["prepared_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)

    df = clean_telco(pd.read_csv(params["data"]["raw_path"]))
    df = df.drop(columns=["customerID"])
    df["Churn"] = (df["Churn"] == "Yes").astype(int)

    train_df, test_df = train_test_split(
        df, test_size=test_size, random_state=seed, stratify=df["Churn"]
    )
    train_df.to_csv(out_dir / "train.csv", index=False)
    test_df.to_csv(out_dir / "test.csv", index=False)
    print(f"train: {train_df.shape}, test: {test_df.shape}")


if __name__ == "__main__":
    main()
