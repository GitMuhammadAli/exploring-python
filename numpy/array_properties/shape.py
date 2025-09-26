import numpy as np;

twoD_arr = np.array([[1,2,3],
            [4,5,6]])
print(twoD_arr.shape)
print("-" * 20)

print(twoD_arr.size)
print("-" * 20)



arr = np.array([1.2 , 3.2 , 2.3])

int_arr = arr.astype(int)

print(int_arr)
print("-" * 20)

print(int_arr.dtype)