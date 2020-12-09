# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:24:57 2020

@author: s1430
"""


import pandas as pd
import numpy as np

data = np.random.randn(5, 5)
data[1, 3] = np.nan
data[2, 0] = np.nan
print(data)
df = pd.DataFrame(data, columns=["A", "B", "C", "D", "E"])
print(df)

print(df.isnull().any())
print(df.notnull().all())

df = pd.Series([1, 2, 3, np.nan, 0, None], index = ["A", "B", "C", "D", "E", "F"])
print(df)
print(df.dropna())

df_2 = pd.DataFrame({
        "A": [0, 1, np.nan, 2],
        "B": [np.nan, 2, 3, 4]}
)
print(df_2)
print(df_2.dropna())

df = pd.DataFrame({
        "A": [1, np.nan, 2, np.nan, 2, np.nan],
        "B": [np.nan, np.nan, 3, 4, 5, 6]}
)
print(df.dropna(how="all"))
print(df.dropna(subset=["A"]))

df_copy = df.copy()
print(df_copy.dropna(inplace=True))
print(df_copy)

df = pd.DataFrame({
        "A": [0, np.nan, np.nan, 2, 3, 4],
        "B": [np.nan, np.nan, 2, 3, 5, 6],
        "C": [1, np.nan, np.nan, 3, 4, np.nan]}
)
print(df.dropna(thresh=2))

df_t = df.T
print(df_t.dropna(axis="columns"))

print(df.fillna(0))
print(df.fillna("missing"))
print(df.fillna({"A": -10, "B": 0, "C": 000}))

df_method = df.copy()
df_method.iloc[3:, 1] = np.nan
print(df_method)

print(df_method.fillna(method="ffill"))
print(df_method.fillna(method="bfill"))

print(df_method.fillna(method="ffill", limit=2))
print(df_method.fillna(method="ffill", limit=1))

print(df.fillna(np.mean(df)))
print(df.fillna(df.median()))
print(df.fillna(df.mode()))

fill_df = pd.DataFrame(np.arange(18).reshape(6, 3), columns=["A", "B", "C"])
print(df.fillna(fill_df))