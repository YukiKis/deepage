# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 12:17:10 2020

@author: s1430
"""


import pandas as pd
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["a", "b", "c"])
print(df)
print(df.rename({0: 11}))

print(df.rename({0: 11}, axis=0))
print(df.rename({"a": "aa"}, axis=1))
print(df.rename({"a": "aa"}, axis="columns"))

print(df.rename(index={0: 11}, columns={"a": "aa"}))

print(df.rename(lambda x: x * 2))
print(df.rename(columns= lambda x: x.upper()))

a = df.rename(index={1: 11})
b = df.rename(index={1: 11}, copy=False)

b.iloc[1, 1] = 25
print(a)
print(b)
print(df)
a.iloc[0, 1] = 33
print(a)
print(b)
print(df)

df.rename(columns={"b": "bb", "c": "C"}, inplace=True)
print(df)

df = pd.read_csv("sample_index.csv")
print(df)

multi = df.set_index(["state", "gender"])
print(multi)
print(multi.rename(index={"M": "Male", "F": "Female"}, level=1))
print(multi.rename(index= lambda x: x.upper(), level=0))