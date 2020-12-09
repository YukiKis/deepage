# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 19:36:52 2020

@author: s1430
"""


import pandas as pd

sr = pd.Series([1, 12, 5, 1, 9, 3, 4, 10, 8])
print(pd.qcut(sr, 3))

print(pd.qcut(sr, 3).value_counts())
print(pd.qcut(sr, 3, labels=["low", "middle", "high"]))
print(pd.qcut(sr, 3, labels=False))
sr_cut, bins = pd.qcut(sr, 3, retbins=True)
print(sr_cut)
print(bins)
print(pd.qcut(sr, 3, precision=1))
print(pd.qcut(sr, 3, precision=4))

age_list = pd.Series([0, 20, 32, 21, 15, 40, 12, 35, 32, 39, 24, 58, 54, 19])
print(age_list)
print(pd.cut(age_list, bins=[-1, 19, 39, 59]))
print(pd.cut(age_list, bins=[-1, 19, 39, 59]).value_counts())

print(pd.cut(age_list, bins=[-1, 19, 39, 59], labels=["young", "young-adult", "adult"]))
print(pd.cut(age_list, bins=[-1, 19, 39, 59], labels=["Y", "YA", "A"]).value_counts())
print(pd.cut(age_list, bins=[-1, 19, 39, 59], labels=False))

print(pd.cut(age_list, bins=[-1, 19, 39, 59], right=False))
print(pd.cut(age_list, bins=[-1, 19, 39, 59], right=False).value_counts())
print(pd.cut(age_list, bins=[-1, 19, 39, 59], right=True).value_counts())
print(pd.cut(age_list, bins=[0, 20, 40, 60], right=False).value_counts())

score_list = np.random.randint(0, 100, size=14)
df = pd.DataFrame({"Age": age_list, "Score": score_list})
print(df)

cut = pd.qcut(df["Age"], 4)
print(cut)
print(df.groupby(cut).mean())

cut = pd.cut(df["Age"], bins=[-1, 19, 39, 59], labels=["L", "M", "H"])
print(df.groupby(cut).mean())