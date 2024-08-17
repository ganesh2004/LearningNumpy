# Initializing All 0s matrix
import numpy as np
a = np.zeros((2,3,3))
print(a)
# Initializing All 1s matrix
b = np.ones((2,2),dtype = "int16")
print(b)
# Any other number (shape of array,number)
c = np.full((2,2),99)
print(c)
# Similar function full_like(array,number)
d = np.full_like(c,89)
print(d)
# passing in random values in [0,1] (dont pass a tuple)
e = np.random.rand(4,2)
print(e)
# to pass a tuple use np.random.random_sample(can pass array.shape)
f = np.random.random_sample(a.shape)
print(f)
# Generating random integers randint(starting value(included),end value(excluded),size=(n,m..))
# If no starting value is specified then 0 will be default
f = np.random.randint(7,size=(3,3))
# Generating an identity matrix
g = np.identity(4)
print(g)
# Repeating anumbers in array
arr = np.array([1,2,3])
arr2 = np.repeat(arr,3)
print(arr)
print(arr2)
# Repeating along different axis (ante rows repeat cheyyochu leda 2d arrays repeat cheyyochu)
arrd2 = np.array([[1,2,3],[1,2,3]])
reparrd2 = np.repeat(arrd2,3,axis = 0)# axis 1 ante column vasthundi 0 unte row elements access chese tappudu indexation
# idhi koncham gamaninchu
print(arrd2)
print(reparrd2)

