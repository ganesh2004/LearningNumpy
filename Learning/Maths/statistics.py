import numpy as np
stats = np.array([[0,2,3],[-1,3,4]])
# Printing the minimum value
minval = np.min(stats)
print(minval)
# can also do it on row and colum basis
minvalrow1 = np.min(stats,axis = 0)
"""indentation lage chudu axis ippudu array 2D kaabatti 1 unte row and 0 unte column 3d ithe 3 z axis ipoddhi,2 row
and 0 column """
print(minvalrow1) # this will print min value of each column
