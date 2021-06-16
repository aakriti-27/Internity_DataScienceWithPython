import numpy as np
#Numpy array       
#(creating,indexing,slicing done previously)

#Iteration
arr = np.array([[4,7], [9,1]])   #iterate over elements of 2-D array
for x in arr:
  print(x)

for x in arr:    
  for y in x:            #iterate over scalar elements of array
    print(y)

#nditer() is a helping function that can be used from very basic to very advanced iterations.
for x in np.nditer(arr):
  print(x)

#op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
#NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action.
#That extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered']

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

#Iterating With Different Step Size
for x in np.nditer(arr[:, ::2]):
  print(x)

#For index of the element while iterating, the ndenumerate() method can be used.
for idx, x in np.ndenumerate(arr):
  print(idx, x)

#----------------

#Joining numpy arrays

#sequence of arrays is passed that we want to join to the concatenate() function, along with the axis. 
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2))    #axis=0
print(arr)
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

#Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
arr = np.stack((arr1, arr2), axis=1)
print(arr)
arr = np.hstack((arr1, arr2))   #stack along row
print(arr)
arr = np.vstack((arr1, arr2))    #stack along column
print(arr)
arr = np.dstack((arr1, arr2))    #stack along height(depth)
print(arr)

#---------
#Splitting numpy array
#array_split() for splitting arrays, we pass it the array we want to split and the number of splits

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
newarr = np.array_split(arr, 3, axis=1)   #split along the row (axis=1)
print(newarr)
newarr = np.hsplit(arr, 2)    #split along rows
print(newarr)

#--------
#Searching arrays

#search even values
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)   #print indexes

#searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
#The searchsorted() method is assumed to be used on sorted arrays.
x = np.searchsorted(arr, 7)
print(x)

#----------
#Sorting

arr = np.array([True, False, True])
print(np.sort(arr))

arr = np.array([[1,2], [5, 4]])
print(np.sort(arr))

#--------
#Filtering
#A boolean index list is a list of booleans corresponding to indexes in the array.

#to filter even numbers from list
arr = np.array([66,76,33,97,12])
filter_arr = []

for element in arr:
  if element %2 ==0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

#creating filter array directly
arr = np.array([66,76,33,97,12])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)