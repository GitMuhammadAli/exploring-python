import pandas as pd
import numpy as np
import json

FILE = "c:/Ali/py/one/Pandas/US_STATE_recipes.json"

with open(FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame.from_dict(data, orient="index")
print(df.describe(include='all'))
if 'serves' in df.columns:
    nut = pd.json_normalize(df['nutrients'])
    df = pd.concat([df.drop(columns=['nutrients']), nut], axis=1)

df['rating'].fillna(df['rating'].mean(), inplace=True)
df['Country_State'].fillna('Unknown', inplace=True)
df = df.convert_dtypes()


high_rated = df[df['rating'] > 4.7]
print(high_rated[['title', 'rating']].head())

print("*" * 100)

quick_best = df[(df['rating'] > 4.5) & (df['total_time'] < 60)]
print(quick_best[['title', 'rating', 'total_time']].head())

print("*" * 100)
