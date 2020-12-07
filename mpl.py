# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:58:10 2020

@author: s1430
"""


import numpy as np
import matplotlib as plt

x = np.linspace(-10, 10, 1000)
y = np.sin(x)

plt.pyplot.plot(x, y)
plt.pyplot.show()
plt.pyplot.grid(True)
plt.pyplot.plot(x, y)
plt.pyplot.show()

plt.pyplot.title("Sine Wave")
plt.pyplot.xlabel("X")
plt.pyplot.ylabel("Y")
plt.pyplot.plot(x, y)
plt.pyplot.show()

plt.pyplot.xlim(-5, 5)
plt.pyplot.ylim(-0.5, 1.0)

plt.pyplot.xlabel("X")
plt.pyplot.ylabel("Y")
plt.pyplot.title("Limited Scale")
plt.pyplot.plot(x, y)
plt.pyplot.show()

x = np.random.randn(1000)
y = np.random.randn(1000)

plt.pyplot.scatter(x, y)
plt.pyplot.title("Scatter")
plt.pyplot.xlabel("X")
plt.pyplot.ylabel("Y")
plt.pyplot.grid()
plt.pyplot.show()

plt.pyplot.hist(x)
plt.pyplot.xlabel("X")
plt.pyplot.ylabel("Y")
plt.pyplot.show()

x = np.linspace(-10, 10, 1000)
y_1 = np.sin(x)
y_2 = np.cos(x)

plt.pyplot.plot(x, y_1)
plt.pyplot.plot(x, y_2)
plt.pyplot.grid(True)
plt.pyplot.xlabel("X")
plt.pyplot.ylabel("Y")
plt.pyplot.show()