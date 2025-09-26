import numpy as np, sys

lst = [1,2,3,4,5]
arr = np.array(lst)

print(sys.getsizeof(lst))  
print(arr.nbytes)          


print("/" *40)

OneD = np.arange(10,55 , 5)
print(OneD)

print("/" *40)

twoD = np.arange(1,13).reshape(3,4)
print(twoD)

print("/" *40)
a3 = np.random.randint(0, 10, (2,3,4)) 
print(a3)


print("/" *40)
I  = np.identity(6)
print(I)

print("/" *40)

print(twoD.shape)  
print(twoD.size)  
print(twoD.ndim)   
print(twoD.dtype)  

a2_float = twoD.astype('float64')
print(a2_float.nbytes)

print("/" *40)

arr = np.arange(1, 21, 2)  
arr_f = arr.astype('float32')  
arr_c = arr.astype('complex')  

print(arr, arr.dtype)     
print(arr_f, arr_f.dtype) 
print(arr_c, arr_c.dtype) 


print("/" *40)

a = np.arange(1, 11)
b = np.arange(11, 21)

print(a + b)   # [12 14 16 18 20 22 24 26 28 30]
print(a - b)   # [-10 -10 -10 -10 -10 -10 -10 -10 -10 -10]
print(a * b)   # [11 24 39 56 75 96 119 144 171 200]
print(b / a)   # [11.   6.   4.33 ... 2.5]
print(a ** 2)  # [1 4 9 ... 100]
print(b // a)  # [11 3 2 2 2 2 2 2 2 2]
print(b % a)   # [0 1 1 1 1 1 1 1 1 1]

print("/" *40)

prod = a * b
print(prod.mean())               
print(np.sqrt(prod))             
print(prod[prod > 50].sum())     
