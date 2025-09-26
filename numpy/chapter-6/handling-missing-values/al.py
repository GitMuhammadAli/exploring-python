import numpy as np

print("=== Handling Missing Values in NumPy ===\n")

# --------------------------
# 1. Creating arrays with NaN
# --------------------------
arr = np.array([1, 2, np.nan, 4, np.nan])
print("Original array:", arr)

# Check for NaN
print("Is NaN:", np.isnan(arr))

# Count NaNs
print("Number of NaNs:", np.sum(np.isnan(arr)), "\n")


# --------------------------
# 2. Replacing NaN with a value
# --------------------------
# Replace NaN with 0
arr_filled = np.nan_to_num(arr, nan=0)
print("Replace NaN with 0:", arr_filled)

# Replace NaN with mean of non-NaN values
mean_val = np.nanmean(arr)
arr_mean_filled = np.where(np.isnan(arr), mean_val, arr)
print("Replace NaN with mean:", arr_mean_filled, "\n")


# --------------------------
# 3. Handling infinite values
# --------------------------
arr_inf = np.array([1, np.inf, -np.inf, 4])
print("Original array with inf:", arr_inf)

# Check for inf
print("Is infinite:", np.isinf(arr_inf))

# Replace inf with large finite number or 0
arr_no_inf = np.nan_to_num(arr_inf, posinf=999, neginf=-999)
print("Replace inf values:", arr_no_inf, "\n")


# --------------------------
# 4. Filtering valid values
# --------------------------
valid = arr[~np.isnan(arr)]
print("Only valid numbers (no NaN):", valid, "\n")


# --------------------------
# 5. Combining NaN handling with arithmetic
# --------------------------
arr1 = np.array([1, np.nan, 3])
arr2 = np.array([4, 5, np.nan])

# Add arrays, treating NaN as 0
result = np.nan_to_num(arr1) + np.nan_to_num(arr2)
print("Sum treating NaN as 0:", result, "\n")


# --------------------------
# 6. Detecting unrealistic/outlier values
# --------------------------
salaries = np.array([50000, 60000, -1000, 70000, 1000000])
# Replace negative salaries with mean
mean_salary = np.mean(salaries[salaries > 0])
cleaned_salaries = np.where(salaries < 0, mean_salary, salaries)
print("Replace negative salaries:", cleaned_salaries)

# Cap extreme outliers (e.g., > 3 std dev)
std_val = np.std(cleaned_salaries)
mean_val = np.mean(cleaned_salaries)
capped_salaries = np.clip(cleaned_salaries, mean_val - 3*std_val, mean_val + 3*std_val)
print("Capped extreme outliers:", capped_salaries)
