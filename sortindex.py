# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 16:56:48 2020

@author: s1430
"""


import pandas as pd
import numpy as np

ser = pd.Series(range(6), index=[0, np.nan, -1, 2, 5, 1])
print(ser)
print(ser.sort_index())

print(ser.sort_index(ascending=False))
print(ser.sort_index(na_position="first"))
print(ser.sort_index(inplace=True))

str_ser = pd.Series(range(6), index=["a", "AA", "b", "B", "cB", "c"])
print(str_ser)
print(str_ser.sort_index())

print(str_ser.sort_index(ascending=False))

data = np.arange(25).reshape(5, 5)
df = pd.DataFrame(data, index=[0, 3, 2, 1, 9], columns=[1, 2, 4, 3, 0])
print(df)

print(df.sort_index(axis="index"))
print(df.sort_index(axis="columns"))

print(df.sort_index(axis="index", ascending=False))

df2 = pd.DataFrame(np.arange(25).reshape(5, 5), index=[0, 1, 3, np.nan, 2], columns=[0, 3, 1, np.nan, -1])
print(df2.sort_index(axis="index", na_position="first"))
print(df2.sort_index(axis="columns", na_position="first"))

multi = pd.read_csv("sample_multi.csv")
print(multi)
multi = multi.set_index(["class", "gender"])
print(multi)
print(multi.sort_index(level=0))
print(multi.sort_index(level="gender"))

print(multi.sort_index(level="gender", sort_remaining=False))
print(multi.sort_index(level="gender", sort_remaining=True))