#Pandas is a Python library.
#Pandas is used for working with data sets and analyzing it.

#Pandas Series is a one-dimensional array holding data of any type(like a column in a table)
import pandas as pd   #creating an alias while importing
a = [1, 2, 3]
myvar = pd.Series(a)
print(myvar[0])       #values are labeled with their index number

myvar = pd.Series(a, index = ["a", "b", "c"])    #creating new labels
print(myvar)

b = {"a1": 10, "b2": 20, "c3": 30}      #using key,object while making series
myvar = pd.Series(b)
print(myvar)

#DataFrames are datasets in Pandas are usually multi-dimensional tables(like a whole table)
mydataset = {
  'char': ["A", "B", "C"],
  'value': [1,2,3]
}
myvar = pd.DataFrame(mydataset)
print(myvar)
print(myvar.loc[0])     #loc attribute to return one or more specified row(s)
print(myvar.loc[[1, 2]])    

myvar1 = pd.DataFrame(mydataset, index = ["v1", "v2", "v3"])    #giving own indexes
print(myvar1)
print(myvar1.loc["v2"])

#Reading csv file
file = pd.read_csv('data.csv')
print(file.to_string()) 

#Viewing the data
print(file.head())   #return the top 5 rows
print(file.head(3))  #return the top 3 rows
print(file.tail())   #return last  5 rows of dataframe

print(file.info())    #to get more information about data set