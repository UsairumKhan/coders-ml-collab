import pandas as pd


def clean_telco(df: pd.DataFrame) -> pd.DataFrame:
    """Convert TotalCharges to numeric; blanks (tenure == 0) become 0."""
    df = df.copy()
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce").fillna(0)
    return df
