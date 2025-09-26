import numpy as np


arr  = np.array([1,2,np.nan,4,5,np.nan,5,6,6])

ok = np.nan_to_num(arr)

print(ok)