#Dataframe.aggregate() function is used to apply some aggregation across one or more column

import pandas as pd

df = pd.read_csv("data.csv")
df2=df.aggregate(['min'])   #minimum value has been found of each column
print(df2)

df2=df.aggregate({"High":['sum', 'min']})    #minimun and sum of values in column 'High'
print(df2)

df2=df.aggregate({"High":['sum', 'max'],
              "Low":['max', 'min'],})
print(df2)


#Merging
#Pandas provides a single function, merge, as the entry point for all standard database join operations between DataFrame objects −
#pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,left_index=False, right_index=False, sort=True)

college1 = pd.DataFrame({
   'roll_no':[1,2,3,4,5,6,7],
   'Name': ['Rita', 'Vinit', 'Naman', 'Sarika', 'Mayank','Dev','Gauri'],
   'Subject':['CS','Physics','Chemistry','Geology','Maths','English','Economics']})
college2 = pd.DataFrame({
   'roll_no':[1,2,3,4,5,6],
   'Name': ['Samar', 'Preeti', 'Tushar', 'Harshita', 'Deeksha','Dev'],
   'Subject':['Maths','Chemistry','Physics','Geology','CS','English']})
print(college1)
print(college2)

print(pd.merge(college1,college2,on='roll_no'))   #Merging 2 dataframe on a key
print(pd.merge(college1,college2,on=['roll_no','Subject']))   #Merging 2 dataframe on multiple key

print(pd.merge(college1, college2, on='Subject', how='left'))    #using keys from left object
print(pd.merge(college1, college2, on='Subject', how='right'))   #using keys from right object
print(pd.merge(college1, college2, on='Subject', how='inner'))   #using intersection of keys
print(pd.merge(college1, college2, on='Subject', how='outer'))   #using union of keys 



