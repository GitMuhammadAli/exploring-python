import numpy as np

# -------------------------
# 1. Save & Load (Binary .npy)
# -------------------------
arr = np.arange(10)
np.save("array.npy", arr)   # saves in NumPy format
loaded_arr = np.load("array.npy")
print("Original:", arr)
print("Loaded from .npy:", loaded_arr)


# -------------------------
# 2. Save & Load Multiple Arrays (Compressed .npz)
# -------------------------
a = np.arange(5)
b = np.arange(10, 15)
np.savez("multi_arrays.npz", first=a, second=b)

data = np.load("multi_arrays.npz")
print("\nFirst Array:", data["first"])
print("Second Array:", data["second"])


# -------------------------
# 3. Save & Load Text Files (.txt / .csv)
# -------------------------
mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
np.savetxt("matrix.txt", mat, delimiter=",", fmt="%d")

loaded_txt = np.loadtxt("matrix.txt", delimiter=",", dtype=int)
print("\nSaved Matrix:\n", mat)
print("Loaded from txt:\n", loaded_txt)
