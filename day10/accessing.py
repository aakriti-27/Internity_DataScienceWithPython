#acccsessing series

#Accessing Element from Series with Position
import numpy as np
import pandas as pd

data = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
ser = pd.Series(data)

print(ser[0])   # retrieve the first element
print(ser[:2])   #retrive first 2 elements
print(ser[-6:])   # retrieve last 6 elements

df = pd.read_csv("data1.csv")  
ser = pd.Series(df['Pulse']) 
print(ser.head())    #accessing first 5 elements of column Pulse

#Accessing Element Using Label (index)

data = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
ser = pd.Series(data,index=[11,22,33,44,55,66])
print(ser[33])    # accessing a element using index element
print(ser[[22,44,66]])     #accessing multiple elements

#Accessing Panel
# data = {'List1' : pd.DataFrame(np.random.randn(4, 3)), 
#    'List2' : pd.DataFrame(np.random.randn(4, 2))}
# p = pd.Panel(data)
# print(p['List1'])
# print(p.major_xs(1))
# print(p.minor_xs(1))

