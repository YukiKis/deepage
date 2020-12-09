# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 22:44:24 2020

@author: s1430
"""


import pandas as pd
sr = pd.Series(["A", "A", "B", "A", "C"])
print(pd.get_dummies(sr))

df = pd.DataFrame({
        "col1": ["A", "B", "A", "D", "A"],
        "col2": ["B", "C", None, "B", "D"]})

print(df)
print(pd.get_dummies(df))

print(pd.get_dummies(df, columns=["col1"]))
print(pd.get_dummies(df, columns=["col2"]))

print(pd.get_dummies(df["col2"], dummy_na=True))

print(pd.get_dummies(sr, drop_first=True))

print(pd.get_dummies(df["col2"], drop_first=True))
print(pd.get_dummies(df["col2"], drop_first=True, dummy_na=True))

print(pd.get_dummies(df, prefix="data"))
print(pd.get_dummies(df, prefix=["one", "two"]))