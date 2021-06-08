#Program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
num=int(input("Input a number "))
d1 = dict()
for x in range(1,num+1):
    d1[x]=x*x
print("Dictionary:",d1)

#To print key,values of the dictionary separately using functions
d1={'a':1,'b':2,'c':3}
print(d1.keys())
print(d1.values())
print(d1.items())

#Program to filter a dictionary based on values i.e if value is an odd number
d1 = {'a': 17, 'b': 80, 'c': 26, 'd': 35}
print("Original Dictionary:",d1)
d2=dict()
for (key,value) in d1.items():
    if value%2 !=0:
        d2[key]=value
print("Dictionary with odd value:",d2)

#Replace last 2 items of dictionary with average of their values
l1=[{'a': 1, 'b': 2, 'c': 3},{'a': 2, 'b': 5, 'c': 5}]
for x in l1:
    b1=x.pop('b')
    c1=x.pop('c')
    x['avg']=(b1+c1)/2
print(l1)

#program to find the length of a given dictionary values.
d1 = {1 : 'hello', 2 : 'hi', 3 : 'greetings', 4 : 'hey'}
d2 = dict()
for value in d1.values():
    d2[value]=len(value)
print("length of dictionary value:",d2)
