# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:00:06 2020

@author: s1430
"""


import numpy as np

a = np.array([33, 44, 54, 23, 25, 55, 32, 76])
print(np.average(a))

a = a.reshape(2, 4)

print(np.average(a))
print(np.average(a, axis=0))

b = np.random.randn(24).reshape(2, 3, 4)
print(np.average(b, axis=0))
print(np.average(b, axis=1))
print(np.average(b, axis=2))

a = a.flatten()
w = np.array([0.1, 0.05, 0.2, 0.0, 0.0, 0.4, 0.2, 0.05])
print(np.average(a, weights = w))
w2 = np.array([0.2, 0.8])
a = a.reshape(2, 4)
print(np.average(a, axis=0, weights = w2))

print(np.average(a, returned=True))

a = a.flatten()
print(a)
print(np.average(a, weights = w, returned="True"))

a = np.random.randint(0, 10, 20)
print(a)

print(np.mean(a))
b = a.reshape(4, 5)
print(np.mean(b))

print(np.mean(b, axis=0))
print(np.mean(b, axis=1))

c = np.random.rand(24).reshape((2, 3, 4))
print(c)
print(np.mean(c, axis=0))
print(np.mean(c, axis=1))
print(np.mean(c, axis=2))

d = np.random.rand(1000)
print(d.dtype)
print(np.mean(d))
print(np.mean(d, dtype="float32"))
print(np.mean(d, dtype="float16"))

e = np.mean(b, keepdims=True)
print(e)
print(e.shape)
f = np.mean(b, keepdims=False)
print(f)
print(f.shape)

g = np.mean(b, axis=1, keepdims=True)
print(g.shape)
h = np.mean(b, axis=1, keepdims=False)
print(h.shape)