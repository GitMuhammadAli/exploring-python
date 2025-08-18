# -----------------------------
# Basic function
# -----------------------------
def greet():
    print("Hello, World!")

greet()


# -----------------------------
# Function with parameters
# -----------------------------
def add(a, b):
    return a + b

print(add(5, 3))  # 8


# -----------------------------
# Default parameters
# -----------------------------
def greet_user(name="Guest"):
    return f"Hello, {name}!"

print(greet_user())        # Hello, Guest!
print(greet_user("Ali"))   # Hello, Ali!


# -----------------------------
# Keyword arguments
# -----------------------------
def introduce(name, age):
    return f"My name is {name}, I am {age} years old."

print(introduce(age=25, name="Sara"))


# -----------------------------
# *args (variable number of positional arguments)
# -----------------------------
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10


# -----------------------------
# **kwargs (variable keyword arguments)
# -----------------------------
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_info(name="Ali", age=25, city="Lahore")


# -----------------------------
# Return multiple values
# -----------------------------
def get_min_max(nums):
    return min(nums), max(nums)

mn, mx = get_min_max([1, 2, 3, 4, 5])
print("Min:", mn, "Max:", mx)


# -----------------------------
# Scope (local, global, nonlocal)
# -----------------------------
x = 10  # global

def outer():
    x = 5  # enclosing

    def inner():
        nonlocal x
        x += 1
        print("Inner x:", x)

    inner()
    print("Outer x:", x)

outer()
print("Global x:", x)


# -----------------------------
# Lambda functions
# -----------------------------
square = lambda x: x**2
print(square(4))  # 16

# With sorted()
nums = [("Ali", 25), ("Sara", 23), ("Omar", 27)]
nums_sorted = sorted(nums, key=lambda x: x[1])  # Sort by age
print(nums_sorted)


# -----------------------------
# Higher-order functions
# -----------------------------
def apply_func(func, values):
    return [func(v) for v in values]

print(apply_func(lambda x: x*2, [1, 2, 3]))  # [2, 4, 6]


# -----------------------------
# Built-ins with functions
# -----------------------------
nums = [1, 2, 3, 4, 5]

print(list(map(lambda x: x**2, nums)))     # map -> [1, 4, 9, 16, 25]
print(list(filter(lambda x: x % 2 == 0, nums)))  # filter -> [2, 4]

from functools import reduce
print(reduce(lambda a, b: a + b, nums))   # reduce -> 15


# -----------------------------
# Docstrings
# -----------------------------
def multiply(a, b):
    """
    Multiply two numbers.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: Product of a and b
    """
    return a * b

print(multiply.__doc__)
