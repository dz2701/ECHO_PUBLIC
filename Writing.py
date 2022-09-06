from t2 import std
import numpy as np
import pandas as pd
import pygsheets

new = []
for i in range(1,len(std)):
    new.append([std[i].Timestamp,
    std[i].Email,
    std[i].Last,
    std[i].First,
    std[i].PName,
    std[i].Year,
    std[i].FallS,
    std[i].WinterS,
    std[i].SpringS,
    std[i].Backup,
    std[i].conf1,
    std[i].conf2,
    std[i].conf3,
    std[i].c1,
    std[i].c2])

new = pd.DataFrame(new)
df = new.to_csv(r'results.csv',encoding = "utf-8")
