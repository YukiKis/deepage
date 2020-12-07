# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:46:20 2020

@author: s1430
"""


import numpy as np

a = np.arange(12)
b = np.arange(9)
print(a)
print(b)
c = np.hstack((a, b))
print(c)

c = np.arange(2).reshape(1, 2)
print(c)

d = np.arange(5).reshape(1, 5)
#e = np.hstack((c, d))
#print(e)

e = np.arange(12).reshape(2, 2, 3)
f = np.arange(6).reshape(2, 1, 3)

print(e)
print(f)

g = np.hstack((e, f))
print(g)

#axis = 1が違ってもOK!

a = np.arange(12).reshape(-1, 1)
b = np.arange(2).reshape(-1, 1)
print(a)
print(b)

c = np.vstack((a, b))
print(c)

c = np.arange(2).reshape(1, 2)
#print(c)
#e = np.vstack((c, d))

e = np.arange(24).reshape(4 , 3, 2)
f = np.arange(6).reshape(1, 3, 2)
print(e)
print(f)

g = np.vstack((e, f))
print(g)
print(g.shape)