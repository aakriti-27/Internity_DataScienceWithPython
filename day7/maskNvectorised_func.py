import numpy as np

#Boolean Masks
# Masking is when you want manipulated data in a collection based on some criteria. 
# The criteria you use is typically of a true or false nature, hence the boolean part. 
# Most efficient way to quantify a sub-collection in a collection.

a = np.array([1,2,3,4,5,6])
c=a < 3               #Creates a boolean mask for values less than 3
print(c)
print("Median:",np.median(a[c]))

# construct a mask of all summer days (June 21st is the 172nd day)
days = np.arange(365)
summer = (days > 172) & (days < 262)


#Vectorized Operations
#The concept of vectorized operations on NumPy allows the use of more optimal and pre-compiled functions and mathematical operations on NumPy array objects and data sequences. 
#The Output and Operations will speed-up when compared to simple non-vectorized operations.

#Sum of 0-499 integers using vectorized sum method
s=np.sum(np.arange(500)) 
print("SUM: ",s)

#computations that invoke vectorized functions
print(2 * np.array([1, 3, 7]))

print(np.array([10.2, 3.5, -0.9]) - np.array([8.2, 3.5, 6.5]))

print(np.dot(np.array([1, -3, 4]), np.array([2, 0, 1])))

print(np.exp(np.arange(150)))  #exponential