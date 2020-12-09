# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 22:37:08 2020

@author: s1430
"""


import pandas as pd

df = pd.read_csv("c02.csv", encoding="shift_jis")
print(df.head())
population = df[df["年齢5歳階級"] == "総数"]
print(population.head())

population = population[["西暦（年）", "人口（総数）"]]
population.columns = ["Year", "Population"]
print(population.head())

import matplotlib.pyplot as plt

population = population.set_index("Year")
population.plot()
plt.xlabel("Year")
plt.ylabel("Population")
plt.grid()
plt.show()

import statsmodels.api as sm

model = sm.OLS(population.population, sm.add_constant(population.index)).fit()
model.params
