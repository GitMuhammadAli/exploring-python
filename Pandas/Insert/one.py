import pandas as pd
import numpy as np
import json

FILE = "c:/Ali/py/one/Pandas/US_STATE_recipes.json"

with open(FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame.from_dict(data, orient="index")
print(df.describe(include='all'))
print("*" * 100)



# Add a new column (like SQL computed column)
df['rating_percent'] = df['rating'] * 20
print(df[['title', 'rating', 'rating_percent']].head())
print("*" * 100)

df.rename(columns={'Contient': 'Continent', 'cuisine': 'Cuisine_Type'}, inplace=True)
print(df[['title', 'Continent', 'Cuisine_Type']].head())
print("*" * 100)

# Filter all recipes whose title contains “chicken”
chicken_recipes = df[df['title'].str.contains("chicken", case=False, na=False)]
print(chicken_recipes[['title', 'rating']].head())
print("*" * 100)



# Assignment (Small Practice)

# Add a new column cook_ratio = df['cook_time'] / df['total_time'] (rounded to 2 decimals).

# Create a difficulty column:

# "Easy" if total_time < 30

# "Medium" if between 30 and 90

# "Hard" otherwise.

# Replace any missing rating with the mean rating.

# Find the top 5 easiest & highest-rated recipes.

print("*" * 100)

# Your code here
df['cook_ratio'] = (df['cook_time'] / df['total_time']).round(2)
def difficulty_level(total_time):
    if total_time < 30:
        return "Easy"
    elif 30 <= total_time <= 90:
        return "Medium"
    else:
        return "Hard"
    
df['difficulty'] = df['total_time'].apply(difficulty_level)
df['rating'].fillna(df['rating'].mean(), inplace=True)
easiest_highest_rated = df[df['difficulty'] == 'Easy'].sort_values(by='rating', ascending=False).head(5)
print(easiest_highest_rated[['title', 'rating', 'difficulty']])
