# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:32:21 2020

@author: s1430
"""


import numpy as np

a = np.array([0, 1, 2])
print(np.tile(a, 2))
print(np.tile(a, (3, 2)))
print(np.tile(a, (2, 3, 4)))

b = np.arange(6).reshape(2, 3)
print(np.tile(b, 2))

print(np.tile(b, (2, 3)))
print(np.tile(b, (2, 1, 1)))

a = np.arange(10000).reshape(-1, 1)
b = np.arange(10000).reshape(1, -1)
print(a * b)

a = np.arange(10000).reshape(-1, 1)
b = np.arange(10000)

import time
time1 = time.time()
a * b
time1 = time.time() - time1
time2 = time.time()
np.tile(a, (1, 10000)) * np.tile(b, (10000, 1))
time2 = time.time() - time2
print(time1, time2)