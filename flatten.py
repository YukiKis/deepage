# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 10:06:24 2020

@author: s1430
"""


import numpy as np
a = np.arange(10).reshape(2, 5)
print(a)
b = a.flatten()
print(b)
print(a.shape)
print(b.shape)

c = np.arange(12).reshape(2, 2, 3)
print(c)
d = c.flatten()
print(d)

print(c.shape)
print(d.shape)

arr = np.repeat(5, 10000).reshape(250, 40)

import time
time1 = time.time()
arr.flatten()
time1 = time.time() - time1
time2 = time.time()
np.ravel(arr)
time2 = time.time() - time2
print(time1, time2)