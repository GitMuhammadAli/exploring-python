import numpy as np

# -------------------------
# 1. Sorting
# -------------------------
arr = np.array([5, 2, 9, 1, 7])
sorted_arr = np.sort(arr)     # returns a sorted copy
print("Original:", arr)
print("Sorted:", sorted_arr)

# 2D Sorting (row-wise)
mat = np.array([[5, 2, 9], [1, 7, 3]])
print("\nOriginal Matrix:\n", mat)
print("Row-wise Sort:\n", np.sort(mat, axis=1))
print("Column-wise Sort:\n", np.sort(mat, axis=0))


# -------------------------
# 2. Argsort (Get Indices)
# -------------------------
arr2 = np.array([50, 10, 40, 20])
indices = np.argsort(arr2)   # returns indices of sorted order
print("\nArray:", arr2)
print("Sorted Indices:", indices)
print("Values in Sorted Order:", arr2[indices])


# -------------------------
# 3. Argmax / Argmin
# -------------------------
arr3 = np.array([5, 8, 2, 9, 1])
print("\nArray:", arr3)
print("Index of Max:", np.argmax(arr3))
print("Index of Min:", np.argmin(arr3))


# -------------------------
# 4. Conditional Search
# -------------------------
arr4 = np.array([10, 20, 30, 40, 50])
cond = np.where(arr4 > 25)   # indices where condition is True
print("\nArray:", arr4)
print("Indices where > 25:", cond)
print("Values > 25:", arr4[cond])
