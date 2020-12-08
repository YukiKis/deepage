# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 12:36:49 2020

@author: s1430
"""


import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(20).reshape(5, 4), index=["Tokyo", "Osaka", "Fukuoka",
                  "Nagano", "Nara"], columns=["A", "B", "C", "D"])

print(df)
print(df.loc["Tokyo", "B"])
print(df.loc["Osaka":"Nara", "B"])
print(df.loc["Fukuoka", "B":"D"])
print(df.loc["Osaka":"Nagano", "A": "C"])
print(df.loc[:, "D"])

print(df.iloc[0, 1])
print(df.iloc[1:4, 0])
print(df.iloc[2, 1:])
print(df.iloc[1:4, 0:3])
print(df.iloc[:, 3])

#print(df.at[["Fukuoka", "Narano"], "D"])
print(df.loc["Nara", "A"])