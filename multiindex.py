# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:57:02 2020

@author: s1430
"""


import pandas as pd

df = pd.read_csv("sample_news.csv", index_col=[0, 1, 2, 3])
print(df)

df = pd.read_csv("sample_news.csv", index_col=[0, 1])
print(df)

news_list = df.sort_index(level=0)
print(df)
print(news_list)
news_list = news_list.sort_index(level=1)
print(news_list)

arrays = [["foo", "foo", "bar", "bar", "baz", "baz"],
          ["A", "B", "A", "B", "A", "B"]
          ]
tuples = list(zip(*arrays))
print(tuples)

index = pd.MultiIndex.from_tuples(tuples, names=["grade", "class"])
print(index)

import numpy as np
series = pd.Series(np.random.randn(6), index=index)
print(series)

# pd.Multindex.from_product(iterables, name=["grade", "class"])

arrays = [["foo", "foo", "bar", "bar", "baz", "baz"], 
          ["A", "B", "A", "B", "A", "B"]
          ]
series2 = pd.Series(np.random.randn(6), index=arrays)
print(series2)

tuples = [("foo", "A"), ("foo", "B"), ("bar", "A"), ("bar", "B"), ("baz", "A"), ("baz", "B")]

print(series2.index)

series2.index = series2.index.rename(["grade", "class"])
print(series2)

news_list = pd.read_csv("sample_news.csv")
print(news_list)

news_list = news_list.set_index(["genre", "year"])
print(news_list)
news_list = news_list.T
print(news_list)
print(news_list["sports"])
print(news_list["sports"][2016])

news_list = news_list.T
print(news_list.loc[("sports", 2016), "title"])
news_list.loc["music", "title"]