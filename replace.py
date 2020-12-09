# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:46:32 2020

@author: s1430
"""


import pandas as pd

sr = pd.Series(range(7))

print(sr.replace(3, 10))

print(sr.replace([0, 1, 2, 3], -99))

df = pd.DataFrame({
        "A": [0, 1, 2, 3],
        "B": [4, 5, 6, 7],
        "C": ["a", "b", "c", "d"]}
)
print(df.replace([0, 1, "a"], -99))
print(df.replace((0, 1, "a"), -99))

print(sr.replace({0: -1, 1: -2, 2: -3}))
#print(sr.replace({0: "b", "a": -20}))
print(sr.replace([0, 1, 2], [-1, -2, -3]))
#print(sr.replace([0, "a"], ["b", -20]))

df_2 = pd.DataFrame({
        "A": [0, 1, 2],
        "B": [0, 1, 2],
        "C": [0, 1, 2]}
)
print(df_2.replace(0, {"A": "a", "B": "b", "C": "c"}))

df_3 = pd.DataFrame({
        "A": ["Syslog", "Syslog", "Syslog", "Syslog"],
        "B": ['PD380_003 %LINK-3-UPDOWN','NM380_005 %BGP-5-NBR_RESET','NM380_005 %BGP-5-NBR_RESET','DO NOT TICKET LO380_004 %SYS-5-CONFIG_I Config']}
)
print(df_3.replace("^.*([A-Z]{2}[0-9]{3}_[0-9]{3}).*$", {"B": r"\1"}, regex=True))

data = pd.Series([0, 1, 3, -999, -999, 5, 2, -999, -999, 1])
print(data.replace(-999))
print(data.replace(-999, method="bfill"))
print(data.replace(-999, method="ffill", limit=2))