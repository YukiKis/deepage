# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 18:01:26 2020

@author: s1430
"""

import pandas as pd

a = pd.Series([1, 2, 3])
print(a)
array = [1., 2., 3.]
b = pd.Series(array)
print(b)

import numpy as np
np_array = np.array([1, 2, 3])
c = pd.Series(np_array)
print(c)

dic = {"Tokyo": 100, "Osaka": 250, "Nagoya": 300 }
d = pd.Series(dic)
print(d)

e = pd.Series(1)
print(e)

f = pd.Series(["A", "B", "C"])
print(f)

g = pd.Series(["A", 1, 1.0, None])
print(g)

series = pd.Series([1, 2, 3, 4, 5])
print(series)

print(series.index)

series2 = pd.Series(np.arange(6), index=np.arange(6))
print(series2)
print(series2.index)

series3 = pd.Series([5, 4, 3, 2, 1], index=["a", "b", "c", "d", "e"])
print(series3)
print(series3.index)

dic2 = {"a": 5, "b": 4, "c": 3, "d": 2, "e": 1}
series4 = pd.Series(dic2)
print(series4)
print(series4.index)

print(series2)

series2.index = ["A", "B", "C", "D", "E", "F"]
print(series2)
print(series2.index)

series5 = pd.Series(dic2, index=["a", "c", "e", "f"])
print(series5)

array2 = [20, 0, 0, 0, 0]
series6 = pd.Series(array2)
print(series6)
series7 = pd.Series(series6, copy=False)
series8 = pd.Series(series6, copy=True)
print(series7)
series7[0] = 11
print(series7)
print(series6)

print(series8)
series6[0] = 100
print(series6)
print(series7)
print(series8)

series9 = series6.copy()
print(series9)

print(series[0])
print(series[0:2])
print(series[series % 2 == 0])

print(series3)
print(series3["a"])
print(series3[["a", "c"]])

print(series + 1)
print(series + pd.Series([1, 1, 2, 2, 2]))
print(series * 2)

print(series.sum())
print(series.std())

np.sum(series)
np.log(series)

series = pd.Series([0, 0, 0, 0, 0])
series[7] = 10
print(series)
series["a"] = 11
print(series)
series["a"] = 100
print(series)

date = pd.date_range("2018/11/11", periods = 10, freq = "D")
print(date)
date_series = pd.Series(date)
date_series2 = pd.Series(np.random.rand(10), index=date)

a = pd.Series([1, 2, 3, 4, 5])
print(a.T)
#print(a.asobject)
b = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
print(b.at["b"])
print(b.axes)
print(b.index)

f = [2, 3, 1, 2, 3]
c = pd.Series(f)
print(c)
#print(c.base)
#print(c.blocks)

#print(c.data)
print(c.dtype)
print(c.dtypes)
#print(c.flags)

random_array = np.random.randn(1000000)
random_series = pd.Series(random_array)
random_series.at[99000] = np.nan
print(random_series.hasnans)
print(random_series.isnull().any())

import time
time1 = time.time()
random_series.hasnans
time1 = time.time() - time1
time2 = time.time()
random_series.isnull().any()
time2 = time.time() - time2
print(time1, time2)

b.iat[1]
b.iloc[1]

print(b.index)
print(b)
print(b.is_monotonic)
print(b.is_monotonic_decreasing)
print(b.is_monotonic_increasing)

print(b.is_unique)
b[1] = 1
print(b.is_unique)
#print(b.itemsize)
print(b.ndim)
print(b.shape)
print(b.size)
print(len(b))

#print(b.strides)
print(b.values)
empty_series = pd.Series()
print(empty_series.empty)
print(b.empty)

name_series = pd.Series([1, 2, 3], name="Name")
print(name_series.name)
print(b.name)

array = np.array([1 + 2j, -2 + 3j, -1-4j])
imag_array = pd.Series(array)
#print(imag_array.real)
