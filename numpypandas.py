# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:01:32 2020

@author: s1430
"""


import pandas as pd

#df = pd.read_csv("titanic.csv")
#df = df.dropna()
#pd.pivot_table(df, values="survived", index="sex", columns="age")
#df.gropuby("survived").mean()

import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(10, 10) * np.arange(10).reshape(-1, 10))
df.plot()
plt.show()

a = np.random.randn(10, 10) * np.arange(10).reshape(-1, 10)
plt.plot(a)
plt.show()

a = np.random.randn(10000)
b = pd.DataFrame(a)

import time
time1 = time.time() 
a.mean()
time1 = time.time() - time1
time2 = time.time()
b.mean()
time2 = time.time() - time2
print(time1, time2)

array = np.arange(10)
series_sample = pd.Series(array)
array2 = np.arange(20).reshape(4, 5)
df_sample = pd.DataFrame(array2)
print(series_sample)
print(df_sample)

df_sample2 = pd.DataFrame(array2, index=np.linspace(0, 10, 4))
print(df_sample2)

a = {"class": ["a", "b", "c", "c", "b", "c", "a"], "grade": [0, 1, 3 , 2, 1, 4, 5]}
df = pd.DataFrame(a)

array1 = df.values
print(array1)
#print(array1.mean())

array2 = df["grade"].values
print(array2)
print(array2.mean())

dummies = pd.get_dummies(df)
print(dummies)

dummies_array = dummies.iloc[:, 1:].values
print(dummies_array)
print(dummies_array.sum(axis=0))