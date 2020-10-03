import numpy as np

"""BASICS"""
a = np.array([1, 2, 3])     # creates a rank 1 array
print(type(a))              # prints <class 'numpy.ndarray'>
print(a.shape)              # prints (3,) **3 by one**
print(a[0], a[1], a[2])     # prints 1 2 3
a[0] = 5                    # sets a[0] to 5
print(a)                    # prints [5 2 3]

b = np.array([[1, 2, 3], [4, 5, 6]])    # creates a rank 2 array
print(b.shape)                          # prints (2, 3) **2 by 3**
print(b[0, 0], b[0, 1], b[1, 0])        # prints 1 2 4
print(b)                                # prints [[1 2 3] \n [4 5 6]]

"""NUMPY FUNCTIONS"""
zeroArray = np.zeros((2, 2))     # creates a 2x2 array of zeros
print(zeroArray)

onesArray = np.ones((4, 4))      # creates a 4x4 array of ones
print(onesArray)

fullArray = np.full((5, 4), 'hello')   # creates an array full of constants/data types
print(fullArray)

eyeArray = np.eye(4, 4)           # creates an identity matrix
print(eyeArray)

randomArray = np.random.random((5, 5)) # creates an array of random values from 0 to 1
print(randomArray)

"""ARRAY INDEXING"""
