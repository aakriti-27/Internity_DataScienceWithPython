#Closures
#A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

#Print name and marks of a student using closure
def student(n,m):
    name = n
    marks = m
    def display():
        print("Name: ",name)
        print("Marks: ",marks)
    return display 
obj = student('Dev',50)
obj()

#The decorators are used to modify the behavior of function or class. 
#Functions are taken as the argument into another function and then called inside the wrapper function.

#Demonstration of decorator  
def decorator1(func):   # defining a decorator
    def inner1():        # inner1 is a Wrapper function
        print("Before execution!")
        func()       
        print("After execution!")
    return inner1

def function1():    
	print("Inside the function!")

function1 = decorator1(function1)   # passing 'function1' inside the decorator to control its behavior
function1()

#If a function returns something or an argument is passed to the function
#To calculate product of 2 numbers
def decorator2(func):
	def inner2(*args, **kwargs):
		print("Before Execution")
		returned_value = func(*args, **kwargs)   # getting the returned value
		print("After Execution")
		return returned_value
		
	return inner2

@decorator2
def product(a, b):
	print("Inside the function")
	return a * b

a, b = 6, 2
print("Product: ", product(a, b))

#Chaining decorators
def display1(func):
	def inner():
		func()
		print("Hello world!")
	return inner
def display2(func):
	def inner():
		func()
		print("Hello everyone!")
	return inner

@display1
@display2
def display():
	print("Hello!")

display()     #decor1(decor2(display))

