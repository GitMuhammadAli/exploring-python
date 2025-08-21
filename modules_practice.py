"""
modules_practice.py
-------------------
Covers most frequently used Python built-in modules with examples
"""

# ===============================
# 1. math → mathematical functions
# ===============================
import math

print("\n--- math module ---")
print("Square root of 16:", math.sqrt(16))
print("Pi value:", math.pi)
print("Cos(0):", math.cos(0))


# ===============================
# 2. random → random numbers
# ===============================
import random

print("\n--- random module ---")
print("Random integer (1-10):", random.randint(1, 10))
print("Random choice from list:", random.choice(['apple', 'banana', 'cherry']))
print("Random float:", random.random())


# ===============================
# 3. datetime → dates & times
# ===============================
import datetime

print("\n--- datetime module ---")
now = datetime.datetime.now()
print("Current datetime:", now)
print("Year:", now.year, "Month:", now.month, "Day:", now.day)


# ===============================
# 4. time → sleep, timestamps
# ===============================
import time

print("\n--- time module ---")
print("Current time (timestamp):", time.time())
print("Sleeping for 1 second...")
time.sleep(1)
print("Awake now!")


# ===============================
# 5. os → operating system
# ===============================
import os

print("\n--- os module ---")
print("Current working dir:", os.getcwd())
print("List of files:", os.listdir("."))


# ===============================
# 6. sys → system specific
# ===============================
import sys

print("\n--- sys module ---")
print("Python version:", sys.version)
print("Platform:", sys.platform)


# ===============================
# 7. statistics → mean, median, etc.
# ===============================
import statistics

print("\n--- statistics module ---")
data = [2, 5, 7, 9, 10]
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))


# ===============================
# 8. collections → advanced data structures
# ===============================
from collections import Counter, defaultdict, namedtuple

print("\n--- collections module ---")
print("Counter:", Counter("banana"))

dd = defaultdict(int)
dd['a'] += 1
print("DefaultDict:", dict(dd))

Point = namedtuple("Point", "x y")
p = Point(10, 20)
print("NamedTuple:", p.x, p.y)


# ===============================
# 9. itertools → iterators
# ===============================
import itertools

print("\n--- itertools module ---")
nums = [1, 2, 3]
print("Permutations of [1,2,3]:", list(itertools.permutations(nums)))
print("Combinations of 2:", list(itertools.combinations(nums, 2)))


# ===============================
# 10. functools → higher-order functions
# ===============================
import functools

print("\n--- functools module ---")
def multiply(x, y): return x * y
print("Reduce (multiply all):", functools.reduce(multiply, [1, 2, 3, 4]))


# ===============================
# 11. json → JSON parsing
# ===============================
import json

print("\n--- json module ---")
person = {"name": "Ali", "age": 22}
json_str = json.dumps(person)
print("Dict to JSON:", json_str)
print("JSON back to dict:", json.loads(json_str))


# ===============================
# 12. re → regular expressions
# ===============================
import re

print("\n--- re module ---")
txt = "My number is 12345"
x = re.findall(r"\d+", txt)
print("Numbers found:", x)


# ===============================
# 13. pathlib → modern file paths
# ===============================
from pathlib import Path

print("\n--- pathlib module ---")
path = Path(".")
print("Files in current dir:", [p.name for p in path.iterdir()])


# ===============================
# 14. shutil → file operations
# ===============================
import shutil

print("\n--- shutil module ---")
print("Disk usage (current dir):", shutil.disk_usage("."))


# ===============================
# 15. csv → CSV files
# ===============================
import csv

print("\n--- csv module ---")
rows = [["Name", "Age"], ["Ali", 22], ["Sara", 25]]
with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
print("CSV file 'people.csv' created.")


# ===============================
# 16. argparse → command line args
# ===============================
import argparse

print("\n--- argparse module ---")
# Only works when running via CLI
# parser = argparse.ArgumentParser()
# parser.add_argument("--name", help="Your name")
# args = parser.parse_args()
# print("Hello", args.name)
print("Argparse demo (uncomment when running from CLI)")
