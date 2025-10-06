import pandas as pd
import numpy as np
import json
import os


FILE = "c:/Ali/py/one/Pandas/US_STATE_recipes.json"  
print("✅ File Exists:", os.path.exists(FILE))

# TODO: load the JSON file into a DataFrame
# HINT: use `json.load()` and `pd.DataFrame.from_dict()`
with open(FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame.from_dict(data, orient="index")

# -------------------------------
# 2️⃣ BASIC INSPECTION
# -------------------------------
print("\n🔹 HEAD:")
print(df.head(5))

print("\n🔹 TAIL:")
print(df.tail(3))

print("\n🔹 INFO:")
print(df.info())

print("\n🔹 DESCRIBE (numeric):")
print(df.describe())

print("\n🔹 DESCRIBE (all):")
print(df.describe(include="all"))

print("\n🔹 SHAPE:", df.shape)
print("🔹 COLUMNS:", df.columns.tolist())
print("🔹 INDEX:", df.index)

# -------------------------------
# 3️⃣ MISSING VALUE CHECK
# -------------------------------
print("\n🧩 Missing Values:")
print(df.isna().sum())

# TODO: Fill missing numeric columns with mean or median
df["rating"].fillna(df["rating"].mean(), inplace=True)

# TODO: Fill missing text columns with "Unknown" or "Not Provided"
df["Country_State"].fillna("Unknown", inplace=True)

print("\n✅ Missing Values After Cleaning:")
print(df.isna().sum())

# -------------------------------
# 4️⃣ DATA TYPE CONVERSION
# -------------------------------
print("\n📋 Before Conversion:")
print(df.dtypes)

# TODO: Convert all columns to best possible dtypes automatically
df = df.convert_dtypes()

# Optional manual conversion example:
df["rating"] = df["rating"].astype(float)

print("\n📋 After Conversion:")
print(df.dtypes)

# -------------------------------
# 5️⃣ HANDLE NESTED JSON COLUMNS (like 'nutrients')
# -------------------------------
if "nutrients" in df.columns:
    print("\n🥣 Normalizing 'nutrients' column...")
    nutrients_df = pd.json_normalize(df["nutrients"])
    df = pd.concat([df.drop(columns=["nutrients"]), nutrients_df], axis=1)

print("\n✅ Final Columns:", df.columns.tolist())

# -------------------------------
# 6️⃣ SAVE CLEANED DATA
# -------------------------------
output_path = "c:/Ali/py/one/Pandas/cleaned_recipes.csv"
df.to_csv(output_path, index=False)
print("\n💾 Cleaned dataset saved at:", output_path)
print("📏 Final Shape:", df.shape)

# ===============================================================
# 🐞 DEBUG TASK — Intentional Bugs Below
# ===============================================================

print("\n\n🐞 DEBUG TASK — Find and Fix the Bugs")

try:
    print(df.head())

    # BUG 1: wrong syntax
    df['rating'].fillna(df['rating'].mean , index=False)

    # BUG 2: wrong assignment for fillna
    df['Country_State'].fillna('Unknown' , inplace=True)

    # BUG 3: wrong function name
    df = df.convert_dtype()

    print(df.isnan().sum())

except Exception as e:
    print("🚨 Error Found:", e)
