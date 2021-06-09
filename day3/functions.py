#Multiple arguments
def display(fname, cname):
  print(fname + " is " + cname)

display("Apple", "Red")

#Arbitrary arguments *args  &  Arbitrary keyword arguments **kwargs
def display1(*colors):
  print("Third color: " + colors[2])
def display2(**colors):
  print("Length of 'blue': ",colors["Blue"])

display1("Blue", "Red", "Black", "Green")
display2(Blue=4, Red=3, Black=5, Green=5)

#Function to check if a number is prime or not
def prime(n):
    if (n==1):
        print("Not a prime number!")
    elif (n==2):
        print("Prime number!")
    else:
        c=0
        for x in range(2,n):
            if(n % x==0):
                c=c+1
        if(c==0):
            print("Prime number!")
        else:
            print("Not a prime number!")

num=int(input("Enter a number: "))
prime(num)

#Print factorial of a number using module
import module1
n=int(input("Enter value of n: "))
print("Factorial: ",module1.factorial(n))

#Python function that accepts a string and calculate the number of upper case letters and lower case letters
def count(str1):
    u=0
    l=0
    for char in str1:
        if char.isupper():
           u+=1
        elif char.islower():
           l+=1
        else:
           pass
    print ("No. of Upper case characters : ",u)
    print ("No. of Lower case Characters : ",l)
s=input("Enter a string: ")
count(s)

#Recursion- find power of a function
def power(num,p):
    if p==0:
        return 1
    elif p==1:
        return num
    else:
        return (num*power(num,p-1))

num=int(input("Enter a number: "))
p=int(input("Enter power: "))
print("Result:",power(num,p))