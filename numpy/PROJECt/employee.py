import pandas as pd
import numpy as np


df = pd.read_csv("c:/Ali/py/one/numpy/PROJECt/Employee.csv")

print(df.head())
print(df.isnull().sum())

# Check for duplicates before removal
print(f"\nNumber of duplicate rows before removal: {df.duplicated().sum()}")

# Remove duplicate rows and create a new DataFrame
df_cleaned = df.drop_duplicates()

# Check again after removal
print(f"Number of duplicate rows after removal: {df_cleaned.duplicated().sum()}")


print("\nMissing Values Count:")
print(df_cleaned.isnull().sum())


# Let's assume 'Salary' and 'Age' are numerical columns with missing values
if 'Salary' in df_cleaned.columns and df_cleaned['Salary'].isnull().any():
    median_salary = df_cleaned['Salary'].median()
    df_cleaned['Salary'].fillna(median_salary, inplace=True)
    print(f"\nMissing 'Salary' values filled with median: {median_salary}")

if 'Age' in df_cleaned.columns and df_cleaned['Age'].isnull().any():
    median_age = df_cleaned['Age'].median()
    df_cleaned['Age'].fillna(median_age, inplace=True)
    print(f"Missing 'Age' values filled with median: {median_age}")

# For categorical data (e.g., a 'Department' column), you might fill with the mode (most frequent value)
if 'Department' in df_cleaned.columns and df_cleaned['Department'].isnull().any():
    mode_department = df_cleaned['Department'].mode()[0]
    df_cleaned['Department'].fillna(mode_department, inplace=True)
    print(f"Missing 'Department' values filled with mode: {mode_department}")


    print("\nFinal Data Info after Preprocessing:")
df_cleaned.info()
print("\nFinal DataFrame Head:")
print(df_cleaned.head())



employee_salary= df['PaymentTier'].mean()
print(" employee " , employee_salary)