"""Create a small synthetic Telco-like dataset for CI smoke runs.

Refuses to run if the real CSV already exists, so it can never overwrite the
DVC-tracked dataset on a developer machine.
"""

from pathlib import Path

import numpy as np
import pandas as pd

RAW_PATH = Path("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")
N_ROWS = 300


def main() -> None:
    if RAW_PATH.exists():
        print(f"{RAW_PATH} already exists, not overwriting it.")
        return

    rng = np.random.default_rng(0)
    tenure = rng.integers(0, 72, N_ROWS)
    monthly = rng.uniform(20, 120, N_ROWS).round(2)
    total = (tenure * monthly).round(2).astype(str)
    total[tenure == 0] = " "  # mimic the blank TotalCharges in the real data

    def pick(options: list[str]) -> np.ndarray:
        return rng.choice(options, N_ROWS)

    internet_addon = ["Yes", "No", "No internet service"]
    df = pd.DataFrame(
        {
            "customerID": [f"ID_{i}" for i in range(N_ROWS)],
            "gender": pick(["Male", "Female"]),
            "SeniorCitizen": rng.integers(0, 2, N_ROWS),
            "Partner": pick(["Yes", "No"]),
            "Dependents": pick(["Yes", "No"]),
            "tenure": tenure,
            "PhoneService": pick(["Yes", "No"]),
            "MultipleLines": pick(["Yes", "No", "No phone service"]),
            "InternetService": pick(["DSL", "Fiber optic", "No"]),
            "OnlineSecurity": pick(internet_addon),
            "OnlineBackup": pick(internet_addon),
            "DeviceProtection": pick(internet_addon),
            "TechSupport": pick(internet_addon),
            "StreamingTV": pick(internet_addon),
            "StreamingMovies": pick(internet_addon),
            "Contract": pick(["Month-to-month", "One year", "Two year"]),
            "PaperlessBilling": pick(["Yes", "No"]),
            "PaymentMethod": pick(
                [
                    "Electronic check",
                    "Mailed check",
                    "Bank transfer (automatic)",
                    "Credit card (automatic)",
                ]
            ),
            "MonthlyCharges": monthly,
            "TotalCharges": total,
            "Churn": np.where(rng.random(N_ROWS) < 0.27, "Yes", "No"),
        }
    )

    RAW_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(RAW_PATH, index=False)
    print(f"wrote {len(df)} sample rows to {RAW_PATH}")


if __name__ == "__main__":
    main()
