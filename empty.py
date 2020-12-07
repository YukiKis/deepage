# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:58:14 2020

@author: s1430
"""


import numpy as np

a = np.empty(10)
print(a)

a = np.empty((2, 10))
print(a)

a = np.empty(5, dtype=np.int8)
print(a)
a = np.empty(10, dtype=np.bool)
print(a)
a = np.empty(100, dtype=complex)
print(a)

import time
time1 = time.time()
np.zeros(10000)
time1 = time.time() - time1
time2 = time.time()
np.ones(10000)
time2 = time.time() - time2
time3 = time.time()
np.empty(10000)
time3 = time.time() - time3
print(time1, time2, time3)
