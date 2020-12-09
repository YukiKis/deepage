# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:08:36 2020

@author: s1430
"""


import pandas as pd
df1 = pd.DataFrame({
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"]},
        index=[0, 1, 2, 3]
)

df2 = pd.DataFrame({
        "A": ["A4", "A5", "A8"],
        "C": ["C4", "C5", "C6"]},
        index=[4, 5, 6]
)

print(pd.concat([df1, df2]))

df3 = pd.DataFrame({"C": ["C0", "C1", "C2", "C4"],
                    "D": ["D0", "D1", "D2", "D4"]},
                    index=[0, 1, 2, 4]
)
print(pd.concat([df1, df3], axis=1))

df4 = pd.DataFrame({
        "A": ["A0", "A1", "A3"],
        "B": ["B0", "B1", "B3"]},
        index=["K0", "K1", "K3"]
)
df5 = pd.DataFrame({
        "A": ["A2", "A4", "A5"],
        "B": ["B2", "B4", "B5"]}, index=["L0", "L1", "L2"]
)

print(pd.concat([df4, df5], ignore_index=True))
print(pd.concat([df1, df3], axis="columns", ignore_index=True))
print(pd.concat([df1, df2], keys=["df1", "df2"]))
print(pd.concat([df1, df3], axis=1, keys=["df1", "df3"]))
print(pd.concat([df1, df2], join="inner"))
print(pd.concat([df1, df3], join="inner", axis=1))
print(pd.concat([df1, df2], join_axes=[df1.columns]))