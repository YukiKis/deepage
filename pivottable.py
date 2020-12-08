# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:56:34 2020

@author: s1430
"""


import pandas as pd
import numpy as np

df = pd.read_csv("train.csv")
df.columns
pd.pivot_table(df, values="Age", index="Survived", columns="Embarked", aggfunc="mean")
pd.pivot_table(df, values="Age", index=["Pclass", "Embarked"], columns="Survived")
df.pivot_table(index="Survived", columns="Embarked", aggfunc="count")
df.pivot_table(values="Age", index="Survived", columns="Embarked", aggfunc="count", margins=True)
df.pivot_table(values="Age", index="Survived", coluns="Embarked", aggfunc="count", margins=True, margins_name="TOTAL")
df.pivot_table(values="Age", index="Survived", columns="Embarked", aggunc=["count", "mean"])
df.pivot_table(values="Age", index="Survived", columns="Embarked", aggfunc=[np.mean, np.std])

pd.pivot_table(df, values="Age", index="Cabin", columns="Embarked")
pd.pivot_table(df, values="Age", index="Cabin", columns="Embarked", fill_value=0)
pd.pivot_table(df, values="Age", index="Cabin", columns="Embarked", dropna=False)