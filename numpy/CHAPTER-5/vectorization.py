import numpy as np
import time

print("=== Vectorization Examples ===\n")

# 1. Basic loop vs vectorized addition
arr1 = np.arange(1, 1000001)  # 1 to 1,000,000
arr2 = np.arange(1, 1000001)

# Python loop
start = time.time()
result_loop = [x + y for x, y in zip(arr1, arr2)]
end = time.time()
print("Loop time:", end - start)

# Vectorized
start = time.time()
result_vec = arr1 + arr2
end = time.time()
print("Vectorized time:", end - start, "\n")

# 2. Element-wise operations
arr = np.array([1, 2, 3, 4, 5])
print("arr^2:", arr ** 2)
print("sqrt(arr):", np.sqrt(arr))
print("arr * arr:", arr * arr, "\n")

# 3. Apply function (e.g., Celsius → Fahrenheit)
celsius = np.array([0, 20, 37, 100])
fahrenheit = (celsius * 9/5) + 32
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit, "\n")

# 4. Conditional vectorization (masking)
data = np.array([5, -3, 7, -1, 0])
print("Data:", data)
print("Replace negatives with 0:", np.where(data < 0, 0, data), "\n")

# 5. Vectorized distance calculation
# Distance = sqrt((x2-x1)^2 + (y2-y1)^2)
points1 = np.array([[1, 2], [3, 4], [5, 6]])
points2 = np.array([[7, 8], [9, 10], [11, 12]])
distances = np.sqrt(np.sum((points2 - points1) ** 2, axis=1))
print("Vectorized distances:", distances)
