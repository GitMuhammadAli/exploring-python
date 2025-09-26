import numpy as np

marks = np.array([
    [78, 85, 90, 66],
    [55, 72, 60, 80],
    [92, 88, 79, 95],
    [70, 60, 65, 75],
    [85, 99, 70, 89],
    [45, 55, 50, 65]
])

# Chapter 1
print("\n=== Chapter 1 Solutions ===")
print("Q1:", np.eye(5))
print("Q2:\n", np.arange(1, 25).reshape(2, 3, 4))

# Chapter 2
print("\n=== Chapter 2 Solutions ===")
print("Q3: Student index with max Maths marks:", np.argmax(marks[:, 0]))
print("Q4: Average per subject:", np.mean(marks, axis=None))
print("Q5: Float32 conversion:\n", marks.astype(np.float32))

# Chapter 3
print("\n=== Chapter 3 Solutions ===")
print("Q6:", marks[3, :-1])
print("Q7:\n", marks[:, ::2])  # odd-numbered = 1st & 3rd subject
print("Q8:\n", marks[::-1, 1])  # reversed Physics column

# Chapter 4
print("\n=== Chapter 4 Solutions ===")
new_student = [50, 50, 50, 50]
print("Q9:\n", np.insert(marks, 2, new_student, axis=0))

new_subject = np.random.randint(40, 101, size=(marks.shape[0], 1))
print("Q10:\n", np.append(marks, new_subject, axis=1))

all_100 = np.full_like(marks, 100)
all_0 = np.zeros_like(marks)
print("Q11:\n", np.concatenate([marks, all_100, all_0], axis=0))

filtered = marks[marks[:, 0] >= 60]
print("Q12:\n", filtered)

print("Q13:\n", np.vstack([marks, marks.T]))

print("Q14:\n", np.split(marks, 3))
