# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 23:36:59 2020

@author: s1430
"""


import pandas as pd
df = pd.read_csv("sample_index.csv")
print(df)

print(df.set_index("state"))

print(df.set_index(["state", "age"]))

print(df.set_index(["state"], drop=False))

print(df.set_index(["state"], append=True))

print(df.set_index(["state"], inplace=True))
print(df)

print(df.set_index(["age"], verify_integrity=True))