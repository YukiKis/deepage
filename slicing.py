# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:38:11 2020

@author: s1430
"""


import pandas as pd

sr = pd.Series(["a123a21", "b232b33", "c122c222"])
print(sr)
print(sr.str[0])
print(sr.str[3])
print(sr.str[-1])

print(sr.str[1:4])
print(sr.str[:4])
print(sr.str)
print(sr.str[4:])

print(sr.str[::2])
print(sr.str[::-1])
print(sr.str[::3])

print(sr.str.extract("(a)(1)"))

print(sr.str.extract("([a-z])([0-9]){3}"))
print(sr.str.extract("([a-z])([0-9]{3})([ab])"))
print(sr.str.extract("(?P<class>[a-z])(?P<number>[0-9]{3})"))
print(sr.str.extractall("([a-z])([0-9]{2})"))