# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 23:07:35 2020

@author: s1430
"""


import pandas as pd
a = pd.DataFrame([[1, 1, 1], [2, 1, 2], [3, 2, 3]], index=["one", "two", "three"], columns=["a", "b", "c"])
print(a)

print(a.index, a.columns)

a.rename(index={"two": "eight"}, columns={"b": "BB"}, inplace=True)
print(a)

a.rename(columns={"BB": "b"}, inplace=True)
print(a)

print(a[:1])
print(a[1:])
print(a.index[1:])

print(a.stack())
print(a.unstack())

import numpy as np

df = pd.DataFrame(np.arange(20).reshape(4, 5), index=[0, 2, 4, 5], columns=["a", "c", "d", "f", "g"])
print(df)

index = pd.Index([0, 2, 4, 5])
columns = pd.Index(["a", "c", "d", "f", "g"])
df = pd.DataFrame(np.arange(20).reshape(4, 5), index=index, columns=columns)
print(df)

print(index)
print(columns)

df = pd.DataFrame(np.arange(20).reshape(4, 5), index=range(4), columns=columns)
print(df)

a = pd.DataFrame(np.arange(20).reshape(4, 5), index=[0, 2, 4, 5], columns=["a", "c", "d", "f", "g"])
print(a)
print(a.reindex(range(6)))
print(a.reindex([0, 3, 2, 1, 4, 0]))
print(a.reindex(columns=["a", "b", "c", "d", "e", "F", "g"]))
print(a.reindex(index=range(6)))
print(a.reindex(index=range(6), method="ffill"))
print(a.reindex(index=range(6), method="bfill"))

print(a.rename(columns={"a": "AA"}))
print(a.rename(index={0:22}))

df = pd.read_csv("sample_index.csv")
print(df)
print(df.set_index(["state"]))
df_2 = df.set_index(["state"])
print(df_2.set_index(["age"], append=True))
print(df_2.reset_index())

print(df_2.transpose())
print(df_2.T)