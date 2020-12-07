# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:41:34 2020

@author: s1430
"""


import numpy as np
a = np.arange(12).reshape(3, 4)
print(a)

print(a.transpose())
print(a.transpose((1, 0)))
print(a.transpose((0, 1)))

b = np.arange(6)
print(b)

print(b.transpose())
print(b.transpose().shape)

b = b.reshape((1, 6))
print(b)
print(b.transpose())

c = np.arange(24).reshape(4, 3, 2)
print(c)

print(c.transpose())

print(c.transpose(1, 0, 2))

print(np.transpose(c))
print(np.transpose(c).shape)

array = np.transpose(c, (1, 0, 2))
print(array)
print(np.transpose(c, (1, 0, 2)).shape)

print(b)
array = np.transpose(b)

b = b.reshape((1, 6))
print(b)
print(np.transpose(b))

print(a)
print(a.T)
print(b)
print(b.T)
print(c)
print(c.T)