# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:03:08 2020

@author: s1430
"""


import numpy as np
n = np.amin(np.array([1, 2, 3, 2, 1]))
print(n)

a = np.array([[1.2, 1.2, 0.1, 1.5], [2.1, 0.2, 0.3, 2.0],
              [0.2, 0.5, 0.5, 2.3]])
n = np.amin(a)
print(n)

array = np.amin(a, axis=0)
print(array)

array = np.amin(a, axis=1)
print(array)

array = np.amin(a, axis=0, keepdims=True)
print(array)

b = a - np.amin(a, axis=1, keepdims=True)
print(b)

#a - np.amin(a, axis=1)

a = np.array([[1.2, 1.3, 0.1, 1.5], [2.1, 0.2, 0.3, 2.0],
[0.1, 0.5, 0.5, 2.3]])

n = a.min()
print(n)
n = a.min(axis=1)
print(n)
n = a.min(axis=0)
print(n)
array = a.min(axis=0, keepdims=True)
print(array)
array = a.min(axis=1, keepdims=True)