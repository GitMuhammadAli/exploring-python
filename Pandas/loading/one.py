import pandas as pd
import numpy as np
import json
import os

FILE = "c:/Ali/py/one/Pandas/US_STATE_recipes.json"
print("exists:", os.path.exists(FILE))
with open(FILE, "r", encoding="utf-8") as f:
    data = json.load(f)         
df = pd.DataFrame.from_dict(data, orient="index")  # keys become rows




if 'serves' in df.columns:
   nut = pd.json_normalize(df['nutrients'])
   df = pd.concat([df.drop(columns=['nutrients']), nut], axis=1)


print (df)
print("*" *100)
print(df.head(3))
print("*" *100)
print(df.tail(2))
print("*" *100)
print(df.info())
print("*" *100)
print(df.describe())
print("*" *100)
print(df.describe(include='all'))
print("*" *100)
print(df.dtypes)
print("*" *100)
print(df.isna().sum())
