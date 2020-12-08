# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 10:10:55 2020

@author: s1430
"""


import numpy as np
a = np.arange(10).reshape(2, 5)
print(a)
print(a.ravel())
print(np.ravel(a))

print(a)
print(a.ravel(order="C"))
print(a.ravel(order="F"))
print(a.ravel(order="A"))
print(a.ravel(order="K"))

b = np.arange(10).reshape(2, 5, order="F")
print(b)

print(b.ravel(order="F"))
print(b.ravel(order="A"))
print(b.ravel())

c = b.T
print(c)
print(c.ravel())
print(c.ravel(order="K"))
print(c.T.ravel(order="K"))