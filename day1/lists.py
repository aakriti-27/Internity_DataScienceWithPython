#Counting the occurrences of items in a list entered by user
list1=[]
n = int(input("Enter number of items : "))
for i in range(0, n):
    item = int(input())
    list1.append(item) 

for i in set(list1):
    c=list1.count(i)
    print(i,"occurs",c,"times")  

#To check if the item is present in the list
a=['a','y','j']
c=input("Enter item to check if it is present or not:")
if(c in a):
    print("Found!")
else:
    print("Not found!")

#To Sort even-placed elements in increasing and odd-placed in decreasing order
l1=[4,7,2,1,5,6,9,33,21,66,11,23,0,8]
odd=[]
even=[]
for i in range(0,len(l1)):
     if i%2!=0:
         odd.append(l1[i])
     else:
         even.append(l1[i])
odd.sort(reverse=True)
even.sort()
print("even placed elements:",even)
print("odd placed elements:",odd)

#To print first seven items of a list in reverse order using slicing
l1=[3,55,27,76,98,45,67,1,23,45,69]
print(l1[6::-1])

#To print square of even numbers in the range of 1-10 (list comprehension)
sqr = [x ** 2 for x in range(1, 11) if x % 2 == 0]    
print (sqr) 