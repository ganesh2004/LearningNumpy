import numpy as np

a = np.array([[1, 2, 3, 4, 134, 3, 3143, 341, 341, 32], [1, 2, 3, 34, 34, 3, 43, 5, 343, 34]])
# Getting a specific element [r,c]
print(a[1,3])
# Getting a specific row
print(a[1,:])
#Getting a specific column
print(a[:,5])
#Getting a little fancy [Startindex:endindex:stepsize]
print(a[0,1:6:2])
#changing specific values
a[1,2] = 6
a[:,3] = 5
a[:,4] = [1,2]
print(a)
#same with 3D array
b = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
print(b)
# Getting a specific element
b[1,1,1] = 69
print(b)
