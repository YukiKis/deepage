# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:39:55 2020

@author: s1430
"""


import pandas as pd

df = pd.DataFrame({
        "A": [0, 1, 2, 3, 4, 5],
        "B": [6, 7, 8, 9, 10, 11],
        "C": [12, 13, 14, 15, 16, 17]}
)
print(df.drop(0))
print(df.drop([1, 2]))

df.index = ["a", "b", "c", "d", "e", "f"]
print(df)
print(df.drop("f"))
print(df.drop(index="f"))
print(df.drop(index=["c", "f"]))

print(df.drop("A", axis=1))
print(df.drop(["A", "C"], axis="columns"))
print(df.drop(columns=["A", "C"]))
print(df.drop(columns="A"))

print(df.drop(index="a", columns="B"))
print(df.drop(index=["d", "f"], columns=["A", "C"]))

df_2 = df.copy()
df_2.drop("a", inplace=True)
print(df.drop(index=["a", "c"], inplace=True))

del df["A"]
#del df["b"]