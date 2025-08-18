# -----------------------------
# Python Tuple Examples
# -----------------------------

# Initial tuple
my_tuple = (10, 20, 30)

# -----------------------------
# Creating tuples
# -----------------------------
t1 = (1, 2, 3)
t2 = tuple([4, 5, 6])   # Convert list → tuple
t3 = (7,)               # Single-element tuple (needs comma!)
empty = ()              # Empty tuple

# -----------------------------
# Accessing elements
# -----------------------------
print(my_tuple[0])      # 10
print(my_tuple[-1])     # 30
print(my_tuple[1:])     # (20, 30) → slicing works like lists

# -----------------------------
# Tuple methods (only 2 exist)
# -----------------------------
print(my_tuple.count(20))   # Count occurrences
print(my_tuple.index(30))   # Get index of first occurrence

# -----------------------------
# Iterating
# -----------------------------
for item in my_tuple:
    print("Item:", item)

for i, v in enumerate(my_tuple):
    print(f"Index {i} -> Value {v}")

# -----------------------------
# Unpacking
# -----------------------------
a, b, c = my_tuple
print(a, b, c)   # 10 20 30

x, y, *rest = (1, 2, 3, 4, 5)
print(x, y, rest)  # 1 2 [3, 4, 5]

# -----------------------------
# Nesting and immutability
# -----------------------------
nested = ((1, 2), (3, 4))
print(nested[0][1])  # 2

# Tuples are immutable → but can contain mutable objects:
t_with_list = (1, [2, 3])
t_with_list[1].append(4)
print(t_with_list)  # (1, [2, 3, 4])

# -----------------------------
# Useful built-in functions
# -----------------------------
print(len(my_tuple))    # Number of elements
print(max(my_tuple))    # Largest
print(min(my_tuple))    # Smallest
print(sum(my_tuple))    # Sum (if numeric)

# -----------------------------
# Conversions
# -----------------------------
as_list = list(my_tuple)   # Convert to list (to modify)
back_to_tuple = tuple(as_list)

# -----------------------------
# Concatenation & repetition
# -----------------------------
t4 = (1, 2) + (3, 4)     # (1, 2, 3, 4)
t5 = ("a",) * 3          # ('a', 'a', 'a')

# -----------------------------
# Membership test
# -----------------------------
print(20 in my_tuple)    # True
print(50 not in my_tuple) # True
