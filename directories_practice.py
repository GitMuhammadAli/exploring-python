"""
directories_practice.py
------------------------
Covers most frequently used Python functions & modules
for working with directories (folders).
"""

import os
from pathlib import Path
import shutil

# ===============================
# 1. Current Working Directory
# ===============================
print("\n--- Current Working Directory ---")
print("CWD:", os.getcwd())


# ===============================
# 2. List directory contents
# ===============================
print("\n--- List directory contents ---")
print("Using os.listdir():", os.listdir("."))
print("Using pathlib:", [p.name for p in Path(".").iterdir()])


# ===============================
# 3. Create a new directory
# ===============================
print("\n--- Create Directory ---")
if not os.path.exists("demo_folder"):
    os.mkdir("demo_folder")
    print("Directory 'demo_folder' created.")

# Create nested directories
if not os.path.exists("parent/child"):
    os.makedirs("parent/child")
    print("Nested directories 'parent/child' created.")


# ===============================
# 4. Rename directory
# ===============================
print("\n--- Rename Directory ---")
if os.path.exists("demo_folder"):
    os.rename("demo_folder", "renamed_folder")
    print("'demo_folder' renamed to 'renamed_folder'")


# ===============================
# 5. Remove directories
# ===============================
print("\n--- Remove Directories ---")
if os.path.exists("renamed_folder"):
    os.rmdir("renamed_folder")  # only works if empty
    print("'renamed_folder' removed.")

# Remove tree of directories
if os.path.exists("parent"):
    shutil.rmtree("parent")
    print("'parent' and all its subfolders removed.")


# ===============================
# 6. Join & Split Paths
# ===============================
print("\n--- Join & Split Paths ---")
path = os.path.join("folder", "subfolder", "file.txt")
print("Joined Path:", path)
print("Split Path:", os.path.split(path))
print("Base name:", os.path.basename(path))
print("Directory name:", os.path.dirname(path))


# ===============================
# 7. Pathlib Examples
# ===============================
print("\n--- Pathlib Examples ---")
p = Path("example.txt")
print("Absolute Path:", p.resolve())
print("Parent Dir:", p.parent)
print("Suffix (extension):", p.suffix)


# ===============================
# 8. Check if a path exists
# ===============================
print("\n--- Path Checks ---")
print("Does 'example.txt' exist?", os.path.exists("example.txt"))
print("Is current path a directory?", os.path.isdir("."))
print("Is current path a file?", os.path.isfile(__file__))


# ===============================
# 9. Directory Walk (list all files recursively)
# ===============================
print("\n--- Walk Through Directories ---")
for root, dirs, files in os.walk("."):
    print("Root:", root)
    print("Dirs:", dirs)
    print("Files:", files)
    break  # remove break to walk entire tree
