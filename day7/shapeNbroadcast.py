import numpy as np

#NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

arr = np.array([1, 2, 3], ndmin=4)
print(arr)
print('shape of array :', arr.shape)

#By reshaping we can add or remove dimensions or change number of elements in each dimension.
#convert 1-D to 2-D array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(6, 2)
print(newarr)

#convert 1-D to 3-D array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(3, 2, 2)
print(newarr)

#Unknown dimensions
#We do not have to specify an exact number for one of the dimensions in the reshape method.
#Pass -1 as the value, and NumPy will calculate this number for you.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

#Flattening the arrays
#Flattening array means converting a multidimensional array into a 1-D array.

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)

#broadcasting refers to how numpy treats arrays with different Dimension during arithmetic operations which lead to certain constraint. 
#the smaller array is broadcast across the larger array so that they have compatible shapes. 
a = np.array([14, 45, 62]) # 1x3 Dimension array
print(a)
b = np.array(3) 
print(b)
c = a - b  # Broadcasting happened because of miss match in array Dimension.
print(c)

A = np.array([[25,65,86], [12,54,11]])
print(A)
b = 4
print(b)
C = A - b
print(C)

#to calculate outer product of v and w
v = np.array([3, 7, 6])
w = np.array([4, 5])
s= np.reshape(v, (3, 1))  #To compute an outer product we first reshape v to a column vector of shape 3x1
print( s * w)      #broadcasting it against w to yield an output of shape 3x2

# Numpy treats scalars as arrays of shape();
A = np.array([[25,65,86], [12,54,11]])
print(A * 2)      # these can be broadcast together to shape 2x3.
