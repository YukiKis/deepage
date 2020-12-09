# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 22:15:51 2020

@author: s1430
"""


import pandas as pd

sr = pd.Series(range(10))
sr.rolling(3)

print(sr.rolling(3).sum())

print(sr.rolling(3, min_periods=1).sum())

print(sr.rolling(3, center=True).sum())

index = pd.date_range("1/1/2018", periods=20)
print(index)
sr_time = pd.Series(range(20), index=index)
print(sr_time)
print(sr_time.rolling("3D").sum())
print(sr_time.rolling("7D").sum())

print(sr.rolling(5, win_type="triang").sum())
print(sr.rolling(5).sum())

import numpy as np

random_walk = np.random.choice([-1, 1], size=1000)
random_walk = random_walk.cumsum()
random_sr = pd.Series(random_walk)

import matplotlib.pyplot as plt

random_sr.plot()
plt.xlabel("time")
#Text(0.5, 0, "time")
plt.ylabel("walk")
#Text("walk")
plt.title("RandomWalk")
#Text(0.5, 1, "Randomwalk")
plt.grid()
plt.legend()
plt.show()

roll_mean = random_sr.rolling(500).mean()
random_sr.name = "Original"
roll_mean.name = "Rolled"
print(roll_mean)

random_sr.plot()
roll_mean.plot()
plt.legend()
plt.xlabel("Time")
plt.ylabel("Walk")
plt.grid()
plt.title("RandomWlak")
plt.savefig("random_walk_rolling.png")
plt.show()