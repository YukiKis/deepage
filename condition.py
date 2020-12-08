# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 16:31:47 2020

@author: s1430
"""


import pandas as pd

df = pd.read_csv("sample_extract.csv")
print(df)
print(df["name"] == "Satoh")

bool_list = df["name"] == "Satoh"
print(df[bool_list])

print(df[df["name"] == "Satoh"])

print(df[df["age"] > 30])

print(df[(df["name"] == "Egawa") & (df["state"] == "Ohsaka")])

print(df[~(df["name"] == "Egawa")])

print(df[(df["name"] == "Egawa") | (df["name"] == "Satoh")])

print(df[(~(df["name"] == "Satoh") | (df["age"] > 30)) & (df["state"] == "Ohsaka")]) 

print(df.query("name == 'Satoh'"))
print(df.query("name == 'Satoh' & age > 25"))
print(df.query("~(name == 'Satoh') & age > 25"))
print(df.query("~(name == 'Satoh') | (age > 30 )"))

age = 25
print(df.query("age > @age"))

print(df.query("id in [1021, 2152]"))

df_cp = df.copy()
df_cp.query("name == 'Egawa'", inplace=True)
print(df_cp)