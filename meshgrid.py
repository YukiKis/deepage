# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:38:39 2020

@author: s1430
"""


import numpy as np

xx = np.array([[x for x in range(5)] for _ in range(5)])
print(xx)

yy = np.array([[y for _ in range(5)] for y in range(5)])
print(yy)

a = np.array([0, 1, 2])
b = np.array([0, 4])
aa, bb = np.meshgrid(a, b)
print(aa)
print(bb)

c = np.array([0, 9])
aaa, bbb, ccc = np.meshgrid(a, b, c)

aa2, bb2 = np.meshgrid(a, b, indexing="xy")
print(aa2)
print(bb2)

aa3, bb3 = np.meshgrid(a, b, indexing="ij")

aaa1, bbb1, ccc1 = np.meshgrid(a, b, c, indexing="xy")
print(aaa1, bbb1, ccc1)

aaa2, bbb2, ccc2 = np.meshgrid(a, b, c, indexing="ij")

av, bv = np.meshgrid(a, b, sparse=True)
print(av)
print(bv)

aav, bbv, ccv = np.meshgrid(a, b, c, sparse=False)
print(aav)
print(ccv)
print(bbv)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)

xx, yy = np.meshgrid(x, y)
ret = np.sin(xx**2 + yy*2)

def plot1():
    plt.gca().set_aspect("equal", adjustable="box")
    plt.contourf(x, y, ret > 0, cmap=plt.cm.bone)
    plt.show()
    
def plot2():
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(aa, bb, ret)
    plt.show()
   
plot1()
plot2()