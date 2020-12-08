# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:06:21 2020

@author: s1430
"""


import pandas as pd
import numpy as np

df = pd.DataFrame({
        "A": [1, 2, 3, -1, 2, -2, 5],
        "B": [3, 3, 6, -5, 2, 2, -1]
        }
)

print(df)
print(df.where(df["A"] > 0, 0))
print(df.where(df > 0, 0))

print(df["A"].where(df["A"] > 0, df["B"]))
print(df["B"].where(df["A"] > 0, df["B"] * 2))

mask = [True, True, True, False, False, False, True]
print(df["A"].where(mask, 0))

masks = [[True, True],
         [False, True],
         [False, False],
         [True, True],
         [True, False],
         [True, False],
         [False, False]
         ]
print(df.where(masks, 0))

print(df.where(df > 0, np.abs(df)))

df["C"] = df["A"].copy()
df["C"].where(df["C"] < 0, 0, inplace=True)
print(df)

df["D"] = ["abc", "aaa", "abb", "acc", "bcc", "bbc", "ccc"]
print(df)

print(df["D"].where(df["D"].str.find("a") > -1, "There is no A"))

#print(np.where(df>2, 1, 0))
