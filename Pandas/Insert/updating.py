import pandas as pd
import numpy as np
import json

FILE = "c:/Ali/py/one/Pandas/US_STATE_recipes.json"

with open(FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame.from_dict(data, orient="index")
print(df.describe(include='all'))
print("*" * 100)

print(df['rating'].isna().sum())
print("*" * 100)
df.loc[df['rating'].isna(), 'rating'] = df['rating'].mean()
print(df[['title', 'rating']])
print("*" * 100)
print(df['rating'].isna().sum())

print("*" * 100)


