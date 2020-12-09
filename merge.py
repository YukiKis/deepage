# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:11:30 2020

@author: s1430
"""


import pandas as pd

df1 = pd.DataFrame({
        "data1": range(6),
        "key": ["A", "B", "B", "A", "C", "A"]
        })
df2 = pd.DataFrame({
        "data2": range(2),
        "key": ["A", "B"]
        })
print(pd.merge(df1, df2))
print(df1.merge(df2))

df3 = pd.DataFrame({
        "data1": range(6),
        "key": ["A", "B", "C", "A", "B", "C"]
        })
df4 = pd.DataFrame({
        "data2": range(3),
        "key": ["A", "C", "D"]
        })
print(pd.merge(df3, df4, how="inner"))
print(pd.merge(df3, df4, how="outer"))
print(pd.merge(df3, df4, how="left"))
print(pd.merge(df3, df4, how="right"))

df5 = pd.DataFrame({
        "data1": range(6),
        "key1": ["A", "B", "A", "B", "A", "B"],
        "key2": [0, 0, 0, 1, 1, 1]
        })
df6 = pd.DataFrame({
        "data2": range(3),
        "key1": ["A", "B", "A"],
        "key2": [1, 1, 0]
        })
print(pd.merge(df5, df6, on="key1"))
print(pd.merge(df5, df6, on="key2"))

df5_2 = df5.set_index(["key1"])
df6_2 = df6.set_index(["key1"])

print(df5_2)

print(pd.merge(df5_2, df6_2, on="key1"))
print(pd.merge(df5, df6, left_index=True, right_index=True))
print(pd.merge(df5, df6, on=["key1", "key2"]))

df5.columns = ["data1", "lkey1", "lkey2"]
df6.columns = ["data2", "rkey1", "rkey2"]
print(pd.merge(df5, df6, left_on="lkey1", right_on="rkey1"))
print(pd.merge(df5, df6, left_on=["lkey1", "lkey2"], right_on=["rkey1", "rkey2"]))

df7 = pd.DataFrame({
        "data1": range(6),
        "key1": ["A", "B", "A", "B", "A", "B"],
        "key2": [0, 0, 0, 1, 1, 1]
        })
df8 = pd.DataFrame({
        "data1": range(3),
        "key1": ["A", "A", ""],
        "key2": [1, 1, 0]
        })

print(pd.merge(df7, df8, suffixes = ["_l", "_r"], on="key1"))
