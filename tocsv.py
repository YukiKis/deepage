# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:38:45 2020

@author: s1430
"""


import pandas as pd

df = pd.read_csv("sample_tocsv.csv", index_col=0, parse_dates=["birth"])
print(df)

df.to_csv("s1.csv")


df.to_csv("s2.csv", header=False)

df.to_csv("s3.csv", index=False)

df2 = df.reset_index()
print(df2)

df2.to_csv("s5.csv", index=False)

df.to_csv("s6.csv", columns=["name", "math"])

data = {"id": [88, 120],
        "age": [22, 21],
        "name": ["Cathy", "Ronald"],
        "math": [80, 81],
        "english": [34, 87],
        "birth": [pd.Timestamp(1995, 8, 25), pd.Timestamp(1996, 9, 4)]
        }
df_ad = pd.DataFrame(data, columns=["age", "name", "math", "english", "birth", "id"])
df_ad.set_index("id", inplace=True)
df_ad.to_csv("s1.csv", mode="a", header=False)

import sys
df.to_csv("s7.csv", sep=":")
df = pd.read_csv("sample_tocsv.csv", index_col=0, parse_dates=["birth"])
df.to_csv(sys.stdout)