# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:50:11 2020

@author: s1430
"""


import pandas as pd

print(pd.__version__)

sample = pd.read_csv("sample_unique.csv", index_col=0)
print(sample)

# print(sample.unique())

a = sample["age"].unique()
print(a)

a = sample["state"].unique()
print(a)

a = sample["id"].unique()
print(a)

import numpy as np
a = sample["age"].unique()
print(np.sort(a))

print(sample.index.unique())

print(pd.unique([0, 1, 2, 2, 1]))
print(pd.unique((1, 2, 1, 1, 2, 1, 1, 0)))
print(pd.unique(["Satou", "Satou", "Arakawa", "Takahashi"]))

print(pd.unique(sample["age"]))
print(pd.unique(sample["id"]))

print(pd.unique(sample.index))