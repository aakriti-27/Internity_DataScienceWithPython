import re

#Check if the string has any digits
txt = "ab12hy3i4"
x = re.findall("[0-9]", txt)   
print(x)
if x:
  print("Yes, the string has atleast a digit!")
else:
  print("No digits found!")

#Q2
txt = "ab12hy3i4"
x1 = re.findall("[^arn]", txt)  #To find if the string has other characters than a, r, or n
x2 = re.findall("[arn]", txt)  #To find if the string has characters a, r, or n
print(x1)
print(x2)
txt1="hello world"
x3 = re.findall("world$", txt1) #To find if the string ends with 'world'
x4 = re.findall("^hello", txt1) #To find if the string starts with 'hello'
print(x3)
print(x4)

#Program that matches a word at the beginning of a string.
txt=" hello"
patterns = '^\w+'
if re.search(patterns,  txt):
    print('Found a match!')
else:
    print('Not matched!')

#Program to match a string that contains only upper and lowercase letters, numbers, and underscores.
txt="Hello_123"
patterns = '^[a-zA-Z0-9_]*$'
if re.search(patterns,  txt):
    print('Found a match!')
else:
    print('Not matched!')

#Replace all white-space characters with the digit "%"
txt = "This is beautiful."
x = re.sub("\s", "%", txt)  #sub() replaces the matches with the text of your choice
x1 = re.sub("\s", "%", txt, 1)  #replaces only first space
print(x)
print(x1)