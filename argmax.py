# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:10:53 2020

@author: s1430
"""


import numpy as np
a = np.random.randint(10, size=10)
print(a)

max_index = np.argmax(a)
print(max_index)

b = np.random.randint(10, size=(3, 4))
print(b)
max_index = np.argmax(b)
print(max_index)
print(b.argmax())

max_indexes = np.argmax(b, axis=0)
print(max_indexes)
print(b.argmax(axis=0))

max_indexes = np.argmax(b, axis=1)
print(max_indexes)
print(b.argmax(axis=1))

c = np.random.randint(10, size=(2, 3, 4))
print(c)

print(np.argmax(c, axis=0))

print(c.argmax(axis=0))
max_indexes = np.argmax(c, axis=1)
print(max_indexes)
print(c.argmax(axis=1))

max_indexes = np.argmax(c, axis=2)
print(max_indexes)
print(c.argmax(axis=2))