# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 16:22:46 2020

@author: s1430
"""


import pandas
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")
del df["Name"], df["Ticket"], df["Cabin"]
df.hear()

from pylab import rcParams
rcParams["figure.figsize"] = 10, 10

df.hist()
plt.tight_layout()
plt.show()

df = pd.read_csv("train.csv")
df["Age"].hist(bins=20)
plt.savefifg("age_bins.png")
plt.show()

df["Age"].hist(by=df["Sex"])

df["Embarked"].value_counts()

df["Embarked"].value_counts().plot(kind="bar")
plt.show()