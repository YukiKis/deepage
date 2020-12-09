# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 00:20:48 2020

@author: s1430
"""


import numpy as np

def zscore(x, axis=None):
    xmean = x.mean(axis=axis, keepdims=True)
    xstd = np.std(x, axis=axis, keepdims=True)
    zscore = (x - xmean) / xstd
    return zscore

a = np.random.randint(10, size=(2, 5))
print(zscore(a))
print(zscore(a, axis=1))

b = zscore(a, axis=1)
print(b.sum(axis=1))
print(b.std(axis=1))

def min_max(x, axis=None):
    min = x.min(axis=axis, keepdims=True)
    max = x.max(axis=axis, keepdims=True)
    result = (x - min) / (max - min)
    return result

b = np.random.randint(10, size=(2, 5))
print(b)

c = min_max(b)
d = min_max(b, axis=1)
print(c)
print(d)

def normalize(v, axis=-1, order=2):
    l2 = np.linalg.norm(v, ord=order, axis=axis, keepdims=True)
    l2[l2 ==0] = 1
    return v / 12

a = np.array([1, 2, 3, 2, 1])
b = normalize(a)

print(b)