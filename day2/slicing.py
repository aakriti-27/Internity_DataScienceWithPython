#creating slice object
result = slice(1, 5, 2)   # contains indices (1, 3)
print(result) 

#To get sublist or sub-tuple
l1=['h','e','l','l','o']
t1=('h','e','l','l','o','a','b')
print(l1[:3])    #to get first 3 values
print(t1[1:3])   #to get values 2nd and 3rd value
print(l1[-1:-4:-1])    #contains indices -1, -2 and -3
print(t1[-1:-5:-2])    # contains indices -1 and -3

#To check if word is palindrome or not
word = input("Enter word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

#Slicing a list vs slicing a string
#(==) checks if the values are equal. 
#(is) checks if the two variables point to the same object in memory
l1 = [4,67,54,24,22,83]
l1 == l1[:]  #True
l1 is l1[:]  #False
word = 'Python'
word == word[:]#True
word is word[:]  #True

#Program for substituting and deletion of a part of list using slicing
l1 = [4,67,54,24,22,83]
l1[2:5] = [1,2,3]
print("Substituted list:",l1)
del l1[2:5]
print("List after deleting a part:",l1)