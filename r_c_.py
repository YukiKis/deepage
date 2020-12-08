# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 12:05:36 2020

@author: s1430
"""


import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.r_[a, b])

print(np.r_[2, 5, 3, np.array([2, 3]), 4.2])

c = np.zeros((2, 3))
d = np.ones((3, 3))
print(np.r_[c, d])
print(np.vstack((c, d)))

print(np.r_[0:10])
print(np.r_[:10])
print(np.r_[-10:])
print(np.r_[0:10:2])
print(np.r_[10:0:-1])
print(np.r_[0:10:10j])
print(np.r_[0:9:20j])
print(np.r_[0:10, 0, 4, np.array([3, 3])])

a = np.ones((2, 2))
b = np.zeros((2, 2))
print(np.r_["1", a, b])
print(np.r_["1", a, b].shape)
print(np.r_["0", a, b])
print(np.r_["0", a, b].shape)

c = np.ones((2, 2, 2))
d = np.zeros((2, 2, 2))
print(np.r_["0", c, d])
print(np.r_["1", c, d])
print(np.r_["2", c, d])
print(np.r_["0", c, d].shape)
print(np.r_["1", c, d].shape)
print(np.r_["2", c, d].shape)

print(np.r_["0, 2", [0, 1, 2], [3, 3, 3]])
print(np.r_["0, 2", [0, 1, 2], [3, 3, 3]].shape)
print(np.r_["0, 3", [0, 1, 2], [3, 3, 3]])
print(np.r_["0, 3", [0, 1, 2], [3, 3, 3]].shape)
print(np.r_["-1, 4", [0, 1, 2], [3, 3, 3]])
print(np.r_["-1, 4", [0, 1, 2], [3, 3, 3]].shape)

a = np.array([1, 4, 6])
b = np.array([2, 2, 2])
print(np.r_["r", a, b])
print(np.r_["c", a, b])

a = np.ones((3, 2))
b = np.zeros((3, 3))

print(np.c_[a, b])
print(np.hstack((a, b)))
c = np.zeros(3)
print(np.c_[a, c].shape)
print(np.c_[[[1, 2, 3]], [[4, 5, 6]], 2, 3])