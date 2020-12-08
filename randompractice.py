# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:36:37 2020

@author: s1430
"""


import numpy as np
from numpy.random import *

print(rand())
print(randint(10))

print(rand(2, 3))
print(randint(10, size=(2, 3)))

print(randint(5, 10, size= 10))
print((10-5) * rand(10) + 5)

seed(seed=21)
print(rand())

seed(21)
print(rand())

seed(10)
print(rand(20))
seed(23)
print(rand(20))
seed(10)
print(rand(20))

a = ["Python", "Ruby", "Java", "JavaScript", "PHP"]
print(choice(a, 3))
print(choice(a, 5, replace=False))
print(choice(a, 20, p = [0.8, 0.05, 0.05, 0.05, 0.05]))
print(choice(5, 10))

a = np.arange(20)
print(a)
shuffle(a)
print(a)

print(randn())
print(randn(10))

print(normal(loc=1, scale=2.0, size=10))
print(normal(size=20))

print(binomial(100, 0.5, 30))

from matplotlib import pyplot as plt

def standard_normal_distribution(x):
    return ( 1/ np.sqrt(2 * np.pi)) * np.exp(-x ** 2 / 2) * 1000

a = np.random.randn(100000)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = np.linspace(-5, 5, 1000)
ax.hist(a, bins=1000)
ax.plot(x, standard_normal_distribution(x))
fig.show()