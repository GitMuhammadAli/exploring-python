import numpy as np

# Dataset: [ID, Age, Salary, Bonus, DeptID]
data = np.array([
    [1, 25, 50000, 2000, 1],
    [2, 28, np.nan, 2500, 2],
    [3, 35, 70000, np.nan, 1],
    [4, np.nan, 60000, 2200, 3],
    [5, 45, 80000, 3000, 2],
    [6, 38, 75000, 2800, 2],
    [7, 29, np.nan, 2400, 1],
    [8, 50, 90000, 4000, 3],
    [9, 31, 72000, 2700, 1],
    [10, 42, np.nan, 3100, 2]
])

np.savetxt(
    "c:/Ali/py/one/numpy/PROJECt/people.csv",
    data,
    delimiter=",",
    fmt="%.2f",
    header="ID,Age,Salary,Bonus,DeptID",
    comments=""
)


loaded = np.loadtxt("people.csv", delimiter=",", skiprows=1)
print("Shape:", loaded.shape)
print("Size:", loaded.size)
print("Dimensions:", loaded.ndim)
print("Data Type:", loaded.dtype)


print("First row:", loaded[0])
print("All Salaries:", loaded[:, 2])
print("First 3 Employees:", loaded[:3])
print("Last Column (Dept):", loaded[:, -1])


reshaped = loaded.reshape(5, 10)   
print("Reshaped:\n", reshaped)

flat = loaded.ravel()
print("Flattened Array:", flat)


data = loaded.copy()

net_income = np.zeros((data.shape[0], 1))
data = np.hstack([data, net_income])

print("After adding NetIncome column:\n", data)

new_employee = np.array([[11, 34, 68000, 2600, 1, 0]])
data = np.vstack([data, new_employee])


data[data[:, 4] == 2, 2] *= 1.10  

data[:, 3] *= 1.05  

data[:, 5] = data[:, 2] + data[:, 3]


# Replace NaN Salary with mean
salary_col = data[:, 2]
mean_salary = np.nanmean(salary_col)
data[np.isnan(data[:, 2]), 2] = mean_salary

# Replace NaN Bonus with 0
data[np.isnan(data[:, 3]), 3] = 0

# Replace NaN Age with median
age_col = data[:, 1]
median_age = np.nanmedian(age_col)
data[np.isnan(data[:, 1]), 1] = median_age



# Average Salary per Dept
for dept in np.unique(data[:, 4]):
    avg_salary = data[data[:, 4] == dept, 2].mean()
    print(f"Dept {int(dept)} Avg Salary: {avg_salary:.2f}")

# Highest Earner
max_salary = np.max(data[:, 2])
print("Highest Salary:", max_salary)

# Employees >70k
print("Employees with salary > 70k:\n", data[data[:, 2] > 70000])


np.savetxt(
    "c:/Ali/py/one/numpy/PROJECt/employees_cleaned.csv",  # full path
    data,
    delimiter=",",
    fmt="%.2f",
    header="ID,Age,Salary,Bonus,DeptID,NetIncome",
    comments=""
)




import pandas as pd

df = pd.read_csv("c:/Ali/py/one/numpy/PROJECt/employees_cleaned.csv")

print(df.head())