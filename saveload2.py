# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:07:41 2020

@author: s1430
"""


import numpy as np
a = np.random.rand(1200 * 1000).reshape(1200, -1)
np.save("a", a)
b = np.load("a.npy")
print(a)
print(a.shape)

c = np.random.randn(12 * 20 * 40).reshape(12, 20, 40)
np.save("c", c)

d = np.load("c.npy")
print(d.shape)

e = np.loadtxt("c.npy")
