# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 12:45:13 2020

@author: s1430
"""


import pandas as pd
import numpy as np

a = pd.DataFrame(np.arange(20).reshape(4, 5), columns=["a", "b", "d", "e", "f"], index=[0, 2, 3, 5])
print(a)
print(a.reindex([0, 1, 2, 3, 4, 5], axis="index"))
print(a.reindex(["a", "b", "c", "d", "e", "f"], axis=1))

print(a.reindex(index=np.arange(6)))
print(a.reindex(columns=["a", "b", "c", "d", "e", "f"]))
print(a.reindex(index=[1, 7]))
print(a.reindex(index=[0, 1, 2, 3, 4, 5], columns=["a", "b", "c", "d", "e", "f"]))
b = pd.DataFrame(np.arange(20).reshape(4, 5), index=[0, 4, 5, 6], columns=["a", "e", "g", "j", "k"])

print(b)
print(b.reindex(range(10), method="ffill"))
print(b.reindex(range(20), method="bfill"))
print(b.reindex(range(10), method="nearest"))

c = b.reindex()
print(c)
c.iloc[0, 0] = 22
print(c)
print(b)

d = b.reindex(copy=False)
d.iloc[0, 0] = 22
print(d)
print(b)

b.iloc[0, 0] = 0
e = b.reindex(index=range(10), copy=False)
print(e)
e.iloc[5, 0] = 100

df = pd.read_csv("sample_reindex.csv")
print(df)
df = df.set_index(["class", "time"])
print(df)

df_new = df.mean(level="class")
print(df_new)

print(df_new.reindex(df.index, level=0))
print(df_new.reindex(df.index, level=1))

print(a.reindex(index=range(6), fill_value=-999))
print(a.reindex(index=range(100), fill_value = "missing"))

print(b.reindex(index=range(6), limit=2, method="ffill"))

print(b.reindex(index=range(10), tolerance=2, method="ffill"))
print(b.reindex(index=range(10), tolerance=[1, 1, 1, 2, 2, 2, 2, 0, 0, 0], method="ffill"))