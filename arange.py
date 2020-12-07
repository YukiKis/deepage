# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:40:17 2020

@author: s1430
"""

import numpy as np

print([x for x in range(10)])
print(np.array(range(10)))

a = np.arange(5)
print(a)

b = np.arange(-10)
print(b)

c = np.arange(4.5)
print(c)

d = np.arange(1, 8)
print(d)
f = np.arange(2, 10)
print(f)
print(np.arange(0.5, 5.5))
print(np.arange(0.05, 5.55))

g = np.arange(2, 12, 2)
print(g)

h = np.arange(start=2, stop=5, step=0.2)
print(h)
print(np.arange(5, 2, -1))

print(np.arange(5, dtype="float64"))
print(np.arange(5.0, dtype="int"))
print(np.arange(0, 5, 1.5, dtype="int"))