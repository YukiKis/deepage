# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 23:31:02 2020

@author: s1430
"""


import numpy as np

a = np.array([1, 2])
b = np.array([4, 3])
print(np.dot(a, b))
print(np.dot(a, a))

print(np.dot(4, 5))

c = np.array([1j, 2j])
d = np.array([4j, 3j])
print(np.dot(c, d))
print(np.dot(a, d))

e = np.matrix([1, 2])
f = np.matrix([4, 3])
print(e)
#print(np.dot(e, f))
print(e.shape)
#f = np.matrix([[4], [3]])
#print(f.shape)
#print(np.dot(e, f))

a = np.array([[1, 2], [3, 4]])
b = np.array([[4, 3], [2, 1]])
print(np.dot(a, b))
print(np.dot(b, a))

c = np.arange(9).reshape((3, 3))
d = np.ones((3, 3))
print(np.dot(c, d))

a = np.arange(12).reshape((4, 3))
b = np.arange(16).reshape((4, 4))
#print(np.dot(a, b))
print(np.dot(b, a))

d = np.matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
e = np.matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(np.dot(d, e))

result = np.zeros((2,2))
a = np.arange(4).reshape(2, 2)
b = np.ones((2, 2))
print(a)
print(b)
print(np.dot(a, b, out=result))
print(np.dot(b, a, out=result))