# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:03:00 2020

@author: s1430
"""


import numpy as np
import matplotlib.pyplot as plt

mean = np.array([0, 0])
cov = np.array([[1, -1], 
               [-1, 1]])
x, y = np.random.multivariate_normal(mean, cov, 5000).T
plt.plot(x, y, "x")
plt.axis("Equal")
plt.show()

a = np.array([[10, 5, 2, 4, 9, 3, 2], 
             [10, 2, 8, 3, 7, 4, 1]])
print(np.var(a, axis=1))
print(np.cov(a))

c = np.array([3, 2, 1, 5, 7, 2, 1])
print(np.cov(a, c))

a_transpose = a.T
c_transpose = np.reshape(c, (-1, 1))
print(np.cov(a_transpose, y=c_transpose, rowvar=False))

print(np.cov(a, bias=False))
print(np.cov(a, bias=True))

print(np.cov(a, ddof=None))
print(np.cov(a, ddof=0))
print(np.cov(a, ddof=1))
print(np.cov(a, ddof=2))

fweights = np.array([1, 2, 2, 1, 1, 1, 1])
print(np.cov(a, fweights = fweights))

aweights = np.array([0.1, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1])
print(np.cov(a, aweights=None))
print(np.cov(a, aweights = aweights))