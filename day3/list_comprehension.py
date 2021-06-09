#To add all colors of list except "Blue"
newlist = [x for x in ["Red","Blue","Green"] if x != "Blue"]
print(newlist)

#Store the reverse of each element in list
newlist=[element[::-1] for element in ["Red","Blue","Green"]]
print(newlist)

#Move all 0's at the end
newlist=([x for x in [0,6,4,0,3,2,0,7] if x!=0] + [y for y in [0,6,4,0,3,2,0,7] if y==0])
print(newlist)

#Append 4 sublist of 3 elements each inside the list
#Nested list comprehension
list1 = [[j for j in range(3)] for i in range(4)]
print(list1)

# Double all numbers from 1 to 10 using map and lambda
newlist = list(map(lambda x: x + x,[x for x in range(1,11)]))
print(newlist)