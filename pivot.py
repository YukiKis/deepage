# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:08:14 2020

@author: s1430
"""


import pandas as pd
df = pd.read_csv("pivot_sample.csv")
print(df)

print(df.pivot(index="class", columns="state", values="name"))
print(df.pivot(index="class", columns="state"))
print(df.pivot(columns="state", values="name"))