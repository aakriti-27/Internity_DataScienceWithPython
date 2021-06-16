import numpy as np
#Universal functions in Numpy are simple mathematical functions. 
#These functions include standard trigonometric functions, functions for arithmetic operations, handling complex numbers, statistical functions, etc.

a = np.array([12,23,45])
b = np.array([4,3,5])
print("Remainder:",np.remainder(a,b))
print("Modulus:",np.mod(a,b))
print("Power:",np.power(a,b))


#Trigonometric functions

a = np.array([0, 30, 45, 60, 90, 180])  #array of angles
r = np.deg2rad(a)         #to convert degree to radians

print('Sine of angles:',np.sin(r))    # sine of angles

i=np.rad2deg(np.arccos(np.cos(r)))
print('Inverse cos of cos values:',i)   # inverse cos of cos values

print('Tangent hyperbolic of angles :',np.tanh(r))   # hyperbolic tangent of angles
 
print('Inverse Sine hyperbolic:',np.sin(np.sinh(r)))   # inverse sine hyperbolic

base = 5
height = 6
print('hypotenuse of right triangle is:',np.hypot(base, height))     #to find hypotenuse of triangle

#Statistical functions
temp = np.array([43.7, 52.5, 65.78, 23.21, 49.5, 37])  #array of temperature

print('Minimum temperature: ',np.amin(temp))
print('Maximum temperature: ',np.amax(temp))

print('Range of the temperature: ',np.ptp(temp))  #range of temperature ie(max-min)

print('Temperature below which 50% temperature fall: ',np.percentile(temp, 50))

print('Mean temperature: ',np.mean(temp))

print('Median temperature: ',np.median(temp))

print('Standard deviation of temperature: ',np.std(temp))

print('Variance of temperature: ',np.var(temp))

print('Average weight of temperature: ',np.average(temp))

#Bit-twiddling functions:
#These functions accept integer values as input arguments and perform bitwise operations on binary representations of those integers.

# Python code to demonstrate bitwise-function
import numpy as np

# construct an array of even and odd numbers
n1 = np.array([2,4,5,6,7])
n2 = np.array([1,3,8,9,0])

print('bitwise_and of two arrays: ',np.bitwise_and(n1,n2))

print('bitwise_or of two arrays: ',np.bitwise_or(n1,n2))

print('bitwise_xor of two arrays: ',np.bitwise_xor(n1,n2))

print('inversion of n1 array: ',np.invert(n1))

print('left_shift of n1 array: ',np.left_shift(n1, 2))

print('right_shift of n1 array: ',np.right_shift(n2, 2))
