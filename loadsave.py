# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 10:21:51 2020

@author: s1430
"""


import numpy as np
a = np.random.randn(3, 4)
np.savetxt("sample.txt", a)
b = np.loadtxt("sample.txt")

print(a)
print(b)

np.savetxt("sample.csv", a)
c = np.loadtxt("sample.csv")
print(c)

np.savetxt("sample.dat", a)
d = np.loadtxt("sample.dat")
print(d)

np.savetxt("sample2.txt", a, delimiter=",")
e = np.loadtxt("sample2.txt", delimiter=",")
print(e)

np.savetxt("sample3.txt", a, fmt="%.2e")
f = np.loadtxt("sample3.txt")
print(f)

np.savetxt("sample4.txt", a, fmt="%.2f")
g = np.loadtxt("sample4.txt")
print(g)

#h = np.array([[10.1 + 3.21j, 100 + 32.1j], [20.0 + 0.2j, 22.1 - 1j]])
#np.savetxt("sample6.txt", h, fmt="%.3e+%.3ej")
#i = np.loadtxt("sample6.txt")
#print(i)

print(np.loadtxt("sample4.txt", usecols=(0, 2)))
print(np.loadtxt("sample4.txt", skiprows=1))
np.savetxt("sample7.txt", a, fmt="%.3e", header="This is a header", footer="This is a footer")

np.savetxt("sample8.txt", a, fmt="%.3e", header="This is a header", footer="This is a footer", comments=">>>")
print(np.loadtxt("sample8.txt", comments=">>>"))

print(np.loadtxt("foo.csv", dtype=[("col1", "i8"), ("col2", "S10"), ("col3", "f8"), ("col4", "S10")]))

print(np.loadtxt("foo.csv", dtype=[("col1", "i8"), ("col2", "S10"), ("col3", "f8"), ("col4", "S10")], unpack=True))
age, gender, tall, driver_lisence = np.loadtxt("foo.csv", dtype=[("col1", "i8"), ("col2", "S10"), ("col3", "f8"), ("col4", "S10")], unpack=True)
print(age)
print(gender)

def driver_license(str):
    if str == b"Yes":
        return 1
    else:
        return -1
    
def gender(str):
    if str == b"male":
        return 1
    else:
        return -1

print(np.loadtxt("foo.csv", converters={1: lambda x: gender(x), 3: lambda x: driver_license(x)}))

def gender2(str):
    if not str:
        return 0
    elif str == b"male":
        return 1
    else:
        return 0

np.loadtxt("foo.csv", converters={1: lambda s: gender2(s), 3: lambda s: driver_license(s)})

a = np.genfromtxt("bar.txt", delimiter=",")
print(a)

b = np.genfromtxt("bar.txt", delimiter=",", dtype=["int", "float", "int"])
print(b)
