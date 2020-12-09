# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:47:31 2020

@author: s1430
"""


import pandas as pd
import numpy as np

df = pd.DataFrame({
        "A": range(6),
        "B": [0.0, 1.0, 2.0, np.nan, 4.0, 5.0],
        "C": ["a", "b", "c", "d", "e", "f"]}
)
print(df)
print(df.mean())
print(df.mean(axis=1))
print(df.mean(axis="columns"))
print(df.mean(skipna=False))

df["D"] = ["1", "2", "3", "4", "5", "6"]
print(df)
print(df.mean())
print(df.mean(numeric_only=True))

df_multi = pd.DataFrame([
        [5, 2, 2, 4, 1],
        [8, 1, 6, 0, 4],
        [3, 6, 6, 2, 6],
        [0, 5, 0, 9, 5],
        [0, 4, 1, 9, 0]],
        columns=range(5),
        index=[["A", "A", "A", "B", "B"], ["a", "b", "a", "b", "a"]]
        )
print(df_multi)
print(df_multi.mean(level=0))
print(df_multi.describe().unstack())