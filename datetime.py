# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 23:10:52 2020

@author: s1430
"""


import datetime
import pandas as pd

time = datetime.datetime.now()
print(time)

t1 = pd.Timestamp(2018, 12, 18)
print(t1)

t2 = pd.Timestamp(year=2018, month=12, day=19, hour=23, minute=12, second=32)

t3 = pd.Timestamp(1111111111, unit="s")
print(t3)

t4 = pd.Timestamp(1111111111, unit="s", tz="Asia/Tokyo")

print(pd.to_datetime("2018-12-11"))
print(pd.to_datetime("2018/02/12 12:21+0900"))
print(pd.to_datetime("09/21/2018 03:34"))
print(pd.to_datetime("2018年8月8日 15時32分", format="%Y年%m月%d日 %H時%M分"))

print(pd.date_range("2016-04-01", "2020-12-09", freq="D"))
time_idx = pd.date_range("2018/9/21", periods=3, freq="W")
print(time_idx)
type(time_idx[0])

t5 = pd.Timestamp(2020, 12, 9, 23, 19, 23, 12, 30000, 12222)
print(t5)
print(t5.year)
print(t5.month)
print(t5.day)
print(t5.hour)
print(t5.minute)
print(t5.second)
print(t5.nanosecond)
print(t5.dayofweek)
print(t5.dayofyear)
print(t5.week)
print(t5.weekofyear)
print(t5.days_in_month)
print(t5.is_leap_year)
print(t5.is_month_end)
print(t5.is_month_start)
print(t5.is_quarter_end)
print(t5.is_quarter_start)
print(t5.is_year_end)
print(t5.is_year_start)

t_tz = pd.Timestamp("2018-12-13 12:00")
print(t_tz.tzinfo)
t_tz = t_tz.tz_localize("utc")
print(t_tz)

import pytz
print(pytz.all_timezones)

t_tz = t_tz.tz_convert("Asia/Tokyo")
print(t_tz)
t_tz = t_tz.tz_convert("America/Chicago")
print(t_tz)

t_tz.tz_localize(None)
t_tz.tz_convert(None)

import pandas.tseries.offsets as offsets

t = pd.Timestamp(2018, 12, 10)
#print(t + offsets.Day(3))
#print(t - offsets.Day(3))
#print(t + offsets.Hour(3))
#print(t + offsets.YearEnd)

delta = t - pd.Timestamp(2018, 12, 5, 22, 32)
print(delta)
print(t_tz + delta)
