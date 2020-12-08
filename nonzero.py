# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:23:00 2020

@author: s1430
"""


import numpy as np

a = np.random.randint(0, 10, size=20)
print(a)
print(np.nonzero(a))
a[np.nonzero(a)]

b = np.random.randint(0, 10, size=(4, 5))
print(b)
print(np.nonzero(b))
print(b[np.nonzero(b)])

a = np.random.randint(0, 10, size=(100, 100))
b = np.ones(shape=(100, 100))
print(np.where(a != 0, a, b))

a = np.random.randint(0, 10, size=(100, 100))
print(np.nonzero(a))

print(np.where(a != 0))
print(np.argwhere(a != 0))