# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:26:46 2020

@author: s1430
"""


import numpy as np
a = np.zeros(10)
print(a)

b = np.zeros(10, dtype = int)
print(b)
print(np.zeros((3, 4)))

def zeros():
    for i in range(10000):
        _ = np.zeros((1, i))

def empty():
    for i in range(10000):
        _ = np.empty((1, i))

import time
time1 = time.time()
zeros()
time1 = time.time() - time1
time2 = time.time()
empty()
time2 = time.time() - time2
print(time1, time2)

b = np.zeros(a.shape)
b = np.zeros_like(a)