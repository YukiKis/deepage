# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:58:24 2020

@author: s1430
"""


import pandas as pd

df = pd.DataFrame({
        "A": [0, 1, 2, 3, 4],
        "B": ["a", "b", "c", "d", "e"]}
)
print(df)
for index, item in df.iterrows():
    print("index: ", index)
    print("item: \n", item)
    print("------\n")
    
for index, item in df.iterrows():
    print("A: ", item["A"])
    print("B: ", item["B"])
    print("---\n")
    
df_t = df.T.copy()
for label, items in df_t.iteritems():
    print("label: ", label)
    print("item: ", items)
    print("---\n")
    
df_cp = df.copy()
for index, items in df_cp.iterrows():
    df_cp.loc[index, "A"] = index * items["B"]
print(df_cp)
    
df["C"] = [0, 2, 4, 6, 8]
print(df)
for a, b in zip(df["A"], df["B"]):
    print("a: ", a)
    print("b: ", b)
    
sr = pd.Series([1, 2, 3, 4, 5])
for item in sr:
    print(item)
    print("---\n")
    
for index in sr.index:
    print(index)
    print("---\n")
    
sr = pd.Series([1, 2, 3, 4, 5])
print(sr * 100)
for index in sr.index:
    sr[index] *= 100
print(sr)

def function(x):
    if type(x) == int:
        if x > 0:
            return 1
        else:
            return 0
    else:
        return x * 2
    
print(function(df))
print(df.applymap(function))