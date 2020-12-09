# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 19:29:08 2020

@author: s1430
"""


import pandas as pd

sr = pd.Series(["a", "a", "a", "b", "b", "c", "c", "e", None])
print(sr)
print(sr.value_counts())
print(sr.value_counts(normalize=True))
print(sr.value_counts(sort=True))
print(sr.value_counts(sort=True, ascending=True))

import numpy as np
data = np.random.randn(1000)

sr_2 = pd.Series(data)
print(sr_2.value_counts(bins=5))
print(sr_2.value_counts(bins=10))

df = pd.DataFrame({
        "A": [0, 1, 0, 1, 1, 1, 1],
        "B": [1, 1, 2, 2, 1, 1, 1]}
)
print(df.apply(pd.value_counts))
#print(df.value_counts())