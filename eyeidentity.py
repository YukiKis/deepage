# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:53:30 2020

@author: s1430
"""


import numpy as np
a = np.eye(3)
print(a)
a = np.eye(10)
print(a)

a = np.eye(2, 3)
print(a)
a = np.eye(4, 5)
print(a)

a = np.eye(5, k=0)
print(a)
a = np.eye(5, k=1)
print(a)
a = np.eye(5, k=-1)
print(a)
a = np.eye(5, k=3)
print(a)
a = np.eye(5, dtype=int)
print(a)
a = np.eye(5, dtype=complex)
print(a)

a = np.identity(5)
print(a)
a = np.identity(2)
print(a)

a = np.identity(3, dtype=int)
print(a)
a = np.identity(4, dtype="float32")
print(a)

import time
time1 = time.time()
a = np.eye(10000)
time1 = time.time() - time1

time2 = time.time()
a = np.identity(10000)
time2 = time.time() - time2
print(time1, time2)