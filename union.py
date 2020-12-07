# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 23:41:42 2020

@author: s1430
"""


import pandas as pd
import numpy as np
a = pd.DataFrame(np.arange(25).reshape(5, 5), columns=["a", "b", "c", "f", "g"])
print(a)

print(a.index.union([-1, -2, 3, 8]))
print(a.index.union(["a", "b"]))

print(a.reindex(a.index.union([4, 5, 6, 7])))

# a.index = a.index.union([4, 5, 6, 7])
