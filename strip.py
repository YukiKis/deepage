# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:29:05 2020

@author: s1430
"""


import pandas as pd

a = pd.Series(["aaabbaabbaa"])
print(a)
print(a.str.strip("a"))
sr = pd.Series([" a ", " ", " c", "d "])
print(sr.str.strip())
print(sr.str.lstrip())
print(sr.str.rstrip())

print(sr.str.lstrip().str[:1])
print(sr.str.lstrip().str[-1:])
print(sr.str.rstrip().str[:1])
print(sr.str.rstrip().str[-1:])

sr2 = pd.Series(["www.example.com", "www.sample.com"])
print(sr2.str.strip("w."))

sr3 = pd.Series(["a-b-c", "a-b-d", "b-a-d"])
print(sr3)
print(sr3.str.replace("a-b", "A"))

sr4 = pd.Series([" a b c ", "a b c "])
print(sr4.str.replace(" ", ""))
print(sr4.str.strip())

sr5 = pd.Series(["A", "B", "1234bde45"])
print(sr5.str.replace("^[1-9]", "A"))
print(sr5.str.replace("^[1-9]+", "A"))

sr6 = pd.Series(["[1-9]"])
print(sr6.str.replace("[1-9]", "NUMBER"))
print(sr6.str.replace("[1-9]", "NUMBER", regex=False))