# Program to remove tuples having duplicate first value from given list of tuples

t1 = [(1,2),(7,6),(4,5),(1,2),(8,2),(7,6)]
visited = []
final = []
for a, b in t1:
	if not a in visited:
		visited.append(a)
		final.append((a, b))

print("Original list:", t1)
print("List of tuple after removing duplicates:", final)

# Program to sort list of tuple based on sum of element in tuple.

t1 = [(1,2),(7,6),(4,5),(8,2)]
print("Original list:", t1)
    #selection sort
for i in range(len(t1)):
    minimum = i
    for j in range(i+1, len(t1)):
        if (t1[minimum][0]+t1[minimum][1]) > (t1[j][0]+t1[j][1]):
            minimum = j           
    # Swap the tuple with least sum with first tuple        
    t1[i], t1[minimum] = t1[minimum], t1[i]
print("Sorted list based on sum of element of tuple: ",t1)

#Program to calculate the average value of the numbers in a given tuple of tuples.

t1 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print ("Original Tuple: ",t1)
output=[]
for x in t1:
    a=sum(x)/len(x)
    output.append(a)
print("Average value of the numbers of tuples:",output)

#Program to check if a specified element presents in a tuple of tuples.

t1 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
num=int(input("Enter number to be searched:"))
a=0
for x in t1:
    if num in x:
        print("Found!")
        a=a+1
        break
if a==0:
    print("Not found!")    

# Calculate product of all the elements of tuple
t1=(4,6,5,2,1)
product=1
for x in range(len(t1)):
    product=product*t1[x]
print("Product of elements:",product)