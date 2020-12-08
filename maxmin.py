# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:39:32 2020

@author: s1430
"""


import pandas as pd

df = pd.DataFrame({
        "A": [1, -1, 0, 9, 8, 1, -10],
        "B": [-1 , 0, 7, 6, 1, 3, 2],
        "C": ["A", "B", "C", "D", "c", "a", "b"]
        })

print(df.describe())
print(df["A"].describe())

print(df.max())
print(df["A"].sort_values())
print(df["B"].sort_values())
print(df["C"].sort_values())

print(df.max(axis=0))
print(df.max(axis=1))

import numpy as np

df.iloc[3, 0] = np.nan
df.iloc[3, 2] = np.nan

print(df)
print(df.max())
print(df.max(skipna=False))

df["C"] = df["C"].fillna("Missing")
print(df)

print(df.max(numeric_only=True))
print(df.max(numeric_only=False))

df.columns = pd.MultiIndex.from_tuples([("foo", 0), ("foo", 1), ("bar", 1)], names=["A", "B"])
print(df)

print(df.max(axis=1))
# print(df.max(axis=1, level="A"))
# print(df.max(axis=1, level="B"))

df = pd.DataFrame({
        "A": [1, -1, 0, 9, 8, 1, -10],
        "B": [-1, 0, 7, 6, 1, 3, 2],
        "C": ["A", "B", "c", "D", "C", "a", "b"]
        })
print(df)
print(df.min())
print(df.min(axis=0))
print(df.min(axis=1))

df.iloc[3, 0] = np.nan
df.iloc[3, 2] = np.nan

print(df)
print(df.min())
print(df.min(skipna=False))

df["C"] = df["C"].fillna("missing")
print(df)
print(df.min(numeric_only=True))
print(df.min(numeric_only=False))

df.columns = pd.MultiIndex.from_tuples([("foo", 0), ("foo", 1), ("bar", 1)], names=["A", "B"])
print(df)

print(df.min(axis=1))
#print(df.min(axis=1, level="A"))
#print(df.min(axis=1, level="B"))