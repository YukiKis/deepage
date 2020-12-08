# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 12:05:36 2020

@author: s1430
"""


import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.r_[a, b])

print(np.r_[2, 4, 3, np.array([2, 3, ]), 4.2])

c = np.zeros((2, 3))
d = np.ones((3, 3))
print(np.r_[c, d])
# d = np.ones((3, 4)); np_r[c, d]

print(np.r_[0:10])
print(np.r_[:10])
print(np.r_[-10:])
print(np.r_[0:10:2])
print(np.r_[10:0:-1])
print(np.r_[0:10:10j])
print(np.r_[0:9:20])
print(np.r_[0:10, 0, 4, np.array([3, 3])])


