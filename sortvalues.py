# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 16:43:48 2020

@author: s1430
"""


import pandas as pd
import numpy as np
series = pd.Series([7, 3, 1, np.nan, 0, -12.5])
print(series.sort_values())
print(series.sort_values(ascending=False))
print(series.sort_values(na_position="first"))
print(series.sort_values(na_position="last"))
print(series.sort_values(inplace=True))
print(series)

str_series = pd.Series(["a", "A", "c", "E", "f"])
print(str_series.sort_values())
print(str_series.sort_values(ascending=False))

data = {"a": [3, 1, -5, 3, 8, 1, np.nan, 0, -1],
        "b": ["a", "b", "A", "G", "k", "C", "c", "cc", "d"]
        }
df = pd.DataFrame(data)
print(df)

print(df.sort_values(by="a"))
print(df.sort_values(by="b"))

print(df.sort_values(by=["a", "b"]))
print(df.sort_values(by=["b", "a"]))

df2 = pd.DataFrame([
        [1, 3, -1, 9],
        ["a", "B", "bb", "b"]
        ], index=["sample1", "sample2"]
)
print(df2)

print(df2.sort_values(by="sample1", axis="columns"))
print(df2.sort_values(by="sample2", axis="columns"))

df.sort_values(by="a", ascending=False)
df.sort_values(by="b", ascending=False)
df.sort_values(by="a", na_position="first")
df.sort_values(by="a", inplace=True)