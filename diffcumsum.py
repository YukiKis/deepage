# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:51:46 2020

@author: s1430
"""


import numpy as np

a = np.array([1, 2, 4, 1, 6, 8, 3])
print(np.diff(a, n=1))
#print(np.diff(a, n=2))
#print(np.diff(a, n=3))
#print(np.diff(a, n=4))

b = np.random.randint(10, size=(5, 5))
print(b)
print(np.diff(b, axis=0))
print(np.diff(b, axis=1))
#print(np.diff(b, axis=1, n=2))

a = np.random.randint(10, size=20)
print(a)
print(np.cumsum(a))
print(a.cumsum())

print(np.cumsum(a, dtype="float32"))
print(a.cumsum(dtype="float32"))

b = np.random.rand(3, 4) * 10
print(b)

c = np.random.randint(10, size=10, dtype="int8")
print(c, c.dtype)
print(c.cumsum())
print(c.cumsum().dtype)
print(c.cumsum(dtype="int8").dtype)

print(b)
print(b.cumsum())
print(b.cumsum(axis=1))
print(b.cumsum(axis=0))