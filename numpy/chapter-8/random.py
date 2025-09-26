import numpy as np

# -------------------------
# 1. Random Integers
# -------------------------
rand_ints = np.random.randint(1, 10, size=5)  # 5 random numbers from 1–9
print("Random Integers:", rand_ints)

# 2D array of random ints
rand_matrix = np.random.randint(0, 100, size=(3, 3))
print("\nRandom 3x3 Matrix:\n", rand_matrix)


# -------------------------
# 2. Random Floats
# -------------------------
rand_floats = np.random.rand(5)   # uniform [0,1)
print("\nRandom Floats (0–1):", rand_floats)

rand_floats2 = np.random.uniform(5, 10, size=5)  # between 5–10
print("Random Floats (5–10):", rand_floats2)


# -------------------------
# 3. Normal Distribution
# -------------------------
normal_dist = np.random.randn(5)  # mean=0, std=1
print("\nNormal Distribution:", normal_dist)

normal_custom = np.random.normal(loc=50, scale=5, size=10)  # mean=50, std=5
print("Custom Normal Distribution:", normal_custom)


# -------------------------
# 4. Shuffling
# -------------------------
arr = np.arange(10)
np.random.shuffle(arr)
print("\nShuffled Array:", arr)


# -------------------------
# 5. Seed (Reproducibility)
# -------------------------
np.random.seed(42)
print("\nRandom with Seed:", np.random.randint(0, 100, size=5))
