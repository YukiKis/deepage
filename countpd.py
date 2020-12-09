# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 19:21:26 2020

@author: s1430
"""


import pandas as pd

df = pd.DataFrame({
        "A": [0, 2, 3, 1, 4],
        "B": ["a", "c", "e", "e", "a"]}
)
print(df.count())
df.iloc[3, 0] = None
print(df)
print(df.count())

print(df.count(axis=1))

df_2 = pd.DataFrame(range(9), index=[["A", "A", "A", "A", "A", "B", "B", "B", "B"], [1, 2, 3, 1, 2, 3, 1, 2, 3]])
print(df_2)
df_2.index.names = ["Class", "Grade"]
print(df_2)
print(df_2.count(level="Class"))
print(df_2.count(level="Grade"))

print(df.count(numeric_only=True))
df.loc[3, "B"] = 10
print(df.count(numeric_only=True))

df = pd.DataFrame({
        "class": ["a", "a", "a", "b", "b", "c"],
        "score": [0, 20, 10, 1, 3, 21]}
)
print(df)
print(df.groupby("class").count())
print(df.groupby("class").agg(["count", "sum"]))