import numpy as np

a = np.array([1, 2, 3], dtype="int16")
print(a)
b = np.array([[1.0, 2.0, 3.9], [2.5, 6.4, 5.7]])
print(b)
# dimension of the array
print(a.ndim)
print(b.ndim)
# the shape of the array
print(a.shape)
print(b.shape)
# get the type
print(a.dtype)
print(b.dtype)
# getting size of each element in the array in bytes
print(a.itemsize)
print(b.itemsize)
# getting the number of elements in the array itself
print(a.size)
print(b.size)
# multiplying the both a.itemsize and a.size will give you the space in memory used by the array
# or you can use nbytes
print(a.nbytes)
