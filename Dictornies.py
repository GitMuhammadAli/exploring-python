# -----------------------------
# Python Dictionary Examples
# -----------------------------

# Initial dictionary
my_dict = {"name": "Ali", "age": 25, "city": "Lahore"}

# -----------------------------
# Accessing values
# -----------------------------
print(my_dict["name"])        # Ali
print(my_dict.get("age"))     # 25
print(my_dict.get("country", "Pakistan"))  # Default if key not found

# -----------------------------
# Adding & Updating
# -----------------------------
my_dict["job"] = "Developer"   # Add new key
my_dict["age"] = 26            # Update value
my_dict.update({"city": "Karachi", "country": "Pakistan"})

# -----------------------------
# Removing
# -----------------------------
my_dict.pop("job")             # Remove by key
my_dict.pop("unknown", None)   # Safe remove with default
removed = my_dict.popitem()    # Remove last inserted item
# my_dict.clear()              # Remove all items (uncomment to use)

# -----------------------------
# Dictionary Views
# -----------------------------
print(my_dict.keys())      # dict_keys([...])
print(my_dict.values())    # dict_values([...])
print(my_dict.items())     # dict_items([...]) -> (key, value) pairs

# Iterating over keys
for key in my_dict:
    print(key, "->", my_dict[key])

# Iterating over values
for value in my_dict.values():
    print("Value:", value)

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(f"{key} = {value}")

# -----------------------------
# Membership test
# -----------------------------
print("name" in my_dict)   # True
print("salary" not in my_dict) # True

# -----------------------------
# Copying
# -----------------------------
copy1 = my_dict.copy()
copy2 = dict(my_dict)      # Equivalent

# -----------------------------
# Dictionary comprehensions
# -----------------------------
squares = {x: x**2 for x in range(5)}   # {0:0, 1:1, 2:4, 3:9, 4:16}
evens = {x: "even" for x in range(6) if x % 2 == 0}

# -----------------------------
# Nested dictionaries
# -----------------------------
students = {
    "Ali": {"age": 25, "grade": "A"},
    "Sara": {"age": 23, "grade": "B"},
}
print(students["Ali"]["grade"])  # A

# -----------------------------
# Useful built-in functions
# -----------------------------
print(len(my_dict))   # Number of key-value pairs
print(list(my_dict))  # List of keys
print(sorted(my_dict))# Sorted keys

# -----------------------------
# Merging dictionaries
# -----------------------------
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = {**d1, **d2}   # {'a':1, 'b':3, 'c':4} (d2 overwrites d1)


map = {
    '1' : "One",
    '2' : "two",
    '3' : "three"
}


out = ''
inn = input('enter num')
for i in map:
    out += map.get(i , '!') + " "
print(out)