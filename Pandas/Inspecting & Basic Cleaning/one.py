import pandas as pd
import numpy as np
import json
import os

# -----------------------------------------------------------
# 📂 STEP 1: Load JSON dataset safely
# -----------------------------------------------------------
FILE = r"c:\Ali\py\one\Pandas\US_STATE_recipes.json"

print("File exists:", os.path.exists(FILE))
if not os.path.exists(FILE):
    raise FileNotFoundError("❌ JSON file not found! Please check the path.")

# Load JSON data
with open(FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Convert JSON → DataFrame
df = pd.DataFrame.from_dict(data, orient="index")  # keys become rows

print("✅ DataFrame Loaded Successfully!")
print("=" * 120)

# -----------------------------------------------------------
# 📊 STEP 2: Normalize nested columns (like 'nutrients')
# -----------------------------------------------------------
if 'nutrients' in df.columns:
    nutrients_df = pd.json_normalize(df['nutrients'])
    df = pd.concat([df.drop(columns=['nutrients']), nutrients_df], axis=1)
    print("✅ 'nutrients' column expanded into multiple columns!")

print("=" * 120)
print("📋 First 3 Rows:")
print(df.head(3))
print("=" * 120)
print("📋 Last 2 Rows:")
print(df.tail(2))
print("=" * 120)

# -----------------------------------------------------------
# 🧠 STEP 3: Info and Overview
# -----------------------------------------------------------
print("🧱 DataFrame Info:")
print(df.info())
print("=" * 120)

# -----------------------------------------------------------
# 📈 STEP 4: Describe Data (Numeric + All Columns)
# -----------------------------------------------------------
print("📊 Summary Statistics (Numeric Only):")
print(df.describe())
print("=" * 120)

print("📊 Summary Statistics (All Columns):")
print(df.describe(include='all'))
print("=" * 120)

# -----------------------------------------------------------
# 🔍 STEP 5: Data Types and Missing Values
# -----------------------------------------------------------
print("🧾 Data Types:")
print(df.dtypes)
print("=" * 120)

print("🔍 Missing Values per Column:")
print(df.isna().sum())
print("=" * 120)

# -----------------------------------------------------------
# 🧹 STEP 6: Basic Cleaning - Fix Missing Values
# -----------------------------------------------------------

# Fill NaN values with meaningful defaults
df['Country_State'].fillna("Unknown", inplace=True)
df['rating'].fillna(df['rating'].mean(), inplace=True)
df['cook_time'].fillna(0, inplace=True)
df['prep_time'].fillna(df['prep_time'].median(), inplace=True)

print("✅ Missing values handled!")
print("=" * 120)

# -----------------------------------------------------------
# 🔢 STEP 7: Convert Dtypes Automatically
# -----------------------------------------------------------
df = df.convert_dtypes()
print("✅ Data Types Optimized Automatically:")
print(df.dtypes)
print("=" * 120)

# -----------------------------------------------------------
# 📏 STEP 8: Shape, Columns, and Index
# -----------------------------------------------------------
print("📏 Shape (rows, columns):", df.shape)
print("📚 Columns:", df.columns.tolist())
print("🔢 Index:", df.index)
print("=" * 120)

# -----------------------------------------------------------
# 🧩 STEP 9: Quick Validation
# -----------------------------------------------------------
print("✅ Sample Cleaned Data:")
print(df.sample(3))
print("=" * 120)
