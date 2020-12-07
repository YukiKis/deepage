# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:46:37 2020

@author: s1430
"""


import numpy as np

a = np.linspace(0, 1)
print(a)

b = np.linspace(0, 49)
print(b)

c = np.linspace(0, 2, 3)
print(c)

d = np.linspace(0, -2, 3)
print(d)

e = np.linspace(0, 2, num=3)
print(e)

f = np.linspace(0, 2, num=3, endpoint=False)
print(f)

g = np.linspace(0, 2, num=3, endpoint=True)
print(g)

h = np.linspace(0, 1, retstep=True)
print(h)

g = np.linspace(0, 2, num=3, retstep=False)
print(g)

h = np.linspace(0, 2, num=3)
print(h)
print(h.dtype)

i = np.linspace(0, 2, num=3, dtype="int")
print(i)
print(i.dtype)

j = np.linspace(0, 1, num=4, dtype="float32")
print(j)
print(j.dtype)