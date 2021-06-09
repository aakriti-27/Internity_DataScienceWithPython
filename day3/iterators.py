#Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
#The iterator object is initialized using the iter() method. 
#It uses the next() method for iteration.

#To print all the elements of list using inbuilt iterator
l1=[1,2,3,4]
iterable_obj = iter(l1)
while True:
    try:
        element = next(iterable_obj)
        print(element)
    except StopIteration:
        break

#To print all the uppercase letters of a string
str1="HelLo WorlD"
iobj=iter(str1)
while True:
    try:
        element = next(iobj)
        if element.isupper():
            print(element)
    except StopIteration:
        break

# Iterating over dictionary  
d = {'a':1,'b':2,'c':3}
iobj=iter(d)
while True:
    try:
        key = next(iobj)
        print(key," ",d[key])
    except StopIteration:
        break

#Create an iterator that returns first 10 even numbers
class even:
  def __iter__(self):
    self.a = 2
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 2
      return x
    else:
      raise StopIteration

myclass = even()
myiter = iter(myclass)
print("Even numbers:")
for x in myiter:
  print(x)