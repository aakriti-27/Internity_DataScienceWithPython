#Generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return
#Generator functions return a generator object.

#Generator for Fibonacci Numbers(first 10)
def fibonacci(limit):     #generator function
    a=0
    b=1
    c=0
    while c<limit:
        yield a
        a,b=b,a+b
        c=c+1
	
x = fibonacci(10)  #generator object
print("Fibonacci Series:")
for i in x:
	print(i)

#To implement a sequence of power of 2 using an iterator class
def power(max):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

x=power(4)
print("Sequence of power of 2:")
for i in x:
    print(i)

#To find out the sum of squares of numbers in the Fibonacci series
#Pipelining generators(multiple generators)
def fibonacci(limit):     
    a=0
    b=1
    c=0
    while c<limit:
        yield a
        a,b=b,a+b
        c=c+1

def square(nums):
    for num in nums:
        yield num**2
print("Sum of squares of numbers in Fibonacci series: ")
print(sum(square(fibonacci(5))))

#Reversing a string using generator
def rev(str1):
    for i in range(len(str1) - 1, -1, -1):
        yield str1[i]
for char in rev("hello world"):
    print(char)