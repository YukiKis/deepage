# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:35:14 2020

@author: s1430
"""

import numpy as np
a = np.ones(3)
print(a)

print(np.ones((2, 3)))

b = np.ones(4, dtype="float32")
print(b)

c = np.ones(4, dtype="int8")
print(c)

d = np.ones((2, 3), dtype="complex")
print(d)

e = np.ones(a.shape)
f = np.ones_like(a)

a = np.array([[1, 2, 3], [2, 3, 4]])
print(np.ones_like(a))
