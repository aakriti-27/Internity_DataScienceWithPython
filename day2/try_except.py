#Program to input a number, if it is not a number generates an error message.
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("This is not a number.")

#Program to depict else clause with try-except
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
try:
    calc = (num1+num2) / (num1-num2)
except ZeroDivisionError:
    print("a-b result in 0")
else:
    print("Result: ",calc)

#Program to depict multiple exception block and finally block with try-except 
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
finally:
    print("This statement is always executed")

# Program to handle multiple errors with one except statement
try : 
    num = int(input("Enter a number: "))
    if num < 4 :
        c = num/(num-2)  # throws ZeroDivisionError for num = 2
    print("Value of c = ", c)  # throws NameError if num >= 4
except(ZeroDivisionError, NameError):
    print("Error was handled!")

#Raising exception
num = int(input("Enter a positive number: "))
if num < 0:
  raise Exception("Sorry, no negative numbers!")
x = "hello"  #raising TypeError exception
if not type(x) is int:
  raise TypeError("Only integers are allowed!")

