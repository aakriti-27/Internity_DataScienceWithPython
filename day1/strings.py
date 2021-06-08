#Program to remove duplicate words from a given string
str1="This is pen is"
print("Original string:",str1)
l=str1.split()
l1=[]
for x in l:
    if x not in l1:
        l1.append(x)
str1=' '.join(l1)
print("New string:",str1)

#Program to swap cases of a given string
str1="Hello Everyone"
str2=""
for x in str1:
    if x.isupper():
        str2=str2+x.lower()
    else:
        str2=str2+x.upper()
print("Original string:",str1)
print("New string:",str2)

#Program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
str1='madam'
print("Original string:",str1)
c=str1[0]
str1=str1.replace(c,'$')
str1=c+str1[1:]
print("New string:",str1)

#Program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically)
str1='a,d,b,u,s'
l=str1.split(',')
str2=",".join(sorted(l))
print("Original string:",str1)
print("New string:",str2)

#program to extract numbers from a given string
str1="a 7 b 4 c 9"
l1=str1.split()
l2=[]
for x in l1:
    if x.isdigit():
        l2.append(int(x))
print("Numbers:",l2)
