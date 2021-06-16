import numpy as npy 
#Linear Algebra
#NumPy package contains numpy.linalg module that provides all the functionality required for linear algebra.

a1 = npy.array([1,2,3])
b1 = npy.array([4,5,6])

a2 = npy.array([[1,2],[3,4]]) 
b2 = npy.array([[11,12],[13,14]]) 

#numpy.dot() returns the dot product of two arrays. 
# For 2-D vectors, it is the equivalent to matrix multiplication. 
# For 1-D arrays, it is the inner product of the vectors. 
# For N-dimensional arrays, it is a sum product over the last axis of a and the second-last axis of b
print(npy.dot(a1,b1))
print(npy.dot(a2,b2))

#numpy.vdot() function returns the dot product of the two vectors. 
#If the first argument is complex, then its conjugate is used for calculation.
print(npy.vdot(a1,b1))
print(npy.vdot(a2,b2))

#numpy.inner() returns the inner product of vectors for 1-D arrays. 
#For higher dimensions, it returns the sum product over the last axes.
print(npy.inner(a1,b1))
print(npy.inner(a2,b2))

#numpy.matmul() function returns the matrix product of two arrays. While it returns a normal product for 2-D arrays 
#if dimensions of either argument is >2, it is treated as a stack of matrices residing in the last two indexes and is broadcast accordingly
print(npy.matmul(a2,b2))

#if either argument is 1-D array, it is promoted to a matrix by appending a 1 to its dimension, which is removed after multiplication.
a3 = [[1,2],[2,3]] 
b3 = [1,2] 
print(npy.matmul(a3,b3))
print(npy.matmul(b3,a3))

#numpy.linalg.det() function calculates the determinant of the input matrix
print(npy.linalg.det(a2))
b = npy.array([[6,1,1], [4, -2, 5], [2,8,7]])
print(npy.linalg.det(b))

#numpy.linalg.solve() function gives the solution of linear equations in the matrix form
#3 * x0 + x1 = 9 and x0 + 2 * x1 = 8
a = npy.array([[3,1], [1,2]])    
b = npy.array([9,8])
print(npy.linalg.solve(a, b))

#numpy.linalg.inv() function to calculate the inverse of a matrix
x = npy.array([[1,2],[3,4]]) 
print(npy.linalg.inv(x))