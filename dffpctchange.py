# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:14:35 2020

@author: s1430
"""


import pandas as pd
import numpy as np

df = pd.DataFrame(range(7))
print(df)
print(df.pct_change())

print(df.pct_change(periods=1))
print(df.pct_change(periods=2))

sr_a = pd.Series(range(7))
sr_a[3] = np.nan
print(sr_a)
print(sr_a.pct_change())
print(sr_a.pct_change(fill_method="bfill"))

df = pd.DataFrame({
        "A": [0, 1, 2, 3, 4, 5, 6],
        "B": [0, 4, 1, 6, 2, 35, 8]}
)

print(df.diff())
print(df.diff(axis=1))
print(df.diff(periods = 2))
print(df.diff(periods = -1))
print(df["A"].diff())

print(np.diff(df))
print(df.diff())
print(df.apply(np.diff))