# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 12:27:07 2020

@author: s1430
"""


import pandas as pd
import numpy as np

df = pd.DataFrame({"A": np.random.rand(10),
                   "B": np.random.rand(10)
                   })
print(df)
print(np.exp(df))

print(np.sum(df))
print(np.sum(df["A"]))

print(np.cumsum(df))
print(np.cumsum(df["A"]))
print(np.sum(df, axis=1))
print(np.cumsum(df, axis=1))
df.iloc[4, :] = np.nan
print(np.sum(df))

def func(x):
    return x * 2

print(func(df))

def func2(x):
    return x ** 2 + 4 * x -1

func2(df)

df_str = pd.DataFrame({"A": ["I do not have a cake", "i am hungry"],
                       "B": ["He does not have a cake", "He is hungry"]})
print(df_str["A"].str.replace("not", ""))

f = lambda x: (x - x.min()) / (x.max() - x.min())
print(df.apply(f))
print(f(df))

def function(dataframe):
    return dataframe.max() - dataframe.min()

print(df.apply(function))
print(function(df))

print(df.apply(function, axis=1))

df_2 = pd.DataFrame({"data1": np.random.randn(10),
                     "data2": np.random.randn(10)
                     })
f = lambda x: "大" if x > 0 else "小"
print(df_2.applymap(f))
#print(f(df_2))

print(df_2["data1"].map(f))

train = pd.read_csv("train.csv")
train.info()

def stats(s):
    return {"Mean": s.maen(), "Max": s.max(), "Min": s.min(), "Count": s.count()})

train.groupby(["Sex", "Pclass"])["SibSp"].apply(stats)

train.groupby(["Sex"], ["Pclsas"])["SibSp"].apply(stats).unstack()

f = lambda x: x.std()
train.groupby(["Sex", "Pclass"])["SibSp"].apply(f)