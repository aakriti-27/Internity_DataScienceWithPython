#Find the index of the 1st matching element and insert 'a' at that index
l1=['h','e','l','l','o']
i=l1.index('l')
print(i)
l1.insert(i, 'a')
print(l1)

#Program to iterate over characters of a string using indexing
txt="hello world"
for char in range(0,len(txt)):
    print(txt[char])

#Program to demonstrate working of Key index in Dictionary
d1 = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
search_key = 'b'
print("The original dictionary is : ",d1)
list1=list(d1.keys())
i = list1.index(search_key)
print("Index of search key is : " ,i)

#To get first and last value of tuple using negative indexing
t1=('h','e','l','l','o')
print("First value: ",t1[-len(t1)])
print("Last value: ",t1[-1])

#To print the domain of an email
email="abc@gmail.com"
i=email.rindex('@')      #rindex() returns the last index
print("Domain: ",email[i+1:])