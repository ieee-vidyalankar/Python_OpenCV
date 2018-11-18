# # NumPy is an open source Python package for scientific computing. 
# # NumPy supports large, multidimensional arrays and matrices. 
# # NumPy is written in Python and C. NumPy arrays are faster compared to Python lists. 
# # But NumPy arrays are not flexible like Python lists, you can store only same data type in each column.
# #NumPy’s main object is the homogeneous multidimensional array. 
# #It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers. 
# #In NumPy dimensions are called axes. The number of axes is rank.

import numpy as np
# #1.
a = np.array([1,2,3]) #Create a rank1 numpy array
print(type(a))        #prints "<class 'numpy.ndarray>"
print(a[0],a[1],a[2])
a[0]=5
print(a)

#2.  2 row 3 column
d = np.array([[1,2,3],[4,5,6]])
print(d.shape)
print(d)

#3.create numpy array from list
list1 = [[1,2,3],[4,5,6],[7,8,9]]
c = np.array(list1)
print(c.shape)
print(c)

#4.create array of all zeros & for ones - np.ones
a = np.zeros((2,2)) 
print(a)
print(type(a[0,0]))

#5.create a identity matrix
d = np.eye(2) 
print(d)
print(type(d))

#6.create a array filled with random values
e = np.random.random((2,2)) 
print(e)
print(type(e))

# # #Array Map
x = np.array([[1,2],[3,4]], dtype=np.float)
y = np.array([[5,6],[7,8]], dtype=np.float)
print(x + y)      #Elementwise sum;both produce the array
#or
print(np.add(x,y))

print(x - y)      #Elementwise sutraction;both produce the array
#or
print(np.subtract(x,y))

print(x * y)      #Elementwise multiply;both produce the array
#or
print(np.multiply(x,y))

print(x / y)      #Elementwise divide;both produce the array
#or
print(np.divide(x,y))

print(np.sqrt(x)) #Elementwise square root;both produce the array