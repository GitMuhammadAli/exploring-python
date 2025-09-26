import numpy as np

print("=== Broadcasting Examples ===\n")

# 1. Scalar with array
arr = np.array([1, 2, 3, 4])
print("Original 1D:", arr)
print("arr + 5:", arr + 5)
print("arr * 2:", arr * 2, "\n")

# 2. Row broadcasting
mat = np.array([[1, 2, 3],
                [4, 5, 6]])
row = np.array([10, 20, 30])
print("Matrix:\n", mat)
print("Add row:", mat + row, "\n")

# 3. Column broadcasting
col = np.array([[100],
                [200]])
print("Add column:\n", mat + col, "\n")

# 4. Shape (3,1) with (3,) → expand
A = np.ones((3, 1))
B = np.arange(3)
print("A shape:", A.shape, "B shape:", B.shape)
print("A + B:\n", A + B, "\n")

# 5. 1D reshaped → 2D
arr2 = np.array([1, 2, 3, 4]).reshape(4, 1)   # shape (4,1)
row2 = np.array([10, 20, 30, 40]).reshape(1, 4)  # shape (1,4)
print("Sum table (4x4):\n", arr2 + row2, "\n")

# 6. Incompatible shapes
try:
    a = np.array([1, 2, 3])       # shape (3,)
    b = np.array([[1, 2], [3, 4]])  # shape (2,2)
    print(a + b)  # fails
except ValueError as e:
    print("Incompatible shapes error:", e, "\n")
