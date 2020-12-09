# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 22:55:18 2020

@author: s1430
"""


import pandas as pd

str1 = "2020/04/07"
print(pd.to_datetime(str1))

t_str = "20190407"
print(pd.to_datetime(t_str))

time_sr = pd.Series([20181024, 20200915, 20210111])
convert_time = pd.to_datetime(time_sr, format="%Y%m%d")
print(convert_time)

time_sr_2 = pd.Series(["181024 13:24", "200915 07:59", "210111 23:45"])
print(pd.to_datetime(time_sr_2, format="%y%m%d %H:%M"))
time_j = "2018年11月12日　05時25分"
print(pd.to_datetime(time_j, format="%Y年%m月%d日　%H時%M分"))

print(pd.to_datetime(1527417500, unit="s"))
print(pd.to_datetime(1537234898, unit="s").tz_localize("utc").tz_convert("Asia/Tokyo"))
utc_time = pd.to_datetime(1111111111, unit="s", utc=True)
print(utc_time)
print(utc_time.tz_convert("Asia/Tokyo"))

long_t = pd.Series(["3/11/2000", "3/12/2000", "3/13/2000"] * 2000)

pd.to_datetime(long_t, infer_datetime_format=False)
pd.to_datetime(long_t, infer_datetime_format=True)

df = pd.DataFrame({
        "year": [1998, 2012, 1990, 2018],
        "month": [10, 1, 10, 12],
        "day": [10, 11, 21, 11],
        "hour": [12, 23, 14, 1],
        "minute": [29, 3, 30, 59]}
)
print(pd.to_datetime(df))