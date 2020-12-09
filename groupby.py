# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:40:08 2020

@author: s1430
"""


import pandas as pd

df = pd.read_csv("sample_group.csv")
print(df)

class_groupby = df.groupby("class")
print(class_groupby)
print(class_groupby.groups)
print(class_groupby.get_group("A"))

multi_groupby = df.groupby(["class", "sex"])
print(multi_groupby)
print(multi_groupby.groups)
print(multi_groupby.get_group(("A", "F")))

index_df = df.set_index("class")
print(index_df)

index_groupby2 = index_df.groupby("class")
print(index_groupby2.groups)

multi_df = df.set_index(["class", "sex"])
print(multi_df)

in_df = multi_df.groupby(level="sex")
print(in_df)

in_df_2 = multi_df.groupby("sex")

multi_in_group = multi_df.groupby(level=[0, 1])
print(multi_in_group.groups)

class_groupby = df.groupby("class")
print(class_groupby)
print(class_groupby.groups)
print(class_groupby.get_group("A"))

for name, group in class_groupby:
    print(name)
    print(group)
    
print(class_groupby["weight"].mean())

class_groupby = df.groupby("class")
print(class_groupby.mean())
print(class_groupby.max())
print(class_groupby.min())
print(class_groupby.std())
print(class_groupby.count())

print(class_groupby.describe().stack())

print(multi_in_group.mean())
print(multi_in_group.max())
print(multi_in_group.describe().stack())

def max_min(group):
    return group.max() - group.min()

print(df.groupby("class")[["weight", "height"]].min())

def stats(group):
    return {"Mean": group.mean(), "Max": group.max(), "Min": group.min(), "Count": group.count()}

print((df.groupby("sex")["time"].apply(stats)))

print(df.groupby("class")["weight"].agg([np.sum, np.mean]))
print(df.groupby("class").agg({"weight": np.mean, "height": np.max, "time": lambda x:np.std(x)}))

zscore = lambda x: (x - x.mean() / x.std())
print(df.groupby("class")["weight"].transform(zscore))
print(df["weight"].transform(zscore))
print(df.groupby("class")["weight"].filter(lambda x: x.min() > x.max() / 1.3))
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)
df.groupby("class")[["weight", "height", "time"]].max().plot.bar(ax = ax)
fig.savefig("group_sum.png")