# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:42:32 2020

@author: s1430
"""


import numpy as np

x = np.arange(15).reshape(3, 5)
print(x)

print(x[np.newaxis, :, :])
print(x[:, np.newaxis, :])
print(x[:, None, :])
x = x.flatten()
print(x)
print(x[:, np.newaxis])

x = np.arange(15).reshape(3, 5)
print(np.reshape(x, (1, 3, 5)))
print(np.reshape(x, (3, 1, 5)))
x = x.flatten()
print(np.reshape(x, (-1, 1)))


