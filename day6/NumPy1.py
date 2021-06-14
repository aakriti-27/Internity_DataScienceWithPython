import numpy
#creating arrays
#We can create a NumPy ndarray object by using the array() function.

arr = numpy.array([1, 2, 3])
print(arr)
print(type(arr))

arr = numpy.array((1, 2, 3))  #by passing tuple
print(arr)

arr1=numpy.array(45)   #0-D array
arr2=numpy.array([1, 2, 3])   #1-D array
arr3=numpy.array([[1, 2, 3],[4,5,6]],dtype=object)  #2-D array
arr4=numpy.array([[[1, 2, 3],[4,5,9]],[[6,7,8],[9,5,8]]],dtype=object)  #3-D array

print(arr4.ndim)    #ndim to check dimension of the array
arr = numpy.array([1, 2, 3, 4], ndmin=5)       #to create higher dimensional array
print(arr)

#NumPy Array Indexing(The indexes in NumPy arrays start with 0)

arr3=numpy.array([[1, 2, 3],[4,5,6]],dtype=object)
print('2nd element on 2nd dim: ', arr3[0, 1])

arr4=numpy.array([[[1, 2, 3],[4,5,9]],[[6,7,8],[9,5,8]]],dtype=object)  #3-D array
print(arr4[0, 1, 2])

arr3=numpy.array([[1, 2, 3],[4,5,6]],dtype=object)
print('Last element from 2nd dim: ', arr3[1, -1])

#NumPy Array Slicing

arr = numpy.array([1, 2, 3, 4, 5, 6, 7])   
print(arr[:4])                     #from beginning to index 3

print(arr[-4:-2])                   #negative slicing(3rd and 4th index)

print(arr[::2])                  #print all the elements in step of 2

arr1 = numpy.array([[1, 2, 3],[4,5,6]],dtype=object)     #slicing 2-D array 
print(arr1[1, 1:2])           #from 2nd element,at index 1

print(arr1[0:2, :2])           #From both elements, slice index 0,1

#Datatypes

arr = numpy.array([1,2,3])
print(arr.dtype)

arr = numpy.array([1, 2, 3, 4], dtype='S')  #creating array with defined datatypes
print(arr)
print(arr.dtype)

#coverting datatype of existing array
#The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

arr = numpy.array([4.5, 3.8, 2.1])
arr2 = arr.astype('i')           #float to integer
print(arr2)
print(arr2.dtype)

#Copy
arr = numpy.array([1, 2, 3])
x = arr.copy()
arr[0] = 5
print(arr)
print(x)

#View
arr1 = numpy.array([1, 2, 3])
x = arr1.view()
arr1[0] = 5
print(arr1)
print(x)



