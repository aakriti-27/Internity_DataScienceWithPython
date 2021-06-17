#Pandas is a Python library used for working with data sets.
#It has functions for analyzing, cleaning, exploring, and manipulating data.

#Data Structure - Series,DataFrame,Panel 
#DataFrame is a container of Series, Panel is a container of DataFrame.

# Data Structure	Dimensions	Description
# Series	           1	    1D labeled homogeneous array, sizeimmutable.
# Data Frames	       2	    General 2D labeled, size-mutable tabular structure with potentially heterogeneously typed columns.
# Panel	               3	    General 3D labeled, size-mutable array.

import pandas as pd
import numpy as np

#SERIES
s = pd.Series(dtype='int64')   #creating empty series of int type
print(s)

arr = np.array(['a','b','c','d'])   #creating series from ndarray
s = pd.Series(arr)
print(s)
s = pd.Series(arr,index=[11,22,33,44])
print(s)

d = {'a' : 0, 'b' : 1, 'c' : 2, 'd':3}   #creating series from dictionary
s = pd.Series(d,index=['b','c','d','a'])
print(s)    #Index order is persisted 

#If data is a scalar value, an index must be provided. The value will be repeated to match the length of index
s = pd.Series(6, index=[1, 2, 3, 4])
print(s)

#Accessing Data from Series with Position
s = pd.Series([1,2,3,4],index = ['a','b','c','d'])
print(s[0])
print(s[-2:])

#Retrieve Data Using Label (Index)
print(s['d'])
print(s[['a','b']])


#DATAFRAME
#pandas.DataFrame( data, index, columns, dtype, copy)

df = pd.DataFrame()   #creating empty dataframe
print(df)

l1 = [1,2,3,4,5]      #creating dataframe using list
df = pd.DataFrame(l1)
print(df)

l2 = [['Aakriti',94],['Sanchita',95],['Avyakt',98]]
df = pd.DataFrame(l2,columns=['Name','Marks'],dtype=float)
print(df)

d1 = {'Name':['Aakriti', 'Sanchita', 'Avyakt'],'Marks':[94,95,98]}    #creating dataframe from dictionary of ndarrays or lists
df = pd.DataFrame(d1)
print(df)
df = pd.DataFrame(d1, index=['rank3','rank2','rank1'])
print(df)

d = [{'a': 78, 'b': 52},{'a':37, 'b': 11, 'c': 64}]   #Creating dataFrame from List of dictionaries
df1 = pd.DataFrame(d, index=['one', 'two'], columns=['a', 'b'])
df2 = pd.DataFrame(d, index=['one', 'two'], columns=['a', 'b1'])
print(df1)
print(df2)

d = {'number1' : pd.Series([11, 22, 33], index=['a', 'b', 'c']),
   'number2' : pd.Series([11, 22, 33, 44], index=['a', 'b', 'c', 'd'])}  #Creating a DataFrame from Dict of Series
df = pd.DataFrame(d)
print(df)

print(df['number1'])    #column selection
df['number3']=pd.Series([11,22,33],index=['a','b','c'])   #adding a new column by passing new series
print(df)
df['number4']=df['number1']+df['number3']    #adding column using existing columns
print(df)

del df['number4']    #deleting column using delete
df.pop('number3')  #deleting column using pop

print(df.loc['b'])      #Rows selection by passing row label to a loc function.
print(df.iloc[1])      #Rows selection by passing integer location to an iloc function.
print(df[2:4])          #Row slicing

df = pd.DataFrame([[11, 22], [33, 44]], columns = ['a','b'],index=[0,1])
df2 = pd.DataFrame([[77, 99], [66, 55]], columns = ['a','b'],index=[2,3])
df = df.append(df2)     #row addition
print(df)

df = df.drop(1)   #row deletion

#Panel
#pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)


# data = np.random.rand(3,3,4)  #creating panel From 3D ndarray
# p = pd.Panel(data)
# print(p)

# p = pd.Panel()    #creating data using Panel constructor
# print(p)

# data = {'one' : pd.DataFrame(np.random.rand(4, 3)), 
#    'two' : pd.DataFrame(np.random.rand(4, 3))}   #creating panel from dict of DataFrame Objects
# p = pd.Panel(data)
# print(p)
# print(p['one'])   #selection using items
# print(p.major_xs(1))   #using major axis
# print(p.minor_xs(1))    #using minor axis

#ceating dataframe from text file
file1 = open("data1.txt", "r")
df = pd.DataFrame([file1], index = None) 
print(df)

#creating dataframe from csv file
import csv  
with open("data.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    df = pd.DataFrame([csv_reader], index = None) # using csv files into the pandas
print(df)

#creating dataframe from database
import sqlite3
conn = sqlite3.connect("flights.db")
df = pd.read_sql_query("select * from airlines limit 5;", conn)
print(df)

##creating dataframe from api
# import requests
# r = requests.get('https://api.box.com/2.0/files/:file_id/content/')
# x = r.json()
# df = pd.DataFrame(x['content'])
# print(df)


#Examining the data
file = pd.read_csv('data.csv')
print(file.to_string()) 

#Viewing the data
print(file.head())   #return the top 5 rows
print(file.head(3))  #return the top 3 rows
print(file.tail())   #return last  5 rows of dataframe

print(file.info())    #to get more information about data set

#Describing and Summarizing of the data
import csv  
with open("data.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    df = pd.DataFrame([csv_reader], index = None) # using csv files into the pandas

print(df.shape)
print(df.columns)
print(df.describe())
print(df.info())


