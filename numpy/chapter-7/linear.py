import numpy as np

# -------------------------
# 1. Dot Product
# -------------------------
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot = np.dot(a, b)   # 1*4 + 2*5 + 3*6 = 32
print("Dot Product:", dot)

# -------------------------
# 2. Matrix Multiplication
# -------------------------
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

matmul1 = np.matmul(A, B)   # same as A @ B
matmul2 = A @ B
print("\nMatrix Multiplication:\n", matmul1)
print("Using @ operator:\n", matmul2)

# -------------------------
# 3. Determinant
# -------------------------
det_A = np.linalg.det(A)
print("\nDeterminant of A:", det_A)

# -------------------------
# 4. Inverse
# -------------------------
inv_A = np.linalg.inv(A)
print("\nInverse of A:\n", inv_A)

# -------------------------
# 5. Eigenvalues & Eigenvectors
# -------------------------
eigvals, eigvecs = np.linalg.eig(A)
print("\nEigenvalues:", eigvals)
print("Eigenvectors:\n", eigvecs)

# -------------------------
# 6. Norm (Length of Vector)
# -------------------------
vec = np.array([3,4])
norm = np.linalg.norm(vec)  # sqrt(3^2 + 4^2) = 5
print("\nNorm of vector:", norm)
