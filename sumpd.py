# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:57:51 2020

@author: s1430
"""


import pandas as pd
import numpy as np

df = pd.DataFrame({"A": [0, 1, 2, 3, 4, 5],
                   "B": [0, 1, 2, None, 4, 5],
                   "C": ["a", "b", "c", "d", "e", "f"]}
)
print(df)
print(df.sum())
print(df["A"].sum())
print(df.sum(axis=1))
print(df.sum(skipna=False))

df_nan = df.copy()
df_nan.iloc[:3, 0] = None
print(df_nan.sum(min_count=4))
print(df_nan.sum(min_count=3))

print(df.sum())
print(df.sum(numeric_only=True))

data = np.random.randint(10, size=(5, 5))
df_multi = pd.DataFrame(data, index = [["A", "A", "A", "B", "B"], ["a", "b", "a", "b", "a"]])
print(df_multi)
print(df_multi.sum())
print(df_multi.sum(level=0))
print(df_multi.sum(level=1))