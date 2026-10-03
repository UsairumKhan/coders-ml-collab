# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import sys

sys.path.insert(0, "..")

import pandas as pd

from src.cleaning import clean_telco

# %%
df = pd.read_csv("../data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")
print(df.shape)
df.head()

# %%
df.info()
df.isna().sum()

# %%
df[df["TotalCharges"].str.strip() == ""][["customerID", "tenure", "TotalCharges"]]

# %%
df = clean_telco(df)
df["TotalCharges"].describe()

# %%
df["Churn"].value_counts(normalize=True)

# %%
df.groupby("Contract")["Churn"].apply(lambda s: (s == "Yes").mean())

# %%
