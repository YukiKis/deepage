# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:46:49 2020

@author: s1430
"""


import numpy as np

a = np.array([10, 20, 12, 0, 3, 5])
print(np.mean(a))
print(np.var(a))
print(np.std(a))

b = np.random.randint(20, size=(3, 4))
print(b)

print(np.mean(b))
print(np.var(b))
print(np.std(b))

print(np.mean(b, axis=0))
print(np.var(b, axis=0))
print(np.std(b, axis=0))
print(np.var(b, axis=(0, 1)))

c = np.random.randn(100).reshape(5, 20)
print(c.dtype)

print(np.var(c, dtype="float32"))
print(np.var(c, dtype="float64"))

d = np.random.randn(10)
print(np.var(d, ddof=0))
print(np.var(d, ddof=1))

e = np.random.randn(5)
print(np.var(e))
print(np.var(e, ddof=1))

f = np.random.randint(20, size=(2, 5, 10))
print(f)
f_var = np.var(f, axis=1)
print(f_var.shape)

f_var = np.var(f, axis=1, keepdims=True)
print(f_var.shape)