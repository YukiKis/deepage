# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:31:00 2020

@author: s1430
"""


import numpy as np

a = np.random.rand(10)
print(a)
print(a.std())

b = np.random.rand(2, 3, 4)
print(b)

print(np.std(b, axis=0))
print(np.std(b, axis=(0, 1)))
print(np.std(b, axis=(0, 1, 2)))

print(np.std(b, dtype="float16"))
print(np.std(b, dtype="complex"))

c = np.empty((2, 3))
np.std(b, axis=2, out=c)
print(c)

print(np.std(c))
print(np.std(c, ddof=1))

print(np.std(b, keepdims=True))
print(np.std(b, axis=0, keepdis=True))
print( b / np.std(b, axis=0, keepdims=True))
print(b / np.std(b, axis=0, keepdims=False))
#print(b / np.std(b, axis=1, keepdims=False))