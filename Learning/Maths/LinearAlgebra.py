# https://numpy.org/doc/stable/reference/routines.linalg.html
# Matrix multiplication
import numpy as np
a = np.full((2,3),1)
b = np.full((3,2),4)
# is used a normal a*b just each matrix will be multiplied with each other it won't be the normal matrix multiplication
c = np.matmul(a,b)
print(c)
# Finding a determinant of a matrix
det = np.linalg.det(c)
print(det)


