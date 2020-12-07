# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 23:55:20 2020

@author: s1430
"""


import pandas as pd
df = pd.read_csv("sample_index.csv")
print(df)

df.set_index("state", inplace=True)
print(df)
print(df.reset_index())
print(df.reset_index(drop=True))

multi_ind = df.set_index("gender", append=True)
print(multi_ind)
print(multi_ind.reset_index())
print(multi_ind.reset_index(level="gender"))
print(multi_ind.reset_index(level=1))
print(multi_ind.reset_index(level=0))

triple_ind = df.set_index(["gender", "age"], append=True)
print(triple_ind)

print(triple_ind.reset_index(["state", "gender"]))
triple_ind.reset_index("state", inplace=True)
print(triple_ind)

index = pd.MultiIndex.from_tuples([("bird", "falcon"), ("bird", "parrot"), ("mammal", "lion"), ("mammal", "monkey")], names=["class", "name"])
columns = pd.MultiIndex.from_tuples([("speed", "max"), ("species", "type")])
import numpy as np
df = pd.DataFrame([(389.0, "fly"), (24.0, "fly"), (80.5, "run"), (np.nan, "jump")], index=index, columns=columns)
print(df)

df[("speed", "mean")] = [200.0, 12.0, 40.0, 15.0]
print(df)

df = df.sort_index(axis="columns", level=0)
print(df)

print(df.reset_index(level="class", col_level=1))

print(df.reset_index(level="class", col_level=1, col_fill="species"))