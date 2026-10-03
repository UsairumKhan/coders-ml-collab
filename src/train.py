import os

import pandas as pd


def train_model():
    # Use relative path from root
    data_path = os.path.join("data", "raw", "WA_Fn-UseC_-Telco-Customer-Churn.csv")

    if not os.path.exists(data_path):
        print(f"Dataset not found at {data_path}")
        return

    df = pd.read_csv(data_path)
    print(f"Dataset loaded successfully. Shape: {df.shape}")


if __name__ == "__main__":
    train_model()
