import numpy as np

# =========================
# Chapter 1: Basics
# =========================
print("\n=== Chapter 1: Basics ===")

# Difference between List and NumPy array
list_data = [1, 2, 3, 4]
np_array = np.array([1, 2, 3, 4])
print("List:", list_data, "Type:", type(list_data))
print("NumPy Array:", np_array, "Type:", type(np_array))

# Creating arrays
arr1 = np.array([10, 20, 30])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.arange(1, 10, 2)
identity = np.eye(3)

print("1D Array:", arr1)
print("2D Array:\n", arr2)
print("Range Array:", arr3)
print("Identity Matrix:\n", identity)


# =========================
# Chapter 2: Properties & Operations
# =========================
print("\n=== Chapter 2: Properties & Operations ===")

marks = np.array([
    [78, 85, 90, 66],
    [55, 72, 60, 80],
    [92, 88, 79, 95],
    [70, 60, 65, 75],
    [85, 99, 70, 89],
    [45, 55, 50, 65]
])

print("Shape:", marks.shape)
print("Size:", marks.size)
print("Dimensions:", marks.ndim)
print("Dtype:", marks.dtype)

print("Sum:", marks.sum())
print("Mean:", marks.mean())
print("Max:", marks.max())
print("Min:", marks.min())
print("Std:", marks.std())
print("Var:", marks.var())

print("Add 5 to all marks:\n", marks + 5)
print("Square of marks:\n", marks ** 2)


# =========================
# Chapter 3: Indexing & Slicing
# =========================
print("\n=== Chapter 3: Indexing & Slicing ===")

print("Student 1 Marks:", marks[0])
print("Maths column:", marks[:, 0])
print("Student 2–4:\n", marks[1:4])
print("Last two students:\n", marks[-2:])
print("Student 3 Physics:", marks[2, 1])
print("First 3 Students, first 2 subjects:\n", marks[:3, :2])
print("Every alternate student:\n", marks[::2])
print("Reverse students:\n", marks[::-1])


# =========================
# Chapter 4: Array Manipulation
# =========================
print("\n=== Chapter 4: Array Manipulation ===")

# Insert new subject
comp = [90, 85, 88, 70, 95, 60]
marks_inserted = np.insert(marks, 4, comp, axis=1)
print("After Inserting new subject:\n", marks_inserted)

# Append new student
new_student = [[60, 70, 80, 90]]
marks_appended = np.append(marks, new_student, axis=0)
print("After Appending new student:\n", marks_appended)

# Concatenate with Section B
section_b = np.random.randint(40, 101, (6, 4))
marks_concat = np.concatenate([marks, section_b], axis=0)
print("After Concatenation:\n", marks_concat)

# Delete Physics column
marks_deleted = np.delete(marks, 1, axis=1)
print("After Deleting Physics column:\n", marks_deleted)

# Delete Student 6
marks_deleted_row = np.delete(marks, 5, axis=0)
print("After Deleting Student 6:\n", marks_deleted_row)

# Stacking
extra = np.array([[100, 100, 100, 100]])
marks_vstack = np.vstack([marks, extra])
print("Vertical Stack:\n", marks_vstack)

bonus = np.array([[5], [10], [5], [10], [5], [10]])
marks_hstack = np.hstack([marks, bonus])
print("Horizontal Stack:\n", marks_hstack)

stacked = np.dstack([marks, marks])
print("Depth Stack Shape:", stacked.shape)

# Split
group_a, group_b = np.split(marks, 2)
print("Group A:\n", group_a)
print("Group B:\n", group_b)

sub1, sub2 = np.split(marks, 2, axis=1)
print("Subjects 1–2:\n", sub1)
print("Subjects 3–4:\n", sub2)
