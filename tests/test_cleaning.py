import pandas as pd
from src.cleaning import clean_telco


def test_blank_total_charges_becomes_zero():
    df = pd.DataFrame({"TotalCharges": ["29.85", " ", "1889.5"]})
    out = clean_telco(df)
    assert out["TotalCharges"].dtype == "float64"
    assert out["TotalCharges"].tolist() == [29.85, 0.0, 1889.5]


def test_does_not_mutate_input():
    df = pd.DataFrame({"TotalCharges": [" "]})
    clean_telco(df)
    assert df["TotalCharges"].iloc[0] == " "
