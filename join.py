# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:25:26 2020

@author: s1430
"""


import pandas as pd

left = pd.DataFrame({
        "A": ["a", "b", "c"],
        "B": [0, 1, 2]},
        index = ["K0", "K1", "K2"]
        )
right = pd.DataFrame({
        "C": ["aa", "bb", "cc"],
        "D": [0, 2, 4]},
        index = ["K0", "K1", "K3"]
        )
result = left.join(right)
print(result)

right1 = right.copy()
right2 = pd.DataFrame({
        "E": ["A", "B", "C"],
        "F": [0, 3, 6]},
        index=["K0", "K2", "K4"]
        )
result = left.join([right1, right2])
print(result)

right = pd.Series(["A", "B", "C"], name="C", index=["K0", "K1", "K2"])
result = left.join(right)
print(result)

right = pd.DataFrame({"C": ["aa", "bb", "cc"], "D": [0, 2, 4]}, index=["K0", "K1", "K2"])
print(left.join(right, how="left"))
print(left.join(right, how="inner"))
print(left.join(right, how="outer"))
print(left.join(right, how="right"))

left = pd.DataFrame({"A": ["a", "b", "c"],
                     "B": [0, 1, 2],
                     "key": ["K0", "K1", "K2"]
                     })
print(left.join(right, on="key"))

left = pd.DataFrame({"A": ["a", "b", "c", "d"],
                     "B": [0, 1, 2, 3],
                     "key1": ["foo", "bar", "foo", "bar"],
                     "key2": ["A", "B", "C", "A"]
                     })
right = pd.DataFrame({"C": ["A", "BB", "CC", "D"],
                      "D": [0, 2, 4, 6]}, 
                        index= [["foo", "foo", "bar", "bar"], ["A", "B", "A", "C"]]
                        )
print(left.join(right, on=["key1", "key2"]))

left = pd.DataFrame({"A": ["a", "b", "c"],
                     "B": [0, 1, 2]},
                        index=["K0", "K1", "K2"]
                        )
right = pd.DataFrame({"A": ["aa", "bb", "cc"],
                      "B": [2, 1, 0]},
                        index=["K0", "K1", "K2"]
                        )
print(left.join(right, lsuffix="_l", rsuffix="_r"))