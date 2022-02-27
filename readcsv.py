#!/bin/python3

import pandas as pd

df = pd.read_csv("channel-01.csv")
ch = df[" channel"].unique()
bssid = df["BSSID"].unique()
result = []
zip_obj = zip(ch, bssid)
for e1, e2 in zip_obj:
    se1 = e1.strip()
    se2 = e2.strip()
    ans = f"{se2} {se1}"
    result.append(ans)
for i in result:
    data = i.split(" ")
    if mac in data:
        sub
