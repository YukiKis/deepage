# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:58:09 2020

@author: s1430
"""


import numpy as np
a = np.random.randn(1000)

print(np.histogram(a))

hist, bins = np.histogram(a)
print(hist)
print(bins)

c = np.random.randint(10, size=30)
print(c)

print(np.histogram(c, range=(0, 10)))
print(np.histogram(c))

d = np.random.randn(40)
print(d)
print(np.histogram(d, range=(-3, 3)))

print(np.histogram(a, bins=5))
print(np.histogram(a, bins=np.arange(-3, 3)))
print(np.histogram(a, bins=np.linspace(-3, 3, 20)))
print(np.histogram(a, bins=np.linspace(-3, 3, 20)))

b = np.random.randint(-3, 4, size=20)
weights = np.tile(np.array([1, 0]), 10)
print(np.histogram(b, bins = 6, weights = weights))

print(np.histogram(b, bins=6, density=False))
print(np.histogram(b, bins=6, density=True))