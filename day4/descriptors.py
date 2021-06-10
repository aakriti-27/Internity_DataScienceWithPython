#Python descriptors are created to manage the attributes of different classes which use the object as reference.
#In descriptors we use three different methods that are __getters__(), __setters__(), and __delete__().
#Descriptors are invoked by the __getattribute__() method.

#Demonstration of descriptors
class Descriptor1(object):

	def __init__(self, name =''):
		self.name = name

	def __get__(self, obj, objtype):
		return "Name is "+self.name

	def __set__(self, obj, name):
		if isinstance(name, str):
			self.name = name
		else:
			raise TypeError("Name should be string")
		
class display(object):
    name=Descriptor1("Vidhi")
    print("In function!")

g = display()
print(g.name)
g.name = "Rahul"
print(g.name)

#Creating a Descriptor using property() :
#property(), it is easy to create a usable descriptor for any attribute.
# Python program to explain property() function
	
class Display:
	def __init__(self, value):
		self._value = value
	def getValue(self):    # getting the values
		print('Getting value')
		return self._value
	def setValue(self, value):    # setting the values
		print('Setting value to ' + value)
		self._value = value
	def delValue(self):
		print('Deleting value')     # deleting the values
		del self._value
		
	value = property(getValue, setValue, delValue )
	
x = Display('Hello World!')
print(x.value)
x.value = 'HELLO'
del x.value