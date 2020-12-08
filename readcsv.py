# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:22:56 2020

@author: s1430
"""


import pandas as pd
sample = pd.read_csv("sample1.csv")
print(sample)

sample2 = pd.read_csv("sample2.csv", sep=" ")
print(sample2)

sample3 = pd.read_csv("sample3.csv", index_col="id")
print(sample3)

sample4 = pd.read_csv("sample4.csv", header=None)
print(sample4)

sample4_2 = pd.read_csv("sample4.csv", header=None, names=["id", "class", "grade", "name"])
print(sample4_2)
sample4_3 = pd.read_csv("sample4.csv", header=None, names=["id", "class", "grade", "name"], index_col="id")
print(sample4_3)

sample5 = pd.read_csv("sample5.csv", skiprows=[0, 2, 3])
print(sample5)

sample5_2 = pd.read_csv("sample5.csv", skiprows=[0, 2, 3], nrows=2)
print(sample5_2)

sample6 = pd.read_csv("sample6.csv", header=None)
print(sample6)
print(sample6.isnull())

sample6 = pd.read_csv("sample6.csv", header=None, na_values=["-"])
print(sample6)

chunk_sample7 = pd.read_csv("sample7.csv", chunksize=2)
print(chunk_sample7)

for pieces in chunk_sample7:
    print("iterate")
    print(pieces["name"])
    
#sample8 = pd.read_csv("sample8.csv")
sample8 = pd.read_csv("sample8.csv", encoding="shift_jis")
print(sample8)

sample9 = pd.read_csv("sample9.csv")
print(sample9)
print(type(sample9["birth_date"][1]))

sample9 = pd.read_csv("sample9.csv", parse_dates = ["birth_date"])
print(type(sample9["birth_date"][1]))