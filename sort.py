# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:25:51 2020

@author: s1430
"""


import numpy as np
a = np.random.randint(0, 100, size=20)
print(a)
print(np.sort(a))

a = np.array([1, 3, 2])
print(np.argsort(a))

for index in np.argsort(a):
    print(a[index])

#import time
#def sort_comparison(n):
#    result1 = np.empty(1000)
#    for i in range(1000):
#        a = np.random.rand(n)
#        time1 = time.time()
#        b = np.sort(a, kind="quicksort")
#        time1 = time.time() - time1
#    result1[i] = time1
#    result2 = np.empty(1000)
#    for i in range(1000):
#        a = np.random.rand(n)
#        time1 = time.time()
#        b = np.sort(a, kind="mergesort")
#        time1 = time.time() - time1
#        result2[i] = time1
#    result3 = np.empty(1000)
#    for i in range(1000):
#        a = np.random.rand(n)
#        time1 = time.time()
#        b = np.sort(a, kind="heapsort")
#        time1 - time.time() - time1
#        result3[i] = time1
#    print("Quicksort average {}, max {}".format(np.average(result1), np.max(result1)))
#    print("Mergesort average {}, max {}".format(np.average(result2), np.max(result2)))
#    print("Heapsort average {}, max{}".format(np.average(result3), np.max(result3)))

#from test import *
#sort_comparison(100)
#sort_comparison(1000)
#sort_comparison(10000)

values = [("Alice", 25, 9.6), ("Bob", 12, 8.5), ("Catherine", 1, 8.6), ("David", 10, 7.6)]
dtype = [("name", "S10"), ("ID", int), ("score", float)]
a = np.array(values, dtype = dtype)
print(a)

print(np.sort(a, order = "score"))
print(np.argsort(a, order="score"))

np.sort(a, order=["score", "ID"])
np.argsort(a, order=["score", "ID"])

b = np.random.randint(0, 100, size=20).reshape(4, 5)
print(b)

print(np.sort(b))
print(np.argsort(b))

print(np.sort(b, axis=0))
print(np.argsort(b, axis=0))

c = np.random.randint(0, 100, size=(2, 4, 5))
print(c)

print(np.sort(c, axis=0))
print(np.argsort(c, axis=0))

a = np.random.randint(0, 100, 20)
print(a)
print(np.sort(a))
print(a)
a.sort()
print(a)