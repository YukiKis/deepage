# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:15:53 2020

@author: s1430
"""


import numpy as np

a = np.random.randint(100, size=(2, 3, 4))
print(np.median(a))
print(np.mean(a))
print(np.amax(a))
print(np.amin(a))

print(np.median(a, axis=2))
print(np.median(a, axis=1))
print(np.median(a, axis=(1, 2)))

b = a.copy()
print(b)

print(np.median(b, axis=1, overwrite_input=True))
print(np.all(a == b))
print(a)
print(b)

print(np.median(a, axis=0, keepdims=True))
print(np.median(a, axis=1, keepdims=False))
print(np.median(a, axis=1, keepdims=False))
print(np.median(a, axis=(0, 2), keepdims=True))