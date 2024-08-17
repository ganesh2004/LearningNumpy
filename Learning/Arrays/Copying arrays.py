"""Remember while copying numpy arrays"""
import numpy as np
a = np.array([1,2,3])
"""If we do b = a then the variable b will just point to a so any changes to to b will be done to a"""
""" So usr .copy()"""
b = a.copy()