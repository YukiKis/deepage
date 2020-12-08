# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:45:58 2020

@author: s1430
"""


import numpy as np

a = np.array([0, 1, 2, 3, 4])
b = np.array([2, 4, 6, 8, 10])
print(a + b)
print(np.add(a, b))

print(a - b)
print(np.subtract(b, a))
print(a - 4)

print(a * b)
print(np.multiply(a, 200))

print(b / a)
print(b / 2)
print(np.divide(b, 3))
print(b // 3)
print(b % 3)
print(np.mod(b, 2))

print(np.power(2, 3))
a = np.arange(1, 11, 1)
b = np.array([1, 2, 1, 2, 1, 2, 1, 2, 1, 2])
print(a)
print(b)
print(np.power(a, b))
print(a ** b)
print(np.sqrt(2))
print(2 ** 0.5)
print(np.sqrt(a))

print(np.sin(0))
print(np.cos(0))
print(np.tan(0))
print(np.sin(np.pi * 0.5))
print(np.cos(np.pi * 0.5))
print(np.tan(np.pi * 0.5))

print(np.arcsin(0.5))
print(np.arccos(0.5))
print(np.arctan(1.0))
print(np.arcsin(-1.0))
print(np.arccos(-1.0))
print(np.arctan(-0.5))

print(np.radians(120))
print(np.deg2rad(120))
print(np.rad2deg(3.14))
print(np.deg2rad(2.3))

print(np.exp(1))
print(np.exp(2))
print(np.exp(0))

a = np.array([-1.0, -1.4, -1.0, -0.6, -0.2, 0., 0.2, 0.6, 1.0, 1.4, 1.8])
print(np.floor(a))
print(np.trunc(a))
print(np.ceil(a))
print(np.round(a))
print(np.around(a))
print(np.rint(a))
print(np.fix(a))

a = 1 + 2j
b = -2 + 1j
print(np.real(a))
print(np.imag(a))
print(a + b)

print(a * b)
print(a / b)
print(np.conj(a))

a = -2.5
print(np.absolute(a))
print(np.fabs(a))
b = -2 + 3j
print(np.abs(b))
# print(pn.fabs(b))
c = np.array([1, 2, 0.8, 12, 1 + 2j])
print(np.abs(c))

print(np.e)
print(np.pi)
