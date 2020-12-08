# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:14:45 2020

@author: s1430
"""


import pandas as pd

df_single = pd.read_csv("sample_stack.csv", skiprows=[0], index_col=0)
print(df_single)

print(df_single.stack())

df_multi = pd.read_csv("sample_stack.csv", index_col=0, header=[0, 1])
print(df_multi)
print(df_multi.stack())
print(df_multi.stack(level=0))
print(df_multi.stack(level=1))
print(df_multi.stack(level=[0, 1]))

import numpy as np
df_multi["score", "English"] = np.nan
print(df_multi)

print(df_multi.stack())
print(df_multi.stack(dropna=False))

print(df_multi.unstack())

df_multi_index = pd.read_csv("sample_stack.csv", index_col=[0, 1], header=[0, 1])
print(df_multi_index)
print(df_multi_index.unstack())
print(df_multi_index.unstack(level=0))
print(df_multi_index.unstack(fill_value="MISSING"))