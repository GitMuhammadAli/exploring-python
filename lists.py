# -----------------------------
# Python List Examples
# -----------------------------

# Initial list
my_list = [12]

# -----------------------------
# Adding elements
# -----------------------------
my_list.append(20)        # Add single element at the end
my_list.extend([30, 40])  # Add multiple elements
my_list.insert(1, 15)     # Insert at specific index

# -----------------------------
# Removing elements
# -----------------------------
my_list.remove(30)        # Remove first occurrence of a value
popped = my_list.pop()    # Remove last element and return it
popped_at_index = my_list.pop(0)  # Remove element at index 0
# my_list.clear()         # Remove all elements (uncomment to use)

# -----------------------------
# Searching / checking
# -----------------------------
print(20 in my_list)      # Check if element exists
print(my_list.index(20))  # Get index of first occurrence
print(my_list.count(20))  # Count occurrences of a value

# -----------------------------
# Sorting and reversing
# -----------------------------
nums = [5, 3, 8, 1]
nums.sort()               # Ascending
nums.sort(reverse=True)   # Descending
nums.reverse()            # Reverse order (not sort)

# -----------------------------
# Copying
# -----------------------------
copy1 = my_list.copy()        # Shallow copy
copy2 = my_list[:]            # Slice copy
copy3 = list(my_list)         # Using list() constructor

# -----------------------------
# Iterating
# -----------------------------
for item in my_list:
    print("Item:", item)

for i, v in enumerate(my_list):
    print(f"Index {i} -> Value {v}")

# -----------------------------
# List comprehensions
# -----------------------------
squares = [x**2 for x in range(5)]          # [0,1,4,9,16]
evens = [x for x in range(10) if x % 2 == 0] # even numbers

# -----------------------------
# Useful functions with lists
# -----------------------------
print(len(my_list))    # Number of elements
print(sum(nums))       # Sum of elements
print(max(nums))       # Largest element
print(min(nums))       # Smallest element

# -----------------------------
# Nested lists (Matrix)
# -----------------------------
matrix = [
    [1, 3, 2],
    [2, 3, 4],
    [9, 8, 7]
]

# Accessing
print(matrix[0][1])  # 3
print(matrix[2][2])  # 7

# Flatten a matrix
flat = [num for row in matrix for num in row]
print(flat)

# -----------------------------
# Joining & Splitting
# -----------------------------
chars = ["a", "b", "c"]
word = "".join(chars)   # "abc"
split_back = list(word) # ['a','b','c']

# -----------------------------
# Unpacking
# -----------------------------
a, b, *rest = [10, 20, 30, 40, 50]
print(a, b, rest)  # 10 20 [30, 40, 50]


newL = [2,3,45,61,2,3,5,66,7,66]
li = []
for i in newL:
    if i not in li:
        li.append(i)
print(li)    