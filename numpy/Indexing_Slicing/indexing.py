import numpy as np

# ---------------------------
# Setup: Student Marks Matrix
# ---------------------------
marks = np.array([
    [78, 85, 90, 66],   # Student 1
    [55, 72, 60, 80],   # Student 2
    [92, 88, 79, 95],   # Student 3
    [70, 60, 65, 75],   # Student 4
    [85, 99, 70, 89],   # Student 5
    [45, 55, 50, 65]    # Student 6
])

print("Original Marks Matrix:\n", marks)

# ---------------------------
# 1. Row & Column Access
# ---------------------------
print("\n1) Student 3’s marks:", marks[2])
print("2) Physics marks:", marks[:, 1])
print("3) Student 5’s Chemistry mark:", marks[4, 2])

# ---------------------------
# 2. Row/Column Slicing
# ---------------------------
print("\n4) First 3 students:\n", marks[0:3 , :])
print("5) Last 2 subjects for all:\n", marks[:, 2:4])
print("6) Students 2–4, Physics & Chemistry:\n", marks[1:4, 1:3])

# ---------------------------
# 3. Fancy Indexing
# ---------------------------
print("\n7) Students 1,3,5:\n", marks[[0, 2, 4], :])
print("8) Math & English for all:\n", marks[:, [0, 3]])
print("9) Sub-matrix (Students 2&3, Chemistry & English):\n", marks[1:3, 2:4])

# ---------------------------
# 4. Boolean Indexing
# ---------------------------
print("\n10) All marks > 85:", marks[marks > 85])
print("11) Students with <50 in any subject:\n", marks[np.any(marks < 50, axis=1)])
print("12) Students with Math > 80:\n", marks[marks[:, 0] > 80])

# ---------------------------
# 5. Modification via Indexing
# ---------------------------
marks_copy = marks.copy()  # keep original safe

# Add 5 to Student 1’s English
marks_copy[:, -1] += 5

print("\n13) After +5 to Student 1’s English:\n", marks_copy)

# Set all marks < 60 → 60
marks_copy[marks_copy < 60] = 60
print("14) After setting <60 to 60:\n", marks_copy)

# Swap Student 2 and Student 4
marks_copy[[1, 3]] = marks_copy[[3, 1]]
print("15) After swapping Student 2 and 4:\n", marks_copy)
