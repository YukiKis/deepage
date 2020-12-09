# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:19:41 2020

@author: s1430
"""


import numpy as np
import matplotlib.pyplot as plt
mean = np.array([0, 0])
cov= np.array([[1, 0.8],
               [0.8, 1]])
x, y = np.random.multivariate_normal(mean, cov, 5000).T
plt.plot(x, y, "x")
plt.title("r=0.8")
plt.axis("equal")
plt.show()

x = np.array([
        [1, 2, 1, 9, 10, 3, 2, 6 ,7],
        [2, 1, 8, 3, 7, 5, 10, 7, 2]
        ])
print(np.corrcoef(x))

y = np.array([2, 1, 1, 8, 9, 4, 3, 5, 7])
print(np.corrcoef(x, y))

x_transpose = x.T
print(np.corrcoef(x_transpose, rowvar=False))
print(np.corrcoef(x_transpose, rowvar=True))