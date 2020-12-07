# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 22:13:43 2020

@author: s1430
"""

import pandas as pd
twod_array = [[0, 1, 2], [3, 4, 5]]
df = pd.DataFrame(twod_array)
print(df)

list_arr = {"A": ["Tokyo", "Nagano", "Osaka"], "B": [
        "Saitama", "Tochigi", "Ibaraki"]}
df = pd.DataFrame(list_arr)
print(df)

tup_arr = {"A": (1, 2, 3), "B": (4, 5, 6)}
df = pd.DataFrame(tup_arr)
print(df)

mix_dic = {"A": [1, 2, 3], "B": ["A", "B", "C"], "C": (1, 2, 3)}
df = pd.DataFrame(mix_dic)
print(df)

#pd.DataFrame(numpy_array)

state = pd.Series(["Tokyo", "Osaka", "Aichi", "Hiroshima", "Fukuoka"])
population = pd.Series([134543, 1234, 5553, 1234, 6423])
num_household = pd.Series([111, 333, 444, 555, 75465])
statistic = pd.DataFrame({
        "state": state,
        "population": population,
        "num_household": num_household}
)
print(statistic)

statistic_dict = {
        "Population":
            {"Tokyo": 1, "Osaka": 2, "Aichi": 3, "Hiroshima": 4, "Fukuoka": 5},
        "num_household":
            {"Osaka": 2, "Tokyo": 1, "Aichi": 3, "Fukuoka": 5, "Hiroshima": 4},
}
    
statistic2 = pd.DataFrame(statistic_dict)
print(statistic2)

df = pd.DataFrame([{"Tokyo": 1, "Osaka": 2, "Hiroshima": 3},
                   {"Osaka": 22, "Tokyo": 11, "Hiroshima": 33}
                   ], index=["num_household", "population"])
print(df)

df = pd.DataFrame([
        pd.Series([1, 2, 3], index=["Tokyo", "Osaka", "Nara"]),
        pd.Series([11, 22, 33], index=["Tokyo", "Osaka", "Nara"])
        ])
print(df)

df = pd.DataFrame([(1, 2, 3, 4), (1, 2, 3, 4)], index=["num_household", "population"], columns=["Tokyo", "Osaka", "Nara", "Shiga"])
print(df)


import numpy as np
import numpy.ma as ma

x = np.arange(10).reshape(2, 5)
mask = np.random.choice([0, 1], size=10).reshape(2, 5)
print(mask)
mx = ma.masked_array(x, mask=mask)
df = pd.DataFrame(mx)
print(df)

df = pd.DataFrame({
        "a": [1, 1, 0],
        "b": [0, 1, 0]}, dtype=bool
)
print(df)

df = pd.DataFrame({
        "a": [1, 1, 0],
        "b": [0, 1, 0]
        }, dtype=float
)
print(df)

df_2 = pd.DataFrame(df, copy=False)
df_3 = pd.DataFrame(df, copy=True)
df["c"] = df["a"] == df["b"]
print(df)
print(df_2)
print(df_3)

num_per_house = pd.Series({
        "Tokyo": 1.99, "Osaka": 2.22, "Aichi": 1.23, "Hiroshima": 0.23}
)
statistic2["num_per_house"] = num_per_house
print(statistic2)

series = pd.Series([0, 0, 0])
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], index =["a", "b"], columns=["new", "old", "now"])
print(df)
df["predict"] = series
print(df)

del df["predict"]
print(df)

rand_int = pd.DataFrame(np.random.randint(0, 10, 20).reshape(4, 5), index=["a", "b", "c", "d"], columns=["A", "B", "C", "D", "E"])
print(rand_int)
print(rand_int.loc["a", "B"])
print(rand_int.iloc[0, 1])
print(rand_int.A)
print(rand_int.loc[:, "B"])
print(rand_int[2:4])

print(df.columns)
print(df.style)
print(df.axes)