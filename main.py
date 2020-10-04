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
wholeArray = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])    # creates an array
sliceArray = wholeArray[1:3, 1:3]                                        # takes a slice of the array, slices can influence the values of the whole
# the slice is defined by "starting index" : to "ending index (not including ending index value)", 0 = "empty space"
print(wholeArray)
print(sliceArray)

row_1 = wholeArray[0, :]    # same as [1, :]  ':' represents all
row_2 = wholeArray[1, :4]    # same as [1:2, :] but [1, 0:4] forms a different shape
print(row_1, row_1.shape)
print(row_2, row_2.shape)

col_1 = wholeArray[:, 0]    # same as [0:4, 0:1] but forms a different shape
col_2 = wholeArray[0:4, 1:2]    # same as [:, 1] but forms a different shape
print(col_1, col_1.shape)
print(col_2, col_2.shape)

"""INTEGER ARRAY INDEXING"""
print(wholeArray[[0, 1, 0], [0, 1, 2]]) # prints the same thing as print(np.array([wholeArray[0, 0], wholeArray[1, 1], wholeArrray[2, 0]])
# first group is the row index, second group is the column index
print(wholeArray[[0, 1], [1, 0]]) # these will have a single row shape

# this can be helpful when it comes to mutating a single element in the matrix
print(wholeArray)
mutate = np.array([0, 2, 3])
wholeArray[np.arange(3), mutate] += 10 # arange just lets you make a range lmao
print(wholeArray)

"""BOOLEAN ARRAYS"""
bool_idx = (wholeArray > 5)     # can be used to pick out the numbers that satisfy a condition

print(wholeArray[bool_idx])
print(wholeArray[wholeArray > 5])

"""DATA TYPES"""
# Every numpy array is of one datatype. It usually guesses the data type, but you can define the data type if you want
intArray = np.array([3, 4], dtype=np.int64)
print(intArray)
print(intArray.dtype)

"""ARRAY MATH"""
x = np.array([[2, 23, 76, 19, 3, 5, 6], [43, 5, 6, 7, 2, 5, 56]], dtype=float)
y = np.array([[14, 62, 23, 64, 63, 13, 1], [2, 54, 6, 324, 4, 6, 1]], dtype=float)

print(x + y)    # print(np.add(x, y))
print(x - y)    # print(np.subtract(x, y))
print(x * y)    # print(np.multiply(x, y))
print(x / y)    # print(np.divide(x, y))
print(np.sqrt(x))

