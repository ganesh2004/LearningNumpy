""" Challenge try creating the array in the image img.png using array elements accessing concepts and
 initializing concepts """
import numpy as np
array = np.full((5,5),1)
array [1:4,1:4] = np.full((3,3),0)
array[2,2] = 9
print(array)