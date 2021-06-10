#Create a class student.Print name of student and the average marks in 3 subjects.
class Student:
  def __init__(self, name, m1,m2,m3):
    self.name = name
    self.marks1 = m1
    self.marks2 = m2
    self.marks3 = m3

  def average(self):
      avg=(self.marks1+self.marks2+self.marks3)/3
      print("Student name: " + self.name)
      print("Average marks:" ,avg)

s1 = Student("Vidhi Awasthi", 12,18,20)
s1.average()

#The self parameter is a reference to the current instance of the class.
#It is used to access variables that belongs to the class.It can be given any name.
class Person:
  def __init__(person_object, name, age):
    person_object.name = name           # person_object is self parameter
    person_object.age = age

  def myfunc(p2):
    print("Hello my name is " + p2.name)

p1 = Person("John", 36)
p1.myfunc()

#Create a class to calculate area and perimeter of triangle 
import math
class Triangle():
    def __init__(self, s1,s2,s3):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3

    def area(self):
        s=(self.side1+self.side2+self.side3)/2
        p=(s-self.side1)*(s-self.side2)*(s-self.side3)
        area=math.sqrt(p)
        return area
    
    def perimeter(self):
        return self.side1+self.side2+self.side3

t1 = Triangle(3,4,5)
print("Area: ",t1.area())
print("Perimeter: ",t1.perimeter())

#Write a Python class which has two methods get_String and print_String. 
#get_String accept a string from the user and print_String print the string in upper case and in reverse .
class Str_class():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Enter a string:")

    def print_String(self):
        rev=self.str1[::-1]
        print("Reversed string in upper case: ",rev.upper())

str_obj = Str_class()
str_obj.get_String()
str_obj.print_String()

#Python class to find all pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
class find_pair:
   def sum1(self, nums, target):
        lookup = {}
        pairs=[]
        for i, num in enumerate(nums):  #Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object
            if target - num in lookup:
                t=(lookup[target - num],i)
                pairs.append(t) 
            lookup[num] = i
        print("Pairs: ",pairs)

obj=find_pair()
obj.sum1((10,20,10,40,30,60,70),50)


