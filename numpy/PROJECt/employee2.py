import numpy as np

np.random.seed(42)

# 100 employees: [ID, Age, Salary, Bonus, DeptID]
data = np.zeros((100,5))

# ID
data[:,0] = np.arange(1,101)

# Age 20-60
data[:,1] = np.random.randint(20,61, size=100)

# Salary 30k-120k
data[:,2] = np.random.randint(30000,120001, size=100)

# Bonus 500-5000
data[:,3] = np.random.randint(500,5001, size=100)

# DeptID 1-5
data[:,4] = np.random.randint(1,6, size=100)
np.set_printoptions(suppress=True)   # disables scientific notation
np.set_printoptions(precision=2)     # limit decimals to 2 places

print (data)

print(data.shape)
print(data.size)
print(data.ndim)
print(data.dtype)

print(data[0])
print(data[-1])
print(data[:5])


print(data[: , 2])
print(data[: , 4])

##########################################################
print("-"*100)
# Part 2: Indexing & Slicing.
print(data[9 : 20])
print(data[: , 2])
print(data[data[: , 4] ==3 ])
print(data[::5])
print(data[-10:])




# 1. Flatten the array using ravel()
flat1 = data.ravel()
print(flat1)

# 2. Reshape the array to (50, 10)
reshaped1 = data.reshape(50, 10)
print(reshaped1)

# 3. Reshape the array to (10, 50)
reshaped2 = data.reshape(10, 50)
print(reshaped2)

# 4. Convert the 2D array to 1D using flatten()
flat2 = data.flatten()
print(flat2)




NetIncome = (data[: , 2] + data[:,4]).reshape(-1,1)
one = np.hstack((data,NetIncome))

print(one)


tax = (data[: , -1] * 0.1).reshape(-1,1)
new = np.hstack((one ,tax))
print(new)



  

UpdatedSalary = (data[: , 2] * 0.1).reshape(-1,1)
latest = np.hstack((new , UpdatedSalary))
print(latest)

bonus = (data[::5] * 1.2 ).reshape(-1,1)
newone = np.hstack((new , bonus))
print(newone)


salar = (data[::2] * 1.5 ).reshape(-1,1)


data[data[:,4] == 2, 2] *= 1.15

data[:,3] *= 1.05

NetIncome = (data[:,2] + data[:,3]).reshape(-1,1)
data = np.hstack((data, NetIncome))

data[data[:,1] > 50, 2] -= 2000


# [ID, Age, Salary, Bonus, DeptID, NetIncome, Tax]

salary_stats = {
    "mean": np.mean(data[:,2]),
    "max": np.max(data[:,2]),
    "min": np.min(data[:,2]),
    "std": np.std(data[:,2]),
    "var": np.var(data[:,2])
}

bonus_stats = {
    "mean": np.mean(data[:,3]),
    "max": np.max(data[:,3]),
    "min": np.min(data[:,3]),
    "std": np.std(data[:,3]),
    "var": np.var(data[:,3])
}

print("Salary Stats:", salary_stats)
print("Bonus Stats:", bonus_stats)


for dept in np.unique(data[:,4]):
    avg_salary = data[data[:,4] == dept, 2].mean()
    print(f"Dept {int(dept)} Avg Salary: {avg_salary:.2f}")



max_netincome = np.max(data[:,5])
employee_max_netincome = data[data[:,5] == max_netincome]
print("Highest NetIncome Employee:\n", employee_max_netincome)



# [ID, Age, Salary, Bonus, DeptID, NetIncome]

# 1️⃣ Get all employees with NetIncome > 100k and DeptID = 1
filter1 = data[(data[:,5] > 100000) & (data[:,4] == 1)]
print("Employees with NetIncome > 100k & DeptID=1:\n", filter1)

# 2️⃣ Select employees with Age between 25–35 and Salary > 50k
filter2 = data[(data[:,1] >= 25) & (data[:,1] <= 35) & (data[:,2] > 50000)]
print("Employees Age 25-35 & Salary>50k:\n", filter2)

# 3️⃣ Print IDs of employees who are top 5 earners
top5_indices = np.argsort(data[:,5])[-5:]  # indices of top 5 NetIncome
top5_employees = data[top5_indices]
top5_ids = top5_employees[:,0]
print("Top 5 Earners IDs:", top5_ids)

# 4️⃣ Select employees in DeptID 2 or 3 with Bonus > 3000
filter3 = data[((data[:,4]==2) | (data[:,4]==3)) & (data[:,3] > 3000)]
print("Dept 2 or 3 with Bonus>3000:\n", filter3)

# 5️⃣ Fancy indexing: select first, middle, and last employee rows
fancy_rows = data[[0, data.shape[0]//2, -1]]
print("First, Middle, Last employees:\n", fancy_rows)

# 6️⃣ Select Salary and Bonus columns only for employees older than 40
cols_selected = data[data[:,1] > 40][:, [2,3]]
print("Salary & Bonus for Age>40:\n", cols_selected)
