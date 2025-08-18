# -----------------------------
# Python Exception Handling Examples
# -----------------------------

# -----------------------------
# Basic try/except
# -----------------------------
try:
    x = 10 / 0
except ZeroDivisionError:
    print("❌ Cannot divide by zero")

# -----------------------------
# Multiple exceptions
# -----------------------------
try:
    num = int("abc")
except (ValueError, TypeError) as e:
    print("Error:", e)

# -----------------------------
# else block (runs if no error)
# -----------------------------
try:
    y = 10 / 2
except ZeroDivisionError:
    print("❌ Error dividing by zero")
else:
    print("✅ Division successful, result:", y)

# -----------------------------
# finally block (always runs)
# -----------------------------
try:
    f = open("sample.txt", "w")
    f.write("Hello")
finally:
    f.close()  # Always closes file
    print("File closed safely")

# -----------------------------
# Raising exceptions
# -----------------------------
def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b

try:
    print(divide(5, 0))
except ValueError as e:
    print("Raised error:", e)

# -----------------------------
# Custom exceptions
# -----------------------------
class NegativeNumberError(Exception):
    """Raised when a negative number is not allowed"""
    pass

def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Negative number not allowed")
    return n

try:
    check_positive(-10)
except NegativeNumberError as e:
    print("Custom Exception:", e)

# -----------------------------
# Common built-in exceptions
# -----------------------------
try:
    lst = [1, 2, 3]
    print(lst[5])   # IndexError
except IndexError as e:
    print("Index error:", e)

try:
    d = {"a": 1}
    print(d["b"])   # KeyError
except KeyError as e:
    print("Key error:", e)

try:
    result = "5" + 5   # TypeError
except TypeError as e:
    print("Type error:", e)

# -----------------------------
# Using assert
# -----------------------------
def square_root(x):
    assert x >= 0, "❌ Cannot take square root of negative number"
    return x ** 0.5

try:
    print(square_root(-9))
except AssertionError as e:
    print("Assertion failed:", e)
