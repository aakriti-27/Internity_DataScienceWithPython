#Python program to count the number of lines in a text file.
file = open('text1.txt')
c=0
for line in file:
     c=c+1
     print(line)
print("Total number of lines: ",c)
file.close()  #closing the file

#program to count the frequency of words in a file
file = open('text1.txt')
d = dict()
for line in file:
	line = line.strip()  # Remove the leading spaces and newline character
	line = line.lower()
	line.replace(",", " ")  #If words are separated by commas
	words = line.split(" ")    #to get words

	for w in words:
		if w in d:
			d[w] = d[w] + 1   #counting frequency
		else:
			d[w] = 1
print("Frequency:")
file.close()
for key in list(d.keys()):
	print(key, " : ", d[key])

#Copy contents of one file to another file
firstfile = open('text1.txt','r')
secondfile = open('text2.txt','a')	  # text2.txt does not exists so it will already be created
for line in firstfile:   #reading content from first file
	secondfile.write(line)  # appending content to second file
firstfile.close()
secondfile.close()

#To add a new line in text1.txt and overwrite the content of text2.txt
f = open("text1.txt", "a")   #opening the file in append mode to add content
f.write("\nNew content!")
f = open("text1.txt", "r")
print(f.read())
f.close()

f1 = open("text2.txt", "w")   #opening the file in write mode to overwrite content
f1.write("The content has been over written!")
f1 = open("text2.txt", "r")
print(f1.read())
f1.close()

#To sort the numbers in file 'text3.txt' in ascending order
with open('text3.txt', 'r') as file:
    lines = file.readlines()
l_num = [int(num.strip()) for num in lines]
l_num.sort()
print("Ascending order: ",l_num)

#To delete the file --
# import os
# if os.path.exists("text1.txt"):
#   os.remove("text1.txt")
# else:
#   print("The file does not exist")